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
    os.system('jupyter nbconvert --execute {:s} --to html'.format(IPYNB_FILENAME))
    data = argv[3]
    os.rename('main.html', data+'.html') # str(' '.join(argv)).rfind(' ', ' '.join(argv))
    return None

if __name__ == '__main__':
    main(sys.argv)