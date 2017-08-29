# -*- coding: utf-8 -*-
import urllib2
import urllib
import os
from VideoCapture import Device  
import time
http_url='https://api-cn.faceplusplus.com/facepp/v3/search'
key = "meGJ4N0y0g_fbuM2txVZzlr5vFjr1Pn2"
secret = "yphmLjW-IQQ8HA1fdK-dsPBP8ImyV5JO"
url= "http://cdn.duitang.com/uploads/item/201311/10/20131110162309_tBdAk.jpeg"

def main8():
	print(u'请输入你的人脸集合标识outer_id')
	outer_id=raw_input()
	return_result_count=str(1)

	boundary = '----------%s' % hex(int(time.time() * 1000))
	data = []
	data.append('--%s' % boundary)
	data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_key')
	data.append(key)
	data.append('--%s' % boundary)
	data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_secret')
	data.append(secret)
	data.append('--%s' % boundary)
	data.append('Content-Disposition: form-data; name="%s"\r\n' % 'image_url')
	data.append(url)
	data.append('--%s' % boundary)
	data.append('Content-Disposition: form-data; name="%s"\r\n' % 'outer_id')
	data.append(outer_id)
	data.append('--%s' % boundary)
	data.append('Content-Disposition: form-data; name="%s"\r\n' % 'return_result_count')
	data.append(return_result_count)
	data.append('--%s--\r\n' % boundary)

	http_body='\r\n'.join(data)
#build http request
	req=urllib2.Request(http_url)
#header
	req.add_header('Content-Type', 'multipart/form-data; boundary=%s' % boundary)
	req.add_data(http_body)
	try:
	#post data to server
		resp = urllib2.urlopen(req, timeout=5)
	#get response
		qrcont=resp.read()
		print qrcont

	except urllib2.HTTPError as e:
		print e.read()
