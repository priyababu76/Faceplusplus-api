# -*- coding: utf-8 -*-
import urllib2
import urllib
from facepp import API,File
import time
def main1():
	http_url = 'https://api-cn.faceplusplus.com/facepp/v3/faceset/create'
	key = "meGJ4N0y0g_fbuM2txVZzlr5vFjr1Pn2"
	secret = "yphmLjW-IQQ8HA1fdK-dsPBP8ImyV5JO"
#添加display_name做参数
	print(u'请输入人脸集合的名字:')
	display_name = raw_input()
#添加outer_id做参数
	print(u'请输入人脸集合的唯一标识outer_id:')
	outer_id = raw_input()
#添加tags做参数
	print(u'请输入人脸集合的自定义标签，用逗号分隔:')
	tags = raw_input()
#添加user_data做参数
	print(u'请输入用户自定义信息:')
	user_data = raw_input()
#添加force_merge做参数
	force_merge = str(0)
	boundary = '----------%s' % hex(int(time.time() * 1000))
	data = []
	data.append('--%s' % boundary)
	data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_key')
	data.append(key)
	data.append('--%s' % boundary)
	data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_secret')
	data.append(secret)
	data.append('--%s' % boundary)
	data.append('Content-Disposition: form-data; name="%s"\r\n' % 'display_name')
	data.append(display_name)
	data.append('--%s' % boundary)
	data.append('Content-Disposition: form-data; name="%s"\r\n' % 'outer_id')
	data.append(outer_id)
	data.append('--%s' % boundary)
	data.append('Content-Disposition: form-data; name="%s"\r\n' % 'tags')
	data.append(tags)
	data.append('--%s' % boundary)
	data.append('Content-Disposition: form-data; name="%s"\r\n' % 'user_data')
	data.append(user_data)
	data.append('--%s' % boundary)
	data.append('Content-Disposition: form-data; name="%s"\r\n' % 'force_merge')
	data.append(force_merge)
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
