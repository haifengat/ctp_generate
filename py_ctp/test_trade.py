#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'HaiFeng'
__mtime__ = '2016/9/13'
"""

from py_ctp.ctp_struct import *
from py_ctp.trade import Trade

class TestTrade:

	def __init__(self):
		self.q = Trade()
		self.req = 0

	def OnFrontConnected(self):
		print('connected')
		self.q.ReqUserLogin(BrokerID='9999', UserID='008105', Password='1')

	def OnRspUserLogin(self, rsp, info, req, last):
		i = CThostFtdcRspInfoField()
		i = info
		print(i.getErrorMsg())


	def Run(self):
		#CreateApi时会用到log目录,需要在程序目录下创建**而非dll下**
		api = self.q.CreateApi()
		spi = self.q.CreateSpi()
		self.q.RegisterSpi(spi)

		self.q.OnFrontConnected = self.OnFrontConnected
		self.q.OnRspUserLogin = self.OnRspUserLogin

		self.q.RegCB()


		self.q.RegisterFront('tcp://180.168.146.187:10000')
		self.q.Init()
		self.q.Join()


if __name__ == '__main__':
	t = TestTrade()
	t.Run()
	input()
