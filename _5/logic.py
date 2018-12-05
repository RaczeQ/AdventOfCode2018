def react_polymer(polymer):
    polymer_list = list(polymer)
    while True:
        i = 0
        while i < len(polymer_list) - 1:
            if polymer_list[i].swapcase() == polymer_list[i+1]:
                reacted = True
                polymer_list.pop(i)
                polymer_list.pop(i)
            else:
                i += 1
        if not reacted:
            break
        reacted = False
    return ''.join(polymer_list)

def one(data):
    polymer = react_polymer(data[0])
    print(len(polymer))
    return len(polymer)
    
def two(data):
    polymer = data[0]
    min_length = len(polymer)
    for ascii_code in range(65, 91):
        unit_upper = chr(ascii_code)
        unit_lower = chr(ascii_code+32)
        new_polymer = polymer.replace(unit_lower,'').replace(unit_upper,'')
        reduced_polymer = react_polymer(new_polymer)
        min_length = min(len(reduced_polymer), min_length)
    print(min_length)
    return min_length
