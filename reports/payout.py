from collections import defaultdict

class PayoutReport:
    def generate(self, raw_files_data: list[str]):
        from utils.csv_parser import parse_csv

        all_records = []
        for raw_csv in raw_files_data:
            records = parse_csv(raw_csv)
            all_records.extend(records)

        self.print_report(all_records)

    def print_report(self, records: list[dict]):
        departments = defaultdict(list)

        for record in records:
            departments[record["department"]].append(record)

        print(f"{'':<17}{'name':<20}{'hours':<7}{'rate':<7}{'payout'}")

        for department, employees in departments.items():
            print(f"{department}")

            dept_total_hours = 0
            dept_total_payout = 0

            for employee in employees:
                try:
                    name = employee["name"]
                    hours = float(employee["hours_worked"])
                    rate = float(employee["hourly_rate"])
                    payout = hours * rate

                    dept_total_hours += hours
                    dept_total_payout += payout

                    print(f"{'-' * 15}  {name:<20}{int(hours):<7}{int(rate):<7}${int(payout)}")
                except (KeyError, ValueError):
                    continue

            print(f"{' ' * 19}{'':<18}{int(dept_total_hours):<14}${int(dept_total_payout)}\n")

