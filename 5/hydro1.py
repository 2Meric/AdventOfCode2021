class line:
    def __init__(self, x1 : int, y1 : int, x2 : int, y2 : int):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        try:
            [self.diagonal, self.points] = self.process()
        except:
            print('SELF.PROCESS NOT OK')
            pass

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
            print("horizontal points added")
            return [False, points]
        # Line is vertical:
        if vertical:
            for y in y_range:
                x = x_range[0]
                points.append([x, y])
            print("vertical points added")
            return [False, points]
        # Line is diagonal
        if diagonal:
            for i in range(len(x_range)):
                x = x_range[i]
                y = y_range[i]
                points.append([x, y])
            print("diagonal points added")
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
        
def create_map(points : [int, int]):
    # Maybe another day
    x_min = 0
    x_max = 0
    y_min = 0
    y_max = 0
    for point in points:
        x = point[0]
        y = point[1]
        # adjust window size
        if x < x_min:
            x_min = x
        if x > x_max:
            x_max = x;
        if y < y_min:
            y_min = y
        if y > y_max:
            y_max = y

def count_duplicate_points(points : [int, int]) -> int:
    count = 0
    vent_map = [0]*1000000
    for point in points:
        x = point[0]
        y = point[1]
        idx = x + y*1000
        vent_map[idx] += 1
    for point in vent_map:
        if point > 1:
            count += 1
    return count

if __name__ == "__main__":
    lines = open_file('input')
    # Only horizontal and vertical (hv) lines
    hv_lines = []
    points = []
    for line in lines:
        if not line.is_diagonal():
            hv_lines.append(line)
    for line in hv_lines:
        line_points = line.as_points()
        for point in line_points:
            points.append(point)
    answer = count_duplicate_points(points)
    print(answer)
