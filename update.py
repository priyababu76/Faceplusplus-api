# -*- coding: utf-8 -*-
import urllib2
import urllib
from facepp import API,File
import time
http_url='https://api-cn.faceplusplus.com/facepp/v3/faceset/update'
key = "meGJ4N0y0g_fbuM2txVZzlr5vFjr1Pn2"
secret = "yphmLjW-IQQ8HA1fdK-dsPBP8ImyV5JO"
def main5():
#使用outer_id参数
	print(u'请输入你的人脸集合标识outer_id')
	outer_id=raw_input()

#添加new_outer_id参数
	print(u'请输入新的人脸集合标识new_outer_id')
	new_outer_id=raw_input()
	
#添加display_name参数
	print(u'请输入新的人脸集合名字display_name')
	display_name=raw_input()
	
#添加user_data参数
	print(u'请输入新的自定义用户信息user_data')
	user_data=raw_input()
	
#添加tags参数
	print(u'请输入新的自定义标签tags')
	tags=raw_input()

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

	#添加new_outer_id参数
	data.append('Content-Disposition: form-data; name="%s"\r\n' % 'new_outer_id')
	data.append(new_outer_id)
	data.append('--%s' % boundary)

	#添加display_name参数
	data.append('Content-Disposition: form-data; name="%s"\r\n' % 'display_name')
	data.append(display_name)
	data.append('--%s' % boundary)

	#添加user_data参数
	data.append('Content-Disposition: form-data; name="%s"\r\n' % 'user_data')
	data.append(user_data)
	data.append('--%s' % boundary)

	#添加tags参数
	data.append('Content-Disposition: form-data; name="%s"\r\n' % 'tags')
	data.append(tags)

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
