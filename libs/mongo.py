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