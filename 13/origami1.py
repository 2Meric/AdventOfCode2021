def open_file(input : str) -> [[int, int], [int, int]]:
    file = open(input, 'r')
    [points_str, folds_str] = file.read().split('\n\n')
    # points
    points_xy = points_str.split()
    points = [[int(i) for i in xy.split(',')] for xy in points_xy]
    # folds
    folds = []
    folds_xy = folds_str.split('\n')
    folds_xy.pop()
    for line in folds_xy:
        line = line[11:]
        [x, y] = [0, 0]
        if line[0] == 'x':
            # fold along:
            x = int(line[2:])
        else:
            # fold along:
            y = int(line[2:])
        # line:
        folds.append([x, y])

    return [points, folds]

def create_map(points : [int, int]) -> [[int]]:
    # calculate mapsize
    [x_size, y_size] = [0, 0]
    for point in points:
        [x, y] = point
        x_size = x if x > x_size else x_size
        y_size = y if y > y_size else y_size
    # create empty map
    bitmap = [[0 for i in range(x_size+1)] for i in range(y_size+1)]
    # create points on map
    for point in points:
        [x, y] = point
        bitmap[y][x] += 1
    return bitmap


def draw_map(bitmap : [[int]]):
    # image size
    y_size = len(bitmap)
    x_size = len(bitmap[0])  
    
    # window
    [x0, y0, x1, y1] = [0, 0, x_size, y_size]
    

    border = '╔'
    for x in range(x0, x1, 1):
        border += '══'
    border += '╗'
    print(border)

    for y in range(y0, y1, 1):
        line = '║'
        for x in range(x0, x1, 1):
            symbol = bitmap[y][x]
            # 5 values per pixel
            if symbol > 4:
                symbol = 4
            line += get_symbol(symbol)
        line += '║'
        print(line)

    border = '╚'
    for x in range(x0, x1, 1):
        border += '══'
    border += '╝'
    print(border)

def get_symbol(s : int) -> str:
    if s == 0:
        return '  '
    if s == 1: 
        return '░░'
    if s == 2:
        return '▒▒'
    if s == 3:
        return '▓▓'
    if s == 4:
        return '██'


if __name__ == '__main__':
    [points, folds] = open_file('input')
    bitmap = create_map(points)

    folded = 0
    for fold in folds:
        folded += 1
        [x_f, y_f] = fold
        # x positions dont change
        if x_f == 0:
            # move points up
            for i in range(len(points)):
                [x, y] = points[i]
                if y > y_f:
                    # move point up
                    y = y_f + y_f - y
                # update point
                points[i] = [x, y]
        if y_f == 0:
            # move points left
            for i in range(len(points)):
                [x, y] = points[i]
                if x > x_f:
                    # move point left
                    x = x_f + x_f - x
                # update points
                points[i] = [x, y]

        bitmap = create_map(points)
        cnt = 0
        for y in bitmap:
            for p in y:
                cnt += 1 if p > 0 else 0
        print('FOLDED ' + str(folded) + ' TIMES. ' + str(cnt) + ' POINTS LEFT')
    draw_map(bitmap)

