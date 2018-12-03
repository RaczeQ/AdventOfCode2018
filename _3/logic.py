def generate_coordinates(claim):
    info_1 = claim.split('@')
    claim_id = info_1[0]
    info_2 = info_1[1].split(':')
    spaces = info_2[0].split(',')
    left_space = int(spaces[0])
    top_space = int(spaces[1])
    sizes = info_2[1].split('x')
    width = int(sizes[0])
    height = int(sizes[1])

    coordinates = []
    for x in range(left_space + 1, left_space + width + 1):
        for y in range(top_space + 1, top_space + height + 1):
            coordinates.append((x,y))

    return claim_id, coordinates

def one(data):
    coordinates = set()
    overlaps = set()
    for claim in data:
        _, claim_coordinates = generate_coordinates(claim)
        for coor in claim_coordinates:
            if coor in coordinates:
                overlaps.add(coor)
            coordinates.add(coor)
    
    print(len(overlaps))
    return len(overlaps)

def two(data):
    coordinates = set()
    overlaps = set()
    claims = {}
    for claim in data:
        claim_id, claim_coordinates = generate_coordinates(claim)
        claims[claim_id] = claim_coordinates
        for coor in claim_coordinates:
            if coor in coordinates:
                overlaps.add(coor)
            coordinates.add(coor)

    for claim_id, claim_coordinates in claims.items():
        if all([c not in overlaps for c in claim_coordinates]):
            print(claim_id)
            return claim_id
