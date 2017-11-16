#!/usr/bin/env python
# -*- coding:utf-8 -*-

from model.uvelastic import UvElastic
from model.uvmongo import UvMongo
from model.sendmail import SendMail

class userview():
	def __init__(self):
		self.elastic = UvElastic()
		self.mongo = UvMongo()
		self.mail = SendMail()

	def create(self):
		domain_dict = self.elastic.term_domain()
		self.mongo.write(domain_dict)

	def sendmail(self):
		total_uv = self.elastic.total_uv()
		self.mail.edit_total(total_uv['value'])
		
		domain_dict = self.mongo.limit()
		self.mail.edit_content(domain_dict)

	def drop(self):
		self.mongo.drop()