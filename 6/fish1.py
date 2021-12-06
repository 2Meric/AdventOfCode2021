class Fish:
    def __init__(self, dtr : int):
        self.dtr = dtr          # days to reproduce

    def get_dtr(self):
        return self.dtr

    def pass_day(self, fish_list : [str]) -> bool:
        #dtr = self.dtr
        if self.dtr == 0:
            # spawn new fish
            self.dtr = 6
            return True
        else:
            self.dtr -= 1
            return False

def open_file(input : str) -> [str]:
    fish_list = []
    file = open(input, 'r')
    dtrs = file.read().split(',')
    for dtr in dtrs:
        fish_list.append(Fish(dtr = int(dtr)))
    file.close()
    return fish_list


def pass_day(fish_list : [str]):
    old_fish_list = fish_list.copy()
    for fish in old_fish_list:
        fish.pass_day


if __name__ == "__main__":
    fish_list = open_file('example')
    days_to_pass = 80
    for i in range(days_to_pass+1):
        dtrs = []
        print("Day "+str(i))
        old_fish_list = fish_list.copy()
        for fish in old_fish_list:
            dtrs.append(fish.get_dtr())
            add_fish = fish.pass_day(fish_list = fish_list)
            if add_fish:
                fish_list.append(Fish(dtr = 8))
        #print(dtrs)
        answer = len(dtrs)
        print("current number of fish: "+str(answer))
