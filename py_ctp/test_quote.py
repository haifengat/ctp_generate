#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = 'quote.py testing'
__author__ = 'HaiFeng'
__mtime__ = '2016/9/8'
"""
from py_ctp.ctp_struct import *
from py_ctp.quote import Quote

class TestQuote:

	def __init__(self):
		self.q = Quote()
		self.req = 0

	def OnFrontConnected(self):
		print('connected')
		f = CThostFtdcReqUserLoginField()
		f.BrokerID = '9999'.encode('ascii')
		f.UserID = '123'.encode('ascii')
		f.Password = '***'.encode('ascii')
		self.req += 1
		self.q.ReqUserLogin(byref(f), self.req)

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


		self.q.RegisterFront('tcp://180.168.146.187:10010'.encode('ascii'))
		self.q.Init()
		self.q.Join()


if __name__ == '__main__':
	t = TestQuote()
	t.Run()
	input()
