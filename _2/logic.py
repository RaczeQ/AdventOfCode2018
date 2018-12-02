def one(data):
    boxes = [list(x) for x in data]
    twice = 0
    triple = 0
    for box in boxes:
        letters = set(box)
        twice_appeared = False
        triple_appeared = False
        for letter in letters:
            count = box.count(letter)
            if count == 2:
                twice_appeared = True
            elif count == 3:
                triple_appeared = True
        if twice_appeared:
            twice += 1
        if triple_appeared:
            triple += 1
    print(twice, '*', triple, '=', twice * triple)
    return twice * triple

def two(data):
    for box_1 in data:
        for box_2 in data:
            result = ''
            for l_1, l_2 in zip(list(box_1), list(box_2)):
                if l_1 == l_2:
                    result += l_1
            if len(result) == len(box_1) - 1:
                print(box_1)
                print(box_2)
                print(result)
                return result
