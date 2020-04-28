# Longest Sequence with Two Unique Numbers
Hi, here's your problem today. This problem was recently asked by Facebook:

Given a sequence of numbers, find the longest sequence that contains only 2 unique numbers.

```
Example:
Input: [1, 3, 5, 3, 1, 3, 1, 5]
Output: 4
```
The longest sequence that contains just 2 unique numbers is [3, 1, 3, 1]

Here's the solution signature:

```
def findSequence(seq):
  # Fill this in.

print findSequence([1, 3, 5, 3, 1, 3, 1, 5])
# 4
```

Approach
```
1. Create two windows with a 'given end ptr' --> Note, this is very important. End ptr will always be fixed and same for the two windows in any given iteration.
    i. First window is where the startPtr points such that the given subArray has <= K distinct integers
    ii. Second window is where the startPtr points such that the given subArray has < K distinct integers
2. VERY IMPORTANT - For a given array of length 'N' and 'always ending with last element', number of possible sub-arrays = N
3. With above concept,
    i. Number of possible sub-arrays of first window = N (with <= K distinct integers)
    ii. Number of possible sub-arrays of second window = M (with < K distinct integers)

    Total number of sub-arrays with 'exactly' K distinct integers = N - M,
    since N = endPtr - startPtr1
    and M = endPtr - startPtr2
    N - M = startPtr2 - startPtr1
4. Continue doing this till endPtr iterates from start till end of the input array
```

Algorithm
```
We'll maintain two sliding windows, corresponding to left1 and left2 . Each sliding window will be able to count how many different elements there are in the window, and add and remove elements in a queue-like fashion.
```