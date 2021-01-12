# Description and Solution

## Description

"Lucky triple" is a tuple (x,y,z), where x divides y and y divides z, such as (1,2,4)

Write a function solution(l) that takes a list of positive integers l and counts the number of "lucky triples" of (li, lj, lk) where the list indices meet the requirements i < j < k. Then answer should fit within 32-bit integer. If no triples are found, then return 0.

## Solution

Initially, I regarded the problem as finding the number of 3-simplexes in n-simplex ( where n is the size of l). I solved by going through the list 'l' constructing divisionaries in a dictionary, the algorithmic complexity was O(n^2), yet was solution was timing out in the Google verification procedure.

So I came up with an alternative solution, which is also O(n^2), but is not timing out.

