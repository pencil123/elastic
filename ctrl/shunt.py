#!/usr/bin/env python
# -*- coding:utf-8 -*-

from model.uvelastic import UvElastic
from libs.config import shunt_var
import json
import urllib2

class Shunt():
	def __init__(self):
		self.elastic = UvElastic()
		self.post_url = shunt_var['post_url']

	def create(self):
		domain_dict = self.elastic.term_domain(domain_root=False)
		shunt_list = []
		for domain_uv in domain_dict.items():
			shunt_dict = {}
			shunt_dict['domain'] = domain_uv[0].encode('utf8')
			shunt_dict['uv'] = domain_uv[1]
			shunt_dict['pv'] = 0
			shunt_list.append(shunt_dict)
		json_data = json.dumps(shunt_list)
		req = urllib2.Request(self.post_url,json_data)
		respone = urllib2.urlopen(req)
		return respone.read()