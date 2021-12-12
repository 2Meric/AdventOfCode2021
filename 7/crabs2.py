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
        d = abs(height-ideal)
        fuel_sum += (d+1)*d/2
    return fuel_sum

def find_optimal(heights : [int]):
    curr_fuel = fuel_amount(heights, 0)
    next_fuel = fuel_amount(heights, 1)
    i = 0
    while curr_fuel > next_fuel:
        curr_fuel = next_fuel
        next_fuel = fuel_amount(heights, i+2)
        i += 1
    print("Ideal = "+str(i))
    print("Fuel = "+str(curr_fuel))

if  __name__ == '__main__':
    heights = open_file('input')
    find_optimal(heights)
