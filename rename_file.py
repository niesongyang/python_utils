#!/usr/bin/env python
# This Python file uses the following encoding: utf-8

import os
#s = os.sep
root = "." 
dict = {}
dict["src_file_name"] = "dst_file_name"

for k in dict:
    print "dict[%s]="%k,dict[k]

for i in os.listdir(root):
    path = root + "/" + i
    if(os.path.isdir(path)):
        for j in os.listdir(path):
            if os.path.isfile(os.path.join(path,j)):
                if (j in dict) :
                    os.rename(os.path.join(path,j),os.path.join(path,dict.get(j)))
                    print j
                else :
                    os.remove(os.path.join(path,j))
