# -*- coding: utf-8 -*-

import tarfile
import os

def tarFile(tfname):
	if os.path.exists(tfname):
		os.remove(tfname)
	tf = tarfile.open(tfname, 'w:tar')
	tf.add("src" + os.sep + "resource", arcname='resource')
	tf.add("dist" + os.sep + "littletool.exe", arcname='小工具.exe')
	tf.add("readme.txt")
	# for fname in os.listdir('.'):
	# 	print(fname)
		# if fname.endswith('.xml'):
			# tf.add(fname)
			# os.remove(fname)  # 需要进行删除, 否则会重复添加
	tf.close()

	if not tf.members:
		os.remove(tfname)  # 如果为空,则删除

if __name__ == '__main__':
	tarFile('小工具.tar')
