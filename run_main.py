#!/usr/bin/env python
# coding: utf-8

# In[ ]:
# this file is runnable by: python run_main.py dataset --int_param dataset_name

import sys,os
# import urllib2
IPYNB_FILENAME = 'main.ipynb'
CONFIG_FILENAME = '.config_ipynb'

# data = '{"nw_src": "10.0.0.1/32", "nw_dst": "10.0.0.2/32", "nw_proto": "ICMP", "actions": "ALLOW", "priority": "10"}'
# url = 'http://yann.lecun.com/exdb/mnist/'
# req = urllib2.Request(url, data, {'Content-Type': 'application/json'})
# f = urllib2.urlopen(req)
# for x in f:
#     print(x)
# f.close()


def main(argv):
    with open(CONFIG_FILENAME,'w') as f:
        f.write(' '.join(argv))
        
        
#     http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz
#     http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz
#     http://yann.lecun.com/exdb/mnist/t10k-images-idx3-ubyte.gz
#     http://yann.lecun.com/exdb/mnist/t10k-labels-idx1-ubyte.gz
    
    os.system('jupyter nbconvert --execute {:s} --to html'.format(IPYNB_FILENAME))
    data = argv[3]
    os.rename('main.html', data+'.html') # str(' '.join(argv)).rfind(' ', ' '.join(argv))
    return None

if __name__ == '__main__':
    main(sys.argv)