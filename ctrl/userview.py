#!/usr/bin/env python
# -*- coding:utf-8 -*-

from model.uvelastic import UvElastic
from model.uvmongo import UvMongo
from model.sendmail import SendMail
from model.usermongo import UserMongo
from model.execl import Execl

class userview():
	def __init__(self):
		self.elastic = UvElastic()
		self.mongo = UvMongo()
		self.usermongo = UserMongo()
		self.mail = SendMail()
		self.execl = Execl()
		self.mail_attach = ""

	def create(self):
		domain_dict = self.elastic.term_domain()
		self.mongo.write(domain_dict)


	def update_domain_user(self):
		domain_list = self.mongo.limit()
		for num in range(len(domain_list)):
			domain = domain_list[num]['domain']
			user_num = self.usermongo.get_user(domain)
			where_dict = {'domain':domain}
			value_dict = {'user':user_num}
			self.mongo.update(where_dict,value_dict)
		return True

	def create_execl(self):
		domain_list = self.mongo.limit()
		self.execl.create(domain_list)
		self.mail_attach = self.execl.save()

	def sendmail(self):
		total_uv = self.elastic.total_uv()
		self.mail.edit_total(total_uv['value'])
		
		self.mail.attach(self.mail_attach)

		domain_dict = self.mongo.limit()
		self.mail.edit_content(domain_dict)

	def drop(self):
		self.execl.delete()
		self.mongo.drop()