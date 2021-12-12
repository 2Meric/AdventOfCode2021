
def open_file(input : str) -> [[str], [str]]:
    file = open(input, 'r')
    lines = file.read().split('\n')
    lines.pop()
    #lpart = lines[0].split(' | ')
    #signal = lpart[0].split()
    #print(signal)
    signals = [['' for x in range(10)] for y in range(len(lines))]
    outputs = [['' for x in range(4)] for y in range(len(lines))]
    i = 0
    for line in lines:
        lpart = line.split(' | ')
        signals[i] = lpart[0].split()
        outputs[i] = lpart[1].split()
        i += 1
    return [signals, outputs]

def deduce_num(signal : str) -> int:
    l = len(signal)
    # 2 -> 1
    if l == 2:
        return 1
    # 3 -> 7
    if l == 3:
        return 7
    # 4 -> 4
    if l == 4:
        return 4
    # 7 -> 8
    if l == 7:
        return 8
    return 0

def to_bin(signal : str) -> [bool]:
    chars = [char for char in signal]
    bin_seg = [False]*7
    for s in chars:
        if s == 'a':
            bin_seg[0] = True
        elif s == 'b':
            bin_seg[1] = True
        elif s== 'c':
            bin_seg[2] = True
        elif s == 'd':
            bin_seg[3] = True
        elif s == 'e':
            bin_seg[4] = True
        elif s == 'f':
            bin_seg[5] = True
        elif s == 'g':
            bin_seg[6] = True
        else:
            print("ERROR: UKNOWN CHARACTER FOUND IN SIGNAL!")
            return
    #print(signal, bin_seg)
    return bin_seg

def and_(a : [bool], b : [bool]) -> [bool]:
    if not (len(a) == len(b)):
        print("ERROR: BOOLEAN NOT SAME LENGTH")
        return
    c = [False]*len(a)
    for i in range(len(a)):
        c[i] = a[i] and b[i]
    return c

def is_nin():
    ifand(one, unk)

def get_all_numbers(signals : [str]) -> [[bool]]:

    bin_num = [[False]*7]*10
    
    # First get 1, 4, 7, 8
    for signal in signals:
        num = deduce_num(signal)
        if num:
            bin_num[num] = to_bin(signal)

    # Second get 6, 9 by: 
    for signal in signals:
        l = len(signal)
        if l == 6:
            # 0, 6, 9
            bin_n = to_bin(signal)
            if sum(and_(bin_n, bin_num[1])) == 1:
                bin_num[6] = bin_n
            else:
                # 0, 9
                if sum(and_(bin_n, bin_num[4])) == 4:
                    bin_num[9] = bin_n
                else:
                    bin_num[0] = bin_n

    # get 2, 3, 5
    for signal in signals:
        l = len(signal)
        if l == 5:
            # 2, 3, 5
            bin_n = to_bin(signal)
            if sum(and_(bin_n, bin_num[1])) == 2:
                bin_num[3] = bin_n
            else:
                # 2, 5
                if sum(and_(bin_n, bin_num[6])) == 5:
                    bin_num[5] = bin_n
                else:
                    bin_num[2] = bin_n
    return bin_num



if __name__ == '__main__':
    [s, o] = open_file('input')
    
    output = [[0 for i in range(4)] for j in range(len(o))]
    
    i = 0
    for signals in s:
        outs = o[i]
        bin_nums = get_all_numbers(signals)
        j = 0
        for out in outs:
            bin_out = to_bin(out)
            num = 0
            for bin_num in bin_nums:
                if bin_out == bin_num:
                    output[i][j] = num
                    break
                num += 1
            j += 1
        i += 1
    print(output)
    
    # calculate answer
    answer = 0
    for number in output:
        n_str = ''
        for digit in number:
            n_str += str(digit)
        answer += int(n_str)
        print(n_str)
    print()
    print(answer)
            

