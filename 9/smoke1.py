
def open_file(input : str) -> [[int]]:
    file = open(input, 'r')
    lines = file.read().split()
    h = len(lines)
    w = len(lines[0])
    height_map = [[int(x) for x in lines[y]] for y in range(h)]
    return height_map

def get_mins(h_map : [[int]]) -> [int, int]:
    h = len(h_map)
    w = len(h_map[0])
    mins = []
    # Corners
    if h_map[0][0] < h_map[0][1] and h_map[0][0] < h_map[1][0]:
        mins.append([0, 0])
    if h_map[h-1][0] < h_map[h-1][1] and h_map[h-1][0] < h_map[h-2][0]:
        mins.append([h-1, 0])
    if h_map[0][w-1] < h_map[0][w-2] and h_map[0][w-1] < h_map[1][w-1]:
        mins.append([0, w-1])
    if h_map[h-1][w-1] < h_map[h-1][w-2] and h_map[h-1][w-1] < h_map[h-2][w-1]:
        mins.append([h-1, w-1])

    # Borders
    # Left Right
    for y in range(1, len(h_map)-1, 1):
        # h_map[y][0]
        if h_map[y][0] < h_map[y-1][0] and h_map[y][0] < h_map[y][1] and h_map[y][0] < h_map[y+1][0]:
            mins.append([y, 0])
        # h_map[y][w-1]
        if h_map[y][w-1] < h_map[y-1][w-1] and h_map[y][w-1] < h_map[y][w-2] and h_map[y][w-1] < h_map[y+1][w-1]:
            mins.append([y, w-1])
    # Top Bot
    for x in range(1, len(h_map[0])-1, 1):
        # h_map[0][x]
        if h_map[0][x] < h_map[0][x-1] and h_map[0][x] < h_map[1][x] and h_map[0][x] < h_map[0][x+1]:
            mins.append([0, x])
        # h_map[h-1][x]
        if h_map[h-1][x] < h_map[h-1][x-1] and h_map[h-1][x] < h_map[h-2][x] and h_map[h-1][x] < h_map[h-1][x+1]:
            mins.append([h-1, x])

    for y in range(1, h-1, 1):
        for x in range(1, w-1, 1):
            h = h_map[y][x]
            h_up = h_map[y-1][x]
            h_dn = h_map[y+1][x]
            h_le = h_map[y][x-1]
            h_ri = h_map[y][x+1]
            if h < h_up and h < h_dn and h < h_le and h < h_ri:
                mins.append([y, x])
    return mins

if __name__ == '__main__':
    h_map = open_file('input')
    mins = get_mins(h_map)
    
    answer = 0
    for m in mins:
        y = m[0]
        x = m[1]
        h = h_map[y][x]
        r = h + 1
        answer += r
        print("minimum ["+str(h)+"] at ("+str(x)+", "+str(y)+")")
    print('answer: '+ str(answer))



