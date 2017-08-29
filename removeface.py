# -*- coding: utf-8 -*-
import urllib2
import urllib
import os
from facepp import API,File
import time
http_url='https://api-cn.faceplusplus.com/facepp/v3/faceset/removeface'
key = "meGJ4N0y0g_fbuM2txVZzlr5vFjr1Pn2"
secret = "yphmLjW-IQQ8HA1fdK-dsPBP8ImyV5JO"
def main4():
#使用outer_id参数
	print(u'请输入你的人脸集合标识outer_id')
	outer_id=raw_input()

#使用face_tokens参数
	print(u'是否删除所有图片,0:否,其他：是')
	choose=input()
	if choose==0:
		print(u'请输入要删除的face_tokens:')
		face_tokens=raw_input()
	else:
		face_tokens="RemoveAllFaceTokens"
	
	boundary = '----------%s' % hex(int(time.time() * 1000))
	data = []
	data.append('--%s' % boundary)
	data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_key')
	data.append(key)
	data.append('--%s' % boundary)
	data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_secret')
	data.append(secret)
	data.append('--%s' % boundary)

#使用outer_id参数
	data.append('Content-Disposition: form-data; name="%s"\r\n' % 'outer_id')
	data.append(outer_id)
	data.append('--%s' % boundary)

	data.append('Content-Disposition: form-data; name="%s"\r\n' % 'face_tokens')
	data.append(face_tokens)
	data.append('--%s--\r\n' % boundary)

	http_body='\r\n'.join(data)
#buld http request
	req=urllib2.Request(http_url)
#header
	req.add_header('Content-Type', 'multipart/form-data; boundary=%s' % boundary)
	req.add_data(http_body)
	try:
		#req.add_header('Referer','http://remotserver.com/')
		#post data to server
		resp = urllib2.urlopen(req, timeout=5)
		#get response
		qrcont=resp.read()
		print qrcont

	except urllib2.HTTPError as e:
		print e.read()
