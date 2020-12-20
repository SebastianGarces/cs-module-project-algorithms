'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''

from collections import deque


def sliding_window_max(nums, k):

    # max_vals = [0] * (len(nums) - k + 1)

    # for i in range(len(max_vals)):
    #     current_elem = nums[i]

    #     for j in range(1, k):
    #         if nums[i + j] > current_elem:
    #             current_elem = nums[i + j]

    #     max_vals[i] = current_elem

    # return max_vals

    max_vals = []
    q = deque()

    # Process first k (or first window) elements of array
    for i in range(k):

        # For every element, the previous smaller elements are useless, remove from q
        while q and nums[i] >= nums[q[-1]]:
            q.pop()

        # Add new element at rear of queue
        q.append(i)

    # Process rest of the elements, from arr[k] to nums[len(nums)-1]
    for i in range(k, len(nums)):

        # The element at the front of the queue is the largest element of previous window, append to max_vals
        max_vals.append(nums[q[0]])

        # Remove the elements that are out of this window
        while q and q[0] <= i - k:

            # Remove from front of deque
            q.popleft()

        # Remove all elements smaller than the current one being added (useless elements)
        while q and nums[i] >= nums[q[-1]]:
            q.pop()

        # Add current element at the end of q
        q.append(i)

    # Append the maximum element of last window
    max_vals.append(nums[q[0]])

    return max_vals


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(
        f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
