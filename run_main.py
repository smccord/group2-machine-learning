#!/usr/bin/env python
# coding: utf-8

# In[ ]:
# this file is runnable by: python run_main.py dataset --int_param dataset_name

import sys,os
IPYNB_FILENAME = 'main.ipynb'
CONFIG_FILENAME = '.config_ipynb'

def main(argv):
    with open(CONFIG_FILENAME,'w') as f:
        f.write(' '.join(argv))
    
    a = str(sys.argv[1])
    with open("data/"+a, 'r')as f:
        line=f.readline()
        data = line.rstrip('\n')
        data = data[line.find(" ")+1:]   # gives "mnist" or "fashion" 
    
    os.system('jupyter nbconvert --execute {:s} --to html'.format(IPYNB_FILENAME))
    os.rename('main.html', data+'.html')
    return None

if __name__ == '__main__':
    main(sys.argv)