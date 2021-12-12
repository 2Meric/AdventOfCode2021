def open_file(input : str) -> [int]:
    file = open(input, 'r')
    strings = file.read().split(',')
    ints = []
    for string in strings:
        ints.append(int(string))
    return ints


def fuel_amount(heights : [int], ideal : int) -> int:
    fuel_sum = 0
    for height in heights:
        fuel_sum += abs(height-ideal)
    return fuel_sum

if  __name__ == '__main__':
    heights = open_file('input')
    print(heights)
    h_length = len(heights)
    print(h_length)
    if h_length % 2:
        # uneven
        middle = (h_length+1)/2
        print("odd: middle is ["+str(middle)+"]")
    else:
        # even
        middle = h_length/2
        print("even: middle is ["+str(middle)+"-"+str(middle+1)+"]")
    heights.sort()
    print(heights)
    ideal = heights[int(middle)]
    fuel = fuel_amount(heights, ideal)
    print("Ideal Height = "+str(ideal)+", Fuel consumed = "+str(fuel))
