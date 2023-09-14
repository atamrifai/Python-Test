#!/bin/python3

import math
import os
import random
import re
import sys

def flippingBits(n):
   return (2**32 - 1) - n
   #explanation:
   #don't flip the integer but minus it by n
   #2**32 = maximum integer on 32 Bit. just min by n. because output on 32 Bit integer


