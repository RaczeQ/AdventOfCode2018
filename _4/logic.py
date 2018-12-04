import operator
import re
from datetime import datetime, timedelta


def parse_entry(log):
    m = re.search('\[(.*)\](.*)', log)
    timestamp = datetime.strptime(m.group(1), '%Y-%m-%d %H:%M')
    return (timestamp, m.group(2).strip())


def parse_info(log):
    if 'wakes up' in log:
        return None, False
    elif 'falls asleep' in log:
        return None, True
    else:
        m = re.search('\#(\d*)', log)
        return int(m.group(1).strip()), False


def generate_shitfs(data):
    data.sort()
    log_entries = [parse_entry(log) for log in data]
    shifts = {}
    last_guard_id = None
    last_asleep = False
    last_entry = None
    for date, log in log_entries:
        if date.hour == 23:
            date += timedelta(minutes=60 - date.minute)
        key = date.replace(hour=0, minute=0, second=0, microsecond=0)
        if not key in shifts:
            shifts[key] = {}
        guard_id, asleep = parse_info(log)
        assert guard_id is not None or last_guard_id is not None

        if last_guard_id is not None and not last_guard_id in shifts[key]:
            shifts[key][last_guard_id] = {minute: 0 for minute in range(60)}
        if guard_id is not None and not guard_id in shifts[key]:
            shifts[key][guard_id] = {minute: 0 for minute in range(60)}

        if guard_id is None:
            guard_id = last_guard_id
            if date.day == last_entry.day:
                start_minute = last_entry.minute
                end_minute = date.minute
                for minute in range(start_minute, end_minute):
                    shifts[key][guard_id][minute] += int(last_asleep)

        last_guard_id = guard_id
        last_asleep = asleep
        last_entry = date

    return shifts


def print_shifts(day, guards, guard_filter=None):
    for guard_id in guards.keys():
        if guard_filter in [None, guard_id]:
            shift = ['#' if x == 1 else '.' for x in guards[guard_id].values()]
            print(day.strftime('%Y-%m-%d'), '\t',
                  guard_id, '\t', ''.join(shift))


def calculate_total_asleep(shifts):
    total_asleep = {}
    for day in shifts.keys():
        for guard_id, minutes in shifts[day].items():
            if not guard_id in total_asleep:
                total_asleep[guard_id] = 0
            total_asleep[guard_id] += sum(minutes.values())
    return total_asleep


def calculate_histogram_asleep(shifts):
    histogram_asleep = {}
    for day in shifts.keys():
        for guard_id, minutes in shifts[day].items():
            if not guard_id in histogram_asleep:
                histogram_asleep[guard_id] = {
                    minute: 0 for minute in range(60)}
            for k, v in minutes.items():
                histogram_asleep[guard_id][k] += v
    return histogram_asleep


def one(data):
    shifts = generate_shitfs(data)
    total_asleep = calculate_total_asleep(shifts)
    asleep_guard_id = max(total_asleep.keys(), key=(
        lambda key: total_asleep[key]))
    minutes = {minute: 0 for minute in range(60)}
    for day in shifts.keys():
        if asleep_guard_id in shifts[day]:
            for k, v in shifts[day][asleep_guard_id].items():
                minutes[k] += v
    max_minute = max(minutes.keys(), key=(lambda key: minutes[key]))
    print(asleep_guard_id, max_minute, asleep_guard_id * max_minute)
    return asleep_guard_id * max_minute


def two(data):
    shifts = generate_shitfs(data)
    histogram_asleep = calculate_histogram_asleep(shifts)
    max_minutes = 0
    max_minute = None
    max_guard_id = None
    for guard_id, minutes in histogram_asleep.items():
        if max(minutes.values()) > max_minutes:
            max_minutes = max(minutes.values())
            max_minute = max(minutes.keys(), key=(lambda key: minutes[key]))
            max_guard_id = guard_id
    print(max_guard_id, max_minute, max_guard_id * max_minute)
    return max_guard_id * max_minute
