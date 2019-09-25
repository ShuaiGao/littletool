# -*- coding: utf-8 -*-

# import sys
import os
import json
import base64
import uuid



# basepath = os.path.dirname(os.getcwd())
basepath = os.getcwd()
dirname = r'tooldata'
if not os.path.exists(dirname):
	os.makedirs(dirname)

tool_path = basepath + os.sep + dirname + os.sep


class ToolError(Exception):
    pass



def wFile(dataStr, filename):
	fullPath = tool_path + filename
	try:
		f = open(fullPath, 'w')
		print(dataStr, file=f )
		f.close()
	except PermissionError:
		print("You don't have permission to access this file. " + fullPath )
	

def w_json(data, filename, encrypt = False):
	# 往文件中写入json文件
	with open(tool_path + filename, 'w') as wf:
		if encrypt is not True:
			json.dump(data, wf)
		else:
			dataStr = json.dumps(data)
			wf.write(base64.b64encode(dataStr.encode()).decode())
			#base64.b64encode(dataStr.encode()) 			#返回二进制字符串
			#base64.b64encode(dataStr.encode()).decode() 	#返回正常字符串
	return True


def r_json(filename, encrypt = False):
	# 读取json文件
	data = None
	try:
		rf = open(tool_path + filename, 'r')
		if encrypt is not True:
			data = json.load(rf)
		else:
			data = base64.b64decode(rf.read())
		rf.close()
	except FileNotFoundError:
		print("File is not found.")
	except PermissionError:
		print("You don't have permission to access this file.")
	
	return data

def xor_encrypt(tips,key = None):
	if not key:
		key = get_mac_address()
	ltips=len(tips)
	lkey=len(key)
	secret=[]
	num=0
	for each in tips:
		if num >= lkey:
			num = num%lkey
		secret.append( chr( ord(each)^ord(key[num]) ) )
		num+=1

	xors = "".join( secret ).encode()
	bxors = base64.b64encode(xors).decode()
	return bxors


def xor_decrypt(secret,key = None):
	if not key:
		key = get_mac_address()
	
	tips = base64.b64decode( secret.encode() ).decode()
	ltips=len(tips)
	lkey=len(key)
	secret=[]
	num=0
	for each in tips:
		if num>=lkey:
			num=num%lkey
		secret.append( chr( ord(each)^ord(key[num]) ) )
		num+=1

	return "".join( secret )
	
def getKey():
	return get_mac_address()

def get_mac_address():
	node = uuid.getnode()
	mac = uuid.UUID(int = node).hex[-12:]
	return mac

# 测试代码
def RunTest():
	print("-"*40)
	print("存储对象 " + '{"hello":12}')
	w_json({"hello":12}, "justtest")
	print("读取对象字符串 ", r_json("justtest") or "")
	print("加密存储对象 " + '{"hello":12}')
	w_json({"hello":12}, "justtest", encrypt = True)
	print("加密读取对象字符串 ", r_json("justtest", encrypt = True) or "")
	print("-"*40)

	data = 'This is testing!'
	sss = data + data + data
	print(sss)
	ddd = base64.b64encode(sss.encode()).decode()
	print(ddd)
	aaa = base64.b64decode(ddd).decode()
	print(aaa)
	print("="*40)
	pwd = "my_password"
	xorsss = xor_encrypt(sss, pwd)
	print(xorsss)
	xorddd = xor_decrypt(xorsss, pwd)
	print(xorddd)
	print("="*40)
	print('w_json ok')

	print("*"*40)
	print("mac address is: " + get_mac_address())
	print("*"*40)



# if __name__ == '__main__':
# 	RunTest()
 	
