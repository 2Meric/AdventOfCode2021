def open_file(input : str) -> [[int]]:
    E = [[0 for x in range(10)] for y in range(10)]
    file = open(input, 'r')
    lines = file.read().split()
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            E[y][x] = int(lines[y][x])
    return E

def neighbours(e_p : [int, int]) -> [int, int]:
    x_e = e_p[0]
    y_e = e_p[1]
    N = []
    for y_r in [-1, 0, 1]:
        for x_r in [-1, 0, 1]:
            if y_r == 0 and x_r == 0:
                # current point
                continue
            y = y_r + y_e
            x = x_r + x_e
            if y < 0 or y > 9:
                # out of y bounds
                continue
            if x < 0 or x > 9:
                # out of x bounds
                continue
            #print('+n [' + str(x) + ', ' + str(y) + ']')
            N.append([x, y])
    return N

def inc_E(E : [[int]]):
    E_f = [[False for x in range(10)] for y in range(10)]
    flashes = 0
    for y_s in range(10):
        for x_s in range(10):
            # check for next starting point (x_s, y_s)            
            to_do = []
            to_do.append([x_s, y_s]) 
            while to_do:
                [x, y] = to_do.pop()
                E[y][x] += 1
                if E[y][x] > 9 and not E_f[y][x]:
                    # flash + add neighbours to to_do
                    E_f[y][x] = True
                    to_do += neighbours([x, y])

def fls_E(E : [[int]]) -> int:
    F = 0
    for y in range(10):
        for x in range(10):
            if E[y][x] > 9:
                # flash
                E[y][x] = 0
                F += 1
    return F

def print_E(E : [[int]]):
    for E_y in E:
        line = ''
        for e in E_y:
            if e > 9:
                line += '█'
            else:
                line += str(e)
        print(line)
    print('\n')

def do_step(E : [[int]]) -> int:
    inc_E(E)
    F = fls_E(E)
    return F

if __name__ == "__main__":
    steps = 10000
    E = open_file('input')
    F = 0
    for s in range(steps):
        f = do_step(E)
        F += f
        if f == 100:
            break
        #print_E(E)
    print(s+1)
    print(F)
