from datetime import date, datetime, timezone, timedelta


def utcnow() -> datetime:
    return datetime.now(timezone.utc)


def as_utc(dt: date | None = None) -> datetime:
    if dt is None:
        return utcnow()
    elif isinstance(dt, datetime):
        return dt.astimezone(timezone.utc)
    else:
        return datetime(dt.year, dt.month, dt.day, tzinfo=timezone.utc)


def date_diff(a: date, b: date) -> timedelta:
    if isinstance(a, datetime) or isinstance(b, datetime):
        return as_utc(a) - as_utc(b)
    return a - b
