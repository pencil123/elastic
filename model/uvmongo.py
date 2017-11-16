#!/usr/bin/env python
# -*- coding:utf-8 -*-

from libs.mongo import DomainUV

class UvMongo():
	def write(self,domain_dict):
		list_data = []
		for (k,v) in domain_dict.items():
			#print k,v
			list_data.append(DomainUV(domain=k,uv=v))
		DomainUV.objects.insert(list_data)

	def limit(self,start=0,end=0):
		list_data = []
		for list_info in DomainUV.objects.order_by('-uv'):
			domain = {}
			domain['k'] = list_info['domain']
			domain['v'] = list_info['uv']
			list_data.append(domain)
		self.drop()
		return list_data
	
	def drop(self):
		DomainUV.drop_collection()