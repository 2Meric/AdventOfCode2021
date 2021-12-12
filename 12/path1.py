class Cave():
    def __init__(self, name : str):
        self.name = name
        self.big = name.isupper()
        self.N = []
        self.start = (name == 'start')
        self.end = (name == 'end')

    def get_name(self) -> str:
        return self.name

    def is_big(self) -> bool:
        return self.big

    def get_N(self) -> [int]:
        return self.N

    def add_n(self, n : int):
        self.N.append(n)

def get_idx(name : str, caves : str) -> int:
    i = 0
    for cave in caves:
        if name == cave.get_name():
            return i
        i += 1 
    return -1

def open_file(input : str) -> [str]:
    caves = []
    file = open(input, 'r')
    lines = file.read().split()
    
    for line in lines:
        cave = line.split('-')
        
        idx0 = get_idx(cave[0], caves)
        idx1 = get_idx(cave[1], caves)

        if idx0 == -1:
            # add new cave
            name = cave[0]
            idx0 = len(caves)
            new_cave = Cave(name)
            caves.append(new_cave)

        if idx1 == -1:
            # add new cave
            name = cave[1]
            idx1 = len(caves)
            new_cave = Cave(name)
            caves.append(new_cave)
        
        # add neighbours
        caves[idx0].add_n(idx1)
        caves[idx1].add_n(idx0)

    return caves

def print_map(caves : [str]):
    i = 0
    for cave in caves:
        print(cave.get_name() + " [" + str(i) + "]")
        N = cave.get_N()
        line = ''
        for n in N:
            name = caves[n].get_name()
            line += name
            line += ' '
        print(line)
        print()
        i += 1

def contains(path : [int], i : int) -> bool:
    for p in path:
        if p == i:
            return True
    return False

def get_start(caves : [str]) -> int:
    i = 0
    for cave in caves:
        name = cave.get_name()
        if name == 'start':
            return i
        i += 1

def get_end(caves : [str]) -> int:
    i = 0
    for cave in caves:
        name = cave.get_name()
        if name == 'end':
            return i
        i += 1

def find_paths(caves : str) -> [[int]]:
    # finished paths
    paths = []

    # packet has a path (packets[path]) and destination (dests)
    packets = []
    path = []
    dests = []

    start = get_start(caves)
    end = get_end(caves)

    print('start: ' + str(start))
    print('end:   ' + str(end))

    # initialize an empty packet for the start cave    
    packets.append(path.copy())
    dests.append(start)

    while packets:
        # eval next packet (we are at node i)
        
        # destroy incoming packet
        path = packets.pop()
        i = dests.pop()
        
        # add current node (cave) to path
        path.append(i)

        # Get neighbours that we may send packets to
        N = caves[i].get_N()
        for n in N:
            
            # if the destination is the end node --> This is a complete path
            if n == end:                
                paths.append(path.copy() + [n])
                continue

            # if neighbour is a small cave we already visited --> not valid neighbour (don't send packet)
            if contains(path, n) and not caves[n].is_big():
                continue
                        
            # add the outgoing packet to packets
            packets.append(path.copy())
            dests.append(n)
    
    return paths


if __name__ == '__main__':
    caves = open_file('input')
    paths = find_paths(caves)
    
    print('::::::::::::::::: start - end PATHS :::::::::::::::::::::')
    ends = 0
    for path in paths:
            ends +=1
            line = ''
            for idx in path:
                line += caves[idx].get_name()
                line += ' '
            print(line)

    print(ends)
