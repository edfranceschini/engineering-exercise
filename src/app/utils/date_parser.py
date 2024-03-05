from datetime import datetime

# List of datetime formats to try
datetime_formats = [
    "%Y-%m-%dT%H",
    "%Y-%m-%dT%H:%M:%S",
    "%b %d %Y",
    "%d %b %Y",
    "%B %d %Y",
    "%Y-%m-%d",
    "%Y-%m-%dT%H:%M",
    "%d %b %Y",
    "%b %d %Y",
    "%d %B %Y",
    "%B %d %Y",
    "%Y-%m-%d",
    "%Y-%m-%dT%H:%M:%S",
    "%d %B %Y",
    "%Y-%m-%dT%H:%M:%S",
    "%d %b %Y",
    "%Y-%m-%dT%H:%M",
    "%Y-%m-%dT%H",
]


def parse_date(date_str: str) -> datetime:
    # Assuming that no date means today as the field name implies
    for fmt in datetime_formats:
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue
    return datetime.now()
