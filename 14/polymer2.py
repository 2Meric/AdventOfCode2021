def open_file(input) -> [str, [str], str]:
    E = ''      # Elements in polymer
    P = []      # Pairs
    I = []      # Inserts
    file = open(input, 'r')
    [E, pairs_str] = file.read().split('\n\n')
    pairs = pairs_str.split('\n')[:-1]
    for pair in pairs:
        [p, i] = pair.split(' -> ')
        P.append(p)
        I.append(i)
    return [E, P, I]

def count(P_c : [int], P : [str]):
    chars = []
    char_c = []
    for idx, p in enumerate(P):
        char0 = p[0]
        char1 = p[1]
        # amount
        amount = P_c[idx]
        if not amount:
            continue
        new0 = True
        new1 = True
        for idx, char in enumerate(chars):
            # already in chars?
            if char0 == char:
                new0 = False
                char_c[idx] += amount
            if char1 == char:
                new1 = False
                char_c[idx] += amount
            if not new0 and not new1:
                break
        if new0:
            # new char0
            chars.append(char0)
            # case: new double
            if char0 == char1:
                char_c.append(amount*2)
                continue
            char_c.append(amount)
        if new1:
            # new char1
            chars.append(char1)
            char_c.append(amount)
    large = [char_c[0], chars[1]]
    small = [char_c[0], chars[1]]
    for idx, char in enumerate(chars):
        count = char_c[idx]
        #print(char, count)
        
        if count % 2:
            # odd
            count = count+1
        #print(count)
        count = int(count/2)

        if large[0] < count:
            large[0] = count
            large[1] = char
        if small[0] > count:
            small[0] = count
            small[1] = char

        print(char, count)
        print(large)
        print(small)
        print(large[0] - small[0])

def pair_idx(p : str, P : [str]) -> int:
    for idx, pair in enumerate(P):
        if p == pair:
            return idx

def count_pairs(E : str, P : [str]) -> [int]:
    P_c = [0 for idx in P]
    for e_idx in range(len(E)-1):
        p_e = E[e_idx] + E[e_idx+1]
        for idx, p in enumerate(P):
            if p_e == p:
                P_c[idx] += 1
    return P_c


def insert_pairs(P_c : [int], P : [str], I : [str]) -> [int]:
    P_c2 = [0 for idx in P]
    for idx, p_c in enumerate(P_c):
        p = P[idx]      #pp
        i = I[idx]      #i
        pi = p[0] + i
        ip = i + p[1]
        pi_idx = pair_idx(pi, P)
        ip_idx = pair_idx(ip, P)
        P_c2[pi_idx] += p_c
        P_c2[ip_idx] += p_c
    return P_c2

def print_pair_list(P_c : [int], P : [str]):
    for idx, p in enumerate(P):
        print(p, P_c[idx])

if __name__ == '__main__':
    [E, P, I] = open_file('input')
    steps = 40
    # create initial pair list
    P_c = count_pairs(E, P)
    for s in range(steps):
        print('___STEP '+str(s)+'___')
        print_pair_list(P_c, P)
        print('COUNT:')
        count(P_c, P)
        P_c = insert_pairs(P_c, P, I)
    print('___STEP '+str(s+1)+'___')
    print_pair_list(P_c, P)
    print('___COUNT:___')
    count(P_c, P)
