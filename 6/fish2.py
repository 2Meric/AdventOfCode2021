def open_file(input : str) -> [int]:
    tdr_fish = [0]*9
    file = open(input, 'r')
    dtrs = file.read().split(',')
    for i in range(len(dtrs)):
        fish_dtr = dtrs[i]
        tdr_fish[int(fish_dtr)] += 1
    file.close()
    return tdr_fish

def pass_day(tdr_fish : [str]) -> [str]:
    new_fish = tdr_fish[0]
    for i in range(len(tdr_fish)-1):
        tdr_fish[i] = tdr_fish[i+1]
    tdr_fish[8] = new_fish
    tdr_fish[6] += new_fish
    return tdr_fish

if __name__ == "__main__":
    tdr_fish = open_file('input')
    days_to_pass = input("Days to pass :")
    for i in range(int(days_to_pass)+1):
        #print("Day "+str(i))
        #print(tdr_fish)
        fish_num = 0
        for tdr in tdr_fish:
            fish_num += tdr
        if i % 10000 == 0:
            print(str(i))
        #print("current number of fish: "+str(fish_num))
        tdr_fish = pass_day(tdr_fish)
    print(fish_num)
