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

def get_insert(e0 : str, e1 : str, P : [str], I : [str]) -> str:
    # get the element that should be inserted between 'e0' and 'e1'
    for idx, p in enumerate(P):
        if p == e0 + e1:
            return I[idx]

def insert(E : str, P : [str], I : [str]) -> str:
    # insert elements in 'E'
    [e0, e1] = ['', '']
    E_i = ''        # inserts
    E_o = ''        # zipped output 
    for e in E:
        e0, e1 = e1, e
        if not e0: continue
        i = get_insert(e0, e1, P, I)
        E_i += i
    
    # zip E_z and E
    while(E_i):
        E_i, e_i = E_i[1:], E_i[0]
        E, e = E[1:], E[0]
        E_o += e + e_i
    E_o += E

    return E_o

def count(E : str):
    E_s = []    # elements seen before
    E_c = []    # times we ve encountered that element

    for e in E:
        new = True
        for idx, e_s in enumerate(E_s):
            if e == e_s:
                # seen before
                E_c[idx] += 1
                new = False
                break
        if new:
            # not seen before
            E_s.append(e)
            E_c.append(1)
   
    # largest, smallest:
    large = [E_s[0], E_c[0]]    
    small = [E_s[0], E_c[0]]    
    for idx, e_c in enumerate(E_c):
        if e_c > large[1]:
            large = [E_s[idx], E_c[idx]]
        elif e_c < small[1]:
            small = [E_s[idx], E_c[idx]]
    print(large)
    print(small)
    print(large[1] - small[1])



if __name__ == '__main__':
    [E, P, I] = open_file('input')
    steps = 10
    for s in range(steps):
        print(s)
        E = insert(E, P, I)
        print(E)
    count(E)
