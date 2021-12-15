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

def enlarge(r_map : [[int]]) -> [[int]]:
    w_o = len(r_map[0])
    h_o = len(r_map)

    new_map = [[0 for x in range(5 * w_o)] for y in range(5 * h_o)]

    for y_t in range(5):
        for x_t in range(5):

            for y_o, yline in enumerate(r_map):
                for x_o, r in enumerate(yline):
                    x = x_o + x_t * w_o
                    y = y_o + y_t * h_o
                    new_r = r + y_t + x_t
                    if new_r > 9:
                        new_r = new_r % 9
                    new_map[y][x] = new_r
    return new_map

def get_N(x : int, y : int, r_map : [[int]], done : [[int]]) -> [int]:
    # returns inactive Neighbours and sets them active in 'done'
    N = []

    x_s = len(r_map[0])
    y_s = len(r_map)
    
    r = r_map[y][x]

    if x > 0 and done[y][x-1] == 0:
        r = r_map[x - 1][y]
        N.append([x - 1, y, r])
        done[y][x-1] = 1
    if y > 0 and done[y-1][x] == 0:
        r = r_map[x][y - 1]
        N.append([x, y - 1, r])
        done[y-1][x] = 1
    if (x < (x_s - 1)) and (done[y][x+1] == 0):
        r = r_map[x + 1][y]
        N.append([x + 1, y, r])
        done[y][x+1] = 1
    if (y < (y_s - 1)) and done[y+1][x] == 0:
        r = r_map[x][y + 1]
        N.append([x, y + 1, r])
        done[y+1][x] = 1
    return N

def step(active : [int, int, int], r_map : [[int]], done : [[int]]) -> [int, int, int]:
    # each step:
    # count active nodes down
    # if an active node reaches 0: 
    #   it activates any not yet activated neighbours: starting at their risk level (time before broadcast)
    #   it becomes done (cant be activated again): It took i steps to reach
    
    next_active = []
    for idx, a in enumerate(active):
        x = a[0]    # x-coordinate
        y = a[1]    # y-coordinate
        c = a[2]    # count
        c -= 1
        if c == 0:
            # set neighbours active
            next_active += get_N(x, y, r_map, done)
            # this node has been reached: set it to done
            done[y][x] = 2
        else:
            # this node has not been reached yet (needs c more steps):
            next_active.append([x, y, c])
    return next_active

def print_map(r_map : [[int]]):
    for yline in r_map:
        line = ''
        for char in yline:
            line += str(char) + ','
        print(line)

if __name__ == '__main__':
    r_map = open_file('input')
    r_map = enlarge(r_map)
    # set start risk to 0
    r_map[0][0] = 0

    # 0 - inactive, 1 - active, 2 - done
    done = [[0 for x in r_map[0]] for y in r_map]

    # initialize active [x, y, risk]
    active = []
    active.append([0, 0, 1])
    
    # start stepping
    for i in range(100000):
        # step until we reach bottom right
        print('step ' + str(i))
        active = step(active, r_map, done)
        if done[len(r_map) - 1][len(r_map[0]) - 1] == 2:
            print('we done: bottom right reached after ' + str(i) + ' steps!')
            break



