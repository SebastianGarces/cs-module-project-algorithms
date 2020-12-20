'''
Input: an integer
Returns: an integer
'''


def eating_cookies(n, arr=None):
    # arr = [0, 0, 1]
    # i = 0

    # while i < n:
    #     arr.append(arr[0] + arr[1] + arr[2])
    #     arr.pop(0)
    #     i += 1

    # return arr[2]

    # iterative, O(n) time, O(n) space
    if n <= 1:
        return 1

    if n == 2:
        return 2

    if arr == None:
        arr = [0 for i in range(n+1)]

    arr[0], arr[1], arr[2] = 1, 1, 2

    for i in range(3, n+1):
        arr[i] = arr[i-1] + arr[i-2] + arr[i-3]

    return arr[n]


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(
        f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
