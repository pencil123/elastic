#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
from libs.config import mongo_parameter
import mongoengine as mongo

mongo.connect(**mongo_parameter)

class DomainUV(mongo.Document):
	meta = {'collection': 'domainuv'}
	domain = mongo.StringField(max_length=40,required=True)
	uv = mongo.IntField(max_length=20,required=True)
	user = mongo.IntField()

class Statistics(mongo.Document):
	meta = {'collection': 'statistics'}
	domain = mongo.StringField()
	user = mongo.IntField()
	route = mongo.IntField()
	own = mongo.IntField()
	https = mongo.IntField()
	mark = mongo.StringField()