# # utils/csv_parser.py
# def parse_csv(csv_content: str) -> list[dict[str, str]]:
#     lines = csv_content.strip().splitlines()
#     headers = [h.strip() for h in lines[0].split(",")]


#     normalized_headers = []
#     for h in headers:
#         if h in ("hourly_rate", "rate", "salary"):
#             normalized_headers.append("hourly_rate")
#         else:
#             normalized_headers.append(h)

#     result = []
#     for line in lines[1:]:
#         values = [v.strip() for v in line.split(",")]
#         record = dict(zip(normalized_headers, values))
#         result.append(record)

#     return result

from typing import Generator


def parse_csv_content(csv_content: str) -> list[dict[str, str]]:
    lines = csv_content.strip().splitlines()
    if not lines:
        return []

    headers = [h.strip() for h in lines[0].split(",")]
    normalized_headers = []
    for h in headers:
        if h in ("hourly_rate", "rate", "salary"):
            normalized_headers.append("hourly_rate")
        else:
            normalized_headers.append(h)

    result = []
    for line in lines[1:]:
        line = line.strip()
        if not line:
            continue
        values = [v.strip() for v in line.split(",")]

        if len(values) < len(normalized_headers):
            values += [""] * (len(normalized_headers) - len(values))
        elif len(values) > len(normalized_headers):
            values = values[:len(normalized_headers)]

        record = dict(zip(normalized_headers, values))
        result.append(record)

    return result


def parse_csv(file_path: str) -> Generator[dict[str, str], None, None]:
    with open(file_path, encoding='utf-8') as f:
        header_line = f.readline()
        if not header_line:
            return  # Пустой файл, ничего не yield
        
        headers = [h.strip() for h in header_line.strip().split(",")]
        normalized_headers = []
        for h in headers:
            if h in ("hourly_rate", "rate", "salary"):
                normalized_headers.append("hourly_rate")
            else:
                normalized_headers.append(h)
        
        for line in f:
            line = line.strip()
            if not line:
                continue
            values = [v.strip() for v in line.split(",")]
            
            if len(values) < len(normalized_headers):
                values += [""] * (len(normalized_headers) - len(values))
            elif len(values) > len(normalized_headers):
                values = values[:len(normalized_headers)]
            
            record = dict(zip(normalized_headers, values))
            yield record
