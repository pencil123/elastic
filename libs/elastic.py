#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
from libs.config import elastic_var,elastic_parameter
from elasticsearch import Elasticsearch as Elastic

class elastic():
	def __init__(self):
		self.client = Elastic(**elastic_var)
		self.query = {}
		self.aggs = {}
		self.aggs_metric = {}
		self.aggs_bucket = {}
		self.time_range()
		self.return_string = ''

	def reset_self(self):
		self.query = {}
		self.aggs = {}
		self.aggs_metric = {}
		self.aggs_bucket = {}
		self.return_string = ''

	def time_range(self):
		time_range_dict = {
		'query':{
			'range':{
					'@timestamp':{
						"gt":'now-24h',
						"lt":"now"
						}
					}
				}
			}
		self.query = time_range_dict
		return True

	def cardinality(self,field):
		field_cardinality = {
			"aggs":{
				"cardinality1":
					{"cardinality":{"field":field}}
				}
			}
		self.aggs_metric = field_cardinality
		self.return_string = 'cardinality1'
		return True

	def terms(self,field,size_num):
		shard_size = size_num
		field_terms = {
			"aggs":{
				"terms1":{
					"terms":{
						"field":field,"size":size_num,"shard_size":shard_size,"missing": "-"
					}
				}
			}
		}

		self.aggs_bucket = field_terms
		return True

	def terms_cardinality(self,field):
		self.aggs_metric = {}
		self.cardinality(field)
		self.aggs_bucket['aggs']['terms1'].update(self.aggs_metric)
		order = {'order':{'cardinality1':'desc'}}
		self.aggs_bucket['aggs']['terms1']['terms'].update(order)
		self.aggs = self.aggs_bucket
		self.return_string = 'terms1'
		return True

	def query_search(self):
		body = {'body':self.query}
		elastic_parameter.update(body)
		result = self.client.search(**elastic_parameter)
		return result['hits']['total']

	def aggs_metric_search(self):
		body = {'body':self.query}
		body['body'].update(self.aggs_metric)

		elastic_parameter.update(body)
		result = self.client.search(**elastic_parameter)
		return result['aggregations'][self.return_string]

	def aggs_bucket_metrics_search(self):
		body = {'body':self.query}
		body['body'].update(self.aggs)

		elastic_parameter.update(body)
		print body
		result = self.client.search(**elastic_parameter)

		return result['aggregations'][self.return_string]['buckets']