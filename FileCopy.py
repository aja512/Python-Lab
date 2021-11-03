# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 15:27:35 2019

@author: ajand
"""

import os
import shutil
from os import path
def main():
    if path.exists(“file.txt"):
    src = path.realpath(“file1.txt") 

    head, tail = path.split(src) 
    print("path:" +head)
    print("file:" +tail)
    dst = src+".bak“ 
    shutil.copy(src, dst) 
    shutil.copystat(src,dst)
