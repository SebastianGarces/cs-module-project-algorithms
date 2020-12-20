'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''


def single_number(arr):
    '''
    my_list = []
    for i in arr:
        if i in my_list:
            my_list.remove(i)
        else:
            my_list.append(i)
    return my_list.pop()
    '''

    '''
    XOR "exclusive or" operator ^
    O(1)

    a | b | a ^ b
    --|---|------
    0 | 0 | 0
    0 | 1 | 1
    1 | 0 | 1
    1 | 1 | 0

    Example: 7 ^ 10
    In binary: 0111 ^ 1010
      0111
    ^ 1010
    ======
      1101 = 13

    Example 2:
    10 ^ 5
    >> 15
    15 ^ 5
    >> 10

    '''

    a = 0
    for i in arr:
        a ^= i
    return a


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 4, 1, 4, 5, 3, 3, 7, 9, 5, 7]

    print(f"The odd-number-out is {single_number(arr)}")
