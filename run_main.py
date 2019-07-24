#!/usr/bin/env python
# coding: utf-8

# In[ ]:
# this file is runnable by: python run_main.py my_input_file --int_param dataset_name

import sys,os
IPYNB_FILENAME = 'main.ipynb'
CONFIG_FILENAME = '.config_ipynb'

def main(argv):
    with open(CONFIG_FILENAME,'w') as f:
        f.write(' '.join(argv))
    os.system('jupyter nbconvert --execute {:s} --to html'.format(IPYNB_FILENAME))
    return None

if __name__ == '__main__':
    main(sys.argv)

