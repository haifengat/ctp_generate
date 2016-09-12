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
		self.q.ReqUserLogin(BrokerID='9999', UserID='xxx', Password='***')

	def OnRspUserLogin(self, rsp, info, req, last):
		i = CThostFtdcRspInfoField()
		i = info
		print(i.getErrorMsg())

		#insts = create_string_buffer(b'cu', 5)
		self.q.SubscribeMarketData('cu1610')

	def OnTick(self, tick):
		f = CThostFtdcMarketDataField()
		f = tick
		print('{0}\t{1}.{2}\t{3}'.format(f.getInstrumentID(), f.getUpdateTime(), f.getUpdateMillisec(), f.getLastPrice()))


	def Run(self):
		#CreateApi时会用到log目录,需要在程序目录下创建**而非dll下**
		api = self.q.CreateApi()
		spi = self.q.CreateSpi()
		self.q.RegisterSpi(spi)

		self.q.OnFrontConnected = self.OnFrontConnected
		self.q.OnRspUserLogin = self.OnRspUserLogin
		self.q.OnRtnDepthMarketData = self.OnTick

		self.q.RegCB()


		self.q.RegisterFront('tcp://180.168.146.187:10010')
		self.q.Init()
		self.q.Join()


if __name__ == '__main__':
	t = TestQuote()
	t.Run()
	input()
