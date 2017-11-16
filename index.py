#!/usr/bin/env python
# -*- coding:utf-8 -*-

from ctrl.userview import userview
'''
    这个uv数据生成的过程:
    1、从es获取数据，写入mongodb
    2、更新数据中的user
    3、将数据写入到文件中
    4、编辑邮件并发送
    5、删除mongodb中的数据
'''
test = userview()
#生成数据写入到mongodb
test.create()
#更新user
test.update_domain_user()
#写入到文件
test.create_execl()
#发送邮件
test.sendmail()
#删除数据
test.drop()