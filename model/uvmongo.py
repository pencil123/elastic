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
			domain['domain'] = list_info['domain']
			domain['uv'] = list_info['uv']
			domain['user'] = list_info['user']
			list_data.append(domain)
		return list_data

	def update(self,where_dict,value_dict):
		doc_handler = DomainUV.objects.get(**where_dict)
		doc_handler.update(**value_dict)
		doc_handler.save()
	def drop(self):
		DomainUV.drop_collection()