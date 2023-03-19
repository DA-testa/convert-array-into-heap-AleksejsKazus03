# python3

def sift_down(data, swaps, i):
    n = len(data)
    min_index = i
    l = 2 * i + 1
    if l < n and data[l] < data[min_index]:
        min_index = l
    r = 2 * i + 2
    if r < n and data[r] < data[min_index]:
        min_index = r
    if i != min_index:
        data[i], data[min_index] = data[min_index], data[i]
        swaps.append((i, min_index))
        sift_down(data, swaps, min_index)
        
def build_heap(data):
     n = len(data)
    swaps = []
    for i in range(n // 2, -1, -1):
        sift_down(data, swaps, i)
    return swaps
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)


    return swaps


def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file


    # input from keyboard
   input_type = input().strip()
    if input_type == 'I':
        n = int(input())
        data = list(map(int, input().split()))
    elif input_type == 'F':
        with open('input.txt') as f:
            n = int(f.readline())
            data = list(map(int, f.readline().split()))
    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
