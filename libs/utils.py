#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re

def domain_root(domain_url):
	#去掉引号
	tmp = domain_url.strip('"')
	#获取根域名
	if checkip(tmp):
		return False
	tmp = tmp.split('.')
	try:
		domain = tmp[-2] + '.' + tmp[-1]
	except:
		return False
	return domain

def domain_roughing(domain_url):
	#去掉引号
	tmp = domain_url.strip('"')
	#获取根域名
	if checkip(tmp):
		return False
	return tmp

def checkip(ip):
	p = re.compile('^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$')  
	if p.match(ip):
		return True
	else:
		return False