# -*- coding: utf-8 -*-
import urllib2
import urllib
from facepp import API,File
from VideoCapture import Device
import time
http_url='https://api-cn.faceplusplus.com/facepp/v3/faceset/addface'
key = "meGJ4N0y0g_fbuM2txVZzlr5vFjr1Pn2"
secret = "yphmLjW-IQQ8HA1fdK-dsPBP8ImyV5JO"
def main2():
#使用outer_id参数
	print(u'请输入你的人脸集合标识outer_id')
	outer_id=raw_input()

#使用faceset_token参数
#faceset_token="cfc30e14ac62fba44f76ee36596a0e3a"
	'''interval = 2  
	cam = Device()
	print(u'请输入您的名字,以.jpg结尾')
	name=raw_input()
	filename='D:/python_sdk/staff/'+name 
	cam.saveSnapshot(filename)  '''
	print(u'请输入图片名')
	name=raw_input()
	filename='D:/picture/'+name+'.jpg'

#使用face_tokens参数
	api = API(key,secret)
	result = api.detect(image_file=File(filename))
	face_tokens =result['faces'][0]['face_token']

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
	print(face_tokens)
