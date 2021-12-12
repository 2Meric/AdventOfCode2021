class line:
    def __init__(self, x1 : int, y1 : int, x2 : int, y2 : int):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.bitmap_points()
        try:
            [self.diagonal, self.points] = self.process()
        except:
            print('SELF.PROCESS NOT OK')
            pass

    def get_bitmap_points(self) -> [int, int]:
        return self.bitmap_points

    def bitmap_points(self):
        start = [3*self.x1, 3*self.y1]
        end = [3*self.x2, 3*self.y2]
        
        if start[0] > end[0]:
            x_range = range(start[0], end[0]-1, -1)
        else:
            x_range = range(start[0], end[0]+1)
        if start[1] > end[1]:
            y_range = range(start[1], end[1]-1, -1)
        else:
            y_range = range(start[1], end[1]+1)

        
        diagonal = True
        if len(y_range) == 1:
            y_range = [y_range[0]]*len(x_range)
            diagonal = False
        elif len(x_range) == 1:
            x_range = [x_range[0]]*len(y_range)
            diagonal = False

        bitmap_points = []
        for i in range(len(x_range)):
            x = x_range[i]
            y = y_range[i]
            bitmap_points.append([x, y])

        self.bitmap_points = bitmap_points




    def get_x1(self) -> int:
        return self.x1

    def is_diagonal(self) -> bool:
        return self.diagonal

    def as_points(self) -> [int, int]:
        return self.points

    def process(self) -> [bool, [int, int]]:
        x1 = self.x1
        y1 = self.y1
        x2 = self.x2
        y2 = self.y2
        points = []
        is_diagonal = False
        if x1 > x2:
            x_range = range(x1, x2-1, -1)
        else:
            x_range = range(x1, x2+1)
        if y1 > y2:
            y_range = range(y1, y2-1, -1)
        else:
            y_range = range(y1, y2+1)
        horizontal = len(y_range) == 1
        vertical = len(x_range) == 1
        diagonal = len(x_range) == len(y_range)
        # Check if valid line
        if not (horizontal or vertical or diagonal):
            print("Error: not a valid line")
            print(x_range)
            print(y_range)
            return
        # Line is horizontal:
        if horizontal:
            for x in x_range:
                y = y_range[0]
                points.append([x, y])
            self.type = '_'
            return [False, points]
        # Line is vertical:
        if vertical:
            for y in y_range:
                x = x_range[0]
                points.append([x, y])
            self.type = '|'
            return [False, points]
        # Line is diagonal
        if diagonal:
            for i in range(len(x_range)):
                x = x_range[i]
                y = y_range[i]
                points.append([x, y])
            return [True, points]
        print("something went wrong")
        return

def open_file(input : str) -> [str]:
    file = open(input, 'r')
    lines_str = file.read().split('\n')
    lines_str.pop()
    lines = []
    for line_str in lines_str:
        [start, end] = line_str.split(' -> ')
        [x1, y1] = start.split(',')
        [x2, y2] = end.split(',')
        lines.append(line(x1 = int(x1), y1 = int(y1), x2 = int(x2), y2 = int(y2)))
    file.close()
    return lines
        
def draw_map(bitmap : [int], size : [int], window : [int]):

    x_min = size[0]
    y_min = size[1]
    x_max = size[2]
    y_max = size[3]

    x_size = x_max - x_min
    y_size = y_max - y_min

    
    x0 = window[0] % x_size
    y0 = window[1] % y_size
    x1 = window[2] % x_size
    y1 = window[3] % y_size

    border = '╔'
    for x in range(x0, x1, 1):
        border += '══'
    border += '╗'
    print(border)

    for y in range(y0, y1, 1):
        line = '║'
        for x in range(x0, x1, 1):
            symbol = bitmap[x + y*x_max]
            if symbol > 4:
                symbol = 4
            line += get_symbol3(symbol)
        line += '║'
        print(line)

    border = '╚'
    for x in range(x0, x1, 1):
        border += '══'
    border += '╝'
    print(border)

def get_symbol3(s : int) -> str:
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




def count_duplicate_points(points : [int, int]) -> int:
    count = 0
    vent_map = [0]*9000000
    for point in points:
        x = point[0]
        y = point[1]
        idx = x + y*3000
        vent_map[idx] += 1
        # adjacent
        vent_map[idx+1] += 1
        vent_map[idx-1] += 1
        vent_map[idx+3000] +=1
        vent_map[idx-3000] += 1
        # diagonal
        vent_map[idx+3001] += 1
        vent_map[idx+2999] += 1
        vent_map[idx-3001] += 1
        vent_map[idx-2999] += 1
    create_map(vent_map)
    for point in vent_map:
        if point > 1:
            count += 1
    return count


def calculate_mapsize(points : [int, int], border : int) -> [int]:
    x_min = points[0][0]
    y_min = points[0][1]
    x_max = x_min
    y_max = y_min
    for point in points:
        x = point[0]
        y = point[1]
        #print(x,y)
        # min and max values
        if x < x_min:
            x_min = x
        elif x > x_max:
            x_max = x
        if y < y_min:
            y_min = y
        elif y > y_max:
            y_max = y
    # apply border
    x_min = x_min - border
    y_min = y_min - border
    x_max = x_max + border
    y_max = x_max + border
    return [x_min, y_min, x_max, y_max]

def create_bitmap(points : [int, int]) -> [[int], [int]]:
    
    [x_min, y_min, x_max, y_max] = calculate_mapsize(points, 6)
    
    x_size = x_max
    y_size = y_max

    bitmap = [0]*x_size*y_size
    
    print(x_size, y_size)
    print(x_size*y_size)
    for point in points:
        x = point[0]
        y = point[1]
        idx = x + y * x_size
        bitmap[idx] += 1
        # adjacent
        if True:
            bitmap[idx+1] += 1
            bitmap[idx-1] += 1
            bitmap[idx + x_size] +=1
            bitmap[idx - x_size] += 1
            # diagonal
            bitmap[idx + 1 + x_size] += 1
            bitmap[idx - 1 + x_size] += 1
            bitmap[idx - 1 - x_size] += 1
            bitmap[idx + 1 - x_size] += 1
    
    size = [x_min, y_min, x_max, y_max]
    return [bitmap, size]


if __name__ == "__main__":
    lines = open_file('example')
    # Only horizontal and vertical (hv) lines
    hv_lines = []
    points = []
    for line in lines:
        if not line.is_diagonal():
            hv_lines.append(line)
    for line in lines:
        line_points = line.get_bitmap_points()
        for point in line_points:
            points.append(point)
    
    
    [bitmap, size] = create_bitmap(points)

    window = [0, 0, 30, 30]

    draw_map(bitmap, size,  window)
    while(True):
        x = int(input('x'))
        y = int(input('y'))
        draw_map(bitmap, size, [x, y, x+30, y+30])
