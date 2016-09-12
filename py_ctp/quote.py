
from py_ctp.ctp_struct import *
import os

class Quote:

	def __init__(self):

		cur_path = os.getcwd()
		# change work directory
		os.chdir(os.path.join(os.getcwd(), "dll"))
		# make log dir for api log
		if not os.path.exists("log"):
			os.mkdir("log")

		self.h = CDLL("ctp_quote.dll")

		self.h.CreateApi.argtypes = []
		self.h.CreateApi.restype = c_void_p

		self.h.CreateSpi.argtypes = []
		self.h.CreateSpi.restype = c_void_p

		self.api = None
		self.spi = None
		self.h.RegisterNameServer.argtypes = [c_void_p , c_char_p]
		self.h.RegisterNameServer.restype = c_void_p
		self.h.UnSubscribeForQuoteRsp.argtypes = [c_void_p , c_char_p , c_int32]
		self.h.UnSubscribeForQuoteRsp.restype = c_void_p
		self.h.ReqUserLogout.argtypes = [c_void_p , c_void_p , c_int32]
		self.h.ReqUserLogout.restype = c_void_p
		self.h.Init.argtypes = [c_void_p]
		self.h.Init.restype = c_void_p
		self.h.GetTradingDay.argtypes = [c_void_p]
		self.h.GetTradingDay.restype = c_void_p
		self.h.RegisterSpi.argtypes = [c_void_p , c_void_p]
		self.h.RegisterSpi.restype = c_void_p
		self.h.SubscribeMarketData.argtypes = [c_void_p , c_char_p , c_int32]
		self.h.SubscribeMarketData.restype = c_void_p
		self.h.Release.argtypes = [c_void_p]
		self.h.Release.restype = c_void_p
		self.h.Join.argtypes = [c_void_p]
		self.h.Join.restype = c_void_p
		self.h.RegisterFensUserInfo.argtypes = [c_void_p , c_void_p]
		self.h.RegisterFensUserInfo.restype = c_void_p
		self.h.RegisterFront.argtypes = [c_void_p , c_char_p]
		self.h.RegisterFront.restype = c_void_p
		self.h.ReqUserLogin.argtypes = [c_void_p , c_void_p , c_int32]
		self.h.ReqUserLogin.restype = c_void_p
		self.h.UnSubscribeMarketData.argtypes = [c_void_p , c_char_p , c_int32]
		self.h.UnSubscribeMarketData.restype = c_void_p
		self.h.SubscribeForQuoteRsp.argtypes = [c_void_p , c_char_p , c_int32]
		self.h.SubscribeForQuoteRsp.restype = c_void_p

		# restore work directory
		os.chdir(cur_path)


	def RegCB(self):
		"""在createapi, createspi后调用"""

		self.h.SetOnRspSubMarketData.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRspSubMarketData.restype = c_void_p
		self.evOnRspSubMarketData = CFUNCTYPE(c_void_p, POINTER(CThostFtdcSpecificInstrumentField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspSubMarketData)
		self.h.SetOnRspSubMarketData(self.spi, self.evOnRspSubMarketData)

		self.h.SetOnRspSubForQuoteRsp.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRspSubForQuoteRsp.restype = c_void_p
		self.evOnRspSubForQuoteRsp = CFUNCTYPE(c_void_p, POINTER(CThostFtdcSpecificInstrumentField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspSubForQuoteRsp)
		self.h.SetOnRspSubForQuoteRsp(self.spi, self.evOnRspSubForQuoteRsp)

		self.h.SetOnFrontDisconnected.argtypes = [c_void_p, c_void_p]
		self.h.SetOnFrontDisconnected.restype = c_void_p
		self.evOnFrontDisconnected = CFUNCTYPE(c_void_p, c_int32)(self.__OnFrontDisconnected)
		self.h.SetOnFrontDisconnected(self.spi, self.evOnFrontDisconnected)

		self.h.SetOnRspUnSubMarketData.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRspUnSubMarketData.restype = c_void_p
		self.evOnRspUnSubMarketData = CFUNCTYPE(c_void_p, POINTER(CThostFtdcSpecificInstrumentField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspUnSubMarketData)
		self.h.SetOnRspUnSubMarketData(self.spi, self.evOnRspUnSubMarketData)

		self.h.SetOnRspUserLogout.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRspUserLogout.restype = c_void_p
		self.evOnRspUserLogout = CFUNCTYPE(c_void_p, POINTER(CThostFtdcUserLogoutField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspUserLogout)
		self.h.SetOnRspUserLogout(self.spi, self.evOnRspUserLogout)

		self.h.SetOnRtnForQuoteRsp.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRtnForQuoteRsp.restype = c_void_p
		self.evOnRtnForQuoteRsp = CFUNCTYPE(c_void_p, POINTER(CThostFtdcForQuoteRspField))(self.__OnRtnForQuoteRsp)
		self.h.SetOnRtnForQuoteRsp(self.spi, self.evOnRtnForQuoteRsp)

		self.h.SetOnHeartBeatWarning.argtypes = [c_void_p, c_void_p]
		self.h.SetOnHeartBeatWarning.restype = c_void_p
		self.evOnHeartBeatWarning = CFUNCTYPE(c_void_p, c_int32)(self.__OnHeartBeatWarning)
		self.h.SetOnHeartBeatWarning(self.spi, self.evOnHeartBeatWarning)

		self.h.SetOnRspError.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRspError.restype = c_void_p
		self.evOnRspError = CFUNCTYPE(c_void_p, POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspError)
		self.h.SetOnRspError(self.spi, self.evOnRspError)

		self.h.SetOnFrontConnected.argtypes = [c_void_p, c_void_p]
		self.h.SetOnFrontConnected.restype = c_void_p
		self.evOnFrontConnected = CFUNCTYPE(c_void_p)(self.__OnFrontConnected)
		self.h.SetOnFrontConnected(self.spi, self.evOnFrontConnected)

		self.h.SetOnRtnDepthMarketData.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRtnDepthMarketData.restype = c_void_p
		self.evOnRtnDepthMarketData = CFUNCTYPE(c_void_p, POINTER(CThostFtdcDepthMarketDataField))(self.__OnRtnDepthMarketData)
		self.h.SetOnRtnDepthMarketData(self.spi, self.evOnRtnDepthMarketData)

		self.h.SetOnRspUserLogin.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRspUserLogin.restype = c_void_p
		self.evOnRspUserLogin = CFUNCTYPE(c_void_p, POINTER(CThostFtdcRspUserLoginField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspUserLogin)
		self.h.SetOnRspUserLogin(self.spi, self.evOnRspUserLogin)

		self.h.SetOnRspUnSubForQuoteRsp.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRspUnSubForQuoteRsp.restype = c_void_p
		self.evOnRspUnSubForQuoteRsp = CFUNCTYPE(c_void_p, POINTER(CThostFtdcSpecificInstrumentField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspUnSubForQuoteRsp)
		self.h.SetOnRspUnSubForQuoteRsp(self.spi, self.evOnRspUnSubForQuoteRsp)

	def __OnRspSubMarketData(self, pSpecificInstrument, pRspInfo, nRequestID, bIsLast):
			print('OnRspSubMarketData:pSpecificInstrument, pRspInfo, nRequestID, bIsLast')
			self.OnRspSubMarketData(POINTER(CThostFtdcSpecificInstrumentField).from_param(pSpecificInstrument).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents, nRequestID, bIsLast)
	
	def __OnRspSubForQuoteRsp(self, pSpecificInstrument, pRspInfo, nRequestID, bIsLast):
			print('OnRspSubForQuoteRsp:pSpecificInstrument, pRspInfo, nRequestID, bIsLast')
			self.OnRspSubForQuoteRsp(POINTER(CThostFtdcSpecificInstrumentField).from_param(pSpecificInstrument).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents, nRequestID, bIsLast)
	
	def __OnFrontDisconnected(self, nReason):
			print('OnFrontDisconnected:nReason')
			self.OnFrontDisconnected(nReason)
	
	def __OnRspUnSubMarketData(self, pSpecificInstrument, pRspInfo, nRequestID, bIsLast):
			print('OnRspUnSubMarketData:pSpecificInstrument, pRspInfo, nRequestID, bIsLast')
			self.OnRspUnSubMarketData(POINTER(CThostFtdcSpecificInstrumentField).from_param(pSpecificInstrument).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents, nRequestID, bIsLast)
	
	def __OnRspUserLogout(self, pUserLogout, pRspInfo, nRequestID, bIsLast):
			print('OnRspUserLogout:pUserLogout, pRspInfo, nRequestID, bIsLast')
			self.OnRspUserLogout(POINTER(CThostFtdcUserLogoutField).from_param(pUserLogout).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents, nRequestID, bIsLast)
	
	def __OnRtnForQuoteRsp(self, pForQuoteRsp):
			print('OnRtnForQuoteRsp:pForQuoteRsp')
			self.OnRtnForQuoteRsp(POINTER(CThostFtdcForQuoteRspField).from_param(pForQuoteRsp).contents)
	
	def __OnHeartBeatWarning(self, nTimeLapse):
			print('OnHeartBeatWarning:nTimeLapse')
			self.OnHeartBeatWarning(nTimeLapse)
	
	def __OnRspError(self, pRspInfo, nRequestID, bIsLast):
			print('OnRspError:pRspInfo, nRequestID, bIsLast')
			self.OnRspError(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents, nRequestID, bIsLast)
	
	def __OnFrontConnected(self, ):
			print('OnFrontConnected:')
			self.OnFrontConnected()
	
	def __OnRtnDepthMarketData(self, pDepthMarketData):
			print('OnRtnDepthMarketData:pDepthMarketData')
			self.OnRtnDepthMarketData(POINTER(CThostFtdcDepthMarketDataField).from_param(pDepthMarketData).contents)
	
	def __OnRspUserLogin(self, pRspUserLogin, pRspInfo, nRequestID, bIsLast):
			print('OnRspUserLogin:pRspUserLogin, pRspInfo, nRequestID, bIsLast')
			self.OnRspUserLogin(POINTER(CThostFtdcRspUserLoginField).from_param(pRspUserLogin).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents, nRequestID, bIsLast)
	
	def __OnRspUnSubForQuoteRsp(self, pSpecificInstrument, pRspInfo, nRequestID, bIsLast):
			print('OnRspUnSubForQuoteRsp:pSpecificInstrument, pRspInfo, nRequestID, bIsLast')
			self.OnRspUnSubForQuoteRsp(POINTER(CThostFtdcSpecificInstrumentField).from_param(pSpecificInstrument).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents, nRequestID, bIsLast)
	
	def OnRspSubMarketData(self, pSpecificInstrument, pRspInfo, nRequestID, bIsLast):
			print('OnRspSubMarketData:pSpecificInstrument, pRspInfo, nRequestID, bIsLast')
	
	def OnRspSubForQuoteRsp(self, pSpecificInstrument, pRspInfo, nRequestID, bIsLast):
			print('OnRspSubForQuoteRsp:pSpecificInstrument, pRspInfo, nRequestID, bIsLast')
	
	def OnFrontDisconnected(self, nReason):
			print('OnFrontDisconnected:nReason')
	
	def OnRspUnSubMarketData(self, pSpecificInstrument, pRspInfo, nRequestID, bIsLast):
			print('OnRspUnSubMarketData:pSpecificInstrument, pRspInfo, nRequestID, bIsLast')
	
	def OnRspUserLogout(self, pUserLogout, pRspInfo, nRequestID, bIsLast):
			print('OnRspUserLogout:pUserLogout, pRspInfo, nRequestID, bIsLast')
	
	def OnRtnForQuoteRsp(self, pForQuoteRsp):
			print('OnRtnForQuoteRsp:pForQuoteRsp')
	
	def OnHeartBeatWarning(self, nTimeLapse):
			print('OnHeartBeatWarning:nTimeLapse')
	
	def OnRspError(self, pRspInfo, nRequestID, bIsLast):
			print('OnRspError:pRspInfo, nRequestID, bIsLast')
	
	def OnFrontConnected(self, ):
			print('OnFrontConnected:')
	
	def OnRtnDepthMarketData(self, pDepthMarketData):
			print('OnRtnDepthMarketData:pDepthMarketData')
	
	def OnRspUserLogin(self, pRspUserLogin, pRspInfo, nRequestID, bIsLast):
			print('OnRspUserLogin:pRspUserLogin, pRspInfo, nRequestID, bIsLast')
	
	def OnRspUnSubForQuoteRsp(self, pSpecificInstrument, pRspInfo, nRequestID, bIsLast):
			print('OnRspUnSubForQuoteRsp:pSpecificInstrument, pRspInfo, nRequestID, bIsLast')
	
	def CreateApi(self):
		self.api = self.h.CreateApi()
		return self.api

	def CreateSpi(self):
		self.spi = self.h.CreateSpi()
		return self.spi

	def RegisterNameServer(self, pszNsAddress):
		self.h.RegisterNameServer(self.api, pszNsAddress)
			
	def UnSubscribeForQuoteRsp(self, ppInstrumentID, nCount):
		self.h.UnSubscribeForQuoteRsp(self.api, ppInstrumentID, nCount)
			
	def ReqUserLogout(self, pUserLogout, nRequestID):
		self.h.ReqUserLogout(self.api, pUserLogout, nRequestID)
			
	def Init(self):
		self.h.Init(self.api)
			
	def GetTradingDay(self):
		self.h.GetTradingDay(self.api)
			
	def RegisterSpi(self, pSpi):
		self.h.RegisterSpi(self.api, pSpi)
			
	def SubscribeMarketData(self, ppInstrumentID, nCount):
		self.h.SubscribeMarketData(self.api, ppInstrumentID, nCount)
			
	def Release(self):
		self.h.Release(self.api)
			
	def Join(self):
		self.h.Join(self.api)
			
	def RegisterFensUserInfo(self, pFensUserInfo):
		self.h.RegisterFensUserInfo(self.api, pFensUserInfo)
			
	def RegisterFront(self, pszFrontAddress):
		self.h.RegisterFront(self.api, pszFrontAddress)
			
	def ReqUserLogin(self, pReqUserLoginField, nRequestID):
		self.h.ReqUserLogin(self.api, pReqUserLoginField, nRequestID)
			
	def UnSubscribeMarketData(self, ppInstrumentID, nCount):
		self.h.UnSubscribeMarketData(self.api, ppInstrumentID, nCount)
			
	def SubscribeForQuoteRsp(self, ppInstrumentID, nCount):
		self.h.SubscribeForQuoteRsp(self.api, ppInstrumentID, nCount)
			