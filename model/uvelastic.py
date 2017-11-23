#!/usr/bin/env python
# -*- coding:utf-8 -*-

from libs.elastic import elastic
from libs.utils import domain_root,domain_roughing

class UvElastic():
	def __init__(self):
		self.client = elastic()

	def total_uv(self):
		self.client.cardinality('remote_addr.keyword')
		return self.client.aggs_metric_search()

	def term_domain(self,domain_root=True):
		#基数的值
		self.client.cardinality('http_host.keyword')
		cardinality = self.client.aggs_metric_search()['value']
		self.client.reset_self()

		#建立域名的bucket
		self.client.time_range()
		self.client.terms('http_host.keyword',cardinality)

		#建立用户IP的metric
		self.client.terms_cardinality('remote_addr.keyword')

		result = self.client.aggs_bucket_metrics_search()
		domain_dict = {}
		for num in range(len(result)):
			if domain_root:
				domain = domain_root(result[num]['key'])
			else:
				domain = domain_roughing(result[num]['key'])
			if domain_dict.has_key(domain):
				domain_dict[domain] = domain_dict[domain] + result[num]['cardinality1']['value']
			elif domain:
				domain_dict[domain] = result[num]['cardinality1']['value']
			else:
				pass
		return domain_dict