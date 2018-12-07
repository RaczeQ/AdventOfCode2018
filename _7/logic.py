def parse_steps(data):
    steps = set()
    locks = {}
    for line in data:
        step = line[36]
        lock = line[5]
        steps.add(step)
        steps.add(lock)
        if not step in locks:
            locks[step] = set()
        locks[step].add(lock)
    return sorted(steps), locks

def generate_durations(steps):
    durations = { step : ord(step)-4 for step in steps}
    return durations

def find_next_step(steps, locks):
    for step in steps:
        if not step in locks.keys():
            return step

def remove_lock(steps, found_step):
    steps_to_remove = set()
    for step, locks in steps.items():
        if found_step in locks:
            locks.remove(found_step)
        if len(locks) == 0:
            steps_to_remove.add(step)
    for step in steps_to_remove:
        steps.pop(step)
    return steps

def one(data):
    steps, locks = parse_steps(data)
    result = ''
    while len(steps) > 0:
        next_step = find_next_step(steps, locks)
        steps.remove(next_step)
        locks = remove_lock(locks, next_step)
        result += next_step
    print(result)
    return result
    
def two(data):
    steps, locks = parse_steps(data)
    durations = generate_durations(steps)
    time = 0
    queue = []
    while len(steps) > 0 or len(queue) > 0:
        time += 1
        found_next_step = True
        while len(queue) < 5 and found_next_step:
            next_step = find_next_step(steps, locks)
            if next_step is None:
                found_next_step = False
            else:
                steps.remove(next_step)
                queue.append(next_step)
        finished_steps = []
        for step in queue:
            durations[step] -= 1
            if durations[step] == 0:
                finished_steps.append(step)
        for step in finished_steps:
            queue.remove(step)
            durations.pop(step)
            locks = remove_lock(locks, step)
    print(time)
    return time