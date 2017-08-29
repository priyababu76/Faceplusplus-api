# -*- coding: utf-8 -*-
#import os,sys
def main():
	a = 2
	while(a!=0):
		print (u'===================================================')
		print (u'欢迎使用faceplusplus')
		print (u'---------------------------------------------------')
		print (u'请选择:')
		print (u'0. 退出系统')
		print (u'1. 创建新的人脸集合')
		print (u'2. 增加新的人脸数据')
		print (u'3. 设置新增人脸的用户标识信息')
		print (u'4. 移除已有人脸数据')
		print (u'5. 更新人脸集合信息')
		print (u'6. 获取单个人脸集合信息')
		print (u'7. 删除已有人脸集合')
		print (u'8. 查找最相近的人脸')
		print (u'9. 获取人脸关联信息')
		print (u'10. 获取所有人脸集合信息')
		print (u'---------------------------------------------------')
		print (u'===================================================')
		a=int (raw_input())
		if(a==1):
			from create import main1
			main1()
		elif(a==2):
			from addface import main2
			main2()
		elif(a==3):
			from setuserid import main3
			main3()
		elif(a==4):
			from removeface import main4
			main4()
		elif(a==5):
			from update import main5
			main5()
		elif(a==6):
			from getdetail import main6
			main6()
		elif(a==7):
			from delete import main7
			main7()
		elif(a==8):
			from search import main8
			main8()
		elif(a==9):
			from face_getdetail import main9
			main9()
		elif(a==10):
			from getfacesets import main10
			main10()
		else:
			print(u'输入错误')
main()
