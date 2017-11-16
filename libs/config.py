#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import yaml

class config():
	config_path = "config/config.yaml"
	def __init__(self,config=""):
		self.config_path = config if config else self.config_path
		self.parse()

	def parse(self):
		config_handler = open(self.config_path)
		config_info = yaml.load(config_handler)
		self.elastic = config_info['elastic']
		self.mongo = config_info['mongo']
		self.elastic_parameter = config_info['elastic_parameter']
		self.mail_info = config_info['sendmail']
		

handler = config()
elastic_var = handler.elastic
elastic_parameter = handler.elastic_parameter
mongo_parameter = handler.mongo
mail_info = handler.mail_info