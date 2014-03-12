'''
Created on Mar 11, 2014

@author: CT61557
'''
import os
from os.path import join
for root,dirs,files in os.walk('../result'):
    for file in files:
        if file != 'TeamMembers.txt':
            path = root +'/' +file
            print "Removed: " + path
            os.remove(path)
