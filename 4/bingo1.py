class Board:
    def __init__(self, numbers : [int], active : [bool]):
        self.numbers = numbers
        self.active = active

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


    def is_bingo(self) -> int:
        active = self.active
        numbers = self.numbers
        for i in range(0,5):
            if active[i] and active[i+5] and active[i+10] and active[i+15] and active[i+20]:
                # BINGO! (on column i)
                print("Bingo! On column "+str(i)+"!")
                return self.add_unmarked()
            if active[i*5] and active[i*5+1] and active[i*5+2] and active[i*5+3] and active[i*5+4]:
                # BINGO! (on row i)
                print("Bingo! On row "+str(i)+"!")
                return self.add_unmarked()
        return 0

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

def update_boards(boards : [str], roll) -> bool:
    for board in boards:
        board.set_active(value = roll)
        bingo_value = board.is_bingo()
        if bingo_value:
            print('Bingo!')
            print(board.get_active())
            print(board.get_board())
            print("Added Bingo Values: "+str(bingo_value))
            answer = roll * bingo_value
            print("Answer: "+ str(answer))
            return True
    return False

if __name__ == "__main__":
    #open_file("example")
    [boards, rolls] = open_file("input")
    for roll in rolls:
        print("checking roll "+str(roll))
        if update_boards(boards, roll):
            break
