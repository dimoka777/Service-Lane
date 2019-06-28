"""
Function Description
Complete the serviceLane function in the editor below. It should return an array of integers representing the maximum
width vehicle that can pass through each segment of the highway described.
serviceLane has the following parameter(s):
n: an integer denoting the size of the  array
cases: a two dimensional array of integers where each element is an array of two integers representing starting
and ending indices for a segment to consider .
Input Format
The first line of input contains two integers,  and , where  denotes the number of width measurements you will
receive and  the number of test cases. The next line has  space-separated integers which represent the array .
The next  lines contain two integers,  and , where  is the start index and  is the end index of the segment
being considered.
Constraints
Output Format
For each test case, print the number that represents the largest vehicle type that can pass through the entire
segment of the service lane between indexes  and  inclusive.
"""
import math
import os
import random
import re
import sys

# Complete the serviceLane function below.


def serviceLane(n, cases, width):

    total = []
    for i in range(len(cases)):
        start = cases[i][0]
        end = cases[i][1]
        new_list = []
        for j in range(start, end + 1):
            new_list.append(width[j])
        new_list = min(new_list)
        total.append(new_list)

    return total


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nt = input().split()
    n = int(nt[0])
    t = int(nt[1])
    width = list(map(int, input().rstrip().split()))
    cases = []
    for _ in range(t):
        cases.append(list(map(int, input().rstrip().split())))
    result = serviceLane(n, cases, width)
    print(result)

    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')
    #
    # fptr.close()
