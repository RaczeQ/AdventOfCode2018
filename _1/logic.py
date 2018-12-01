STARTING_FREQUENCY = 0

def one(data):
    result = sum([int(x) for x in data])
    print(result)
    return result

def two(data):
    frequencies = [int(x) for x in data]
    values = set([STARTING_FREQUENCY])
    actual_frequency = STARTING_FREQUENCY
    i = 0
    while True:
        actual_frequency += frequencies[i]
        if actual_frequency in values:
            print(actual_frequency)
            return actual_frequency
        values.add(actual_frequency)
        i = (i+1) % len(frequencies)