# -*- coding: utf-8 -*-
import urllib2
import urllib
import time
http_url='https://api-cn.faceplusplus.com/facepp/v3/faceset/getfacesets'
key = "meGJ4N0y0g_fbuM2txVZzlr5vFjr1Pn2"
secret = "yphmLjW-IQQ8HA1fdK-dsPBP8ImyV5JO"
def main10():

#使用start参数
	start=str(1)

	boundary = '----------%s' % hex(int(time.time() * 1000))
	data = []
	data.append('--%s' % boundary)
	data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_key')
	data.append(key)
	data.append('--%s' % boundary)
	data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_secret')
	data.append(secret)
	data.append('--%s' % boundary)

#使用start参数
	data.append('Content-Disposition: form-data; name="%s"\r\n' % 'start')
	data.append(start)

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
