#!/usr/bin/env python
# -*- coding:utf-8 -*-

from libs.sendmail import SendMailDIY
from libs.config import mail_info

class SendMail(object):
	def __init__(self):
		self.mail = SendMailDIY()
		self.auto_info()
		self.html_head = ''
		self.total_uv = 0

	def auto_info(self):
		self.mail.subject('test')
		self.mail.receiver(mail_info.mail_to)

	def edit_total(self,total_uv):
		self.total_uv = total_uv
		html_head = '''
		<table border="1" width="90%">
		<tbody><tr>
		<td width="100%" style="background-color:#cc0000" colspan="4" align="center"><strong> 总uv量</strong> </td>
		</tr><tr>
		<td width="50%" style="background-color:white" colspan="4" align="center"><strong> 
		'''
		self.html_head = html_head + str(total_uv) + '''
		</strong> </td>
		</tr><tr>
		<td width="30%" style="background-color:#cc0000" align="center"><strong><span class="il">域名</span></strong></td>
		<td width="30%" style="background-color:#cc0000" align="center"><strong>UV量</strong></td>
		<td width="30%" style="background-color:#cc0000" align="center"> <strong>UV百分比</strong></td>
		</tr>
		'''

	def edit_content(self,data_dict):
		line1 = '''<tr><td style="background-color:#white" align="center"> <strong>'''.encode('utf8')
		line2 = '''</strong></td><td style="background-color:#white" align="center"> <strong>'''.encode('utf8')
		line3 = '''</strong></td><td style="background-color:#white" align="center"> <strong>'''.encode('utf8')
		for num in range(40):
			print num
			print data_dict
			line_string = line1 + data_dict[num]['k'].encode('utf8') + line2 + str(data_dict[num]['v']).encode('utf8') + line3 + str(format(float(data_dict[num]['v'])/float(self.total_uv)*100,'.2f')).encode('utf8') + "%</strong></td></tr>"
			self.html_head += line_string
		html_buttom = '''</tbody></table>'''

		self.html_head += html_buttom

		self.mail.content(self.html_head)
		self.mail.perform()