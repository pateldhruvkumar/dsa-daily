# dsa-daily

Daily data structures & algorithms practice — clean, from-scratch implementations
organized by topic. Mostly **Python**, with the occasional **C++** solution.

The goal is learning by re-implementing the fundamentals: each folder is a self-contained
topic with small, runnable scripts and example usage at the bottom.

## Topics

| Folder | What's inside |
|--------|---------------|
| [search/](search/) | Linear search, binary search |
| [twoPointer/](twoPointer/) | Two-sum, palindrome & valid-palindrome checks |
| [two-sum/](two-sum/) | Two-sum via hash map |
| [slidingWindow/](slidingWindow/) | Sum of a sub-array |
| [maximum-sum-subarray/](maximum-sum-subarray/) | Max fixed-size window sum (brute force; optimized WIP) |
| [2nd-largest/](2nd-largest/) | Second-largest element (Python + C++) |
| [hash-tables/](hash-tables/) | Hash function, insertion, collision handling, search, phone book |
| [linked-list/](linked-list/) | Traverse, insert, delete, find smallest |
| [stack/](stack/) | Stack using an array |
| [trees/](trees/) | Build tree, array-based insert, pre/in/post-order traversal |

## Running the code

Each script is standalone and includes a small example at the bottom.

```bash
# Python
python maximum-sum-subarray/brute-force-approach.py

# C++
g++ 2nd-largest/2nd-largest.c++ -o 2nd-largest.out && ./2nd-largest.out
```

**Requirements:** Python 3, and a C++ compiler (e.g. `g++`) for the C++ files.

## Layout

```
dsa-daily/
├── search/
├── twoPointer/
├── two-sum/
├── slidingWindow/
├── maximum-sum-subarray/
├── 2nd-largest/
├── hash-tables/
├── linked-list/
├── stack/
└── trees/
```
