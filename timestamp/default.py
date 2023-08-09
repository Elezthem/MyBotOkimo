import time
import timeago as timesince
import datetime
import calendar

def some_function():
    "This function does nothing"
    return None


def date(
    target,
    clock: bool = True,
    seconds: bool = False,
    ago: bool = False,
    only_ago: bool = False,
    raw: bool = False,
):
    if isinstance(target, int) or isinstance(target, float):
        target = datetime.datetime.utcfromtimestamp(target)

    if raw:
        if clock:
            timestamp = target.strftime("%d %B %Y, %H:%M")
        elif seconds:
            timestamp = target.strftime("%d %B %Y, %H:%M:%S")
        else:
            timestamp = target.strftime("%d %B %Y")

        if isinstance(target, int) or isinstance(target, float):
            target = datetime.datetime.utcfromtimestamp(target)
            target = calendar.timegm(target.timetuple())

        if ago:
            timestamp += f" ({timesince.format(target)})"
        if only_ago:
            timestamp = timesince.format(target)

        return f"{timestamp} (UTC)"
    else:
        unix = int(time.mktime(target.timetuple()))
        timestamp = f"<t:{unix}:{'f' if clock else 'D'}>"
        if ago:
            timestamp += f" (<t:{unix}:R>)"
        if only_ago:
            timestamp = f"<t:{unix}:R>"
        return timestamp
