#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if (n%2==0 and (1<n<6 or n>20)):
        print("Not", end = ' ') #I was checking the "end" thing there, turned out well
    print("Weird")