def open_file(input : str) -> [[int]]:
    file = open(input, 'r')
    lines = file.read().split('\n')
    while not lines[-1]: lines.pop()
    risk_map = []
    for line in lines:
        y = []
        for char in line:
            y.append(int(char))
        risk_map.append(y)
    return risk_map

def calc_d(pos : [int], r_map : [[int]], d_map : [[int]]) -> [[int]]:
    x = pos[0]
    y = pos[1]
    d0 = d_map[y][x]
    w = len(d_map[0])
    h = len(d_map)
    if x:
        # move in -x direction
        d1 = d_map[y][x - 1]
        r = r_map[y][x - 1]
        if d0 + r < d1:
            d_map[y][x - 1] = d0 + r
    if y:
        # move in -y direction
        d1 = d_map[y - 1][x]
        r = r_map[y - 1][x]
        if d0 + r < d1:
            d_map[y - 1][x] = d0 + r
    if x < w - 1:
        # move in +x direction
        d1 = d_map[y][x + 1]
        r = r_map[y][x + 1]
        if d0 + r < d1:
            d_map[y][x + 1] = d0 + r
    if y < h - 1:
        # move in +y direction
        d1 = d_map[y + 1][x]
        r = r_map[y + 1][x]
        if d0 + r < d1:
            d_map[y + 1][x] = d0 + r
    # finished
    return d_map
    

def sum_map(risk_map : [[int]]) -> int:
    s = 0
    for y in risk_map:
        for r in y:
            s += r
    return s

def create_empty(r_map : [[int]]) -> [[int]]:
    inf = sum_map(r_map)
    empty = [[inf for x in r_map[0]] for y in r_map]
    empty[0][0] = 0
    return empty

def lowest(d_map : [[int]], t_map : [[bool]], end : [int, int], lowest : int) -> [int, int]:
    # we should only consider false, and their neighbours
    # replace t_map with to_do (coordinates)
    pos = end
    for y, y_d in enumerate(d_map):
        for x, d in enumerate(y_d):
            if d < lowest and t_map[y][x]:
                lowest = d
                pos = [x, y]
    return pos

if __name__ == '__main__':
    r_map = open_file('input')
    d_map = create_empty(r_map)
    # replace t_map with to_do (coords)
    t_map = [[True for x in d_map[0]] for y in d_map]
    to_do = []
    to_do.append([0, 0])


    end = [len(d_map[0]) - 1, len(d_map) - 1]
    d_end = d_map[end[1]][end[0]]
    max_i = 100000
    while(max_i):
        # 1) find lowest point in d_map
        #print(max_i)
        pos = lowest(d_map, t_map, end, d_end)
        #print(pos)
        t_map[pos[1]][pos[0]] = False
        if pos == end:
            break
        # 2) find Neighbours, and adjust d's
        d_map = calc_d(pos, r_map, d_map)
        max_i -= 1  
    # 3) recalculate d_map
    # 4) if end is lowest point on map --> path found

    for y in t_map:
        line = ''
        for t in y:
            if t:
                line += '█'
            else:
                line += ' '
        print(line)

    for y in d_map:
        print(y)

