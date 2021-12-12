
def open_file(input : str) -> [[int]]:
    file = open(input, 'r')
    lines = file.read().split()
    h = len(lines)
    w = len(lines[0])
    height_map = [[int(x) for x in lines[y]] for y in range(h)]
    return height_map


def get_basins(h_map : [[int]]) -> [int]:

    d_map = [[False for x in h_map[0]] for y in h_map]
    h = len(h_map)
    w = len(h_map[0])

    basins = []

    for y_a in range(h):
        for x_a in range(w):
            if d_map[y_a][x_a]:
                # already evaluated
                continue
            if h_map[y_a][x_a] == 9:
                # border; not part of a basin
                d_map[y_a][x_a] = True
                continue
            
            x = x_a
            y = y_a

            # current point is a valid part of a NEW basin:
            print("NEW BASIN")
            size = 1
            d_map[y][x] = True
            # 1) get neighbours
            to_do = get_neighbours(x, y, h_map, d_map)
            while to_do:            
                # complete the to_do list this cycle (do_now list)
                do_now = to_do.copy()
                # reset the to_do list
                to_do = []
                print('New To Do: ')
                print(do_now)
                for n in do_now:
                    if not n:
                        continue
                    y = n[0]
                    x = n[1]
                    size += 1
                    d_map[y][x] = True
                    N = get_neighbours(x, y, h_map, d_map)
                    to_do += N
            basins.append(size)        
            print_bool(d_map)
            print()
            # end of current basin
    return basins

def print_bool(d_map : [[bool]]):
    for line in d_map:
        line_str = ''
        for char in line:
            if char:
                line_str += '1'
            else:
                line_str += '0'
        print(line_str)

def get_neighbours(x : int, y : int, h_map : [[int]], d_map : [[bool]]) -> [int, int]:
    h = len(h_map)
    w = len(h_map[0])
    n = []


    # up [y-1]
    if not y == 0:
        if not d_map[y-1][x]:
            d_map[y-1][x] = True
            if not h_map[y-1][x] == 9:
                n.append([y-1, x])  
    # dn [y+1]
    if not y == h-1:
        if not d_map[y+1][x]:
            d_map[y+1][x] = True
            if not h_map[y+1][x] == 9:
                n.append([y+1, x])
    # le [x-1]
    if not x == 0:
        if not d_map[y][x-1]:
            d_map[y][x-1] = True
            if not h_map[y][x-1] == 9:
                n.append([y, x-1])
    # ri [x+1]
    if not x == w-1:
        if not d_map[y][x+1]:
            d_map[y][x+1] = True
            if not h_map[y][x+1] == 9:
                n.append([y, x+1])
    return n


if __name__ == '__main__':

    h_map = open_file('input')
    basins = get_basins(h_map)    
    big = [0, 0, 0]
    for basin in basins:
        if big[0] < basin:
            big[2] = big[1]
            big[1] = big[0]
            big[0] = basin
        elif big[1] < basin:
            big[2] = big[1]
            big[1] = basin
        elif big[2] < basin:
            big[2] = basin
    print(big)
    print(big[0]*big[1]*big[2])
    print(basins)

