# python2.7.5
# author : loveisbug
# email  : ericnomail@gmail.com
# twitter: @loveisbug
#    http://weibo.com/loveisbug
# date        version    PIC    comments
# 20150902    0.0.1      eric 

import hashlib
import sys

def get_file_md5(f):
	m = hashlib.md5()

	while True:
		data = f.read(10240)
		if not data:
			break
		m.update(data)
	return m.hexdigest()


if len(sys.argv) > 1:
    print get_file_md5(open(sys.argv[1], 'r'))
else:
    print "Please input the file name."
