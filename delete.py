# -*- coding: utf-8 -*-
import urllib2
import urllib
import time
http_url='https://api-cn.faceplusplus.com/facepp/v3/faceset/delete'
key = "meGJ4N0y0g_fbuM2txVZzlr5vFjr1Pn2"
secret = "yphmLjW-IQQ8HA1fdK-dsPBP8ImyV5JO"
def main7():
#使用outer_id参数
	print(u'请输入你的人脸集合标识outer_id')
	outer_id=raw_input()

#使用check_empty参数
	print(u'检查是否为空0：不检查1：检查')
	check_empty=str(input())

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

#使用check_empty参数
	data.append('Content-Disposition: form-data; name="%s"\r\n' % 'check_empty')
	data.append(check_empty)

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
