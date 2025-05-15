def get_report(name):
    if name == "payout":
        from .payout import PayoutReport
        return PayoutReport()
    raise ValueError(f"Unknown report type: {name}")
