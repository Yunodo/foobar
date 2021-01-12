# Description and Solution

## Description

### Algorithm

You are given the following algorithm:

1. Start with a random 'n', where 'n' is a non-negative integer of length 'k' in base 'b'
2. Define 'x' and 'y' as integers of length 'k'. 'x' has the digits of 'n' in descending order, and 'y' has digits of 'n' in ascending order
3. Define 'z' such that (z = x-y). Add leading zeros to 'z' to maintain length 'k' if necessary
4. Assign (n=z) and go back to step 2

Example: 

Given (n = 1211, k=4, b=10), then (x = 2111, y = 1112, z = 2111 - 1112 = 0999). Then assign (n=z=0999) and the algorithm iterates again (x = 9990, y = 0999, z = 9990 - 0999 = 8991), and so on.

Depending on the values of n, k (derived from n) and b, at some point reaches a cycle. For example, starting with n =210022, k = 6, b = 3, the algorithm will reach a cycle of values [210111, 122221, 102212] and stay in this loop indefinitely. The length of such cycle 3.

### Task

Write a function solution (n,b) which returns the length of such a cycle. If the algorithm reaches a constant, such as 0, then the length is 1

Example: solution(210022, 3) = 3

## Solution

Develop functions that can:

* perform b-base arithmethic
* generate x and y from n

Combine them to create a list of values and observe if there are any cycles.





