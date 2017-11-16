#!/usr/bin/env python
# -*- coding:utf-8 -*-

from libs.mongo import Statistics

class UserMongo():
	def get_user(self,domain):
		try:
			doc_handler = Statistics.objects.get(domain=domain)
			user = doc_handler.user
			return user
		except:
			return 4