#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import re
import os, sys, fileinput

def replace_file(file_name, src_str, dst_str):
    fp=open(file_name,'r')
    alllines=fp.read()
    fp.close()
    fp=open(file_name,'w')
    fp.writelines(re.sub(src_str, dst_str, alllines))
    fp.close()

#    print_file(file_name)

def replace_folder(file_path, src_str, dst_str):
    file_path_abs = os.path.abspath(file_path)

    if(os.path.isfile(file_path_abs)):
        replace_file(file_path_abs, src_str, dst_str)
        print 'file : ' + file_path_abs
    elif(os.path.isdir(file_path_abs)):
        file_list = os.listdir(file_path_abs)
        for sub_file in file_list:
            sub_file_path = file_path_abs + '/' + sub_file
            replace_folder(sub_file_path, src_str, dst_str)
        print 'folder : '+file_path_abs
    else:
        pass
#        print_error()

def print_file(file_name):
    fp = open(file_name, 'r')
    all_lines = fp.readlines()
    fp.close()

    for each_line in all_lines:
        print each_line,

def print_help():
    print 'please input your filepath, srcStr and dstStr'
    print 'such as:'
    print '    ./replace_str.py filePath/ \'src\' \'dst\''

def print_error():
    print 'Error : no action specified.'
    sys.exit()

def main():
    if(len(sys.argv) < 2):
        print_error()

    if(sys.argv[1].startswith('--')):
        option = sys.argv[1][2:]
        if(option == 'help' or option == 'h'):
            print_help()
    else:
        file_path = sys.argv[1]
        src_str = sys.argv[2]
        dst_str = sys.argv[3]
        replace_folder(file_path, src_str, dst_str)

    return True

if __name__ == '__main__':
    main()
