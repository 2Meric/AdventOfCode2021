def open_file(input : str) -> [str]:
    file = open(input, 'r')
    lines = file.read().split()
    return lines

def check(line : str) -> [str, str]:

    print(line)

    cs = ''
    for c in line:

        if c == '(' or c == '[' or c == '{' or c == '<':
            cs += c

        if c == ')':
            if cs[-1] == '(':
                # correct
                cs = cs[0:-1]
            else:
                # incorrect
                print('needs '+cs[-1]+', got )')
                return [')', cs[::-1]]

        if c == ']':
            if cs[-1] == '[':
                # correct
                cs = cs[0:-1]
            else:
                # incorrect
                print('needs '+cs[-1]+', got ]')
                return [']', cs[::-1]]

        if c == '}':
            if cs[-1] == '{':
                # correct
                cs = cs[0:-1]
            else:
                # incorrect
                print('needs '+cs[-1]+', got }')
                return ['}', cs[::-1]]

        if c == '>':
            if cs[-1] == '<':
                # correct
                cs = cs[0:-1]
            else:
                # incorrect
                print('needs '+cs[-1]+', got >')
                return ['>', cs[::-1]]
        print(cs)
    return ['x', cs[::-1]]

if __name__ == '__main__':
    lines = open_file('input')
    
    score1 = 0
    score2 = []
    i = 0
    for line in lines:
        
        [c, cs] = check(line)
        if c == ')':
            score1 += 3
        elif c == ']':
            score1 += 57
        elif c == '}':
            score1 += 1197
        elif c == '>':
            score1 += 25137
        else:
            #print(cs)
            # autocomplete
            score = 0
            for c_a in cs:
                if c_a == '(':
                    score *= 5
                    score += 1
                if c_a == '[':
                    score *= 5
                    score += 2
                if c_a == '{':
                    score *= 5
                    score += 3
                if c_a == '<':
                    score *= 5
                    score += 4
            score2.append(score)

    print(score1)
    print(score2)
    score2.sort()
    print(score2)
    if len(score2) % 2:
        # odd
        i = int((len(score2)+1)/2)-1
    else:
        # eveni
        print('error: score2 length is even (no middle)')
        i = 0
    print(score2[i])
