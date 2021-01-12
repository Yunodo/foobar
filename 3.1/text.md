# Description and Solution

## Description

You're given a matrix of size (n*n) where each entry is represented either as '1' or '0':

- '1' means that the entry is unpassable
- '0' means that the entry is passable

Your goal is to find shortest path from upper-left entry (0,0) to bottom-right entry (n-1,n-1). Both starting and ending entries have '0', plus it's guaranteed that there exists at least one path from (0,0) to (n-1, n-1). 

Moves can only be made in cardinal directions (left, right, up, down) and n is inclusively between 2 and 20. 

Shortest path can include at most one instance of '1' (meaning that the shortest path should include either no '1' or at mose one '1'). 

## Solution

Use Dijkstra's Algorithms with some modifications to account for the fact that it's possible to remove one instance of the wall (i.e. entry with '1' in it). 

It's possible to find an algorithm with better time complexity, but for a matrix of size up to 20*20, this solution would suffice.

