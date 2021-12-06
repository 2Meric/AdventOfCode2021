class Board:
    def __init__(self, numbers : [int], active : [bool]):
        self.numbers = numbers
        self.active = active
        self.completed = False

    def is_done(self) -> bool:
        return self.completed

    def get_board(self)->str:
        numbers = self.numbers
        numbers_str = ""
        for i in range(25):
            if len(str(numbers[i])) == 1:
                numbers_str += " "
            numbers_str += str(numbers[i])
            if i%5 == 4:
                numbers_str += "\n"
            else:
                numbers_str += " "
        return numbers_str

    def get_active(self) -> str:
        active = self.active
        active_str = ""
        for i in range(25):
            if active[i]:
                active_str += "1"
            else:
                active_str += "0"
            if i%5 == 4:
                active_str += "\n"
            else:
                active_str += " "
        return active_str

    def set_active(self, value : int):
        # set rolled number to True in active
        try:
            idx = self.numbers.index(value)
            self.active[idx] = True
        except ValueError:
            pass
            #print("value not in list")

    def add_unmarked(self) -> int:
        active = self.active
        numbers = self.numbers
        added_unmarked = 0
        idx = 0
        for marked in active:
            if not marked:
                added_unmarked += numbers[idx]
            idx += 1
        return added_unmarked


    def is_bingo(self) -> bool:
        active = self.active
        numbers = self.numbers
        completed = self.completed
        if completed:
            return True
        for i in range(0,5):
            if active[i] and active[i+5] and active[i+10] and active[i+15] and active[i+20]:
                self.completed = True
                return True
            if active[i*5] and active[i*5+1] and active[i*5+2] and active[i*5+3] and active[i*5+4]:
                self.completed = True
                return True
        return False

def open_file(input: str)->[[str],[int]]:
    file = open(input, 'r')
    strspl = file.read().split('\n\n')
    rolls = list(map(int, strspl[0].split(',')))
    boards = []
    for i in range(1, len(strspl)):
        strspl[i] = strspl[i].split()
        boards.append(Board(numbers = list(map(int, strspl[i])), active = [False for i in range(25)]))
    file.close()
    return [boards, rolls]

def update_boards(boards : [str], roll : int, completed_boards : [int]) -> [int]:
    idx = 0
    for board in boards:
        board.set_active(value = roll)
        if not board.is_done():
            if board.is_bingo():
                completed_boards.append(idx)
        idx += 1
    return completed_boards

if __name__ == "__main__":
    #open_file("example")
    [boards, rolls] = open_file("input")
    completed_boards = []
    for roll in rolls:
        print("checking roll "+str(roll))
        completed_boards = update_boards(boards, roll, completed_boards)
        print(completed_boards)
        if len(completed_boards) == len(boards):
            # We are done
            print("We Are Done! : ")
            print(completed_boards)
            last_board_idx = completed_boards[-1]
            unmarked_sum = boards[last_board_idx].add_unmarked()
            answer = unmarked_sum * roll
            print("The Last Roll ("+str(roll)+") Completed the Last Board:" )
            print(boards[last_board_idx].get_active)
            print(boards[last_board_idx].get_board)
            print("The Unmarked Sum ("+str(unmarked_sum)+") multiplied with the Last Roll is: "+str(answer))
            break
