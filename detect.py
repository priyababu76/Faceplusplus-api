# -*- coding: utf-8 -*-
import urllib2
import urllib
from VideoCapture import Device
import time
http_url='https://api-cn.faceplusplus.com/facepp/v3/detect'
key = "meGJ4N0y0g_fbuM2txVZzlr5vFjr1Pn2"
secret = "yphmLjW-IQQ8HA1fdK-dsPBP8ImyV5JO"

#使用image_file做参数
interval = 2  
cam = Device()
print(u'请输入您的名字,以.jpg结尾')
filenpath=raw_input('test_image:') 
cam.saveSnapshot(filename)  

#使用image_url做参数
image_url = 'http://i4.cqnews.net/news/attachement/jpg/site82/20150316/bc305baa3b6816707f500d.jpg'

#使用return_landmark做参数
return_landmark = raw_input('whether or not detect 83 landmarks on face 1.detect 0.not detect')

#使用return_attributes做参数
return_attributes = "gender,age,smiling,headpose,facequality,blur,eyestatus,emotion,ethnicity"

boundary = '----------%s' % hex(int(time.time() * 1000))
data = []
data.append('--%s' % boundary)
data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_key')
data.append(key)
data.append('--%s' % boundary)
data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_secret')
data.append(secret)
data.append('--%s' % boundary)

#使用image_file做参数
fr=open(filepath,'rb')
data.append('Content-Disposition: form-data; name="%s"; filename=" "' % 'image_file')
data.append('Content-Type: %s\r\n' % 'application/octet-stream')
data.append(fr.read())
fr.close()

#使用image_url做参数
'''data.append('Content-Disposition: form-data; name="%s"\r\n' % 'image_url')
data.append(image_url)
data.append('--%s' % boundary)'''

#加入return_landmark参数
data.append('Content-Disposition: form-data; name="%s"\r\n' % 'return_landmark')
data.append(return_landmark)

#加入return_attributes参数
'''data.append('Content-Disposition: form-data; name="%s"\r\n' % 'return_attributes')
data.append(return_attributes)'''
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
