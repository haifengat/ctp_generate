
from py_ctp.ctp_struct import *
import os

class Trade:

	def __init__(self):

		cur_path = os.getcwd()
		# change work directory
		os.chdir(os.path.join(os.getcwd(), "dll"))
		# make log dir for api log
		if not os.path.exists("log"):
			os.mkdir("log")

		self.h = CDLL("ctp_Trade.dll")

		self.h.CreateApi.argtypes = []
		self.h.CreateApi.restype = c_void_p

		self.h.CreateSpi.argtypes = []
		self.h.CreateSpi.restype = c_void_p

		self.api = None
		self.spi = None
		self.nRequestID = 0
		self.h.ReqQryOptionInstrTradeCost.argtypes = [c_void_p , c_void_p , c_int32]
		self.h.ReqQryOptionInstrTradeCost.restype = c_void_p
		self.h.GetTradingDay.argtypes = [c_void_p]
		self.h.GetTradingDay.restype = c_void_p
		self.h.Join.argtypes = [c_void_p]
		self.h.Join.restype = c_void_p
		self.h.ReqQryExecOrder.argtypes = [c_void_p , c_void_p , c_int32]
		self.h.ReqQryExecOrder.restype = c_void_p
		self.h.ReqRemoveParkedOrderAction.argtypes = [c_void_p , c_void_p , c_int32]
		self.h.ReqRemoveParkedOrderAction.restype = c_void_p
		self.h.ReqQryLock.argtypes = [c_void_p , c_void_p , c_int32]
		self.h.ReqQryLock.restype = c_void_p
		self.h.ReqQryInvestorProductGroupMargin.argtypes = [c_void_p , c_void_p , c_int32]
		self.h.ReqQryInvestorProductGroupMargin.restype = c_void_p
		self.h.ReqQrySecAgentACIDMap.argtypes = [c_void_p , c_void_p , c_int32]
		self.h.ReqQrySecAgentACIDMap.restype = c_void_p
		self.h.ReqQryExchange.argtypes = [c_void_p , c_void_p , c_int32]
		self.h.ReqQryExchange.restype = c_void_p
		self.h.ReqQryInstrument.argtypes = [c_void_p , c_void_p , c_int32]
		self.h.ReqQryInstrument.restype = c_void_p
		self.h.ReqTradingAccountPasswordUpdate.argtypes = [c_void_p , c_void_p , c_int32]
		self.h.ReqTradingAccountPasswordUpdate.restype = c_void_p
		self.h.ReqQryMMInstrumentCommissionRate.argtypes = [c_void_p , c_void_p , c_int32]
		self.h.ReqQryMMInstrumentCommissionRate.restype = c_void_p
		self.h.ReqQuoteInsert.argtypes = [c_void_p , c_void_p , c_int32]
		self.h.ReqQuoteInsert.restype = c_void_p
		self.h.ReqQryTransferSerial.argtypes = [c_void_p , c_void_p , c_int32]
		self.h.ReqQryTransferSerial.restype = c_void_p
		self.h.ReqQryProductExchRate.argtypes = [c_void_p , c_void_p , c_int32]
		self.h.ReqQryProductExchRate.restype = c_void_p
		self.h.ReqQryInvestorLevel.argtypes = [c_void_p , c_void_p , c_int32]
		self.h.ReqQryInvestorLevel.restype = c_void_p
		self.h.ReqQryInvestor.argtypes = [c_void_p , c_void_p , c_int32]
		self.h.ReqQryInvestor.restype = c_void_p
		self.h.ReqQryForQuote.argtypes = [c_void_p , c_void_p , c_int32]
		self.h.ReqQryForQuote.restype = c_void_p
		self.h.ReqExecOrderInsert.argtypes = [c_void_p , c_void_p , c_int32]
		self.h.ReqExecOrderInsert.restype = c_void_p
		self.h.ReqOrderInsert.argtypes = [c_void_p , c_void_p , c_int32]
		self.h.ReqOrderInsert.restype = c_void_p
		self.h.ReqFromBankToFutureByFuture.argtypes = [c_void_p , c_void_p , c_int32]
		self.h.ReqFromBankToFutureByFuture.restype = c_void_p
		self.h.ReqQryProduct.argtypes = [c_void_p , c_void_p , c_int32]
		self.h.ReqQryProduct.restype = c_void_p
		self.h.ReqQryInstrumentMarginRate.argtypes = [c_void_p , c_void_p , c_int32]
		self.h.ReqQryInstrumentMarginRate.restype = c_void_p
		self.h.ReqParkedOrderAction.argtypes = [c_void_p , c_void_p , c_int32]
		self.h.ReqParkedOrderAction.restype = c_void_p
		self.h.RegisterNameServer.argtypes = [c_void_p , c_char_p]
		self.h.RegisterNameServer.restype = c_void_p
		self.h.ReqUserLogout.argtypes = [c_void_p , c_void_p , c_int32]
		self.h.ReqUserLogout.restype = c_void_p
		self.h.ReqOrderAction.argtypes = [c_void_p , c_void_p , c_int32]
		self.h.ReqOrderAction.restype = c_void_p
		self.h.ReqForQuoteInsert.argtypes = [c_void_p , c_void_p , c_int32]
		self.h.ReqForQuoteInsert.restype = c_void_p
		self.h.ReqQryInstrumentOrderCommRate.argtypes = [c_void_p , c_void_p , c_int32]
		self.h.ReqQryInstrumentOrderCommRate.restype = c_void_p
		self.h.ReqQryInvestorPositionDetail.argtypes = [c_void_p , c_void_p , c_int32]
		self.h.ReqQryInvestorPositionDetail.restype = c_void_p
		self.h.ReqQrySettlementInfoConfirm.argtypes = [c_void_p , c_void_p , c_int32]
		self.h.ReqQrySettlementInfoConfirm.restype = c_void_p
		self.h.ReqUserPasswordUpdate.argtypes = [c_void_p , c_void_p , c_int32]
		self.h.ReqUserPasswordUpdate.restype = c_void_p
		self.h.ReqAuthenticate.argtypes = [c_void_p , c_void_p , c_int32]
		self.h.ReqAuthenticate.restype = c_void_p
		self.h.ReqQryDepthMarketData.argtypes = [c_void_p , c_void_p , c_int32]
		self.h.ReqQryDepthMarketData.restype = c_void_p
		self.h.ReqQryParkedOrder.argtypes = [c_void_p , c_void_p , c_int32]
		self.h.ReqQryParkedOrder.restype = c_void_p
		self.h.ReqSettlementInfoConfirm.argtypes = [c_void_p , c_void_p , c_int32]
		self.h.ReqSettlementInfoConfirm.restype = c_void_p
		self.h.ReqQryExchangeMarginRate.argtypes = [c_void_p , c_void_p , c_int32]
		self.h.ReqQryExchangeMarginRate.restype = c_void_p
		self.h.ReqQryTradingNotice.argtypes = [c_void_p , c_void_p , c_int32]
		self.h.ReqQryTradingNotice.restype = c_void_p
		self.h.ReqQryCombInstrumentGuard.argtypes = [c_void_p , c_void_p , c_int32]
		self.h.ReqQryCombInstrumentGuard.restype = c_void_p
		self.h.ReqFromFutureToBankByFuture.argtypes = [c_void_p , c_void_p , c_int32]
		self.h.ReqFromFutureToBankByFuture.restype = c_void_p
		self.h.ReqQueryCFMMCTradingAccountToken.argtypes = [c_void_p , c_void_p , c_int32]
		self.h.ReqQueryCFMMCTradingAccountToken.restype = c_void_p
		self.h.ReqQryEWarrantOffset.argtypes = [c_void_p , c_void_p , c_int32]
		self.h.ReqQryEWarrantOffset.restype = c_void_p
		self.h.ReqQryMMOptionInstrCommRate.argtypes = [c_void_p , c_void_p , c_int32]
		self.h.ReqQryMMOptionInstrCommRate.restype = c_void_p
		self.h.ReqQryInvestorPosition.argtypes = [c_void_p , c_void_p , c_int32]
		self.h.ReqQryInvestorPosition.restype = c_void_p
		self.h.ReqQryBrokerTradingParams.argtypes = [c_void_p , c_void_p , c_int32]
		self.h.ReqQryBrokerTradingParams.restype = c_void_p
		self.h.ReqQryContractBank.argtypes = [c_void_p , c_void_p , c_int32]
		self.h.ReqQryContractBank.restype = c_void_p
		self.h.ReqLockInsert.argtypes = [c_void_p , c_void_p , c_int32]
		self.h.ReqLockInsert.restype = c_void_p
		self.h.ReqQryParkedOrderAction.argtypes = [c_void_p , c_void_p , c_int32]
		self.h.ReqQryParkedOrderAction.restype = c_void_p
		self.h.ReqQryBrokerTradingAlgos.argtypes = [c_void_p , c_void_p , c_int32]
		self.h.ReqQryBrokerTradingAlgos.restype = c_void_p
		self.h.ReqExecOrderAction.argtypes = [c_void_p , c_void_p , c_int32]
		self.h.ReqExecOrderAction.restype = c_void_p
		self.h.Release.argtypes = [c_void_p]
		self.h.Release.restype = c_void_p
		self.h.ReqQryCombAction.argtypes = [c_void_p , c_void_p , c_int32]
		self.h.ReqQryCombAction.restype = c_void_p
		self.h.ReqQryTradingCode.argtypes = [c_void_p , c_void_p , c_int32]
		self.h.ReqQryTradingCode.restype = c_void_p
		self.h.ReqQryTradingAccount.argtypes = [c_void_p , c_void_p , c_int32]
		self.h.ReqQryTradingAccount.restype = c_void_p
		self.h.ReqQryNotice.argtypes = [c_void_p , c_void_p , c_int32]
		self.h.ReqQryNotice.restype = c_void_p
		self.h.ReqQryExchangeRate.argtypes = [c_void_p , c_void_p , c_int32]
		self.h.ReqQryExchangeRate.restype = c_void_p
		self.h.ReqQryExecFreeze.argtypes = [c_void_p , c_void_p , c_int32]
		self.h.ReqQryExecFreeze.restype = c_void_p
		self.h.ReqQueryBankAccountMoneyByFuture.argtypes = [c_void_p , c_void_p , c_int32]
		self.h.ReqQueryBankAccountMoneyByFuture.restype = c_void_p
		self.h.Init.argtypes = [c_void_p]
		self.h.Init.restype = c_void_p
		self.h.RegisterFront.argtypes = [c_void_p , c_char_p]
		self.h.RegisterFront.restype = c_void_p
		self.h.ReqQryTransferBank.argtypes = [c_void_p , c_void_p , c_int32]
		self.h.ReqQryTransferBank.restype = c_void_p
		self.h.ReqQryOrder.argtypes = [c_void_p , c_void_p , c_int32]
		self.h.ReqQryOrder.restype = c_void_p
		self.h.ReqQueryMaxOrderVolume.argtypes = [c_void_p , c_void_p , c_int32]
		self.h.ReqQueryMaxOrderVolume.restype = c_void_p
		self.h.ReqQryETFOptionInstrCommRate.argtypes = [c_void_p , c_void_p , c_int32]
		self.h.ReqQryETFOptionInstrCommRate.restype = c_void_p
		self.h.ReqQryCFMMCTradingAccountKey.argtypes = [c_void_p , c_void_p , c_int32]
		self.h.ReqQryCFMMCTradingAccountKey.restype = c_void_p
		self.h.ReqCombActionInsert.argtypes = [c_void_p , c_void_p , c_int32]
		self.h.ReqCombActionInsert.restype = c_void_p
		self.h.ReqQryLockPosition.argtypes = [c_void_p , c_void_p , c_int32]
		self.h.ReqQryLockPosition.restype = c_void_p
		self.h.ReqQryExchangeMarginRateAdjust.argtypes = [c_void_p , c_void_p , c_int32]
		self.h.ReqQryExchangeMarginRateAdjust.restype = c_void_p
		self.h.ReqQryInstrumentCommissionRate.argtypes = [c_void_p , c_void_p , c_int32]
		self.h.ReqQryInstrumentCommissionRate.restype = c_void_p
		self.h.ReqQryOptionInstrCommRate.argtypes = [c_void_p , c_void_p , c_int32]
		self.h.ReqQryOptionInstrCommRate.restype = c_void_p
		self.h.ReqQrySettlementInfo.argtypes = [c_void_p , c_void_p , c_int32]
		self.h.ReqQrySettlementInfo.restype = c_void_p
		self.h.ReqQryTrade.argtypes = [c_void_p , c_void_p , c_int32]
		self.h.ReqQryTrade.restype = c_void_p
		self.h.ReqQryProductGroup.argtypes = [c_void_p , c_void_p , c_int32]
		self.h.ReqQryProductGroup.restype = c_void_p
		self.h.ReqQuoteAction.argtypes = [c_void_p , c_void_p , c_int32]
		self.h.ReqQuoteAction.restype = c_void_p
		self.h.ReqQryInvestorPositionCombineDetail.argtypes = [c_void_p , c_void_p , c_int32]
		self.h.ReqQryInvestorPositionCombineDetail.restype = c_void_p
		self.h.RegisterFensUserInfo.argtypes = [c_void_p , c_void_p]
		self.h.RegisterFensUserInfo.restype = c_void_p
		self.h.ReqRemoveParkedOrder.argtypes = [c_void_p , c_void_p , c_int32]
		self.h.ReqRemoveParkedOrder.restype = c_void_p
		self.h.ReqBatchOrderAction.argtypes = [c_void_p , c_void_p , c_int32]
		self.h.ReqBatchOrderAction.restype = c_void_p
		self.h.ReqQryQuote.argtypes = [c_void_p , c_void_p , c_int32]
		self.h.ReqQryQuote.restype = c_void_p
		self.h.RegisterSpi.argtypes = [c_void_p , c_void_p]
		self.h.RegisterSpi.restype = c_void_p
		self.h.ReqParkedOrderInsert.argtypes = [c_void_p , c_void_p , c_int32]
		self.h.ReqParkedOrderInsert.restype = c_void_p
		self.h.ReqQryAccountregister.argtypes = [c_void_p , c_void_p , c_int32]
		self.h.ReqQryAccountregister.restype = c_void_p
		self.h.ReqUserLogin.argtypes = [c_void_p , c_void_p , c_int32]
		self.h.ReqUserLogin.restype = c_void_p

		# restore work directory
		os.chdir(cur_path)


	def RegCB(self):
		"""在createapi, createspi后调用"""

		self.h.SetOnRspQryCombAction.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRspQryCombAction.restype = c_void_p
		self.evOnRspQryCombAction = CFUNCTYPE(c_void_p, POINTER(CThostFtdcCombActionField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryCombAction)
		self.h.SetOnRspQryCombAction(self.spi, self.evOnRspQryCombAction)

		self.h.SetOnRtnRepealFromFutureToBankByFutureManual.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRtnRepealFromFutureToBankByFutureManual.restype = c_void_p
		self.evOnRtnRepealFromFutureToBankByFutureManual = CFUNCTYPE(c_void_p, POINTER(CThostFtdcRspRepealField))(self.__OnRtnRepealFromFutureToBankByFutureManual)
		self.h.SetOnRtnRepealFromFutureToBankByFutureManual(self.spi, self.evOnRtnRepealFromFutureToBankByFutureManual)

		self.h.SetOnRtnTrade.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRtnTrade.restype = c_void_p
		self.evOnRtnTrade = CFUNCTYPE(c_void_p, POINTER(CThostFtdcTradeField))(self.__OnRtnTrade)
		self.h.SetOnRtnTrade(self.spi, self.evOnRtnTrade)

		self.h.SetOnRspQryParkedOrder.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRspQryParkedOrder.restype = c_void_p
		self.evOnRspQryParkedOrder = CFUNCTYPE(c_void_p, POINTER(CThostFtdcParkedOrderField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryParkedOrder)
		self.h.SetOnRspQryParkedOrder(self.spi, self.evOnRspQryParkedOrder)

		self.h.SetOnRtnForQuoteRsp.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRtnForQuoteRsp.restype = c_void_p
		self.evOnRtnForQuoteRsp = CFUNCTYPE(c_void_p, POINTER(CThostFtdcForQuoteRspField))(self.__OnRtnForQuoteRsp)
		self.h.SetOnRtnForQuoteRsp(self.spi, self.evOnRtnForQuoteRsp)

		self.h.SetOnRtnLock.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRtnLock.restype = c_void_p
		self.evOnRtnLock = CFUNCTYPE(c_void_p, POINTER(CThostFtdcLockField))(self.__OnRtnLock)
		self.h.SetOnRtnLock(self.spi, self.evOnRtnLock)

		self.h.SetOnRspError.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRspError.restype = c_void_p
		self.evOnRspError = CFUNCTYPE(c_void_p, POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspError)
		self.h.SetOnRspError(self.spi, self.evOnRspError)

		self.h.SetOnRspQryTradingAccount.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRspQryTradingAccount.restype = c_void_p
		self.evOnRspQryTradingAccount = CFUNCTYPE(c_void_p, POINTER(CThostFtdcTradingAccountField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryTradingAccount)
		self.h.SetOnRspQryTradingAccount(self.spi, self.evOnRspQryTradingAccount)

		self.h.SetOnRspQrySettlementInfoConfirm.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRspQrySettlementInfoConfirm.restype = c_void_p
		self.evOnRspQrySettlementInfoConfirm = CFUNCTYPE(c_void_p, POINTER(CThostFtdcSettlementInfoConfirmField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQrySettlementInfoConfirm)
		self.h.SetOnRspQrySettlementInfoConfirm(self.spi, self.evOnRspQrySettlementInfoConfirm)

		self.h.SetOnErrRtnForQuoteInsert.argtypes = [c_void_p, c_void_p]
		self.h.SetOnErrRtnForQuoteInsert.restype = c_void_p
		self.evOnErrRtnForQuoteInsert = CFUNCTYPE(c_void_p, POINTER(CThostFtdcInputForQuoteField), POINTER(CThostFtdcRspInfoField))(self.__OnErrRtnForQuoteInsert)
		self.h.SetOnErrRtnForQuoteInsert(self.spi, self.evOnErrRtnForQuoteInsert)

		self.h.SetOnFrontConnected.argtypes = [c_void_p, c_void_p]
		self.h.SetOnFrontConnected.restype = c_void_p
		self.evOnFrontConnected = CFUNCTYPE(c_void_p)(self.__OnFrontConnected)
		self.h.SetOnFrontConnected(self.spi, self.evOnFrontConnected)

		self.h.SetOnRspQryMMInstrumentCommissionRate.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRspQryMMInstrumentCommissionRate.restype = c_void_p
		self.evOnRspQryMMInstrumentCommissionRate = CFUNCTYPE(c_void_p, POINTER(CThostFtdcMMInstrumentCommissionRateField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryMMInstrumentCommissionRate)
		self.h.SetOnRspQryMMInstrumentCommissionRate(self.spi, self.evOnRspQryMMInstrumentCommissionRate)

		self.h.SetOnRspFromBankToFutureByFuture.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRspFromBankToFutureByFuture.restype = c_void_p
		self.evOnRspFromBankToFutureByFuture = CFUNCTYPE(c_void_p, POINTER(CThostFtdcReqTransferField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspFromBankToFutureByFuture)
		self.h.SetOnRspFromBankToFutureByFuture(self.spi, self.evOnRspFromBankToFutureByFuture)

		self.h.SetOnRspQueryMaxOrderVolume.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRspQueryMaxOrderVolume.restype = c_void_p
		self.evOnRspQueryMaxOrderVolume = CFUNCTYPE(c_void_p, POINTER(CThostFtdcQueryMaxOrderVolumeField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQueryMaxOrderVolume)
		self.h.SetOnRspQueryMaxOrderVolume(self.spi, self.evOnRspQueryMaxOrderVolume)

		self.h.SetOnRspQryTrade.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRspQryTrade.restype = c_void_p
		self.evOnRspQryTrade = CFUNCTYPE(c_void_p, POINTER(CThostFtdcTradeField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryTrade)
		self.h.SetOnRspQryTrade(self.spi, self.evOnRspQryTrade)

		self.h.SetOnRspQryDepthMarketData.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRspQryDepthMarketData.restype = c_void_p
		self.evOnRspQryDepthMarketData = CFUNCTYPE(c_void_p, POINTER(CThostFtdcDepthMarketDataField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryDepthMarketData)
		self.h.SetOnRspQryDepthMarketData(self.spi, self.evOnRspQryDepthMarketData)

		self.h.SetOnRspRemoveParkedOrderAction.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRspRemoveParkedOrderAction.restype = c_void_p
		self.evOnRspRemoveParkedOrderAction = CFUNCTYPE(c_void_p, POINTER(CThostFtdcRemoveParkedOrderActionField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspRemoveParkedOrderAction)
		self.h.SetOnRspRemoveParkedOrderAction(self.spi, self.evOnRspRemoveParkedOrderAction)

		self.h.SetOnRspQryOrder.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRspQryOrder.restype = c_void_p
		self.evOnRspQryOrder = CFUNCTYPE(c_void_p, POINTER(CThostFtdcOrderField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryOrder)
		self.h.SetOnRspQryOrder(self.spi, self.evOnRspQryOrder)

		self.h.SetOnRtnFromFutureToBankByFuture.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRtnFromFutureToBankByFuture.restype = c_void_p
		self.evOnRtnFromFutureToBankByFuture = CFUNCTYPE(c_void_p, POINTER(CThostFtdcRspTransferField))(self.__OnRtnFromFutureToBankByFuture)
		self.h.SetOnRtnFromFutureToBankByFuture(self.spi, self.evOnRtnFromFutureToBankByFuture)

		self.h.SetOnRtnErrorConditionalOrder.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRtnErrorConditionalOrder.restype = c_void_p
		self.evOnRtnErrorConditionalOrder = CFUNCTYPE(c_void_p, POINTER(CThostFtdcErrorConditionalOrderField))(self.__OnRtnErrorConditionalOrder)
		self.h.SetOnRtnErrorConditionalOrder(self.spi, self.evOnRtnErrorConditionalOrder)

		self.h.SetOnRspQrySecAgentACIDMap.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRspQrySecAgentACIDMap.restype = c_void_p
		self.evOnRspQrySecAgentACIDMap = CFUNCTYPE(c_void_p, POINTER(CThostFtdcSecAgentACIDMapField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQrySecAgentACIDMap)
		self.h.SetOnRspQrySecAgentACIDMap(self.spi, self.evOnRspQrySecAgentACIDMap)

		self.h.SetOnRtnExecOrder.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRtnExecOrder.restype = c_void_p
		self.evOnRtnExecOrder = CFUNCTYPE(c_void_p, POINTER(CThostFtdcExecOrderField))(self.__OnRtnExecOrder)
		self.h.SetOnRtnExecOrder(self.spi, self.evOnRtnExecOrder)

		self.h.SetOnRspLockInsert.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRspLockInsert.restype = c_void_p
		self.evOnRspLockInsert = CFUNCTYPE(c_void_p, POINTER(CThostFtdcInputLockField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspLockInsert)
		self.h.SetOnRspLockInsert(self.spi, self.evOnRspLockInsert)

		self.h.SetOnRspQryInvestorProductGroupMargin.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRspQryInvestorProductGroupMargin.restype = c_void_p
		self.evOnRspQryInvestorProductGroupMargin = CFUNCTYPE(c_void_p, POINTER(CThostFtdcInvestorProductGroupMarginField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryInvestorProductGroupMargin)
		self.h.SetOnRspQryInvestorProductGroupMargin(self.spi, self.evOnRspQryInvestorProductGroupMargin)

		self.h.SetOnRspQrySettlementInfo.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRspQrySettlementInfo.restype = c_void_p
		self.evOnRspQrySettlementInfo = CFUNCTYPE(c_void_p, POINTER(CThostFtdcSettlementInfoField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQrySettlementInfo)
		self.h.SetOnRspQrySettlementInfo(self.spi, self.evOnRspQrySettlementInfo)

		self.h.SetOnRtnQuote.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRtnQuote.restype = c_void_p
		self.evOnRtnQuote = CFUNCTYPE(c_void_p, POINTER(CThostFtdcQuoteField))(self.__OnRtnQuote)
		self.h.SetOnRtnQuote(self.spi, self.evOnRtnQuote)

		self.h.SetOnErrRtnQuoteInsert.argtypes = [c_void_p, c_void_p]
		self.h.SetOnErrRtnQuoteInsert.restype = c_void_p
		self.evOnErrRtnQuoteInsert = CFUNCTYPE(c_void_p, POINTER(CThostFtdcInputQuoteField), POINTER(CThostFtdcRspInfoField))(self.__OnErrRtnQuoteInsert)
		self.h.SetOnErrRtnQuoteInsert(self.spi, self.evOnErrRtnQuoteInsert)

		self.h.SetOnErrRtnOrderInsert.argtypes = [c_void_p, c_void_p]
		self.h.SetOnErrRtnOrderInsert.restype = c_void_p
		self.evOnErrRtnOrderInsert = CFUNCTYPE(c_void_p, POINTER(CThostFtdcInputOrderField), POINTER(CThostFtdcRspInfoField))(self.__OnErrRtnOrderInsert)
		self.h.SetOnErrRtnOrderInsert(self.spi, self.evOnErrRtnOrderInsert)

		self.h.SetOnRtnQueryBankBalanceByFuture.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRtnQueryBankBalanceByFuture.restype = c_void_p
		self.evOnRtnQueryBankBalanceByFuture = CFUNCTYPE(c_void_p, POINTER(CThostFtdcNotifyQueryAccountField))(self.__OnRtnQueryBankBalanceByFuture)
		self.h.SetOnRtnQueryBankBalanceByFuture(self.spi, self.evOnRtnQueryBankBalanceByFuture)

		self.h.SetOnErrRtnQueryBankBalanceByFuture.argtypes = [c_void_p, c_void_p]
		self.h.SetOnErrRtnQueryBankBalanceByFuture.restype = c_void_p
		self.evOnErrRtnQueryBankBalanceByFuture = CFUNCTYPE(c_void_p, POINTER(CThostFtdcReqQueryAccountField), POINTER(CThostFtdcRspInfoField))(self.__OnErrRtnQueryBankBalanceByFuture)
		self.h.SetOnErrRtnQueryBankBalanceByFuture(self.spi, self.evOnErrRtnQueryBankBalanceByFuture)

		self.h.SetOnRspExecOrderAction.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRspExecOrderAction.restype = c_void_p
		self.evOnRspExecOrderAction = CFUNCTYPE(c_void_p, POINTER(CThostFtdcInputExecOrderActionField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspExecOrderAction)
		self.h.SetOnRspExecOrderAction(self.spi, self.evOnRspExecOrderAction)

		self.h.SetOnRspQryOptionInstrCommRate.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRspQryOptionInstrCommRate.restype = c_void_p
		self.evOnRspQryOptionInstrCommRate = CFUNCTYPE(c_void_p, POINTER(CThostFtdcOptionInstrCommRateField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryOptionInstrCommRate)
		self.h.SetOnRspQryOptionInstrCommRate(self.spi, self.evOnRspQryOptionInstrCommRate)

		self.h.SetOnRspQueryCFMMCTradingAccountToken.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRspQueryCFMMCTradingAccountToken.restype = c_void_p
		self.evOnRspQueryCFMMCTradingAccountToken = CFUNCTYPE(c_void_p, POINTER(CThostFtdcQueryCFMMCTradingAccountTokenField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQueryCFMMCTradingAccountToken)
		self.h.SetOnRspQueryCFMMCTradingAccountToken(self.spi, self.evOnRspQueryCFMMCTradingAccountToken)

		self.h.SetOnRspQryAccountregister.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRspQryAccountregister.restype = c_void_p
		self.evOnRspQryAccountregister = CFUNCTYPE(c_void_p, POINTER(CThostFtdcAccountregisterField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryAccountregister)
		self.h.SetOnRspQryAccountregister(self.spi, self.evOnRspQryAccountregister)

		self.h.SetOnRspQryBrokerTradingAlgos.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRspQryBrokerTradingAlgos.restype = c_void_p
		self.evOnRspQryBrokerTradingAlgos = CFUNCTYPE(c_void_p, POINTER(CThostFtdcBrokerTradingAlgosField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryBrokerTradingAlgos)
		self.h.SetOnRspQryBrokerTradingAlgos(self.spi, self.evOnRspQryBrokerTradingAlgos)

		self.h.SetOnRtnOpenAccountByBank.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRtnOpenAccountByBank.restype = c_void_p
		self.evOnRtnOpenAccountByBank = CFUNCTYPE(c_void_p, POINTER(CThostFtdcOpenAccountField))(self.__OnRtnOpenAccountByBank)
		self.h.SetOnRtnOpenAccountByBank(self.spi, self.evOnRtnOpenAccountByBank)

		self.h.SetOnFrontDisconnected.argtypes = [c_void_p, c_void_p]
		self.h.SetOnFrontDisconnected.restype = c_void_p
		self.evOnFrontDisconnected = CFUNCTYPE(c_void_p, c_int32)(self.__OnFrontDisconnected)
		self.h.SetOnFrontDisconnected(self.spi, self.evOnFrontDisconnected)

		self.h.SetOnRspQryLockPosition.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRspQryLockPosition.restype = c_void_p
		self.evOnRspQryLockPosition = CFUNCTYPE(c_void_p, POINTER(CThostFtdcLockPositionField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryLockPosition)
		self.h.SetOnRspQryLockPosition(self.spi, self.evOnRspQryLockPosition)

		self.h.SetOnRspQryInvestorPosition.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRspQryInvestorPosition.restype = c_void_p
		self.evOnRspQryInvestorPosition = CFUNCTYPE(c_void_p, POINTER(CThostFtdcInvestorPositionField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryInvestorPosition)
		self.h.SetOnRspQryInvestorPosition(self.spi, self.evOnRspQryInvestorPosition)

		self.h.SetOnRspQryExchange.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRspQryExchange.restype = c_void_p
		self.evOnRspQryExchange = CFUNCTYPE(c_void_p, POINTER(CThostFtdcExchangeField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryExchange)
		self.h.SetOnRspQryExchange(self.spi, self.evOnRspQryExchange)

		self.h.SetOnRtnCFMMCTradingAccountToken.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRtnCFMMCTradingAccountToken.restype = c_void_p
		self.evOnRtnCFMMCTradingAccountToken = CFUNCTYPE(c_void_p, POINTER(CThostFtdcCFMMCTradingAccountTokenField))(self.__OnRtnCFMMCTradingAccountToken)
		self.h.SetOnRtnCFMMCTradingAccountToken(self.spi, self.evOnRtnCFMMCTradingAccountToken)

		self.h.SetOnRspAuthenticate.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRspAuthenticate.restype = c_void_p
		self.evOnRspAuthenticate = CFUNCTYPE(c_void_p, POINTER(CThostFtdcRspAuthenticateField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspAuthenticate)
		self.h.SetOnRspAuthenticate(self.spi, self.evOnRspAuthenticate)

		self.h.SetOnRtnRepealFromBankToFutureByBank.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRtnRepealFromBankToFutureByBank.restype = c_void_p
		self.evOnRtnRepealFromBankToFutureByBank = CFUNCTYPE(c_void_p, POINTER(CThostFtdcRspRepealField))(self.__OnRtnRepealFromBankToFutureByBank)
		self.h.SetOnRtnRepealFromBankToFutureByBank(self.spi, self.evOnRtnRepealFromBankToFutureByBank)

		self.h.SetOnRspQryForQuote.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRspQryForQuote.restype = c_void_p
		self.evOnRspQryForQuote = CFUNCTYPE(c_void_p, POINTER(CThostFtdcForQuoteField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryForQuote)
		self.h.SetOnRspQryForQuote(self.spi, self.evOnRspQryForQuote)

		self.h.SetOnErrRtnBatchOrderAction.argtypes = [c_void_p, c_void_p]
		self.h.SetOnErrRtnBatchOrderAction.restype = c_void_p
		self.evOnErrRtnBatchOrderAction = CFUNCTYPE(c_void_p, POINTER(CThostFtdcBatchOrderActionField), POINTER(CThostFtdcRspInfoField))(self.__OnErrRtnBatchOrderAction)
		self.h.SetOnErrRtnBatchOrderAction(self.spi, self.evOnErrRtnBatchOrderAction)

		self.h.SetOnRspQryProductGroup.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRspQryProductGroup.restype = c_void_p
		self.evOnRspQryProductGroup = CFUNCTYPE(c_void_p, POINTER(CThostFtdcProductGroupField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryProductGroup)
		self.h.SetOnRspQryProductGroup(self.spi, self.evOnRspQryProductGroup)

		self.h.SetOnRtnRepealFromBankToFutureByFutureManual.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRtnRepealFromBankToFutureByFutureManual.restype = c_void_p
		self.evOnRtnRepealFromBankToFutureByFutureManual = CFUNCTYPE(c_void_p, POINTER(CThostFtdcRspRepealField))(self.__OnRtnRepealFromBankToFutureByFutureManual)
		self.h.SetOnRtnRepealFromBankToFutureByFutureManual(self.spi, self.evOnRtnRepealFromBankToFutureByFutureManual)

		self.h.SetOnRspQryInstrument.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRspQryInstrument.restype = c_void_p
		self.evOnRspQryInstrument = CFUNCTYPE(c_void_p, POINTER(CThostFtdcInstrumentField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryInstrument)
		self.h.SetOnRspQryInstrument(self.spi, self.evOnRspQryInstrument)

		self.h.SetOnRspQryExchangeMarginRate.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRspQryExchangeMarginRate.restype = c_void_p
		self.evOnRspQryExchangeMarginRate = CFUNCTYPE(c_void_p, POINTER(CThostFtdcExchangeMarginRateField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryExchangeMarginRate)
		self.h.SetOnRspQryExchangeMarginRate(self.spi, self.evOnRspQryExchangeMarginRate)

		self.h.SetOnRspUserLogin.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRspUserLogin.restype = c_void_p
		self.evOnRspUserLogin = CFUNCTYPE(c_void_p, POINTER(CThostFtdcRspUserLoginField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspUserLogin)
		self.h.SetOnRspUserLogin(self.spi, self.evOnRspUserLogin)

		self.h.SetOnRtnTradingNotice.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRtnTradingNotice.restype = c_void_p
		self.evOnRtnTradingNotice = CFUNCTYPE(c_void_p, POINTER(CThostFtdcTradingNoticeInfoField))(self.__OnRtnTradingNotice)
		self.h.SetOnRtnTradingNotice(self.spi, self.evOnRtnTradingNotice)

		self.h.SetOnRspQryTransferSerial.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRspQryTransferSerial.restype = c_void_p
		self.evOnRspQryTransferSerial = CFUNCTYPE(c_void_p, POINTER(CThostFtdcTransferSerialField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryTransferSerial)
		self.h.SetOnRspQryTransferSerial(self.spi, self.evOnRspQryTransferSerial)

		self.h.SetOnRspParkedOrderAction.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRspParkedOrderAction.restype = c_void_p
		self.evOnRspParkedOrderAction = CFUNCTYPE(c_void_p, POINTER(CThostFtdcParkedOrderActionField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspParkedOrderAction)
		self.h.SetOnRspParkedOrderAction(self.spi, self.evOnRspParkedOrderAction)

		self.h.SetOnRtnFromBankToFutureByBank.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRtnFromBankToFutureByBank.restype = c_void_p
		self.evOnRtnFromBankToFutureByBank = CFUNCTYPE(c_void_p, POINTER(CThostFtdcRspTransferField))(self.__OnRtnFromBankToFutureByBank)
		self.h.SetOnRtnFromBankToFutureByBank(self.spi, self.evOnRtnFromBankToFutureByBank)

		self.h.SetOnRspCombActionInsert.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRspCombActionInsert.restype = c_void_p
		self.evOnRspCombActionInsert = CFUNCTYPE(c_void_p, POINTER(CThostFtdcInputCombActionField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspCombActionInsert)
		self.h.SetOnRspCombActionInsert(self.spi, self.evOnRspCombActionInsert)

		self.h.SetOnRtnOrder.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRtnOrder.restype = c_void_p
		self.evOnRtnOrder = CFUNCTYPE(c_void_p, POINTER(CThostFtdcOrderField))(self.__OnRtnOrder)
		self.h.SetOnRtnOrder(self.spi, self.evOnRtnOrder)

		self.h.SetOnRtnCancelAccountByBank.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRtnCancelAccountByBank.restype = c_void_p
		self.evOnRtnCancelAccountByBank = CFUNCTYPE(c_void_p, POINTER(CThostFtdcCancelAccountField))(self.__OnRtnCancelAccountByBank)
		self.h.SetOnRtnCancelAccountByBank(self.spi, self.evOnRtnCancelAccountByBank)

		self.h.SetOnRspQryExchangeMarginRateAdjust.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRspQryExchangeMarginRateAdjust.restype = c_void_p
		self.evOnRspQryExchangeMarginRateAdjust = CFUNCTYPE(c_void_p, POINTER(CThostFtdcExchangeMarginRateAdjustField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryExchangeMarginRateAdjust)
		self.h.SetOnRspQryExchangeMarginRateAdjust(self.spi, self.evOnRspQryExchangeMarginRateAdjust)

		self.h.SetOnRspQryInstrumentOrderCommRate.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRspQryInstrumentOrderCommRate.restype = c_void_p
		self.evOnRspQryInstrumentOrderCommRate = CFUNCTYPE(c_void_p, POINTER(CThostFtdcInstrumentOrderCommRateField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryInstrumentOrderCommRate)
		self.h.SetOnRspQryInstrumentOrderCommRate(self.spi, self.evOnRspQryInstrumentOrderCommRate)

		self.h.SetOnRspQryEWarrantOffset.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRspQryEWarrantOffset.restype = c_void_p
		self.evOnRspQryEWarrantOffset = CFUNCTYPE(c_void_p, POINTER(CThostFtdcEWarrantOffsetField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryEWarrantOffset)
		self.h.SetOnRspQryEWarrantOffset(self.spi, self.evOnRspQryEWarrantOffset)

		self.h.SetOnRspQryInvestorLevel.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRspQryInvestorLevel.restype = c_void_p
		self.evOnRspQryInvestorLevel = CFUNCTYPE(c_void_p, POINTER(CThostFtdcInvestorLevelField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryInvestorLevel)
		self.h.SetOnRspQryInvestorLevel(self.spi, self.evOnRspQryInvestorLevel)

		self.h.SetOnRspQryQuote.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRspQryQuote.restype = c_void_p
		self.evOnRspQryQuote = CFUNCTYPE(c_void_p, POINTER(CThostFtdcQuoteField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryQuote)
		self.h.SetOnRspQryQuote(self.spi, self.evOnRspQryQuote)

		self.h.SetOnRspQryInvestorPositionCombineDetail.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRspQryInvestorPositionCombineDetail.restype = c_void_p
		self.evOnRspQryInvestorPositionCombineDetail = CFUNCTYPE(c_void_p, POINTER(CThostFtdcInvestorPositionCombineDetailField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryInvestorPositionCombineDetail)
		self.h.SetOnRspQryInvestorPositionCombineDetail(self.spi, self.evOnRspQryInvestorPositionCombineDetail)

		self.h.SetOnRspQryInstrumentCommissionRate.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRspQryInstrumentCommissionRate.restype = c_void_p
		self.evOnRspQryInstrumentCommissionRate = CFUNCTYPE(c_void_p, POINTER(CThostFtdcInstrumentCommissionRateField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryInstrumentCommissionRate)
		self.h.SetOnRspQryInstrumentCommissionRate(self.spi, self.evOnRspQryInstrumentCommissionRate)

		self.h.SetOnErrRtnBankToFutureByFuture.argtypes = [c_void_p, c_void_p]
		self.h.SetOnErrRtnBankToFutureByFuture.restype = c_void_p
		self.evOnErrRtnBankToFutureByFuture = CFUNCTYPE(c_void_p, POINTER(CThostFtdcReqTransferField), POINTER(CThostFtdcRspInfoField))(self.__OnErrRtnBankToFutureByFuture)
		self.h.SetOnErrRtnBankToFutureByFuture(self.spi, self.evOnErrRtnBankToFutureByFuture)

		self.h.SetOnRtnRepealFromFutureToBankByFuture.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRtnRepealFromFutureToBankByFuture.restype = c_void_p
		self.evOnRtnRepealFromFutureToBankByFuture = CFUNCTYPE(c_void_p, POINTER(CThostFtdcRspRepealField))(self.__OnRtnRepealFromFutureToBankByFuture)
		self.h.SetOnRtnRepealFromFutureToBankByFuture(self.spi, self.evOnRtnRepealFromFutureToBankByFuture)

		self.h.SetOnErrRtnExecOrderAction.argtypes = [c_void_p, c_void_p]
		self.h.SetOnErrRtnExecOrderAction.restype = c_void_p
		self.evOnErrRtnExecOrderAction = CFUNCTYPE(c_void_p, POINTER(CThostFtdcExecOrderActionField), POINTER(CThostFtdcRspInfoField))(self.__OnErrRtnExecOrderAction)
		self.h.SetOnErrRtnExecOrderAction(self.spi, self.evOnErrRtnExecOrderAction)

		self.h.SetOnRspQryExchangeRate.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRspQryExchangeRate.restype = c_void_p
		self.evOnRspQryExchangeRate = CFUNCTYPE(c_void_p, POINTER(CThostFtdcExchangeRateField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryExchangeRate)
		self.h.SetOnRspQryExchangeRate(self.spi, self.evOnRspQryExchangeRate)

		self.h.SetOnRspQryCFMMCTradingAccountKey.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRspQryCFMMCTradingAccountKey.restype = c_void_p
		self.evOnRspQryCFMMCTradingAccountKey = CFUNCTYPE(c_void_p, POINTER(CThostFtdcCFMMCTradingAccountKeyField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryCFMMCTradingAccountKey)
		self.h.SetOnRspQryCFMMCTradingAccountKey(self.spi, self.evOnRspQryCFMMCTradingAccountKey)

		self.h.SetOnRspQryBrokerTradingParams.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRspQryBrokerTradingParams.restype = c_void_p
		self.evOnRspQryBrokerTradingParams = CFUNCTYPE(c_void_p, POINTER(CThostFtdcBrokerTradingParamsField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryBrokerTradingParams)
		self.h.SetOnRspQryBrokerTradingParams(self.spi, self.evOnRspQryBrokerTradingParams)

		self.h.SetOnRspOrderAction.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRspOrderAction.restype = c_void_p
		self.evOnRspOrderAction = CFUNCTYPE(c_void_p, POINTER(CThostFtdcInputOrderActionField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspOrderAction)
		self.h.SetOnRspOrderAction(self.spi, self.evOnRspOrderAction)

		self.h.SetOnRspQryExecFreeze.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRspQryExecFreeze.restype = c_void_p
		self.evOnRspQryExecFreeze = CFUNCTYPE(c_void_p, POINTER(CThostFtdcExecFreezeField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryExecFreeze)
		self.h.SetOnRspQryExecFreeze(self.spi, self.evOnRspQryExecFreeze)

		self.h.SetOnRspQryCombInstrumentGuard.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRspQryCombInstrumentGuard.restype = c_void_p
		self.evOnRspQryCombInstrumentGuard = CFUNCTYPE(c_void_p, POINTER(CThostFtdcCombInstrumentGuardField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryCombInstrumentGuard)
		self.h.SetOnRspQryCombInstrumentGuard(self.spi, self.evOnRspQryCombInstrumentGuard)

		self.h.SetOnRspQryMMOptionInstrCommRate.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRspQryMMOptionInstrCommRate.restype = c_void_p
		self.evOnRspQryMMOptionInstrCommRate = CFUNCTYPE(c_void_p, POINTER(CThostFtdcMMOptionInstrCommRateField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryMMOptionInstrCommRate)
		self.h.SetOnRspQryMMOptionInstrCommRate(self.spi, self.evOnRspQryMMOptionInstrCommRate)

		self.h.SetOnRspQryInvestorPositionDetail.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRspQryInvestorPositionDetail.restype = c_void_p
		self.evOnRspQryInvestorPositionDetail = CFUNCTYPE(c_void_p, POINTER(CThostFtdcInvestorPositionDetailField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryInvestorPositionDetail)
		self.h.SetOnRspQryInvestorPositionDetail(self.spi, self.evOnRspQryInvestorPositionDetail)

		self.h.SetOnRspUserLogout.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRspUserLogout.restype = c_void_p
		self.evOnRspUserLogout = CFUNCTYPE(c_void_p, POINTER(CThostFtdcUserLogoutField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspUserLogout)
		self.h.SetOnRspUserLogout(self.spi, self.evOnRspUserLogout)

		self.h.SetOnRspQryProduct.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRspQryProduct.restype = c_void_p
		self.evOnRspQryProduct = CFUNCTYPE(c_void_p, POINTER(CThostFtdcProductField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryProduct)
		self.h.SetOnRspQryProduct(self.spi, self.evOnRspQryProduct)

		self.h.SetOnRspQueryBankAccountMoneyByFuture.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRspQueryBankAccountMoneyByFuture.restype = c_void_p
		self.evOnRspQueryBankAccountMoneyByFuture = CFUNCTYPE(c_void_p, POINTER(CThostFtdcReqQueryAccountField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQueryBankAccountMoneyByFuture)
		self.h.SetOnRspQueryBankAccountMoneyByFuture(self.spi, self.evOnRspQueryBankAccountMoneyByFuture)

		self.h.SetOnRtnCombAction.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRtnCombAction.restype = c_void_p
		self.evOnRtnCombAction = CFUNCTYPE(c_void_p, POINTER(CThostFtdcCombActionField))(self.__OnRtnCombAction)
		self.h.SetOnRtnCombAction(self.spi, self.evOnRtnCombAction)

		self.h.SetOnErrRtnRepealBankToFutureByFutureManual.argtypes = [c_void_p, c_void_p]
		self.h.SetOnErrRtnRepealBankToFutureByFutureManual.restype = c_void_p
		self.evOnErrRtnRepealBankToFutureByFutureManual = CFUNCTYPE(c_void_p, POINTER(CThostFtdcReqRepealField), POINTER(CThostFtdcRspInfoField))(self.__OnErrRtnRepealBankToFutureByFutureManual)
		self.h.SetOnErrRtnRepealBankToFutureByFutureManual(self.spi, self.evOnErrRtnRepealBankToFutureByFutureManual)

		self.h.SetOnRspForQuoteInsert.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRspForQuoteInsert.restype = c_void_p
		self.evOnRspForQuoteInsert = CFUNCTYPE(c_void_p, POINTER(CThostFtdcInputForQuoteField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspForQuoteInsert)
		self.h.SetOnRspForQuoteInsert(self.spi, self.evOnRspForQuoteInsert)

		self.h.SetOnRspQryNotice.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRspQryNotice.restype = c_void_p
		self.evOnRspQryNotice = CFUNCTYPE(c_void_p, POINTER(CThostFtdcNoticeField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryNotice)
		self.h.SetOnRspQryNotice(self.spi, self.evOnRspQryNotice)

		self.h.SetOnRspQuoteInsert.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRspQuoteInsert.restype = c_void_p
		self.evOnRspQuoteInsert = CFUNCTYPE(c_void_p, POINTER(CThostFtdcInputQuoteField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQuoteInsert)
		self.h.SetOnRspQuoteInsert(self.spi, self.evOnRspQuoteInsert)

		self.h.SetOnRspExecOrderInsert.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRspExecOrderInsert.restype = c_void_p
		self.evOnRspExecOrderInsert = CFUNCTYPE(c_void_p, POINTER(CThostFtdcInputExecOrderField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspExecOrderInsert)
		self.h.SetOnRspExecOrderInsert(self.spi, self.evOnRspExecOrderInsert)

		self.h.SetOnRspQryExecOrder.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRspQryExecOrder.restype = c_void_p
		self.evOnRspQryExecOrder = CFUNCTYPE(c_void_p, POINTER(CThostFtdcExecOrderField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryExecOrder)
		self.h.SetOnRspQryExecOrder(self.spi, self.evOnRspQryExecOrder)

		self.h.SetOnRspRemoveParkedOrder.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRspRemoveParkedOrder.restype = c_void_p
		self.evOnRspRemoveParkedOrder = CFUNCTYPE(c_void_p, POINTER(CThostFtdcRemoveParkedOrderField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspRemoveParkedOrder)
		self.h.SetOnRspRemoveParkedOrder(self.spi, self.evOnRspRemoveParkedOrder)

		self.h.SetOnRspSettlementInfoConfirm.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRspSettlementInfoConfirm.restype = c_void_p
		self.evOnRspSettlementInfoConfirm = CFUNCTYPE(c_void_p, POINTER(CThostFtdcSettlementInfoConfirmField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspSettlementInfoConfirm)
		self.h.SetOnRspSettlementInfoConfirm(self.spi, self.evOnRspSettlementInfoConfirm)

		self.h.SetOnRspOrderInsert.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRspOrderInsert.restype = c_void_p
		self.evOnRspOrderInsert = CFUNCTYPE(c_void_p, POINTER(CThostFtdcInputOrderField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspOrderInsert)
		self.h.SetOnRspOrderInsert(self.spi, self.evOnRspOrderInsert)

		self.h.SetOnRtnFromFutureToBankByBank.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRtnFromFutureToBankByBank.restype = c_void_p
		self.evOnRtnFromFutureToBankByBank = CFUNCTYPE(c_void_p, POINTER(CThostFtdcRspTransferField))(self.__OnRtnFromFutureToBankByBank)
		self.h.SetOnRtnFromFutureToBankByBank(self.spi, self.evOnRtnFromFutureToBankByBank)

		self.h.SetOnRtnInstrumentStatus.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRtnInstrumentStatus.restype = c_void_p
		self.evOnRtnInstrumentStatus = CFUNCTYPE(c_void_p, POINTER(CThostFtdcInstrumentStatusField))(self.__OnRtnInstrumentStatus)
		self.h.SetOnRtnInstrumentStatus(self.spi, self.evOnRtnInstrumentStatus)

		self.h.SetOnRspQryTradingCode.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRspQryTradingCode.restype = c_void_p
		self.evOnRspQryTradingCode = CFUNCTYPE(c_void_p, POINTER(CThostFtdcTradingCodeField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryTradingCode)
		self.h.SetOnRspQryTradingCode(self.spi, self.evOnRspQryTradingCode)

		self.h.SetOnRspQryProductExchRate.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRspQryProductExchRate.restype = c_void_p
		self.evOnRspQryProductExchRate = CFUNCTYPE(c_void_p, POINTER(CThostFtdcProductExchRateField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryProductExchRate)
		self.h.SetOnRspQryProductExchRate(self.spi, self.evOnRspQryProductExchRate)

		self.h.SetOnRspQryETFOptionInstrCommRate.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRspQryETFOptionInstrCommRate.restype = c_void_p
		self.evOnRspQryETFOptionInstrCommRate = CFUNCTYPE(c_void_p, POINTER(CThostFtdcETFOptionInstrCommRateField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryETFOptionInstrCommRate)
		self.h.SetOnRspQryETFOptionInstrCommRate(self.spi, self.evOnRspQryETFOptionInstrCommRate)

		self.h.SetOnRspParkedOrderInsert.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRspParkedOrderInsert.restype = c_void_p
		self.evOnRspParkedOrderInsert = CFUNCTYPE(c_void_p, POINTER(CThostFtdcParkedOrderField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspParkedOrderInsert)
		self.h.SetOnRspParkedOrderInsert(self.spi, self.evOnRspParkedOrderInsert)

		self.h.SetOnRspQryOptionInstrTradeCost.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRspQryOptionInstrTradeCost.restype = c_void_p
		self.evOnRspQryOptionInstrTradeCost = CFUNCTYPE(c_void_p, POINTER(CThostFtdcOptionInstrTradeCostField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryOptionInstrTradeCost)
		self.h.SetOnRspQryOptionInstrTradeCost(self.spi, self.evOnRspQryOptionInstrTradeCost)

		self.h.SetOnErrRtnQuoteAction.argtypes = [c_void_p, c_void_p]
		self.h.SetOnErrRtnQuoteAction.restype = c_void_p
		self.evOnErrRtnQuoteAction = CFUNCTYPE(c_void_p, POINTER(CThostFtdcQuoteActionField), POINTER(CThostFtdcRspInfoField))(self.__OnErrRtnQuoteAction)
		self.h.SetOnErrRtnQuoteAction(self.spi, self.evOnErrRtnQuoteAction)

		self.h.SetOnErrRtnExecOrderInsert.argtypes = [c_void_p, c_void_p]
		self.h.SetOnErrRtnExecOrderInsert.restype = c_void_p
		self.evOnErrRtnExecOrderInsert = CFUNCTYPE(c_void_p, POINTER(CThostFtdcInputExecOrderField), POINTER(CThostFtdcRspInfoField))(self.__OnErrRtnExecOrderInsert)
		self.h.SetOnErrRtnExecOrderInsert(self.spi, self.evOnErrRtnExecOrderInsert)

		self.h.SetOnRtnRepealFromBankToFutureByFuture.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRtnRepealFromBankToFutureByFuture.restype = c_void_p
		self.evOnRtnRepealFromBankToFutureByFuture = CFUNCTYPE(c_void_p, POINTER(CThostFtdcRspRepealField))(self.__OnRtnRepealFromBankToFutureByFuture)
		self.h.SetOnRtnRepealFromBankToFutureByFuture(self.spi, self.evOnRtnRepealFromBankToFutureByFuture)

		self.h.SetOnRspQryInvestor.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRspQryInvestor.restype = c_void_p
		self.evOnRspQryInvestor = CFUNCTYPE(c_void_p, POINTER(CThostFtdcInvestorField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryInvestor)
		self.h.SetOnRspQryInvestor(self.spi, self.evOnRspQryInvestor)

		self.h.SetOnErrRtnLockInsert.argtypes = [c_void_p, c_void_p]
		self.h.SetOnErrRtnLockInsert.restype = c_void_p
		self.evOnErrRtnLockInsert = CFUNCTYPE(c_void_p, POINTER(CThostFtdcInputLockField), POINTER(CThostFtdcRspInfoField))(self.__OnErrRtnLockInsert)
		self.h.SetOnErrRtnLockInsert(self.spi, self.evOnErrRtnLockInsert)

		self.h.SetOnRspTradingAccountPasswordUpdate.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRspTradingAccountPasswordUpdate.restype = c_void_p
		self.evOnRspTradingAccountPasswordUpdate = CFUNCTYPE(c_void_p, POINTER(CThostFtdcTradingAccountPasswordUpdateField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspTradingAccountPasswordUpdate)
		self.h.SetOnRspTradingAccountPasswordUpdate(self.spi, self.evOnRspTradingAccountPasswordUpdate)

		self.h.SetOnRspUserPasswordUpdate.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRspUserPasswordUpdate.restype = c_void_p
		self.evOnRspUserPasswordUpdate = CFUNCTYPE(c_void_p, POINTER(CThostFtdcUserPasswordUpdateField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspUserPasswordUpdate)
		self.h.SetOnRspUserPasswordUpdate(self.spi, self.evOnRspUserPasswordUpdate)

		self.h.SetOnRtnFromBankToFutureByFuture.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRtnFromBankToFutureByFuture.restype = c_void_p
		self.evOnRtnFromBankToFutureByFuture = CFUNCTYPE(c_void_p, POINTER(CThostFtdcRspTransferField))(self.__OnRtnFromBankToFutureByFuture)
		self.h.SetOnRtnFromBankToFutureByFuture(self.spi, self.evOnRtnFromBankToFutureByFuture)

		self.h.SetOnRspQuoteAction.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRspQuoteAction.restype = c_void_p
		self.evOnRspQuoteAction = CFUNCTYPE(c_void_p, POINTER(CThostFtdcInputQuoteActionField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQuoteAction)
		self.h.SetOnRspQuoteAction(self.spi, self.evOnRspQuoteAction)

		self.h.SetOnRspQryContractBank.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRspQryContractBank.restype = c_void_p
		self.evOnRspQryContractBank = CFUNCTYPE(c_void_p, POINTER(CThostFtdcContractBankField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryContractBank)
		self.h.SetOnRspQryContractBank(self.spi, self.evOnRspQryContractBank)

		self.h.SetOnErrRtnOrderAction.argtypes = [c_void_p, c_void_p]
		self.h.SetOnErrRtnOrderAction.restype = c_void_p
		self.evOnErrRtnOrderAction = CFUNCTYPE(c_void_p, POINTER(CThostFtdcOrderActionField), POINTER(CThostFtdcRspInfoField))(self.__OnErrRtnOrderAction)
		self.h.SetOnErrRtnOrderAction(self.spi, self.evOnErrRtnOrderAction)

		self.h.SetOnRspQryInstrumentMarginRate.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRspQryInstrumentMarginRate.restype = c_void_p
		self.evOnRspQryInstrumentMarginRate = CFUNCTYPE(c_void_p, POINTER(CThostFtdcInstrumentMarginRateField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryInstrumentMarginRate)
		self.h.SetOnRspQryInstrumentMarginRate(self.spi, self.evOnRspQryInstrumentMarginRate)

		self.h.SetOnRspBatchOrderAction.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRspBatchOrderAction.restype = c_void_p
		self.evOnRspBatchOrderAction = CFUNCTYPE(c_void_p, POINTER(CThostFtdcInputBatchOrderActionField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspBatchOrderAction)
		self.h.SetOnRspBatchOrderAction(self.spi, self.evOnRspBatchOrderAction)

		self.h.SetOnRtnChangeAccountByBank.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRtnChangeAccountByBank.restype = c_void_p
		self.evOnRtnChangeAccountByBank = CFUNCTYPE(c_void_p, POINTER(CThostFtdcChangeAccountField))(self.__OnRtnChangeAccountByBank)
		self.h.SetOnRtnChangeAccountByBank(self.spi, self.evOnRtnChangeAccountByBank)

		self.h.SetOnErrRtnRepealFutureToBankByFutureManual.argtypes = [c_void_p, c_void_p]
		self.h.SetOnErrRtnRepealFutureToBankByFutureManual.restype = c_void_p
		self.evOnErrRtnRepealFutureToBankByFutureManual = CFUNCTYPE(c_void_p, POINTER(CThostFtdcReqRepealField), POINTER(CThostFtdcRspInfoField))(self.__OnErrRtnRepealFutureToBankByFutureManual)
		self.h.SetOnErrRtnRepealFutureToBankByFutureManual(self.spi, self.evOnErrRtnRepealFutureToBankByFutureManual)

		self.h.SetOnRspFromFutureToBankByFuture.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRspFromFutureToBankByFuture.restype = c_void_p
		self.evOnRspFromFutureToBankByFuture = CFUNCTYPE(c_void_p, POINTER(CThostFtdcReqTransferField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspFromFutureToBankByFuture)
		self.h.SetOnRspFromFutureToBankByFuture(self.spi, self.evOnRspFromFutureToBankByFuture)

		self.h.SetOnRtnBulletin.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRtnBulletin.restype = c_void_p
		self.evOnRtnBulletin = CFUNCTYPE(c_void_p, POINTER(CThostFtdcBulletinField))(self.__OnRtnBulletin)
		self.h.SetOnRtnBulletin(self.spi, self.evOnRtnBulletin)

		self.h.SetOnRtnRepealFromFutureToBankByBank.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRtnRepealFromFutureToBankByBank.restype = c_void_p
		self.evOnRtnRepealFromFutureToBankByBank = CFUNCTYPE(c_void_p, POINTER(CThostFtdcRspRepealField))(self.__OnRtnRepealFromFutureToBankByBank)
		self.h.SetOnRtnRepealFromFutureToBankByBank(self.spi, self.evOnRtnRepealFromFutureToBankByBank)

		self.h.SetOnRspQryTradingNotice.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRspQryTradingNotice.restype = c_void_p
		self.evOnRspQryTradingNotice = CFUNCTYPE(c_void_p, POINTER(CThostFtdcTradingNoticeField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryTradingNotice)
		self.h.SetOnRspQryTradingNotice(self.spi, self.evOnRspQryTradingNotice)

		self.h.SetOnRspQryLock.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRspQryLock.restype = c_void_p
		self.evOnRspQryLock = CFUNCTYPE(c_void_p, POINTER(CThostFtdcLockField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryLock)
		self.h.SetOnRspQryLock(self.spi, self.evOnRspQryLock)

		self.h.SetOnErrRtnCombActionInsert.argtypes = [c_void_p, c_void_p]
		self.h.SetOnErrRtnCombActionInsert.restype = c_void_p
		self.evOnErrRtnCombActionInsert = CFUNCTYPE(c_void_p, POINTER(CThostFtdcInputCombActionField), POINTER(CThostFtdcRspInfoField))(self.__OnErrRtnCombActionInsert)
		self.h.SetOnErrRtnCombActionInsert(self.spi, self.evOnErrRtnCombActionInsert)

		self.h.SetOnErrRtnFutureToBankByFuture.argtypes = [c_void_p, c_void_p]
		self.h.SetOnErrRtnFutureToBankByFuture.restype = c_void_p
		self.evOnErrRtnFutureToBankByFuture = CFUNCTYPE(c_void_p, POINTER(CThostFtdcReqTransferField), POINTER(CThostFtdcRspInfoField))(self.__OnErrRtnFutureToBankByFuture)
		self.h.SetOnErrRtnFutureToBankByFuture(self.spi, self.evOnErrRtnFutureToBankByFuture)

		self.h.SetOnRspQryTransferBank.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRspQryTransferBank.restype = c_void_p
		self.evOnRspQryTransferBank = CFUNCTYPE(c_void_p, POINTER(CThostFtdcTransferBankField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryTransferBank)
		self.h.SetOnRspQryTransferBank(self.spi, self.evOnRspQryTransferBank)

		self.h.SetOnRspQryParkedOrderAction.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRspQryParkedOrderAction.restype = c_void_p
		self.evOnRspQryParkedOrderAction = CFUNCTYPE(c_void_p, POINTER(CThostFtdcParkedOrderActionField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryParkedOrderAction)
		self.h.SetOnRspQryParkedOrderAction(self.spi, self.evOnRspQryParkedOrderAction)

		self.h.SetOnHeartBeatWarning.argtypes = [c_void_p, c_void_p]
		self.h.SetOnHeartBeatWarning.restype = c_void_p
		self.evOnHeartBeatWarning = CFUNCTYPE(c_void_p, c_int32)(self.__OnHeartBeatWarning)
		self.h.SetOnHeartBeatWarning(self.spi, self.evOnHeartBeatWarning)

	def __OnRspQryCombAction(self, pCombAction, pRspInfo, nRequestID, bIsLast):
		self.OnRspQryCombAction(POINTER(CThostFtdcCombActionField).from_param(pCombAction).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents, nRequestID, bIsLast)
	
	def __OnRtnRepealFromFutureToBankByFutureManual(self, pRspRepeal):
		self.OnRtnRepealFromFutureToBankByFutureManual(POINTER(CThostFtdcRspRepealField).from_param(pRspRepeal).contents)
	
	def __OnRtnTrade(self, pTrade):
		self.OnRtnTrade(POINTER(CThostFtdcTradeField).from_param(pTrade).contents)
	
	def __OnRspQryParkedOrder(self, pParkedOrder, pRspInfo, nRequestID, bIsLast):
		self.OnRspQryParkedOrder(POINTER(CThostFtdcParkedOrderField).from_param(pParkedOrder).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents, nRequestID, bIsLast)
	
	def __OnRtnForQuoteRsp(self, pForQuoteRsp):
		self.OnRtnForQuoteRsp(POINTER(CThostFtdcForQuoteRspField).from_param(pForQuoteRsp).contents)
	
	def __OnRtnLock(self, pLock):
		self.OnRtnLock(POINTER(CThostFtdcLockField).from_param(pLock).contents)
	
	def __OnRspError(self, pRspInfo, nRequestID, bIsLast):
		self.OnRspError(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents, nRequestID, bIsLast)
	
	def __OnRspQryTradingAccount(self, pTradingAccount, pRspInfo, nRequestID, bIsLast):
		self.OnRspQryTradingAccount(POINTER(CThostFtdcTradingAccountField).from_param(pTradingAccount).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents, nRequestID, bIsLast)
	
	def __OnRspQrySettlementInfoConfirm(self, pSettlementInfoConfirm, pRspInfo, nRequestID, bIsLast):
		self.OnRspQrySettlementInfoConfirm(POINTER(CThostFtdcSettlementInfoConfirmField).from_param(pSettlementInfoConfirm).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents, nRequestID, bIsLast)
	
	def __OnErrRtnForQuoteInsert(self, pInputForQuote, pRspInfo):
		self.OnErrRtnForQuoteInsert(POINTER(CThostFtdcInputForQuoteField).from_param(pInputForQuote).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents)
	
	def __OnFrontConnected(self):
		self.OnFrontConnected()
	
	def __OnRspQryMMInstrumentCommissionRate(self, pMMInstrumentCommissionRate, pRspInfo, nRequestID, bIsLast):
		self.OnRspQryMMInstrumentCommissionRate(POINTER(CThostFtdcMMInstrumentCommissionRateField).from_param(pMMInstrumentCommissionRate).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents, nRequestID, bIsLast)
	
	def __OnRspFromBankToFutureByFuture(self, pReqTransfer, pRspInfo, nRequestID, bIsLast):
		self.OnRspFromBankToFutureByFuture(POINTER(CThostFtdcReqTransferField).from_param(pReqTransfer).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents, nRequestID, bIsLast)
	
	def __OnRspQueryMaxOrderVolume(self, pQueryMaxOrderVolume, pRspInfo, nRequestID, bIsLast):
		self.OnRspQueryMaxOrderVolume(POINTER(CThostFtdcQueryMaxOrderVolumeField).from_param(pQueryMaxOrderVolume).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents, nRequestID, bIsLast)
	
	def __OnRspQryTrade(self, pTrade, pRspInfo, nRequestID, bIsLast):
		self.OnRspQryTrade(POINTER(CThostFtdcTradeField).from_param(pTrade).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents, nRequestID, bIsLast)
	
	def __OnRspQryDepthMarketData(self, pDepthMarketData, pRspInfo, nRequestID, bIsLast):
		self.OnRspQryDepthMarketData(POINTER(CThostFtdcDepthMarketDataField).from_param(pDepthMarketData).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents, nRequestID, bIsLast)
	
	def __OnRspRemoveParkedOrderAction(self, pRemoveParkedOrderAction, pRspInfo, nRequestID, bIsLast):
		self.OnRspRemoveParkedOrderAction(POINTER(CThostFtdcRemoveParkedOrderActionField).from_param(pRemoveParkedOrderAction).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents, nRequestID, bIsLast)
	
	def __OnRspQryOrder(self, pOrder, pRspInfo, nRequestID, bIsLast):
		self.OnRspQryOrder(POINTER(CThostFtdcOrderField).from_param(pOrder).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents, nRequestID, bIsLast)
	
	def __OnRtnFromFutureToBankByFuture(self, pRspTransfer):
		self.OnRtnFromFutureToBankByFuture(POINTER(CThostFtdcRspTransferField).from_param(pRspTransfer).contents)
	
	def __OnRtnErrorConditionalOrder(self, pErrorConditionalOrder):
		self.OnRtnErrorConditionalOrder(POINTER(CThostFtdcErrorConditionalOrderField).from_param(pErrorConditionalOrder).contents)
	
	def __OnRspQrySecAgentACIDMap(self, pSecAgentACIDMap, pRspInfo, nRequestID, bIsLast):
		self.OnRspQrySecAgentACIDMap(POINTER(CThostFtdcSecAgentACIDMapField).from_param(pSecAgentACIDMap).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents, nRequestID, bIsLast)
	
	def __OnRtnExecOrder(self, pExecOrder):
		self.OnRtnExecOrder(POINTER(CThostFtdcExecOrderField).from_param(pExecOrder).contents)
	
	def __OnRspLockInsert(self, pInputLock, pRspInfo, nRequestID, bIsLast):
		self.OnRspLockInsert(POINTER(CThostFtdcInputLockField).from_param(pInputLock).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents, nRequestID, bIsLast)
	
	def __OnRspQryInvestorProductGroupMargin(self, pInvestorProductGroupMargin, pRspInfo, nRequestID, bIsLast):
		self.OnRspQryInvestorProductGroupMargin(POINTER(CThostFtdcInvestorProductGroupMarginField).from_param(pInvestorProductGroupMargin).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents, nRequestID, bIsLast)
	
	def __OnRspQrySettlementInfo(self, pSettlementInfo, pRspInfo, nRequestID, bIsLast):
		self.OnRspQrySettlementInfo(POINTER(CThostFtdcSettlementInfoField).from_param(pSettlementInfo).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents, nRequestID, bIsLast)
	
	def __OnRtnQuote(self, pQuote):
		self.OnRtnQuote(POINTER(CThostFtdcQuoteField).from_param(pQuote).contents)
	
	def __OnErrRtnQuoteInsert(self, pInputQuote, pRspInfo):
		self.OnErrRtnQuoteInsert(POINTER(CThostFtdcInputQuoteField).from_param(pInputQuote).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents)
	
	def __OnErrRtnOrderInsert(self, pInputOrder, pRspInfo):
		self.OnErrRtnOrderInsert(POINTER(CThostFtdcInputOrderField).from_param(pInputOrder).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents)
	
	def __OnRtnQueryBankBalanceByFuture(self, pNotifyQueryAccount):
		self.OnRtnQueryBankBalanceByFuture(POINTER(CThostFtdcNotifyQueryAccountField).from_param(pNotifyQueryAccount).contents)
	
	def __OnErrRtnQueryBankBalanceByFuture(self, pReqQueryAccount, pRspInfo):
		self.OnErrRtnQueryBankBalanceByFuture(POINTER(CThostFtdcReqQueryAccountField).from_param(pReqQueryAccount).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents)
	
	def __OnRspExecOrderAction(self, pInputExecOrderAction, pRspInfo, nRequestID, bIsLast):
		self.OnRspExecOrderAction(POINTER(CThostFtdcInputExecOrderActionField).from_param(pInputExecOrderAction).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents, nRequestID, bIsLast)
	
	def __OnRspQryOptionInstrCommRate(self, pOptionInstrCommRate, pRspInfo, nRequestID, bIsLast):
		self.OnRspQryOptionInstrCommRate(POINTER(CThostFtdcOptionInstrCommRateField).from_param(pOptionInstrCommRate).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents, nRequestID, bIsLast)
	
	def __OnRspQueryCFMMCTradingAccountToken(self, pQueryCFMMCTradingAccountToken, pRspInfo, nRequestID, bIsLast):
		self.OnRspQueryCFMMCTradingAccountToken(POINTER(CThostFtdcQueryCFMMCTradingAccountTokenField).from_param(pQueryCFMMCTradingAccountToken).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents, nRequestID, bIsLast)
	
	def __OnRspQryAccountregister(self, pAccountregister, pRspInfo, nRequestID, bIsLast):
		self.OnRspQryAccountregister(POINTER(CThostFtdcAccountregisterField).from_param(pAccountregister).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents, nRequestID, bIsLast)
	
	def __OnRspQryBrokerTradingAlgos(self, pBrokerTradingAlgos, pRspInfo, nRequestID, bIsLast):
		self.OnRspQryBrokerTradingAlgos(POINTER(CThostFtdcBrokerTradingAlgosField).from_param(pBrokerTradingAlgos).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents, nRequestID, bIsLast)
	
	def __OnRtnOpenAccountByBank(self, pOpenAccount):
		self.OnRtnOpenAccountByBank(POINTER(CThostFtdcOpenAccountField).from_param(pOpenAccount).contents)
	
	def __OnFrontDisconnected(self, nReason):
		self.OnFrontDisconnected(nReason)
	
	def __OnRspQryLockPosition(self, pLockPosition, pRspInfo, nRequestID, bIsLast):
		self.OnRspQryLockPosition(POINTER(CThostFtdcLockPositionField).from_param(pLockPosition).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents, nRequestID, bIsLast)
	
	def __OnRspQryInvestorPosition(self, pInvestorPosition, pRspInfo, nRequestID, bIsLast):
		self.OnRspQryInvestorPosition(POINTER(CThostFtdcInvestorPositionField).from_param(pInvestorPosition).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents, nRequestID, bIsLast)
	
	def __OnRspQryExchange(self, pExchange, pRspInfo, nRequestID, bIsLast):
		self.OnRspQryExchange(POINTER(CThostFtdcExchangeField).from_param(pExchange).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents, nRequestID, bIsLast)
	
	def __OnRtnCFMMCTradingAccountToken(self, pCFMMCTradingAccountToken):
		self.OnRtnCFMMCTradingAccountToken(POINTER(CThostFtdcCFMMCTradingAccountTokenField).from_param(pCFMMCTradingAccountToken).contents)
	
	def __OnRspAuthenticate(self, pRspAuthenticateField, pRspInfo, nRequestID, bIsLast):
		self.OnRspAuthenticate(POINTER(CThostFtdcRspAuthenticateField).from_param(pRspAuthenticateField).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents, nRequestID, bIsLast)
	
	def __OnRtnRepealFromBankToFutureByBank(self, pRspRepeal):
		self.OnRtnRepealFromBankToFutureByBank(POINTER(CThostFtdcRspRepealField).from_param(pRspRepeal).contents)
	
	def __OnRspQryForQuote(self, pForQuote, pRspInfo, nRequestID, bIsLast):
		self.OnRspQryForQuote(POINTER(CThostFtdcForQuoteField).from_param(pForQuote).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents, nRequestID, bIsLast)
	
	def __OnErrRtnBatchOrderAction(self, pBatchOrderAction, pRspInfo):
		self.OnErrRtnBatchOrderAction(POINTER(CThostFtdcBatchOrderActionField).from_param(pBatchOrderAction).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents)
	
	def __OnRspQryProductGroup(self, pProductGroup, pRspInfo, nRequestID, bIsLast):
		self.OnRspQryProductGroup(POINTER(CThostFtdcProductGroupField).from_param(pProductGroup).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents, nRequestID, bIsLast)
	
	def __OnRtnRepealFromBankToFutureByFutureManual(self, pRspRepeal):
		self.OnRtnRepealFromBankToFutureByFutureManual(POINTER(CThostFtdcRspRepealField).from_param(pRspRepeal).contents)
	
	def __OnRspQryInstrument(self, pInstrument, pRspInfo, nRequestID, bIsLast):
		self.OnRspQryInstrument(POINTER(CThostFtdcInstrumentField).from_param(pInstrument).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents, nRequestID, bIsLast)
	
	def __OnRspQryExchangeMarginRate(self, pExchangeMarginRate, pRspInfo, nRequestID, bIsLast):
		self.OnRspQryExchangeMarginRate(POINTER(CThostFtdcExchangeMarginRateField).from_param(pExchangeMarginRate).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents, nRequestID, bIsLast)
	
	def __OnRspUserLogin(self, pRspUserLogin, pRspInfo, nRequestID, bIsLast):
		self.OnRspUserLogin(POINTER(CThostFtdcRspUserLoginField).from_param(pRspUserLogin).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents, nRequestID, bIsLast)
	
	def __OnRtnTradingNotice(self, pTradingNoticeInfo):
		self.OnRtnTradingNotice(POINTER(CThostFtdcTradingNoticeInfoField).from_param(pTradingNoticeInfo).contents)
	
	def __OnRspQryTransferSerial(self, pTransferSerial, pRspInfo, nRequestID, bIsLast):
		self.OnRspQryTransferSerial(POINTER(CThostFtdcTransferSerialField).from_param(pTransferSerial).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents, nRequestID, bIsLast)
	
	def __OnRspParkedOrderAction(self, pParkedOrderAction, pRspInfo, nRequestID, bIsLast):
		self.OnRspParkedOrderAction(POINTER(CThostFtdcParkedOrderActionField).from_param(pParkedOrderAction).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents, nRequestID, bIsLast)
	
	def __OnRtnFromBankToFutureByBank(self, pRspTransfer):
		self.OnRtnFromBankToFutureByBank(POINTER(CThostFtdcRspTransferField).from_param(pRspTransfer).contents)
	
	def __OnRspCombActionInsert(self, pInputCombAction, pRspInfo, nRequestID, bIsLast):
		self.OnRspCombActionInsert(POINTER(CThostFtdcInputCombActionField).from_param(pInputCombAction).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents, nRequestID, bIsLast)
	
	def __OnRtnOrder(self, pOrder):
		self.OnRtnOrder(POINTER(CThostFtdcOrderField).from_param(pOrder).contents)
	
	def __OnRtnCancelAccountByBank(self, pCancelAccount):
		self.OnRtnCancelAccountByBank(POINTER(CThostFtdcCancelAccountField).from_param(pCancelAccount).contents)
	
	def __OnRspQryExchangeMarginRateAdjust(self, pExchangeMarginRateAdjust, pRspInfo, nRequestID, bIsLast):
		self.OnRspQryExchangeMarginRateAdjust(POINTER(CThostFtdcExchangeMarginRateAdjustField).from_param(pExchangeMarginRateAdjust).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents, nRequestID, bIsLast)
	
	def __OnRspQryInstrumentOrderCommRate(self, pInstrumentOrderCommRate, pRspInfo, nRequestID, bIsLast):
		self.OnRspQryInstrumentOrderCommRate(POINTER(CThostFtdcInstrumentOrderCommRateField).from_param(pInstrumentOrderCommRate).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents, nRequestID, bIsLast)
	
	def __OnRspQryEWarrantOffset(self, pEWarrantOffset, pRspInfo, nRequestID, bIsLast):
		self.OnRspQryEWarrantOffset(POINTER(CThostFtdcEWarrantOffsetField).from_param(pEWarrantOffset).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents, nRequestID, bIsLast)
	
	def __OnRspQryInvestorLevel(self, pInvestorLevel, pRspInfo, nRequestID, bIsLast):
		self.OnRspQryInvestorLevel(POINTER(CThostFtdcInvestorLevelField).from_param(pInvestorLevel).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents, nRequestID, bIsLast)
	
	def __OnRspQryQuote(self, pQuote, pRspInfo, nRequestID, bIsLast):
		self.OnRspQryQuote(POINTER(CThostFtdcQuoteField).from_param(pQuote).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents, nRequestID, bIsLast)
	
	def __OnRspQryInvestorPositionCombineDetail(self, pInvestorPositionCombineDetail, pRspInfo, nRequestID, bIsLast):
		self.OnRspQryInvestorPositionCombineDetail(POINTER(CThostFtdcInvestorPositionCombineDetailField).from_param(pInvestorPositionCombineDetail).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents, nRequestID, bIsLast)
	
	def __OnRspQryInstrumentCommissionRate(self, pInstrumentCommissionRate, pRspInfo, nRequestID, bIsLast):
		self.OnRspQryInstrumentCommissionRate(POINTER(CThostFtdcInstrumentCommissionRateField).from_param(pInstrumentCommissionRate).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents, nRequestID, bIsLast)
	
	def __OnErrRtnBankToFutureByFuture(self, pReqTransfer, pRspInfo):
		self.OnErrRtnBankToFutureByFuture(POINTER(CThostFtdcReqTransferField).from_param(pReqTransfer).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents)
	
	def __OnRtnRepealFromFutureToBankByFuture(self, pRspRepeal):
		self.OnRtnRepealFromFutureToBankByFuture(POINTER(CThostFtdcRspRepealField).from_param(pRspRepeal).contents)
	
	def __OnErrRtnExecOrderAction(self, pExecOrderAction, pRspInfo):
		self.OnErrRtnExecOrderAction(POINTER(CThostFtdcExecOrderActionField).from_param(pExecOrderAction).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents)
	
	def __OnRspQryExchangeRate(self, pExchangeRate, pRspInfo, nRequestID, bIsLast):
		self.OnRspQryExchangeRate(POINTER(CThostFtdcExchangeRateField).from_param(pExchangeRate).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents, nRequestID, bIsLast)
	
	def __OnRspQryCFMMCTradingAccountKey(self, pCFMMCTradingAccountKey, pRspInfo, nRequestID, bIsLast):
		self.OnRspQryCFMMCTradingAccountKey(POINTER(CThostFtdcCFMMCTradingAccountKeyField).from_param(pCFMMCTradingAccountKey).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents, nRequestID, bIsLast)
	
	def __OnRspQryBrokerTradingParams(self, pBrokerTradingParams, pRspInfo, nRequestID, bIsLast):
		self.OnRspQryBrokerTradingParams(POINTER(CThostFtdcBrokerTradingParamsField).from_param(pBrokerTradingParams).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents, nRequestID, bIsLast)
	
	def __OnRspOrderAction(self, pInputOrderAction, pRspInfo, nRequestID, bIsLast):
		self.OnRspOrderAction(POINTER(CThostFtdcInputOrderActionField).from_param(pInputOrderAction).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents, nRequestID, bIsLast)
	
	def __OnRspQryExecFreeze(self, pExecFreeze, pRspInfo, nRequestID, bIsLast):
		self.OnRspQryExecFreeze(POINTER(CThostFtdcExecFreezeField).from_param(pExecFreeze).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents, nRequestID, bIsLast)
	
	def __OnRspQryCombInstrumentGuard(self, pCombInstrumentGuard, pRspInfo, nRequestID, bIsLast):
		self.OnRspQryCombInstrumentGuard(POINTER(CThostFtdcCombInstrumentGuardField).from_param(pCombInstrumentGuard).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents, nRequestID, bIsLast)
	
	def __OnRspQryMMOptionInstrCommRate(self, pMMOptionInstrCommRate, pRspInfo, nRequestID, bIsLast):
		self.OnRspQryMMOptionInstrCommRate(POINTER(CThostFtdcMMOptionInstrCommRateField).from_param(pMMOptionInstrCommRate).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents, nRequestID, bIsLast)
	
	def __OnRspQryInvestorPositionDetail(self, pInvestorPositionDetail, pRspInfo, nRequestID, bIsLast):
		self.OnRspQryInvestorPositionDetail(POINTER(CThostFtdcInvestorPositionDetailField).from_param(pInvestorPositionDetail).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents, nRequestID, bIsLast)
	
	def __OnRspUserLogout(self, pUserLogout, pRspInfo, nRequestID, bIsLast):
		self.OnRspUserLogout(POINTER(CThostFtdcUserLogoutField).from_param(pUserLogout).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents, nRequestID, bIsLast)
	
	def __OnRspQryProduct(self, pProduct, pRspInfo, nRequestID, bIsLast):
		self.OnRspQryProduct(POINTER(CThostFtdcProductField).from_param(pProduct).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents, nRequestID, bIsLast)
	
	def __OnRspQueryBankAccountMoneyByFuture(self, pReqQueryAccount, pRspInfo, nRequestID, bIsLast):
		self.OnRspQueryBankAccountMoneyByFuture(POINTER(CThostFtdcReqQueryAccountField).from_param(pReqQueryAccount).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents, nRequestID, bIsLast)
	
	def __OnRtnCombAction(self, pCombAction):
		self.OnRtnCombAction(POINTER(CThostFtdcCombActionField).from_param(pCombAction).contents)
	
	def __OnErrRtnRepealBankToFutureByFutureManual(self, pReqRepeal, pRspInfo):
		self.OnErrRtnRepealBankToFutureByFutureManual(POINTER(CThostFtdcReqRepealField).from_param(pReqRepeal).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents)
	
	def __OnRspForQuoteInsert(self, pInputForQuote, pRspInfo, nRequestID, bIsLast):
		self.OnRspForQuoteInsert(POINTER(CThostFtdcInputForQuoteField).from_param(pInputForQuote).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents, nRequestID, bIsLast)
	
	def __OnRspQryNotice(self, pNotice, pRspInfo, nRequestID, bIsLast):
		self.OnRspQryNotice(POINTER(CThostFtdcNoticeField).from_param(pNotice).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents, nRequestID, bIsLast)
	
	def __OnRspQuoteInsert(self, pInputQuote, pRspInfo, nRequestID, bIsLast):
		self.OnRspQuoteInsert(POINTER(CThostFtdcInputQuoteField).from_param(pInputQuote).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents, nRequestID, bIsLast)
	
	def __OnRspExecOrderInsert(self, pInputExecOrder, pRspInfo, nRequestID, bIsLast):
		self.OnRspExecOrderInsert(POINTER(CThostFtdcInputExecOrderField).from_param(pInputExecOrder).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents, nRequestID, bIsLast)
	
	def __OnRspQryExecOrder(self, pExecOrder, pRspInfo, nRequestID, bIsLast):
		self.OnRspQryExecOrder(POINTER(CThostFtdcExecOrderField).from_param(pExecOrder).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents, nRequestID, bIsLast)
	
	def __OnRspRemoveParkedOrder(self, pRemoveParkedOrder, pRspInfo, nRequestID, bIsLast):
		self.OnRspRemoveParkedOrder(POINTER(CThostFtdcRemoveParkedOrderField).from_param(pRemoveParkedOrder).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents, nRequestID, bIsLast)
	
	def __OnRspSettlementInfoConfirm(self, pSettlementInfoConfirm, pRspInfo, nRequestID, bIsLast):
		self.OnRspSettlementInfoConfirm(POINTER(CThostFtdcSettlementInfoConfirmField).from_param(pSettlementInfoConfirm).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents, nRequestID, bIsLast)
	
	def __OnRspOrderInsert(self, pInputOrder, pRspInfo, nRequestID, bIsLast):
		self.OnRspOrderInsert(POINTER(CThostFtdcInputOrderField).from_param(pInputOrder).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents, nRequestID, bIsLast)
	
	def __OnRtnFromFutureToBankByBank(self, pRspTransfer):
		self.OnRtnFromFutureToBankByBank(POINTER(CThostFtdcRspTransferField).from_param(pRspTransfer).contents)
	
	def __OnRtnInstrumentStatus(self, pInstrumentStatus):
		self.OnRtnInstrumentStatus(POINTER(CThostFtdcInstrumentStatusField).from_param(pInstrumentStatus).contents)
	
	def __OnRspQryTradingCode(self, pTradingCode, pRspInfo, nRequestID, bIsLast):
		self.OnRspQryTradingCode(POINTER(CThostFtdcTradingCodeField).from_param(pTradingCode).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents, nRequestID, bIsLast)
	
	def __OnRspQryProductExchRate(self, pProductExchRate, pRspInfo, nRequestID, bIsLast):
		self.OnRspQryProductExchRate(POINTER(CThostFtdcProductExchRateField).from_param(pProductExchRate).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents, nRequestID, bIsLast)
	
	def __OnRspQryETFOptionInstrCommRate(self, pETFOptionInstrCommRate, pRspInfo, nRequestID, bIsLast):
		self.OnRspQryETFOptionInstrCommRate(POINTER(CThostFtdcETFOptionInstrCommRateField).from_param(pETFOptionInstrCommRate).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents, nRequestID, bIsLast)
	
	def __OnRspParkedOrderInsert(self, pParkedOrder, pRspInfo, nRequestID, bIsLast):
		self.OnRspParkedOrderInsert(POINTER(CThostFtdcParkedOrderField).from_param(pParkedOrder).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents, nRequestID, bIsLast)
	
	def __OnRspQryOptionInstrTradeCost(self, pOptionInstrTradeCost, pRspInfo, nRequestID, bIsLast):
		self.OnRspQryOptionInstrTradeCost(POINTER(CThostFtdcOptionInstrTradeCostField).from_param(pOptionInstrTradeCost).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents, nRequestID, bIsLast)
	
	def __OnErrRtnQuoteAction(self, pQuoteAction, pRspInfo):
		self.OnErrRtnQuoteAction(POINTER(CThostFtdcQuoteActionField).from_param(pQuoteAction).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents)
	
	def __OnErrRtnExecOrderInsert(self, pInputExecOrder, pRspInfo):
		self.OnErrRtnExecOrderInsert(POINTER(CThostFtdcInputExecOrderField).from_param(pInputExecOrder).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents)
	
	def __OnRtnRepealFromBankToFutureByFuture(self, pRspRepeal):
		self.OnRtnRepealFromBankToFutureByFuture(POINTER(CThostFtdcRspRepealField).from_param(pRspRepeal).contents)
	
	def __OnRspQryInvestor(self, pInvestor, pRspInfo, nRequestID, bIsLast):
		self.OnRspQryInvestor(POINTER(CThostFtdcInvestorField).from_param(pInvestor).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents, nRequestID, bIsLast)
	
	def __OnErrRtnLockInsert(self, pInputLock, pRspInfo):
		self.OnErrRtnLockInsert(POINTER(CThostFtdcInputLockField).from_param(pInputLock).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents)
	
	def __OnRspTradingAccountPasswordUpdate(self, pTradingAccountPasswordUpdate, pRspInfo, nRequestID, bIsLast):
		self.OnRspTradingAccountPasswordUpdate(POINTER(CThostFtdcTradingAccountPasswordUpdateField).from_param(pTradingAccountPasswordUpdate).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents, nRequestID, bIsLast)
	
	def __OnRspUserPasswordUpdate(self, pUserPasswordUpdate, pRspInfo, nRequestID, bIsLast):
		self.OnRspUserPasswordUpdate(POINTER(CThostFtdcUserPasswordUpdateField).from_param(pUserPasswordUpdate).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents, nRequestID, bIsLast)
	
	def __OnRtnFromBankToFutureByFuture(self, pRspTransfer):
		self.OnRtnFromBankToFutureByFuture(POINTER(CThostFtdcRspTransferField).from_param(pRspTransfer).contents)
	
	def __OnRspQuoteAction(self, pInputQuoteAction, pRspInfo, nRequestID, bIsLast):
		self.OnRspQuoteAction(POINTER(CThostFtdcInputQuoteActionField).from_param(pInputQuoteAction).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents, nRequestID, bIsLast)
	
	def __OnRspQryContractBank(self, pContractBank, pRspInfo, nRequestID, bIsLast):
		self.OnRspQryContractBank(POINTER(CThostFtdcContractBankField).from_param(pContractBank).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents, nRequestID, bIsLast)
	
	def __OnErrRtnOrderAction(self, pOrderAction, pRspInfo):
		self.OnErrRtnOrderAction(POINTER(CThostFtdcOrderActionField).from_param(pOrderAction).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents)
	
	def __OnRspQryInstrumentMarginRate(self, pInstrumentMarginRate, pRspInfo, nRequestID, bIsLast):
		self.OnRspQryInstrumentMarginRate(POINTER(CThostFtdcInstrumentMarginRateField).from_param(pInstrumentMarginRate).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents, nRequestID, bIsLast)
	
	def __OnRspBatchOrderAction(self, pInputBatchOrderAction, pRspInfo, nRequestID, bIsLast):
		self.OnRspBatchOrderAction(POINTER(CThostFtdcInputBatchOrderActionField).from_param(pInputBatchOrderAction).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents, nRequestID, bIsLast)
	
	def __OnRtnChangeAccountByBank(self, pChangeAccount):
		self.OnRtnChangeAccountByBank(POINTER(CThostFtdcChangeAccountField).from_param(pChangeAccount).contents)
	
	def __OnErrRtnRepealFutureToBankByFutureManual(self, pReqRepeal, pRspInfo):
		self.OnErrRtnRepealFutureToBankByFutureManual(POINTER(CThostFtdcReqRepealField).from_param(pReqRepeal).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents)
	
	def __OnRspFromFutureToBankByFuture(self, pReqTransfer, pRspInfo, nRequestID, bIsLast):
		self.OnRspFromFutureToBankByFuture(POINTER(CThostFtdcReqTransferField).from_param(pReqTransfer).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents, nRequestID, bIsLast)
	
	def __OnRtnBulletin(self, pBulletin):
		self.OnRtnBulletin(POINTER(CThostFtdcBulletinField).from_param(pBulletin).contents)
	
	def __OnRtnRepealFromFutureToBankByBank(self, pRspRepeal):
		self.OnRtnRepealFromFutureToBankByBank(POINTER(CThostFtdcRspRepealField).from_param(pRspRepeal).contents)
	
	def __OnRspQryTradingNotice(self, pTradingNotice, pRspInfo, nRequestID, bIsLast):
		self.OnRspQryTradingNotice(POINTER(CThostFtdcTradingNoticeField).from_param(pTradingNotice).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents, nRequestID, bIsLast)
	
	def __OnRspQryLock(self, pLock, pRspInfo, nRequestID, bIsLast):
		self.OnRspQryLock(POINTER(CThostFtdcLockField).from_param(pLock).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents, nRequestID, bIsLast)
	
	def __OnErrRtnCombActionInsert(self, pInputCombAction, pRspInfo):
		self.OnErrRtnCombActionInsert(POINTER(CThostFtdcInputCombActionField).from_param(pInputCombAction).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents)
	
	def __OnErrRtnFutureToBankByFuture(self, pReqTransfer, pRspInfo):
		self.OnErrRtnFutureToBankByFuture(POINTER(CThostFtdcReqTransferField).from_param(pReqTransfer).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents)
	
	def __OnRspQryTransferBank(self, pTransferBank, pRspInfo, nRequestID, bIsLast):
		self.OnRspQryTransferBank(POINTER(CThostFtdcTransferBankField).from_param(pTransferBank).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents, nRequestID, bIsLast)
	
	def __OnRspQryParkedOrderAction(self, pParkedOrderAction, pRspInfo, nRequestID, bIsLast):
		self.OnRspQryParkedOrderAction(POINTER(CThostFtdcParkedOrderActionField).from_param(pParkedOrderAction).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents, nRequestID, bIsLast)
	
	def __OnHeartBeatWarning(self, nTimeLapse):
		self.OnHeartBeatWarning(nTimeLapse)
	
	def OnRspQryCombAction(self, pCombAction = CThostFtdcCombActionField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool):
			print('OnRspQryCombAction:, pCombAction = CThostFtdcCombActionField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool')
	
	def OnRtnRepealFromFutureToBankByFutureManual(self, pRspRepeal = CThostFtdcRspRepealField):
			print('OnRtnRepealFromFutureToBankByFutureManual:, pRspRepeal = CThostFtdcRspRepealField')
	
	def OnRtnTrade(self, pTrade = CThostFtdcTradeField):
			print('OnRtnTrade:, pTrade = CThostFtdcTradeField')
	
	def OnRspQryParkedOrder(self, pParkedOrder = CThostFtdcParkedOrderField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool):
			print('OnRspQryParkedOrder:, pParkedOrder = CThostFtdcParkedOrderField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool')
	
	def OnRtnForQuoteRsp(self, pForQuoteRsp = CThostFtdcForQuoteRspField):
			print('OnRtnForQuoteRsp:, pForQuoteRsp = CThostFtdcForQuoteRspField')
	
	def OnRtnLock(self, pLock = CThostFtdcLockField):
			print('OnRtnLock:, pLock = CThostFtdcLockField')
	
	def OnRspError(self, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool):
			print('OnRspError:, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool')
	
	def OnRspQryTradingAccount(self, pTradingAccount = CThostFtdcTradingAccountField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool):
			print('OnRspQryTradingAccount:, pTradingAccount = CThostFtdcTradingAccountField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool')
	
	def OnRspQrySettlementInfoConfirm(self, pSettlementInfoConfirm = CThostFtdcSettlementInfoConfirmField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool):
			print('OnRspQrySettlementInfoConfirm:, pSettlementInfoConfirm = CThostFtdcSettlementInfoConfirmField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool')
	
	def OnErrRtnForQuoteInsert(self, pInputForQuote = CThostFtdcInputForQuoteField, pRspInfo = CThostFtdcRspInfoField):
			print('OnErrRtnForQuoteInsert:, pInputForQuote = CThostFtdcInputForQuoteField, pRspInfo = CThostFtdcRspInfoField')
	
	def OnFrontConnected(self):
			print('OnFrontConnected:')
	
	def OnRspQryMMInstrumentCommissionRate(self, pMMInstrumentCommissionRate = CThostFtdcMMInstrumentCommissionRateField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool):
			print('OnRspQryMMInstrumentCommissionRate:, pMMInstrumentCommissionRate = CThostFtdcMMInstrumentCommissionRateField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool')
	
	def OnRspFromBankToFutureByFuture(self, pReqTransfer = CThostFtdcReqTransferField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool):
			print('OnRspFromBankToFutureByFuture:, pReqTransfer = CThostFtdcReqTransferField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool')
	
	def OnRspQueryMaxOrderVolume(self, pQueryMaxOrderVolume = CThostFtdcQueryMaxOrderVolumeField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool):
			print('OnRspQueryMaxOrderVolume:, pQueryMaxOrderVolume = CThostFtdcQueryMaxOrderVolumeField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool')
	
	def OnRspQryTrade(self, pTrade = CThostFtdcTradeField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool):
			print('OnRspQryTrade:, pTrade = CThostFtdcTradeField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool')
	
	def OnRspQryDepthMarketData(self, pDepthMarketData = CThostFtdcDepthMarketDataField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool):
			print('OnRspQryDepthMarketData:, pDepthMarketData = CThostFtdcDepthMarketDataField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool')
	
	def OnRspRemoveParkedOrderAction(self, pRemoveParkedOrderAction = CThostFtdcRemoveParkedOrderActionField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool):
			print('OnRspRemoveParkedOrderAction:, pRemoveParkedOrderAction = CThostFtdcRemoveParkedOrderActionField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool')
	
	def OnRspQryOrder(self, pOrder = CThostFtdcOrderField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool):
			print('OnRspQryOrder:, pOrder = CThostFtdcOrderField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool')
	
	def OnRtnFromFutureToBankByFuture(self, pRspTransfer = CThostFtdcRspTransferField):
			print('OnRtnFromFutureToBankByFuture:, pRspTransfer = CThostFtdcRspTransferField')
	
	def OnRtnErrorConditionalOrder(self, pErrorConditionalOrder = CThostFtdcErrorConditionalOrderField):
			print('OnRtnErrorConditionalOrder:, pErrorConditionalOrder = CThostFtdcErrorConditionalOrderField')
	
	def OnRspQrySecAgentACIDMap(self, pSecAgentACIDMap = CThostFtdcSecAgentACIDMapField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool):
			print('OnRspQrySecAgentACIDMap:, pSecAgentACIDMap = CThostFtdcSecAgentACIDMapField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool')
	
	def OnRtnExecOrder(self, pExecOrder = CThostFtdcExecOrderField):
			print('OnRtnExecOrder:, pExecOrder = CThostFtdcExecOrderField')
	
	def OnRspLockInsert(self, pInputLock = CThostFtdcInputLockField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool):
			print('OnRspLockInsert:, pInputLock = CThostFtdcInputLockField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool')
	
	def OnRspQryInvestorProductGroupMargin(self, pInvestorProductGroupMargin = CThostFtdcInvestorProductGroupMarginField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool):
			print('OnRspQryInvestorProductGroupMargin:, pInvestorProductGroupMargin = CThostFtdcInvestorProductGroupMarginField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool')
	
	def OnRspQrySettlementInfo(self, pSettlementInfo = CThostFtdcSettlementInfoField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool):
			print('OnRspQrySettlementInfo:, pSettlementInfo = CThostFtdcSettlementInfoField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool')
	
	def OnRtnQuote(self, pQuote = CThostFtdcQuoteField):
			print('OnRtnQuote:, pQuote = CThostFtdcQuoteField')
	
	def OnErrRtnQuoteInsert(self, pInputQuote = CThostFtdcInputQuoteField, pRspInfo = CThostFtdcRspInfoField):
			print('OnErrRtnQuoteInsert:, pInputQuote = CThostFtdcInputQuoteField, pRspInfo = CThostFtdcRspInfoField')
	
	def OnErrRtnOrderInsert(self, pInputOrder = CThostFtdcInputOrderField, pRspInfo = CThostFtdcRspInfoField):
			print('OnErrRtnOrderInsert:, pInputOrder = CThostFtdcInputOrderField, pRspInfo = CThostFtdcRspInfoField')
	
	def OnRtnQueryBankBalanceByFuture(self, pNotifyQueryAccount = CThostFtdcNotifyQueryAccountField):
			print('OnRtnQueryBankBalanceByFuture:, pNotifyQueryAccount = CThostFtdcNotifyQueryAccountField')
	
	def OnErrRtnQueryBankBalanceByFuture(self, pReqQueryAccount = CThostFtdcReqQueryAccountField, pRspInfo = CThostFtdcRspInfoField):
			print('OnErrRtnQueryBankBalanceByFuture:, pReqQueryAccount = CThostFtdcReqQueryAccountField, pRspInfo = CThostFtdcRspInfoField')
	
	def OnRspExecOrderAction(self, pInputExecOrderAction = CThostFtdcInputExecOrderActionField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool):
			print('OnRspExecOrderAction:, pInputExecOrderAction = CThostFtdcInputExecOrderActionField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool')
	
	def OnRspQryOptionInstrCommRate(self, pOptionInstrCommRate = CThostFtdcOptionInstrCommRateField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool):
			print('OnRspQryOptionInstrCommRate:, pOptionInstrCommRate = CThostFtdcOptionInstrCommRateField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool')
	
	def OnRspQueryCFMMCTradingAccountToken(self, pQueryCFMMCTradingAccountToken = CThostFtdcQueryCFMMCTradingAccountTokenField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool):
			print('OnRspQueryCFMMCTradingAccountToken:, pQueryCFMMCTradingAccountToken = CThostFtdcQueryCFMMCTradingAccountTokenField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool')
	
	def OnRspQryAccountregister(self, pAccountregister = CThostFtdcAccountregisterField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool):
			print('OnRspQryAccountregister:, pAccountregister = CThostFtdcAccountregisterField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool')
	
	def OnRspQryBrokerTradingAlgos(self, pBrokerTradingAlgos = CThostFtdcBrokerTradingAlgosField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool):
			print('OnRspQryBrokerTradingAlgos:, pBrokerTradingAlgos = CThostFtdcBrokerTradingAlgosField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool')
	
	def OnRtnOpenAccountByBank(self, pOpenAccount = CThostFtdcOpenAccountField):
			print('OnRtnOpenAccountByBank:, pOpenAccount = CThostFtdcOpenAccountField')
	
	def OnFrontDisconnected(self, nReason = int):
			print('OnFrontDisconnected:, nReason = int')
	
	def OnRspQryLockPosition(self, pLockPosition = CThostFtdcLockPositionField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool):
			print('OnRspQryLockPosition:, pLockPosition = CThostFtdcLockPositionField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool')
	
	def OnRspQryInvestorPosition(self, pInvestorPosition = CThostFtdcInvestorPositionField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool):
			print('OnRspQryInvestorPosition:, pInvestorPosition = CThostFtdcInvestorPositionField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool')
	
	def OnRspQryExchange(self, pExchange = CThostFtdcExchangeField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool):
			print('OnRspQryExchange:, pExchange = CThostFtdcExchangeField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool')
	
	def OnRtnCFMMCTradingAccountToken(self, pCFMMCTradingAccountToken = CThostFtdcCFMMCTradingAccountTokenField):
			print('OnRtnCFMMCTradingAccountToken:, pCFMMCTradingAccountToken = CThostFtdcCFMMCTradingAccountTokenField')
	
	def OnRspAuthenticate(self, pRspAuthenticateField = CThostFtdcRspAuthenticateField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool):
			print('OnRspAuthenticate:, pRspAuthenticateField = CThostFtdcRspAuthenticateField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool')
	
	def OnRtnRepealFromBankToFutureByBank(self, pRspRepeal = CThostFtdcRspRepealField):
			print('OnRtnRepealFromBankToFutureByBank:, pRspRepeal = CThostFtdcRspRepealField')
	
	def OnRspQryForQuote(self, pForQuote = CThostFtdcForQuoteField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool):
			print('OnRspQryForQuote:, pForQuote = CThostFtdcForQuoteField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool')
	
	def OnErrRtnBatchOrderAction(self, pBatchOrderAction = CThostFtdcBatchOrderActionField, pRspInfo = CThostFtdcRspInfoField):
			print('OnErrRtnBatchOrderAction:, pBatchOrderAction = CThostFtdcBatchOrderActionField, pRspInfo = CThostFtdcRspInfoField')
	
	def OnRspQryProductGroup(self, pProductGroup = CThostFtdcProductGroupField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool):
			print('OnRspQryProductGroup:, pProductGroup = CThostFtdcProductGroupField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool')
	
	def OnRtnRepealFromBankToFutureByFutureManual(self, pRspRepeal = CThostFtdcRspRepealField):
			print('OnRtnRepealFromBankToFutureByFutureManual:, pRspRepeal = CThostFtdcRspRepealField')
	
	def OnRspQryInstrument(self, pInstrument = CThostFtdcInstrumentField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool):
			print('OnRspQryInstrument:, pInstrument = CThostFtdcInstrumentField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool')
	
	def OnRspQryExchangeMarginRate(self, pExchangeMarginRate = CThostFtdcExchangeMarginRateField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool):
			print('OnRspQryExchangeMarginRate:, pExchangeMarginRate = CThostFtdcExchangeMarginRateField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool')
	
	def OnRspUserLogin(self, pRspUserLogin = CThostFtdcRspUserLoginField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool):
			print('OnRspUserLogin:, pRspUserLogin = CThostFtdcRspUserLoginField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool')
	
	def OnRtnTradingNotice(self, pTradingNoticeInfo = CThostFtdcTradingNoticeInfoField):
			print('OnRtnTradingNotice:, pTradingNoticeInfo = CThostFtdcTradingNoticeInfoField')
	
	def OnRspQryTransferSerial(self, pTransferSerial = CThostFtdcTransferSerialField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool):
			print('OnRspQryTransferSerial:, pTransferSerial = CThostFtdcTransferSerialField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool')
	
	def OnRspParkedOrderAction(self, pParkedOrderAction = CThostFtdcParkedOrderActionField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool):
			print('OnRspParkedOrderAction:, pParkedOrderAction = CThostFtdcParkedOrderActionField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool')
	
	def OnRtnFromBankToFutureByBank(self, pRspTransfer = CThostFtdcRspTransferField):
			print('OnRtnFromBankToFutureByBank:, pRspTransfer = CThostFtdcRspTransferField')
	
	def OnRspCombActionInsert(self, pInputCombAction = CThostFtdcInputCombActionField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool):
			print('OnRspCombActionInsert:, pInputCombAction = CThostFtdcInputCombActionField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool')
	
	def OnRtnOrder(self, pOrder = CThostFtdcOrderField):
			print('OnRtnOrder:, pOrder = CThostFtdcOrderField')
	
	def OnRtnCancelAccountByBank(self, pCancelAccount = CThostFtdcCancelAccountField):
			print('OnRtnCancelAccountByBank:, pCancelAccount = CThostFtdcCancelAccountField')
	
	def OnRspQryExchangeMarginRateAdjust(self, pExchangeMarginRateAdjust = CThostFtdcExchangeMarginRateAdjustField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool):
			print('OnRspQryExchangeMarginRateAdjust:, pExchangeMarginRateAdjust = CThostFtdcExchangeMarginRateAdjustField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool')
	
	def OnRspQryInstrumentOrderCommRate(self, pInstrumentOrderCommRate = CThostFtdcInstrumentOrderCommRateField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool):
			print('OnRspQryInstrumentOrderCommRate:, pInstrumentOrderCommRate = CThostFtdcInstrumentOrderCommRateField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool')
	
	def OnRspQryEWarrantOffset(self, pEWarrantOffset = CThostFtdcEWarrantOffsetField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool):
			print('OnRspQryEWarrantOffset:, pEWarrantOffset = CThostFtdcEWarrantOffsetField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool')
	
	def OnRspQryInvestorLevel(self, pInvestorLevel = CThostFtdcInvestorLevelField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool):
			print('OnRspQryInvestorLevel:, pInvestorLevel = CThostFtdcInvestorLevelField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool')
	
	def OnRspQryQuote(self, pQuote = CThostFtdcQuoteField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool):
			print('OnRspQryQuote:, pQuote = CThostFtdcQuoteField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool')
	
	def OnRspQryInvestorPositionCombineDetail(self, pInvestorPositionCombineDetail = CThostFtdcInvestorPositionCombineDetailField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool):
			print('OnRspQryInvestorPositionCombineDetail:, pInvestorPositionCombineDetail = CThostFtdcInvestorPositionCombineDetailField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool')
	
	def OnRspQryInstrumentCommissionRate(self, pInstrumentCommissionRate = CThostFtdcInstrumentCommissionRateField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool):
			print('OnRspQryInstrumentCommissionRate:, pInstrumentCommissionRate = CThostFtdcInstrumentCommissionRateField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool')
	
	def OnErrRtnBankToFutureByFuture(self, pReqTransfer = CThostFtdcReqTransferField, pRspInfo = CThostFtdcRspInfoField):
			print('OnErrRtnBankToFutureByFuture:, pReqTransfer = CThostFtdcReqTransferField, pRspInfo = CThostFtdcRspInfoField')
	
	def OnRtnRepealFromFutureToBankByFuture(self, pRspRepeal = CThostFtdcRspRepealField):
			print('OnRtnRepealFromFutureToBankByFuture:, pRspRepeal = CThostFtdcRspRepealField')
	
	def OnErrRtnExecOrderAction(self, pExecOrderAction = CThostFtdcExecOrderActionField, pRspInfo = CThostFtdcRspInfoField):
			print('OnErrRtnExecOrderAction:, pExecOrderAction = CThostFtdcExecOrderActionField, pRspInfo = CThostFtdcRspInfoField')
	
	def OnRspQryExchangeRate(self, pExchangeRate = CThostFtdcExchangeRateField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool):
			print('OnRspQryExchangeRate:, pExchangeRate = CThostFtdcExchangeRateField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool')
	
	def OnRspQryCFMMCTradingAccountKey(self, pCFMMCTradingAccountKey = CThostFtdcCFMMCTradingAccountKeyField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool):
			print('OnRspQryCFMMCTradingAccountKey:, pCFMMCTradingAccountKey = CThostFtdcCFMMCTradingAccountKeyField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool')
	
	def OnRspQryBrokerTradingParams(self, pBrokerTradingParams = CThostFtdcBrokerTradingParamsField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool):
			print('OnRspQryBrokerTradingParams:, pBrokerTradingParams = CThostFtdcBrokerTradingParamsField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool')
	
	def OnRspOrderAction(self, pInputOrderAction = CThostFtdcInputOrderActionField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool):
			print('OnRspOrderAction:, pInputOrderAction = CThostFtdcInputOrderActionField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool')
	
	def OnRspQryExecFreeze(self, pExecFreeze = CThostFtdcExecFreezeField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool):
			print('OnRspQryExecFreeze:, pExecFreeze = CThostFtdcExecFreezeField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool')
	
	def OnRspQryCombInstrumentGuard(self, pCombInstrumentGuard = CThostFtdcCombInstrumentGuardField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool):
			print('OnRspQryCombInstrumentGuard:, pCombInstrumentGuard = CThostFtdcCombInstrumentGuardField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool')
	
	def OnRspQryMMOptionInstrCommRate(self, pMMOptionInstrCommRate = CThostFtdcMMOptionInstrCommRateField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool):
			print('OnRspQryMMOptionInstrCommRate:, pMMOptionInstrCommRate = CThostFtdcMMOptionInstrCommRateField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool')
	
	def OnRspQryInvestorPositionDetail(self, pInvestorPositionDetail = CThostFtdcInvestorPositionDetailField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool):
			print('OnRspQryInvestorPositionDetail:, pInvestorPositionDetail = CThostFtdcInvestorPositionDetailField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool')
	
	def OnRspUserLogout(self, pUserLogout = CThostFtdcUserLogoutField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool):
			print('OnRspUserLogout:, pUserLogout = CThostFtdcUserLogoutField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool')
	
	def OnRspQryProduct(self, pProduct = CThostFtdcProductField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool):
			print('OnRspQryProduct:, pProduct = CThostFtdcProductField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool')
	
	def OnRspQueryBankAccountMoneyByFuture(self, pReqQueryAccount = CThostFtdcReqQueryAccountField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool):
			print('OnRspQueryBankAccountMoneyByFuture:, pReqQueryAccount = CThostFtdcReqQueryAccountField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool')
	
	def OnRtnCombAction(self, pCombAction = CThostFtdcCombActionField):
			print('OnRtnCombAction:, pCombAction = CThostFtdcCombActionField')
	
	def OnErrRtnRepealBankToFutureByFutureManual(self, pReqRepeal = CThostFtdcReqRepealField, pRspInfo = CThostFtdcRspInfoField):
			print('OnErrRtnRepealBankToFutureByFutureManual:, pReqRepeal = CThostFtdcReqRepealField, pRspInfo = CThostFtdcRspInfoField')
	
	def OnRspForQuoteInsert(self, pInputForQuote = CThostFtdcInputForQuoteField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool):
			print('OnRspForQuoteInsert:, pInputForQuote = CThostFtdcInputForQuoteField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool')
	
	def OnRspQryNotice(self, pNotice = CThostFtdcNoticeField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool):
			print('OnRspQryNotice:, pNotice = CThostFtdcNoticeField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool')
	
	def OnRspQuoteInsert(self, pInputQuote = CThostFtdcInputQuoteField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool):
			print('OnRspQuoteInsert:, pInputQuote = CThostFtdcInputQuoteField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool')
	
	def OnRspExecOrderInsert(self, pInputExecOrder = CThostFtdcInputExecOrderField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool):
			print('OnRspExecOrderInsert:, pInputExecOrder = CThostFtdcInputExecOrderField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool')
	
	def OnRspQryExecOrder(self, pExecOrder = CThostFtdcExecOrderField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool):
			print('OnRspQryExecOrder:, pExecOrder = CThostFtdcExecOrderField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool')
	
	def OnRspRemoveParkedOrder(self, pRemoveParkedOrder = CThostFtdcRemoveParkedOrderField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool):
			print('OnRspRemoveParkedOrder:, pRemoveParkedOrder = CThostFtdcRemoveParkedOrderField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool')
	
	def OnRspSettlementInfoConfirm(self, pSettlementInfoConfirm = CThostFtdcSettlementInfoConfirmField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool):
			print('OnRspSettlementInfoConfirm:, pSettlementInfoConfirm = CThostFtdcSettlementInfoConfirmField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool')
	
	def OnRspOrderInsert(self, pInputOrder = CThostFtdcInputOrderField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool):
			print('OnRspOrderInsert:, pInputOrder = CThostFtdcInputOrderField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool')
	
	def OnRtnFromFutureToBankByBank(self, pRspTransfer = CThostFtdcRspTransferField):
			print('OnRtnFromFutureToBankByBank:, pRspTransfer = CThostFtdcRspTransferField')
	
	def OnRtnInstrumentStatus(self, pInstrumentStatus = CThostFtdcInstrumentStatusField):
			print('OnRtnInstrumentStatus:, pInstrumentStatus = CThostFtdcInstrumentStatusField')
	
	def OnRspQryTradingCode(self, pTradingCode = CThostFtdcTradingCodeField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool):
			print('OnRspQryTradingCode:, pTradingCode = CThostFtdcTradingCodeField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool')
	
	def OnRspQryProductExchRate(self, pProductExchRate = CThostFtdcProductExchRateField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool):
			print('OnRspQryProductExchRate:, pProductExchRate = CThostFtdcProductExchRateField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool')
	
	def OnRspQryETFOptionInstrCommRate(self, pETFOptionInstrCommRate = CThostFtdcETFOptionInstrCommRateField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool):
			print('OnRspQryETFOptionInstrCommRate:, pETFOptionInstrCommRate = CThostFtdcETFOptionInstrCommRateField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool')
	
	def OnRspParkedOrderInsert(self, pParkedOrder = CThostFtdcParkedOrderField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool):
			print('OnRspParkedOrderInsert:, pParkedOrder = CThostFtdcParkedOrderField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool')
	
	def OnRspQryOptionInstrTradeCost(self, pOptionInstrTradeCost = CThostFtdcOptionInstrTradeCostField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool):
			print('OnRspQryOptionInstrTradeCost:, pOptionInstrTradeCost = CThostFtdcOptionInstrTradeCostField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool')
	
	def OnErrRtnQuoteAction(self, pQuoteAction = CThostFtdcQuoteActionField, pRspInfo = CThostFtdcRspInfoField):
			print('OnErrRtnQuoteAction:, pQuoteAction = CThostFtdcQuoteActionField, pRspInfo = CThostFtdcRspInfoField')
	
	def OnErrRtnExecOrderInsert(self, pInputExecOrder = CThostFtdcInputExecOrderField, pRspInfo = CThostFtdcRspInfoField):
			print('OnErrRtnExecOrderInsert:, pInputExecOrder = CThostFtdcInputExecOrderField, pRspInfo = CThostFtdcRspInfoField')
	
	def OnRtnRepealFromBankToFutureByFuture(self, pRspRepeal = CThostFtdcRspRepealField):
			print('OnRtnRepealFromBankToFutureByFuture:, pRspRepeal = CThostFtdcRspRepealField')
	
	def OnRspQryInvestor(self, pInvestor = CThostFtdcInvestorField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool):
			print('OnRspQryInvestor:, pInvestor = CThostFtdcInvestorField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool')
	
	def OnErrRtnLockInsert(self, pInputLock = CThostFtdcInputLockField, pRspInfo = CThostFtdcRspInfoField):
			print('OnErrRtnLockInsert:, pInputLock = CThostFtdcInputLockField, pRspInfo = CThostFtdcRspInfoField')
	
	def OnRspTradingAccountPasswordUpdate(self, pTradingAccountPasswordUpdate = CThostFtdcTradingAccountPasswordUpdateField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool):
			print('OnRspTradingAccountPasswordUpdate:, pTradingAccountPasswordUpdate = CThostFtdcTradingAccountPasswordUpdateField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool')
	
	def OnRspUserPasswordUpdate(self, pUserPasswordUpdate = CThostFtdcUserPasswordUpdateField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool):
			print('OnRspUserPasswordUpdate:, pUserPasswordUpdate = CThostFtdcUserPasswordUpdateField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool')
	
	def OnRtnFromBankToFutureByFuture(self, pRspTransfer = CThostFtdcRspTransferField):
			print('OnRtnFromBankToFutureByFuture:, pRspTransfer = CThostFtdcRspTransferField')
	
	def OnRspQuoteAction(self, pInputQuoteAction = CThostFtdcInputQuoteActionField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool):
			print('OnRspQuoteAction:, pInputQuoteAction = CThostFtdcInputQuoteActionField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool')
	
	def OnRspQryContractBank(self, pContractBank = CThostFtdcContractBankField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool):
			print('OnRspQryContractBank:, pContractBank = CThostFtdcContractBankField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool')
	
	def OnErrRtnOrderAction(self, pOrderAction = CThostFtdcOrderActionField, pRspInfo = CThostFtdcRspInfoField):
			print('OnErrRtnOrderAction:, pOrderAction = CThostFtdcOrderActionField, pRspInfo = CThostFtdcRspInfoField')
	
	def OnRspQryInstrumentMarginRate(self, pInstrumentMarginRate = CThostFtdcInstrumentMarginRateField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool):
			print('OnRspQryInstrumentMarginRate:, pInstrumentMarginRate = CThostFtdcInstrumentMarginRateField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool')
	
	def OnRspBatchOrderAction(self, pInputBatchOrderAction = CThostFtdcInputBatchOrderActionField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool):
			print('OnRspBatchOrderAction:, pInputBatchOrderAction = CThostFtdcInputBatchOrderActionField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool')
	
	def OnRtnChangeAccountByBank(self, pChangeAccount = CThostFtdcChangeAccountField):
			print('OnRtnChangeAccountByBank:, pChangeAccount = CThostFtdcChangeAccountField')
	
	def OnErrRtnRepealFutureToBankByFutureManual(self, pReqRepeal = CThostFtdcReqRepealField, pRspInfo = CThostFtdcRspInfoField):
			print('OnErrRtnRepealFutureToBankByFutureManual:, pReqRepeal = CThostFtdcReqRepealField, pRspInfo = CThostFtdcRspInfoField')
	
	def OnRspFromFutureToBankByFuture(self, pReqTransfer = CThostFtdcReqTransferField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool):
			print('OnRspFromFutureToBankByFuture:, pReqTransfer = CThostFtdcReqTransferField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool')
	
	def OnRtnBulletin(self, pBulletin = CThostFtdcBulletinField):
			print('OnRtnBulletin:, pBulletin = CThostFtdcBulletinField')
	
	def OnRtnRepealFromFutureToBankByBank(self, pRspRepeal = CThostFtdcRspRepealField):
			print('OnRtnRepealFromFutureToBankByBank:, pRspRepeal = CThostFtdcRspRepealField')
	
	def OnRspQryTradingNotice(self, pTradingNotice = CThostFtdcTradingNoticeField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool):
			print('OnRspQryTradingNotice:, pTradingNotice = CThostFtdcTradingNoticeField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool')
	
	def OnRspQryLock(self, pLock = CThostFtdcLockField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool):
			print('OnRspQryLock:, pLock = CThostFtdcLockField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool')
	
	def OnErrRtnCombActionInsert(self, pInputCombAction = CThostFtdcInputCombActionField, pRspInfo = CThostFtdcRspInfoField):
			print('OnErrRtnCombActionInsert:, pInputCombAction = CThostFtdcInputCombActionField, pRspInfo = CThostFtdcRspInfoField')
	
	def OnErrRtnFutureToBankByFuture(self, pReqTransfer = CThostFtdcReqTransferField, pRspInfo = CThostFtdcRspInfoField):
			print('OnErrRtnFutureToBankByFuture:, pReqTransfer = CThostFtdcReqTransferField, pRspInfo = CThostFtdcRspInfoField')
	
	def OnRspQryTransferBank(self, pTransferBank = CThostFtdcTransferBankField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool):
			print('OnRspQryTransferBank:, pTransferBank = CThostFtdcTransferBankField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool')
	
	def OnRspQryParkedOrderAction(self, pParkedOrderAction = CThostFtdcParkedOrderActionField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool):
			print('OnRspQryParkedOrderAction:, pParkedOrderAction = CThostFtdcParkedOrderActionField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool')
	
	def OnHeartBeatWarning(self, nTimeLapse = int):
			print('OnHeartBeatWarning:, nTimeLapse = int')
	
	def CreateApi(self):
		self.api = self.h.CreateApi()
		return self.api

	def CreateSpi(self):
		self.spi = self.h.CreateSpi()
		return self.spi

	def ReqQryOptionInstrTradeCost(self, BrokerID = '', InvestorID = '', InstrumentID = '', HedgeFlag = '', InputPrice = 0, UnderlyingPrice = 0, ExchangeID = ''):
		struc = CThostFtdcQryOptionInstrTradeCostField()
		struc.BrokerID = bytes(BrokerID, encoding='ascii')
		struc.InvestorID = bytes(InvestorID, encoding='ascii')
		struc.InstrumentID = bytes(InstrumentID, encoding='ascii')
		struc.HedgeFlag = bytes(HedgeFlag, encoding='ascii')
		struc.InputPrice = InputPrice
		struc.UnderlyingPrice = UnderlyingPrice
		struc.ExchangeID = bytes(ExchangeID, encoding='ascii')

		self.nRequestID += 1
		self.h.ReqQryOptionInstrTradeCost(self.api, byref(struc), self.nRequestID)
			
	def GetTradingDay(self):
		self.h.GetTradingDay(self.api)
			
	def Join(self):
		self.h.Join(self.api)
			
	def ReqQryExecOrder(self, BrokerID = '', InvestorID = '', InstrumentID = '', ExchangeID = '', ExecOrderSysID = '', InsertTimeStart = '', InsertTimeEnd = ''):
		struc = CThostFtdcQryExecOrderField()
		struc.BrokerID = bytes(BrokerID, encoding='ascii')
		struc.InvestorID = bytes(InvestorID, encoding='ascii')
		struc.InstrumentID = bytes(InstrumentID, encoding='ascii')
		struc.ExchangeID = bytes(ExchangeID, encoding='ascii')
		struc.ExecOrderSysID = bytes(ExecOrderSysID, encoding='ascii')
		struc.InsertTimeStart = bytes(InsertTimeStart, encoding='ascii')
		struc.InsertTimeEnd = bytes(InsertTimeEnd, encoding='ascii')

		self.nRequestID += 1
		self.h.ReqQryExecOrder(self.api, byref(struc), self.nRequestID)
			
	def ReqRemoveParkedOrderAction(self, BrokerID = '', InvestorID = '', ParkedOrderActionID = ''):
		struc = CThostFtdcRemoveParkedOrderActionField()
		struc.BrokerID = bytes(BrokerID, encoding='ascii')
		struc.InvestorID = bytes(InvestorID, encoding='ascii')
		struc.ParkedOrderActionID = bytes(ParkedOrderActionID, encoding='ascii')

		self.nRequestID += 1
		self.h.ReqRemoveParkedOrderAction(self.api, byref(struc), self.nRequestID)
			
	def ReqQryLock(self, BrokerID = '', InvestorID = '', InstrumentID = '', ExchangeID = '', LockSysID = '', InsertTimeStart = '', InsertTimeEnd = ''):
		struc = CThostFtdcQryLockField()
		struc.BrokerID = bytes(BrokerID, encoding='ascii')
		struc.InvestorID = bytes(InvestorID, encoding='ascii')
		struc.InstrumentID = bytes(InstrumentID, encoding='ascii')
		struc.ExchangeID = bytes(ExchangeID, encoding='ascii')
		struc.LockSysID = bytes(LockSysID, encoding='ascii')
		struc.InsertTimeStart = bytes(InsertTimeStart, encoding='ascii')
		struc.InsertTimeEnd = bytes(InsertTimeEnd, encoding='ascii')

		self.nRequestID += 1
		self.h.ReqQryLock(self.api, byref(struc), self.nRequestID)
			
	def ReqQryInvestorProductGroupMargin(self, BrokerID = '', InvestorID = '', ProductGroupID = '', HedgeFlag = ''):
		struc = CThostFtdcQryInvestorProductGroupMarginField()
		struc.BrokerID = bytes(BrokerID, encoding='ascii')
		struc.InvestorID = bytes(InvestorID, encoding='ascii')
		struc.ProductGroupID = bytes(ProductGroupID, encoding='ascii')
		struc.HedgeFlag = bytes(HedgeFlag, encoding='ascii')

		self.nRequestID += 1
		self.h.ReqQryInvestorProductGroupMargin(self.api, byref(struc), self.nRequestID)
			
	def ReqQrySecAgentACIDMap(self, BrokerID = '', UserID = '', AccountID = '', CurrencyID = ''):
		struc = CThostFtdcQrySecAgentACIDMapField()
		struc.BrokerID = bytes(BrokerID, encoding='ascii')
		struc.UserID = bytes(UserID, encoding='ascii')
		struc.AccountID = bytes(AccountID, encoding='ascii')
		struc.CurrencyID = bytes(CurrencyID, encoding='ascii')

		self.nRequestID += 1
		self.h.ReqQrySecAgentACIDMap(self.api, byref(struc), self.nRequestID)
			
	def ReqQryExchange(self, ExchangeID = ''):
		struc = CThostFtdcQryExchangeField()
		struc.ExchangeID = bytes(ExchangeID, encoding='ascii')

		self.nRequestID += 1
		self.h.ReqQryExchange(self.api, byref(struc), self.nRequestID)
			
	def ReqQryInstrument(self, InstrumentID = '', ExchangeID = '', ExchangeInstID = '', ProductID = ''):
		struc = CThostFtdcQryInstrumentField()
		struc.InstrumentID = bytes(InstrumentID, encoding='ascii')
		struc.ExchangeID = bytes(ExchangeID, encoding='ascii')
		struc.ExchangeInstID = bytes(ExchangeInstID, encoding='ascii')
		struc.ProductID = bytes(ProductID, encoding='ascii')

		self.nRequestID += 1
		self.h.ReqQryInstrument(self.api, byref(struc), self.nRequestID)
			
	def ReqTradingAccountPasswordUpdate(self, BrokerID = '', AccountID = '', OldPassword = '', NewPassword = '', CurrencyID = ''):
		struc = CThostFtdcTradingAccountPasswordUpdateField()
		struc.BrokerID = bytes(BrokerID, encoding='ascii')
		struc.AccountID = bytes(AccountID, encoding='ascii')
		struc.OldPassword = bytes(OldPassword, encoding='ascii')
		struc.NewPassword = bytes(NewPassword, encoding='ascii')
		struc.CurrencyID = bytes(CurrencyID, encoding='ascii')

		self.nRequestID += 1
		self.h.ReqTradingAccountPasswordUpdate(self.api, byref(struc), self.nRequestID)
			
	def ReqQryMMInstrumentCommissionRate(self, BrokerID = '', InvestorID = '', InstrumentID = '', ExchangeID = ''):
		struc = CThostFtdcQryMMInstrumentCommissionRateField()
		struc.BrokerID = bytes(BrokerID, encoding='ascii')
		struc.InvestorID = bytes(InvestorID, encoding='ascii')
		struc.InstrumentID = bytes(InstrumentID, encoding='ascii')
		struc.ExchangeID = bytes(ExchangeID, encoding='ascii')

		self.nRequestID += 1
		self.h.ReqQryMMInstrumentCommissionRate(self.api, byref(struc), self.nRequestID)
			
	def ReqQuoteInsert(self, BrokerID = '', InvestorID = '', InstrumentID = '', QuoteRef = '', UserID = '', AskPrice = 0, BidPrice = 0, AskVolume = 0, BidVolume = 0, RequestID = 0, BusinessUnit = '', AskOffsetFlag = '', BidOffsetFlag = '', AskHedgeFlag = '', BidHedgeFlag = '', AskOrderRef = '', BidOrderRef = '', ForQuoteSysID = '', ExchangeID = '', InvestUnitID = '', ClientID = '', IPAddress = '', MacAddress = ''):
		struc = CThostFtdcInputQuoteField()
		struc.BrokerID = bytes(BrokerID, encoding='ascii')
		struc.InvestorID = bytes(InvestorID, encoding='ascii')
		struc.InstrumentID = bytes(InstrumentID, encoding='ascii')
		struc.QuoteRef = bytes(QuoteRef, encoding='ascii')
		struc.UserID = bytes(UserID, encoding='ascii')
		struc.AskPrice = AskPrice
		struc.BidPrice = BidPrice
		struc.AskVolume = AskVolume
		struc.BidVolume = BidVolume
		struc.RequestID = RequestID
		struc.BusinessUnit = bytes(BusinessUnit, encoding='ascii')
		struc.AskOffsetFlag = bytes(AskOffsetFlag, encoding='ascii')
		struc.BidOffsetFlag = bytes(BidOffsetFlag, encoding='ascii')
		struc.AskHedgeFlag = bytes(AskHedgeFlag, encoding='ascii')
		struc.BidHedgeFlag = bytes(BidHedgeFlag, encoding='ascii')
		struc.AskOrderRef = bytes(AskOrderRef, encoding='ascii')
		struc.BidOrderRef = bytes(BidOrderRef, encoding='ascii')
		struc.ForQuoteSysID = bytes(ForQuoteSysID, encoding='ascii')
		struc.ExchangeID = bytes(ExchangeID, encoding='ascii')
		struc.InvestUnitID = bytes(InvestUnitID, encoding='ascii')
		struc.ClientID = bytes(ClientID, encoding='ascii')
		struc.IPAddress = bytes(IPAddress, encoding='ascii')
		struc.MacAddress = bytes(MacAddress, encoding='ascii')

		self.nRequestID += 1
		self.h.ReqQuoteInsert(self.api, byref(struc), self.nRequestID)
			
	def ReqQryTransferSerial(self, BrokerID = '', AccountID = '', BankID = '', CurrencyID = ''):
		struc = CThostFtdcQryTransferSerialField()
		struc.BrokerID = bytes(BrokerID, encoding='ascii')
		struc.AccountID = bytes(AccountID, encoding='ascii')
		struc.BankID = bytes(BankID, encoding='ascii')
		struc.CurrencyID = bytes(CurrencyID, encoding='ascii')

		self.nRequestID += 1
		self.h.ReqQryTransferSerial(self.api, byref(struc), self.nRequestID)
			
	def ReqQryProductExchRate(self, ProductID = ''):
		struc = CThostFtdcQryProductExchRateField()
		struc.ProductID = bytes(ProductID, encoding='ascii')

		self.nRequestID += 1
		self.h.ReqQryProductExchRate(self.api, byref(struc), self.nRequestID)
			
	def SubscribePrivateTopic(self, pInstrumentID):
		self.h.SubscribePrivateTopic.argtypes = [c_void_p , c_char_p*1, c_int32]
		self.h.SubscribePrivateTopic.restype = c_void_p
		self.h.SubscribePrivateTopic(self.api, (c_char_p*1)(bytes(pInstrumentID, encoding = 'ascii')), 1)

	def ReqQryInvestorLevel(self, BrokerID = '', InvestorID = '', ExchangeID = ''):
		struc = CThostFtdcQryInvestorLevelField()
		struc.BrokerID = bytes(BrokerID, encoding='ascii')
		struc.InvestorID = bytes(InvestorID, encoding='ascii')
		struc.ExchangeID = bytes(ExchangeID, encoding='ascii')

		self.nRequestID += 1
		self.h.ReqQryInvestorLevel(self.api, byref(struc), self.nRequestID)
			
	def ReqQryInvestor(self, BrokerID = '', InvestorID = ''):
		struc = CThostFtdcQryInvestorField()
		struc.BrokerID = bytes(BrokerID, encoding='ascii')
		struc.InvestorID = bytes(InvestorID, encoding='ascii')

		self.nRequestID += 1
		self.h.ReqQryInvestor(self.api, byref(struc), self.nRequestID)
			
	def ReqQryForQuote(self, BrokerID = '', InvestorID = '', InstrumentID = '', ExchangeID = '', InsertTimeStart = '', InsertTimeEnd = ''):
		struc = CThostFtdcQryForQuoteField()
		struc.BrokerID = bytes(BrokerID, encoding='ascii')
		struc.InvestorID = bytes(InvestorID, encoding='ascii')
		struc.InstrumentID = bytes(InstrumentID, encoding='ascii')
		struc.ExchangeID = bytes(ExchangeID, encoding='ascii')
		struc.InsertTimeStart = bytes(InsertTimeStart, encoding='ascii')
		struc.InsertTimeEnd = bytes(InsertTimeEnd, encoding='ascii')

		self.nRequestID += 1
		self.h.ReqQryForQuote(self.api, byref(struc), self.nRequestID)
			
	def ReqExecOrderInsert(self, BrokerID = '', InvestorID = '', InstrumentID = '', ExecOrderRef = '', UserID = '', Volume = 0, RequestID = 0, BusinessUnit = '', OffsetFlag = '', HedgeFlag = '', ActionType = '', PosiDirection = '', ReservePositionFlag = '', CloseFlag = '', ExchangeID = '', InvestUnitID = '', AccountID = '', CurrencyID = '', ClientID = '', IPAddress = '', MacAddress = ''):
		struc = CThostFtdcInputExecOrderField()
		struc.BrokerID = bytes(BrokerID, encoding='ascii')
		struc.InvestorID = bytes(InvestorID, encoding='ascii')
		struc.InstrumentID = bytes(InstrumentID, encoding='ascii')
		struc.ExecOrderRef = bytes(ExecOrderRef, encoding='ascii')
		struc.UserID = bytes(UserID, encoding='ascii')
		struc.Volume = Volume
		struc.RequestID = RequestID
		struc.BusinessUnit = bytes(BusinessUnit, encoding='ascii')
		struc.OffsetFlag = bytes(OffsetFlag, encoding='ascii')
		struc.HedgeFlag = bytes(HedgeFlag, encoding='ascii')
		struc.ActionType = bytes(ActionType, encoding='ascii')
		struc.PosiDirection = bytes(PosiDirection, encoding='ascii')
		struc.ReservePositionFlag = bytes(ReservePositionFlag, encoding='ascii')
		struc.CloseFlag = bytes(CloseFlag, encoding='ascii')
		struc.ExchangeID = bytes(ExchangeID, encoding='ascii')
		struc.InvestUnitID = bytes(InvestUnitID, encoding='ascii')
		struc.AccountID = bytes(AccountID, encoding='ascii')
		struc.CurrencyID = bytes(CurrencyID, encoding='ascii')
		struc.ClientID = bytes(ClientID, encoding='ascii')
		struc.IPAddress = bytes(IPAddress, encoding='ascii')
		struc.MacAddress = bytes(MacAddress, encoding='ascii')

		self.nRequestID += 1
		self.h.ReqExecOrderInsert(self.api, byref(struc), self.nRequestID)
			
	def ReqOrderInsert(self, BrokerID = '', InvestorID = '', InstrumentID = '', OrderRef = '', UserID = '', OrderPriceType = '', Direction = '', CombOffsetFlag = '', CombHedgeFlag = '', LimitPrice = 0, VolumeTotalOriginal = 0, TimeCondition = '', GTDDate = '', VolumeCondition = '', MinVolume = 0, ContingentCondition = '', StopPrice = 0, ForceCloseReason = '', IsAutoSuspend = 0, BusinessUnit = '', RequestID = 0, UserForceClose = 0, IsSwapOrder = 0, ExchangeID = '', InvestUnitID = '', AccountID = '', CurrencyID = '', ClientID = '', IPAddress = '', MacAddress = ''):
		struc = CThostFtdcInputOrderField()
		struc.BrokerID = bytes(BrokerID, encoding='ascii')
		struc.InvestorID = bytes(InvestorID, encoding='ascii')
		struc.InstrumentID = bytes(InstrumentID, encoding='ascii')
		struc.OrderRef = bytes(OrderRef, encoding='ascii')
		struc.UserID = bytes(UserID, encoding='ascii')
		struc.OrderPriceType = bytes(OrderPriceType, encoding='ascii')
		struc.Direction = bytes(Direction, encoding='ascii')
		struc.CombOffsetFlag = bytes(CombOffsetFlag, encoding='ascii')
		struc.CombHedgeFlag = bytes(CombHedgeFlag, encoding='ascii')
		struc.LimitPrice = LimitPrice
		struc.VolumeTotalOriginal = VolumeTotalOriginal
		struc.TimeCondition = bytes(TimeCondition, encoding='ascii')
		struc.GTDDate = bytes(GTDDate, encoding='ascii')
		struc.VolumeCondition = bytes(VolumeCondition, encoding='ascii')
		struc.MinVolume = MinVolume
		struc.ContingentCondition = bytes(ContingentCondition, encoding='ascii')
		struc.StopPrice = StopPrice
		struc.ForceCloseReason = bytes(ForceCloseReason, encoding='ascii')
		struc.IsAutoSuspend = IsAutoSuspend
		struc.BusinessUnit = bytes(BusinessUnit, encoding='ascii')
		struc.RequestID = RequestID
		struc.UserForceClose = UserForceClose
		struc.IsSwapOrder = IsSwapOrder
		struc.ExchangeID = bytes(ExchangeID, encoding='ascii')
		struc.InvestUnitID = bytes(InvestUnitID, encoding='ascii')
		struc.AccountID = bytes(AccountID, encoding='ascii')
		struc.CurrencyID = bytes(CurrencyID, encoding='ascii')
		struc.ClientID = bytes(ClientID, encoding='ascii')
		struc.IPAddress = bytes(IPAddress, encoding='ascii')
		struc.MacAddress = bytes(MacAddress, encoding='ascii')

		self.nRequestID += 1
		self.h.ReqOrderInsert(self.api, byref(struc), self.nRequestID)
			
	def ReqFromBankToFutureByFuture(self, TradeCode = '', BankID = '', BankBranchID = '', BrokerID = '', BrokerBranchID = '', TradeDate = '', TradeTime = '', BankSerial = '', TradingDay = '', PlateSerial = 0, LastFragment = '', SessionID = 0, CustomerName = '', IdCardType = '', IdentifiedCardNo = '', CustType = '', BankAccount = '', BankPassWord = '', AccountID = '', Password = '', InstallID = 0, FutureSerial = 0, UserID = '', VerifyCertNoFlag = '', CurrencyID = '', TradeAmount = 0, FutureFetchAmount = 0, FeePayFlag = '', CustFee = 0, BrokerFee = 0, Message = '', Digest = '', BankAccType = '', DeviceID = '', BankSecuAccType = '', BrokerIDByBank = '', BankSecuAcc = '', BankPwdFlag = '', SecuPwdFlag = '', OperNo = '', RequestID = 0, TID = 0, TransferStatus = ''):
		struc = CThostFtdcReqTransferField()
		struc.TradeCode = bytes(TradeCode, encoding='ascii')
		struc.BankID = bytes(BankID, encoding='ascii')
		struc.BankBranchID = bytes(BankBranchID, encoding='ascii')
		struc.BrokerID = bytes(BrokerID, encoding='ascii')
		struc.BrokerBranchID = bytes(BrokerBranchID, encoding='ascii')
		struc.TradeDate = bytes(TradeDate, encoding='ascii')
		struc.TradeTime = bytes(TradeTime, encoding='ascii')
		struc.BankSerial = bytes(BankSerial, encoding='ascii')
		struc.TradingDay = bytes(TradingDay, encoding='ascii')
		struc.PlateSerial = PlateSerial
		struc.LastFragment = bytes(LastFragment, encoding='ascii')
		struc.SessionID = SessionID
		struc.CustomerName = bytes(CustomerName, encoding='ascii')
		struc.IdCardType = bytes(IdCardType, encoding='ascii')
		struc.IdentifiedCardNo = bytes(IdentifiedCardNo, encoding='ascii')
		struc.CustType = bytes(CustType, encoding='ascii')
		struc.BankAccount = bytes(BankAccount, encoding='ascii')
		struc.BankPassWord = bytes(BankPassWord, encoding='ascii')
		struc.AccountID = bytes(AccountID, encoding='ascii')
		struc.Password = bytes(Password, encoding='ascii')
		struc.InstallID = InstallID
		struc.FutureSerial = FutureSerial
		struc.UserID = bytes(UserID, encoding='ascii')
		struc.VerifyCertNoFlag = bytes(VerifyCertNoFlag, encoding='ascii')
		struc.CurrencyID = bytes(CurrencyID, encoding='ascii')
		struc.TradeAmount = TradeAmount
		struc.FutureFetchAmount = FutureFetchAmount
		struc.FeePayFlag = bytes(FeePayFlag, encoding='ascii')
		struc.CustFee = CustFee
		struc.BrokerFee = BrokerFee
		struc.Message = bytes(Message, encoding='ascii')
		struc.Digest = bytes(Digest, encoding='ascii')
		struc.BankAccType = bytes(BankAccType, encoding='ascii')
		struc.DeviceID = bytes(DeviceID, encoding='ascii')
		struc.BankSecuAccType = bytes(BankSecuAccType, encoding='ascii')
		struc.BrokerIDByBank = bytes(BrokerIDByBank, encoding='ascii')
		struc.BankSecuAcc = bytes(BankSecuAcc, encoding='ascii')
		struc.BankPwdFlag = bytes(BankPwdFlag, encoding='ascii')
		struc.SecuPwdFlag = bytes(SecuPwdFlag, encoding='ascii')
		struc.OperNo = bytes(OperNo, encoding='ascii')
		struc.RequestID = RequestID
		struc.TID = TID
		struc.TransferStatus = bytes(TransferStatus, encoding='ascii')

		self.nRequestID += 1
		self.h.ReqFromBankToFutureByFuture(self.api, byref(struc), self.nRequestID)
			
	def ReqQryProduct(self, ProductID = '', ProductClass = '', ExchangeID = ''):
		struc = CThostFtdcQryProductField()
		struc.ProductID = bytes(ProductID, encoding='ascii')
		struc.ProductClass = bytes(ProductClass, encoding='ascii')
		struc.ExchangeID = bytes(ExchangeID, encoding='ascii')

		self.nRequestID += 1
		self.h.ReqQryProduct(self.api, byref(struc), self.nRequestID)
			
	def ReqQryInstrumentMarginRate(self, BrokerID = '', InvestorID = '', InstrumentID = '', HedgeFlag = ''):
		struc = CThostFtdcQryInstrumentMarginRateField()
		struc.BrokerID = bytes(BrokerID, encoding='ascii')
		struc.InvestorID = bytes(InvestorID, encoding='ascii')
		struc.InstrumentID = bytes(InstrumentID, encoding='ascii')
		struc.HedgeFlag = bytes(HedgeFlag, encoding='ascii')

		self.nRequestID += 1
		self.h.ReqQryInstrumentMarginRate(self.api, byref(struc), self.nRequestID)
			
	def ReqParkedOrderAction(self, BrokerID = '', InvestorID = '', OrderActionRef = 0, OrderRef = '', RequestID = 0, FrontID = 0, SessionID = 0, ExchangeID = '', OrderSysID = '', ActionFlag = '', LimitPrice = 0, VolumeChange = 0, UserID = '', InstrumentID = '', ParkedOrderActionID = '', UserType = '', Status = '', ErrorID = 0, ErrorMsg = '', InvestUnitID = '', IPAddress = '', MacAddress = ''):
		struc = CThostFtdcParkedOrderActionField()
		struc.BrokerID = bytes(BrokerID, encoding='ascii')
		struc.InvestorID = bytes(InvestorID, encoding='ascii')
		struc.OrderActionRef = OrderActionRef
		struc.OrderRef = bytes(OrderRef, encoding='ascii')
		struc.RequestID = RequestID
		struc.FrontID = FrontID
		struc.SessionID = SessionID
		struc.ExchangeID = bytes(ExchangeID, encoding='ascii')
		struc.OrderSysID = bytes(OrderSysID, encoding='ascii')
		struc.ActionFlag = bytes(ActionFlag, encoding='ascii')
		struc.LimitPrice = LimitPrice
		struc.VolumeChange = VolumeChange
		struc.UserID = bytes(UserID, encoding='ascii')
		struc.InstrumentID = bytes(InstrumentID, encoding='ascii')
		struc.ParkedOrderActionID = bytes(ParkedOrderActionID, encoding='ascii')
		struc.UserType = bytes(UserType, encoding='ascii')
		struc.Status = bytes(Status, encoding='ascii')
		struc.ErrorID = ErrorID
		struc.ErrorMsg = bytes(ErrorMsg, encoding='ascii')
		struc.InvestUnitID = bytes(InvestUnitID, encoding='ascii')
		struc.IPAddress = bytes(IPAddress, encoding='ascii')
		struc.MacAddress = bytes(MacAddress, encoding='ascii')

		self.nRequestID += 1
		self.h.ReqParkedOrderAction(self.api, byref(struc), self.nRequestID)
			
	def RegisterNameServer(self, pszNsAddress):
		self.h.RegisterNameServer(self.api, bytes(pszNsAddress, encoding='ascii'))
			
	def ReqUserLogout(self, BrokerID = '', UserID = ''):
		struc = CThostFtdcUserLogoutField()
		struc.BrokerID = bytes(BrokerID, encoding='ascii')
		struc.UserID = bytes(UserID, encoding='ascii')

		self.nRequestID += 1
		self.h.ReqUserLogout(self.api, byref(struc), self.nRequestID)
			
	def ReqOrderAction(self, BrokerID = '', InvestorID = '', OrderActionRef = 0, OrderRef = '', RequestID = 0, FrontID = 0, SessionID = 0, ExchangeID = '', OrderSysID = '', ActionFlag = '', LimitPrice = 0, VolumeChange = 0, UserID = '', InstrumentID = '', InvestUnitID = '', IPAddress = '', MacAddress = ''):
		struc = CThostFtdcInputOrderActionField()
		struc.BrokerID = bytes(BrokerID, encoding='ascii')
		struc.InvestorID = bytes(InvestorID, encoding='ascii')
		struc.OrderActionRef = OrderActionRef
		struc.OrderRef = bytes(OrderRef, encoding='ascii')
		struc.RequestID = RequestID
		struc.FrontID = FrontID
		struc.SessionID = SessionID
		struc.ExchangeID = bytes(ExchangeID, encoding='ascii')
		struc.OrderSysID = bytes(OrderSysID, encoding='ascii')
		struc.ActionFlag = bytes(ActionFlag, encoding='ascii')
		struc.LimitPrice = LimitPrice
		struc.VolumeChange = VolumeChange
		struc.UserID = bytes(UserID, encoding='ascii')
		struc.InstrumentID = bytes(InstrumentID, encoding='ascii')
		struc.InvestUnitID = bytes(InvestUnitID, encoding='ascii')
		struc.IPAddress = bytes(IPAddress, encoding='ascii')
		struc.MacAddress = bytes(MacAddress, encoding='ascii')

		self.nRequestID += 1
		self.h.ReqOrderAction(self.api, byref(struc), self.nRequestID)
			
	def ReqForQuoteInsert(self, BrokerID = '', InvestorID = '', InstrumentID = '', ForQuoteRef = '', UserID = '', ExchangeID = '', InvestUnitID = '', IPAddress = '', MacAddress = ''):
		struc = CThostFtdcInputForQuoteField()
		struc.BrokerID = bytes(BrokerID, encoding='ascii')
		struc.InvestorID = bytes(InvestorID, encoding='ascii')
		struc.InstrumentID = bytes(InstrumentID, encoding='ascii')
		struc.ForQuoteRef = bytes(ForQuoteRef, encoding='ascii')
		struc.UserID = bytes(UserID, encoding='ascii')
		struc.ExchangeID = bytes(ExchangeID, encoding='ascii')
		struc.InvestUnitID = bytes(InvestUnitID, encoding='ascii')
		struc.IPAddress = bytes(IPAddress, encoding='ascii')
		struc.MacAddress = bytes(MacAddress, encoding='ascii')

		self.nRequestID += 1
		self.h.ReqForQuoteInsert(self.api, byref(struc), self.nRequestID)
			
	def ReqQryInstrumentOrderCommRate(self, BrokerID = '', InvestorID = '', InstrumentID = '', ExchangeID = ''):
		struc = CThostFtdcQryInstrumentOrderCommRateField()
		struc.BrokerID = bytes(BrokerID, encoding='ascii')
		struc.InvestorID = bytes(InvestorID, encoding='ascii')
		struc.InstrumentID = bytes(InstrumentID, encoding='ascii')
		struc.ExchangeID = bytes(ExchangeID, encoding='ascii')

		self.nRequestID += 1
		self.h.ReqQryInstrumentOrderCommRate(self.api, byref(struc), self.nRequestID)
			
	def ReqQryInvestorPositionDetail(self, BrokerID = '', InvestorID = '', InstrumentID = '', ExchangeID = ''):
		struc = CThostFtdcQryInvestorPositionDetailField()
		struc.BrokerID = bytes(BrokerID, encoding='ascii')
		struc.InvestorID = bytes(InvestorID, encoding='ascii')
		struc.InstrumentID = bytes(InstrumentID, encoding='ascii')
		struc.ExchangeID = bytes(ExchangeID, encoding='ascii')

		self.nRequestID += 1
		self.h.ReqQryInvestorPositionDetail(self.api, byref(struc), self.nRequestID)
			
	def ReqQrySettlementInfoConfirm(self, BrokerID = '', InvestorID = ''):
		struc = CThostFtdcQrySettlementInfoConfirmField()
		struc.BrokerID = bytes(BrokerID, encoding='ascii')
		struc.InvestorID = bytes(InvestorID, encoding='ascii')

		self.nRequestID += 1
		self.h.ReqQrySettlementInfoConfirm(self.api, byref(struc), self.nRequestID)
			
	def ReqUserPasswordUpdate(self, BrokerID = '', UserID = '', OldPassword = '', NewPassword = ''):
		struc = CThostFtdcUserPasswordUpdateField()
		struc.BrokerID = bytes(BrokerID, encoding='ascii')
		struc.UserID = bytes(UserID, encoding='ascii')
		struc.OldPassword = bytes(OldPassword, encoding='ascii')
		struc.NewPassword = bytes(NewPassword, encoding='ascii')

		self.nRequestID += 1
		self.h.ReqUserPasswordUpdate(self.api, byref(struc), self.nRequestID)
			
	def ReqAuthenticate(self, BrokerID = '', UserID = '', UserProductInfo = '', AuthCode = ''):
		struc = CThostFtdcReqAuthenticateField()
		struc.BrokerID = bytes(BrokerID, encoding='ascii')
		struc.UserID = bytes(UserID, encoding='ascii')
		struc.UserProductInfo = bytes(UserProductInfo, encoding='ascii')
		struc.AuthCode = bytes(AuthCode, encoding='ascii')

		self.nRequestID += 1
		self.h.ReqAuthenticate(self.api, byref(struc), self.nRequestID)
			
	def ReqQryDepthMarketData(self, InstrumentID = '', ExchangeID = ''):
		struc = CThostFtdcQryDepthMarketDataField()
		struc.InstrumentID = bytes(InstrumentID, encoding='ascii')
		struc.ExchangeID = bytes(ExchangeID, encoding='ascii')

		self.nRequestID += 1
		self.h.ReqQryDepthMarketData(self.api, byref(struc), self.nRequestID)
			
	def ReqQryParkedOrder(self, BrokerID = '', InvestorID = '', InstrumentID = '', ExchangeID = ''):
		struc = CThostFtdcQryParkedOrderField()
		struc.BrokerID = bytes(BrokerID, encoding='ascii')
		struc.InvestorID = bytes(InvestorID, encoding='ascii')
		struc.InstrumentID = bytes(InstrumentID, encoding='ascii')
		struc.ExchangeID = bytes(ExchangeID, encoding='ascii')

		self.nRequestID += 1
		self.h.ReqQryParkedOrder(self.api, byref(struc), self.nRequestID)
			
	def ReqSettlementInfoConfirm(self, BrokerID = '', InvestorID = '', ConfirmDate = '', ConfirmTime = ''):
		struc = CThostFtdcSettlementInfoConfirmField()
		struc.BrokerID = bytes(BrokerID, encoding='ascii')
		struc.InvestorID = bytes(InvestorID, encoding='ascii')
		struc.ConfirmDate = bytes(ConfirmDate, encoding='ascii')
		struc.ConfirmTime = bytes(ConfirmTime, encoding='ascii')

		self.nRequestID += 1
		self.h.ReqSettlementInfoConfirm(self.api, byref(struc), self.nRequestID)
			
	def ReqQryExchangeMarginRate(self, BrokerID = '', InstrumentID = '', HedgeFlag = ''):
		struc = CThostFtdcQryExchangeMarginRateField()
		struc.BrokerID = bytes(BrokerID, encoding='ascii')
		struc.InstrumentID = bytes(InstrumentID, encoding='ascii')
		struc.HedgeFlag = bytes(HedgeFlag, encoding='ascii')

		self.nRequestID += 1
		self.h.ReqQryExchangeMarginRate(self.api, byref(struc), self.nRequestID)
			
	def ReqQryTradingNotice(self, BrokerID = '', InvestorID = ''):
		struc = CThostFtdcQryTradingNoticeField()
		struc.BrokerID = bytes(BrokerID, encoding='ascii')
		struc.InvestorID = bytes(InvestorID, encoding='ascii')

		self.nRequestID += 1
		self.h.ReqQryTradingNotice(self.api, byref(struc), self.nRequestID)
			
	def ReqQryCombInstrumentGuard(self, BrokerID = '', InstrumentID = ''):
		struc = CThostFtdcQryCombInstrumentGuardField()
		struc.BrokerID = bytes(BrokerID, encoding='ascii')
		struc.InstrumentID = bytes(InstrumentID, encoding='ascii')

		self.nRequestID += 1
		self.h.ReqQryCombInstrumentGuard(self.api, byref(struc), self.nRequestID)
			
	def ReqFromFutureToBankByFuture(self, TradeCode = '', BankID = '', BankBranchID = '', BrokerID = '', BrokerBranchID = '', TradeDate = '', TradeTime = '', BankSerial = '', TradingDay = '', PlateSerial = 0, LastFragment = '', SessionID = 0, CustomerName = '', IdCardType = '', IdentifiedCardNo = '', CustType = '', BankAccount = '', BankPassWord = '', AccountID = '', Password = '', InstallID = 0, FutureSerial = 0, UserID = '', VerifyCertNoFlag = '', CurrencyID = '', TradeAmount = 0, FutureFetchAmount = 0, FeePayFlag = '', CustFee = 0, BrokerFee = 0, Message = '', Digest = '', BankAccType = '', DeviceID = '', BankSecuAccType = '', BrokerIDByBank = '', BankSecuAcc = '', BankPwdFlag = '', SecuPwdFlag = '', OperNo = '', RequestID = 0, TID = 0, TransferStatus = ''):
		struc = CThostFtdcReqTransferField()
		struc.TradeCode = bytes(TradeCode, encoding='ascii')
		struc.BankID = bytes(BankID, encoding='ascii')
		struc.BankBranchID = bytes(BankBranchID, encoding='ascii')
		struc.BrokerID = bytes(BrokerID, encoding='ascii')
		struc.BrokerBranchID = bytes(BrokerBranchID, encoding='ascii')
		struc.TradeDate = bytes(TradeDate, encoding='ascii')
		struc.TradeTime = bytes(TradeTime, encoding='ascii')
		struc.BankSerial = bytes(BankSerial, encoding='ascii')
		struc.TradingDay = bytes(TradingDay, encoding='ascii')
		struc.PlateSerial = PlateSerial
		struc.LastFragment = bytes(LastFragment, encoding='ascii')
		struc.SessionID = SessionID
		struc.CustomerName = bytes(CustomerName, encoding='ascii')
		struc.IdCardType = bytes(IdCardType, encoding='ascii')
		struc.IdentifiedCardNo = bytes(IdentifiedCardNo, encoding='ascii')
		struc.CustType = bytes(CustType, encoding='ascii')
		struc.BankAccount = bytes(BankAccount, encoding='ascii')
		struc.BankPassWord = bytes(BankPassWord, encoding='ascii')
		struc.AccountID = bytes(AccountID, encoding='ascii')
		struc.Password = bytes(Password, encoding='ascii')
		struc.InstallID = InstallID
		struc.FutureSerial = FutureSerial
		struc.UserID = bytes(UserID, encoding='ascii')
		struc.VerifyCertNoFlag = bytes(VerifyCertNoFlag, encoding='ascii')
		struc.CurrencyID = bytes(CurrencyID, encoding='ascii')
		struc.TradeAmount = TradeAmount
		struc.FutureFetchAmount = FutureFetchAmount
		struc.FeePayFlag = bytes(FeePayFlag, encoding='ascii')
		struc.CustFee = CustFee
		struc.BrokerFee = BrokerFee
		struc.Message = bytes(Message, encoding='ascii')
		struc.Digest = bytes(Digest, encoding='ascii')
		struc.BankAccType = bytes(BankAccType, encoding='ascii')
		struc.DeviceID = bytes(DeviceID, encoding='ascii')
		struc.BankSecuAccType = bytes(BankSecuAccType, encoding='ascii')
		struc.BrokerIDByBank = bytes(BrokerIDByBank, encoding='ascii')
		struc.BankSecuAcc = bytes(BankSecuAcc, encoding='ascii')
		struc.BankPwdFlag = bytes(BankPwdFlag, encoding='ascii')
		struc.SecuPwdFlag = bytes(SecuPwdFlag, encoding='ascii')
		struc.OperNo = bytes(OperNo, encoding='ascii')
		struc.RequestID = RequestID
		struc.TID = TID
		struc.TransferStatus = bytes(TransferStatus, encoding='ascii')

		self.nRequestID += 1
		self.h.ReqFromFutureToBankByFuture(self.api, byref(struc), self.nRequestID)
			
	def ReqQueryCFMMCTradingAccountToken(self, BrokerID = '', InvestorID = ''):
		struc = CThostFtdcQueryCFMMCTradingAccountTokenField()
		struc.BrokerID = bytes(BrokerID, encoding='ascii')
		struc.InvestorID = bytes(InvestorID, encoding='ascii')

		self.nRequestID += 1
		self.h.ReqQueryCFMMCTradingAccountToken(self.api, byref(struc), self.nRequestID)
			
	def SubscribePublicTopic(self, pInstrumentID):
		self.h.SubscribePublicTopic.argtypes = [c_void_p , c_char_p*1, c_int32]
		self.h.SubscribePublicTopic.restype = c_void_p
		self.h.SubscribePublicTopic(self.api, (c_char_p*1)(bytes(pInstrumentID, encoding = 'ascii')), 1)

	def ReqQryEWarrantOffset(self, BrokerID = '', InvestorID = '', ExchangeID = '', InstrumentID = ''):
		struc = CThostFtdcQryEWarrantOffsetField()
		struc.BrokerID = bytes(BrokerID, encoding='ascii')
		struc.InvestorID = bytes(InvestorID, encoding='ascii')
		struc.ExchangeID = bytes(ExchangeID, encoding='ascii')
		struc.InstrumentID = bytes(InstrumentID, encoding='ascii')

		self.nRequestID += 1
		self.h.ReqQryEWarrantOffset(self.api, byref(struc), self.nRequestID)
			
	def ReqQryMMOptionInstrCommRate(self, BrokerID = '', InvestorID = '', InstrumentID = '', ExchangeID = ''):
		struc = CThostFtdcQryMMOptionInstrCommRateField()
		struc.BrokerID = bytes(BrokerID, encoding='ascii')
		struc.InvestorID = bytes(InvestorID, encoding='ascii')
		struc.InstrumentID = bytes(InstrumentID, encoding='ascii')
		struc.ExchangeID = bytes(ExchangeID, encoding='ascii')

		self.nRequestID += 1
		self.h.ReqQryMMOptionInstrCommRate(self.api, byref(struc), self.nRequestID)
			
	def ReqQryInvestorPosition(self, BrokerID = '', InvestorID = '', InstrumentID = '', ExchangeID = ''):
		struc = CThostFtdcQryInvestorPositionField()
		struc.BrokerID = bytes(BrokerID, encoding='ascii')
		struc.InvestorID = bytes(InvestorID, encoding='ascii')
		struc.InstrumentID = bytes(InstrumentID, encoding='ascii')
		struc.ExchangeID = bytes(ExchangeID, encoding='ascii')

		self.nRequestID += 1
		self.h.ReqQryInvestorPosition(self.api, byref(struc), self.nRequestID)
			
	def ReqQryBrokerTradingParams(self, BrokerID = '', InvestorID = '', CurrencyID = ''):
		struc = CThostFtdcQryBrokerTradingParamsField()
		struc.BrokerID = bytes(BrokerID, encoding='ascii')
		struc.InvestorID = bytes(InvestorID, encoding='ascii')
		struc.CurrencyID = bytes(CurrencyID, encoding='ascii')

		self.nRequestID += 1
		self.h.ReqQryBrokerTradingParams(self.api, byref(struc), self.nRequestID)
			
	def ReqQryContractBank(self, BrokerID = '', BankID = '', BankBrchID = ''):
		struc = CThostFtdcQryContractBankField()
		struc.BrokerID = bytes(BrokerID, encoding='ascii')
		struc.BankID = bytes(BankID, encoding='ascii')
		struc.BankBrchID = bytes(BankBrchID, encoding='ascii')

		self.nRequestID += 1
		self.h.ReqQryContractBank(self.api, byref(struc), self.nRequestID)
			
	def ReqLockInsert(self, BrokerID = '', InvestorID = '', InstrumentID = '', LockRef = '', UserID = '', Volume = 0, RequestID = 0, BusinessUnit = '', LockType = '', ExchangeID = '', IPAddress = '', MacAddress = ''):
		struc = CThostFtdcInputLockField()
		struc.BrokerID = bytes(BrokerID, encoding='ascii')
		struc.InvestorID = bytes(InvestorID, encoding='ascii')
		struc.InstrumentID = bytes(InstrumentID, encoding='ascii')
		struc.LockRef = bytes(LockRef, encoding='ascii')
		struc.UserID = bytes(UserID, encoding='ascii')
		struc.Volume = Volume
		struc.RequestID = RequestID
		struc.BusinessUnit = bytes(BusinessUnit, encoding='ascii')
		struc.LockType = bytes(LockType, encoding='ascii')
		struc.ExchangeID = bytes(ExchangeID, encoding='ascii')
		struc.IPAddress = bytes(IPAddress, encoding='ascii')
		struc.MacAddress = bytes(MacAddress, encoding='ascii')

		self.nRequestID += 1
		self.h.ReqLockInsert(self.api, byref(struc), self.nRequestID)
			
	def ReqQryParkedOrderAction(self, BrokerID = '', InvestorID = '', InstrumentID = '', ExchangeID = ''):
		struc = CThostFtdcQryParkedOrderActionField()
		struc.BrokerID = bytes(BrokerID, encoding='ascii')
		struc.InvestorID = bytes(InvestorID, encoding='ascii')
		struc.InstrumentID = bytes(InstrumentID, encoding='ascii')
		struc.ExchangeID = bytes(ExchangeID, encoding='ascii')

		self.nRequestID += 1
		self.h.ReqQryParkedOrderAction(self.api, byref(struc), self.nRequestID)
			
	def ReqQryBrokerTradingAlgos(self, BrokerID = '', ExchangeID = '', InstrumentID = ''):
		struc = CThostFtdcQryBrokerTradingAlgosField()
		struc.BrokerID = bytes(BrokerID, encoding='ascii')
		struc.ExchangeID = bytes(ExchangeID, encoding='ascii')
		struc.InstrumentID = bytes(InstrumentID, encoding='ascii')

		self.nRequestID += 1
		self.h.ReqQryBrokerTradingAlgos(self.api, byref(struc), self.nRequestID)
			
	def ReqExecOrderAction(self, BrokerID = '', InvestorID = '', ExecOrderActionRef = 0, ExecOrderRef = '', RequestID = 0, FrontID = 0, SessionID = 0, ExchangeID = '', ExecOrderSysID = '', ActionFlag = '', UserID = '', InstrumentID = '', InvestUnitID = '', IPAddress = '', MacAddress = ''):
		struc = CThostFtdcInputExecOrderActionField()
		struc.BrokerID = bytes(BrokerID, encoding='ascii')
		struc.InvestorID = bytes(InvestorID, encoding='ascii')
		struc.ExecOrderActionRef = ExecOrderActionRef
		struc.ExecOrderRef = bytes(ExecOrderRef, encoding='ascii')
		struc.RequestID = RequestID
		struc.FrontID = FrontID
		struc.SessionID = SessionID
		struc.ExchangeID = bytes(ExchangeID, encoding='ascii')
		struc.ExecOrderSysID = bytes(ExecOrderSysID, encoding='ascii')
		struc.ActionFlag = bytes(ActionFlag, encoding='ascii')
		struc.UserID = bytes(UserID, encoding='ascii')
		struc.InstrumentID = bytes(InstrumentID, encoding='ascii')
		struc.InvestUnitID = bytes(InvestUnitID, encoding='ascii')
		struc.IPAddress = bytes(IPAddress, encoding='ascii')
		struc.MacAddress = bytes(MacAddress, encoding='ascii')

		self.nRequestID += 1
		self.h.ReqExecOrderAction(self.api, byref(struc), self.nRequestID)
			
	def Release(self):
		self.h.Release(self.api)
			
	def ReqQryCombAction(self, BrokerID = '', InvestorID = '', InstrumentID = '', ExchangeID = ''):
		struc = CThostFtdcQryCombActionField()
		struc.BrokerID = bytes(BrokerID, encoding='ascii')
		struc.InvestorID = bytes(InvestorID, encoding='ascii')
		struc.InstrumentID = bytes(InstrumentID, encoding='ascii')
		struc.ExchangeID = bytes(ExchangeID, encoding='ascii')

		self.nRequestID += 1
		self.h.ReqQryCombAction(self.api, byref(struc), self.nRequestID)
			
	def ReqQryTradingCode(self, BrokerID = '', InvestorID = '', ExchangeID = '', ClientID = '', ClientIDType = ''):
		struc = CThostFtdcQryTradingCodeField()
		struc.BrokerID = bytes(BrokerID, encoding='ascii')
		struc.InvestorID = bytes(InvestorID, encoding='ascii')
		struc.ExchangeID = bytes(ExchangeID, encoding='ascii')
		struc.ClientID = bytes(ClientID, encoding='ascii')
		struc.ClientIDType = bytes(ClientIDType, encoding='ascii')

		self.nRequestID += 1
		self.h.ReqQryTradingCode(self.api, byref(struc), self.nRequestID)
			
	def ReqQryTradingAccount(self, BrokerID = '', InvestorID = '', CurrencyID = '', BizType = ''):
		struc = CThostFtdcQryTradingAccountField()
		struc.BrokerID = bytes(BrokerID, encoding='ascii')
		struc.InvestorID = bytes(InvestorID, encoding='ascii')
		struc.CurrencyID = bytes(CurrencyID, encoding='ascii')
		struc.BizType = bytes(BizType, encoding='ascii')

		self.nRequestID += 1
		self.h.ReqQryTradingAccount(self.api, byref(struc), self.nRequestID)
			
	def ReqQryNotice(self, BrokerID = ''):
		struc = CThostFtdcQryNoticeField()
		struc.BrokerID = bytes(BrokerID, encoding='ascii')

		self.nRequestID += 1
		self.h.ReqQryNotice(self.api, byref(struc), self.nRequestID)
			
	def ReqQryExchangeRate(self, BrokerID = '', FromCurrencyID = '', ToCurrencyID = ''):
		struc = CThostFtdcQryExchangeRateField()
		struc.BrokerID = bytes(BrokerID, encoding='ascii')
		struc.FromCurrencyID = bytes(FromCurrencyID, encoding='ascii')
		struc.ToCurrencyID = bytes(ToCurrencyID, encoding='ascii')

		self.nRequestID += 1
		self.h.ReqQryExchangeRate(self.api, byref(struc), self.nRequestID)
			
	def ReqQryExecFreeze(self, BrokerID = '', InvestorID = '', InstrumentID = '', ExchangeID = ''):
		struc = CThostFtdcQryExecFreezeField()
		struc.BrokerID = bytes(BrokerID, encoding='ascii')
		struc.InvestorID = bytes(InvestorID, encoding='ascii')
		struc.InstrumentID = bytes(InstrumentID, encoding='ascii')
		struc.ExchangeID = bytes(ExchangeID, encoding='ascii')

		self.nRequestID += 1
		self.h.ReqQryExecFreeze(self.api, byref(struc), self.nRequestID)
			
	def ReqQueryBankAccountMoneyByFuture(self, TradeCode = '', BankID = '', BankBranchID = '', BrokerID = '', BrokerBranchID = '', TradeDate = '', TradeTime = '', BankSerial = '', TradingDay = '', PlateSerial = 0, LastFragment = '', SessionID = 0, CustomerName = '', IdCardType = '', IdentifiedCardNo = '', CustType = '', BankAccount = '', BankPassWord = '', AccountID = '', Password = '', FutureSerial = 0, InstallID = 0, UserID = '', VerifyCertNoFlag = '', CurrencyID = '', Digest = '', BankAccType = '', DeviceID = '', BankSecuAccType = '', BrokerIDByBank = '', BankSecuAcc = '', BankPwdFlag = '', SecuPwdFlag = '', OperNo = '', RequestID = 0, TID = 0):
		struc = CThostFtdcReqQueryAccountField()
		struc.TradeCode = bytes(TradeCode, encoding='ascii')
		struc.BankID = bytes(BankID, encoding='ascii')
		struc.BankBranchID = bytes(BankBranchID, encoding='ascii')
		struc.BrokerID = bytes(BrokerID, encoding='ascii')
		struc.BrokerBranchID = bytes(BrokerBranchID, encoding='ascii')
		struc.TradeDate = bytes(TradeDate, encoding='ascii')
		struc.TradeTime = bytes(TradeTime, encoding='ascii')
		struc.BankSerial = bytes(BankSerial, encoding='ascii')
		struc.TradingDay = bytes(TradingDay, encoding='ascii')
		struc.PlateSerial = PlateSerial
		struc.LastFragment = bytes(LastFragment, encoding='ascii')
		struc.SessionID = SessionID
		struc.CustomerName = bytes(CustomerName, encoding='ascii')
		struc.IdCardType = bytes(IdCardType, encoding='ascii')
		struc.IdentifiedCardNo = bytes(IdentifiedCardNo, encoding='ascii')
		struc.CustType = bytes(CustType, encoding='ascii')
		struc.BankAccount = bytes(BankAccount, encoding='ascii')
		struc.BankPassWord = bytes(BankPassWord, encoding='ascii')
		struc.AccountID = bytes(AccountID, encoding='ascii')
		struc.Password = bytes(Password, encoding='ascii')
		struc.FutureSerial = FutureSerial
		struc.InstallID = InstallID
		struc.UserID = bytes(UserID, encoding='ascii')
		struc.VerifyCertNoFlag = bytes(VerifyCertNoFlag, encoding='ascii')
		struc.CurrencyID = bytes(CurrencyID, encoding='ascii')
		struc.Digest = bytes(Digest, encoding='ascii')
		struc.BankAccType = bytes(BankAccType, encoding='ascii')
		struc.DeviceID = bytes(DeviceID, encoding='ascii')
		struc.BankSecuAccType = bytes(BankSecuAccType, encoding='ascii')
		struc.BrokerIDByBank = bytes(BrokerIDByBank, encoding='ascii')
		struc.BankSecuAcc = bytes(BankSecuAcc, encoding='ascii')
		struc.BankPwdFlag = bytes(BankPwdFlag, encoding='ascii')
		struc.SecuPwdFlag = bytes(SecuPwdFlag, encoding='ascii')
		struc.OperNo = bytes(OperNo, encoding='ascii')
		struc.RequestID = RequestID
		struc.TID = TID

		self.nRequestID += 1
		self.h.ReqQueryBankAccountMoneyByFuture(self.api, byref(struc), self.nRequestID)
			
	def Init(self):
		self.h.Init(self.api)
			
	def RegisterFront(self, pszFrontAddress):
		self.h.RegisterFront(self.api, bytes(pszFrontAddress, encoding='ascii'))
			
	def ReqQryTransferBank(self, BankID = '', BankBrchID = ''):
		struc = CThostFtdcQryTransferBankField()
		struc.BankID = bytes(BankID, encoding='ascii')
		struc.BankBrchID = bytes(BankBrchID, encoding='ascii')

		self.nRequestID += 1
		self.h.ReqQryTransferBank(self.api, byref(struc), self.nRequestID)
			
	def ReqQryOrder(self, BrokerID = '', InvestorID = '', InstrumentID = '', ExchangeID = '', OrderSysID = '', InsertTimeStart = '', InsertTimeEnd = ''):
		struc = CThostFtdcQryOrderField()
		struc.BrokerID = bytes(BrokerID, encoding='ascii')
		struc.InvestorID = bytes(InvestorID, encoding='ascii')
		struc.InstrumentID = bytes(InstrumentID, encoding='ascii')
		struc.ExchangeID = bytes(ExchangeID, encoding='ascii')
		struc.OrderSysID = bytes(OrderSysID, encoding='ascii')
		struc.InsertTimeStart = bytes(InsertTimeStart, encoding='ascii')
		struc.InsertTimeEnd = bytes(InsertTimeEnd, encoding='ascii')

		self.nRequestID += 1
		self.h.ReqQryOrder(self.api, byref(struc), self.nRequestID)
			
	def ReqQueryMaxOrderVolume(self, BrokerID = '', InvestorID = '', InstrumentID = '', Direction = '', OffsetFlag = '', HedgeFlag = '', MaxVolume = 0, ExchangeID = ''):
		struc = CThostFtdcQueryMaxOrderVolumeField()
		struc.BrokerID = bytes(BrokerID, encoding='ascii')
		struc.InvestorID = bytes(InvestorID, encoding='ascii')
		struc.InstrumentID = bytes(InstrumentID, encoding='ascii')
		struc.Direction = bytes(Direction, encoding='ascii')
		struc.OffsetFlag = bytes(OffsetFlag, encoding='ascii')
		struc.HedgeFlag = bytes(HedgeFlag, encoding='ascii')
		struc.MaxVolume = MaxVolume
		struc.ExchangeID = bytes(ExchangeID, encoding='ascii')

		self.nRequestID += 1
		self.h.ReqQueryMaxOrderVolume(self.api, byref(struc), self.nRequestID)
			
	def ReqQryETFOptionInstrCommRate(self, BrokerID = '', InvestorID = '', InstrumentID = '', ExchangeID = ''):
		struc = CThostFtdcQryETFOptionInstrCommRateField()
		struc.BrokerID = bytes(BrokerID, encoding='ascii')
		struc.InvestorID = bytes(InvestorID, encoding='ascii')
		struc.InstrumentID = bytes(InstrumentID, encoding='ascii')
		struc.ExchangeID = bytes(ExchangeID, encoding='ascii')

		self.nRequestID += 1
		self.h.ReqQryETFOptionInstrCommRate(self.api, byref(struc), self.nRequestID)
			
	def ReqQryCFMMCTradingAccountKey(self, BrokerID = '', InvestorID = ''):
		struc = CThostFtdcQryCFMMCTradingAccountKeyField()
		struc.BrokerID = bytes(BrokerID, encoding='ascii')
		struc.InvestorID = bytes(InvestorID, encoding='ascii')

		self.nRequestID += 1
		self.h.ReqQryCFMMCTradingAccountKey(self.api, byref(struc), self.nRequestID)
			
	def ReqCombActionInsert(self, BrokerID = '', InvestorID = '', InstrumentID = '', CombActionRef = '', UserID = '', Direction = '', Volume = 0, CombDirection = '', HedgeFlag = '', ExchangeID = '', IPAddress = '', MacAddress = ''):
		struc = CThostFtdcInputCombActionField()
		struc.BrokerID = bytes(BrokerID, encoding='ascii')
		struc.InvestorID = bytes(InvestorID, encoding='ascii')
		struc.InstrumentID = bytes(InstrumentID, encoding='ascii')
		struc.CombActionRef = bytes(CombActionRef, encoding='ascii')
		struc.UserID = bytes(UserID, encoding='ascii')
		struc.Direction = bytes(Direction, encoding='ascii')
		struc.Volume = Volume
		struc.CombDirection = bytes(CombDirection, encoding='ascii')
		struc.HedgeFlag = bytes(HedgeFlag, encoding='ascii')
		struc.ExchangeID = bytes(ExchangeID, encoding='ascii')
		struc.IPAddress = bytes(IPAddress, encoding='ascii')
		struc.MacAddress = bytes(MacAddress, encoding='ascii')

		self.nRequestID += 1
		self.h.ReqCombActionInsert(self.api, byref(struc), self.nRequestID)
			
	def ReqQryLockPosition(self, BrokerID = '', InvestorID = '', InstrumentID = '', ExchangeID = ''):
		struc = CThostFtdcQryLockPositionField()
		struc.BrokerID = bytes(BrokerID, encoding='ascii')
		struc.InvestorID = bytes(InvestorID, encoding='ascii')
		struc.InstrumentID = bytes(InstrumentID, encoding='ascii')
		struc.ExchangeID = bytes(ExchangeID, encoding='ascii')

		self.nRequestID += 1
		self.h.ReqQryLockPosition(self.api, byref(struc), self.nRequestID)
			
	def ReqQryExchangeMarginRateAdjust(self, BrokerID = '', InstrumentID = '', HedgeFlag = ''):
		struc = CThostFtdcQryExchangeMarginRateAdjustField()
		struc.BrokerID = bytes(BrokerID, encoding='ascii')
		struc.InstrumentID = bytes(InstrumentID, encoding='ascii')
		struc.HedgeFlag = bytes(HedgeFlag, encoding='ascii')

		self.nRequestID += 1
		self.h.ReqQryExchangeMarginRateAdjust(self.api, byref(struc), self.nRequestID)
			
	def ReqQryInstrumentCommissionRate(self, BrokerID = '', InvestorID = '', InstrumentID = '', ExchangeID = ''):
		struc = CThostFtdcQryInstrumentCommissionRateField()
		struc.BrokerID = bytes(BrokerID, encoding='ascii')
		struc.InvestorID = bytes(InvestorID, encoding='ascii')
		struc.InstrumentID = bytes(InstrumentID, encoding='ascii')
		struc.ExchangeID = bytes(ExchangeID, encoding='ascii')

		self.nRequestID += 1
		self.h.ReqQryInstrumentCommissionRate(self.api, byref(struc), self.nRequestID)
			
	def ReqQryOptionInstrCommRate(self, BrokerID = '', InvestorID = '', InstrumentID = '', ExchangeID = ''):
		struc = CThostFtdcQryOptionInstrCommRateField()
		struc.BrokerID = bytes(BrokerID, encoding='ascii')
		struc.InvestorID = bytes(InvestorID, encoding='ascii')
		struc.InstrumentID = bytes(InstrumentID, encoding='ascii')
		struc.ExchangeID = bytes(ExchangeID, encoding='ascii')

		self.nRequestID += 1
		self.h.ReqQryOptionInstrCommRate(self.api, byref(struc), self.nRequestID)
			
	def ReqQrySettlementInfo(self, BrokerID = '', InvestorID = '', TradingDay = ''):
		struc = CThostFtdcQrySettlementInfoField()
		struc.BrokerID = bytes(BrokerID, encoding='ascii')
		struc.InvestorID = bytes(InvestorID, encoding='ascii')
		struc.TradingDay = bytes(TradingDay, encoding='ascii')

		self.nRequestID += 1
		self.h.ReqQrySettlementInfo(self.api, byref(struc), self.nRequestID)
			
	def ReqQryTrade(self, BrokerID = '', InvestorID = '', InstrumentID = '', ExchangeID = '', TradeID = '', TradeTimeStart = '', TradeTimeEnd = ''):
		struc = CThostFtdcQryTradeField()
		struc.BrokerID = bytes(BrokerID, encoding='ascii')
		struc.InvestorID = bytes(InvestorID, encoding='ascii')
		struc.InstrumentID = bytes(InstrumentID, encoding='ascii')
		struc.ExchangeID = bytes(ExchangeID, encoding='ascii')
		struc.TradeID = bytes(TradeID, encoding='ascii')
		struc.TradeTimeStart = bytes(TradeTimeStart, encoding='ascii')
		struc.TradeTimeEnd = bytes(TradeTimeEnd, encoding='ascii')

		self.nRequestID += 1
		self.h.ReqQryTrade(self.api, byref(struc), self.nRequestID)
			
	def ReqQryProductGroup(self, ProductID = '', ExchangeID = ''):
		struc = CThostFtdcQryProductGroupField()
		struc.ProductID = bytes(ProductID, encoding='ascii')
		struc.ExchangeID = bytes(ExchangeID, encoding='ascii')

		self.nRequestID += 1
		self.h.ReqQryProductGroup(self.api, byref(struc), self.nRequestID)
			
	def ReqQuoteAction(self, BrokerID = '', InvestorID = '', QuoteActionRef = 0, QuoteRef = '', RequestID = 0, FrontID = 0, SessionID = 0, ExchangeID = '', QuoteSysID = '', ActionFlag = '', UserID = '', InstrumentID = '', InvestUnitID = '', ClientID = '', IPAddress = '', MacAddress = ''):
		struc = CThostFtdcInputQuoteActionField()
		struc.BrokerID = bytes(BrokerID, encoding='ascii')
		struc.InvestorID = bytes(InvestorID, encoding='ascii')
		struc.QuoteActionRef = QuoteActionRef
		struc.QuoteRef = bytes(QuoteRef, encoding='ascii')
		struc.RequestID = RequestID
		struc.FrontID = FrontID
		struc.SessionID = SessionID
		struc.ExchangeID = bytes(ExchangeID, encoding='ascii')
		struc.QuoteSysID = bytes(QuoteSysID, encoding='ascii')
		struc.ActionFlag = bytes(ActionFlag, encoding='ascii')
		struc.UserID = bytes(UserID, encoding='ascii')
		struc.InstrumentID = bytes(InstrumentID, encoding='ascii')
		struc.InvestUnitID = bytes(InvestUnitID, encoding='ascii')
		struc.ClientID = bytes(ClientID, encoding='ascii')
		struc.IPAddress = bytes(IPAddress, encoding='ascii')
		struc.MacAddress = bytes(MacAddress, encoding='ascii')

		self.nRequestID += 1
		self.h.ReqQuoteAction(self.api, byref(struc), self.nRequestID)
			
	def ReqQryInvestorPositionCombineDetail(self, BrokerID = '', InvestorID = '', CombInstrumentID = ''):
		struc = CThostFtdcQryInvestorPositionCombineDetailField()
		struc.BrokerID = bytes(BrokerID, encoding='ascii')
		struc.InvestorID = bytes(InvestorID, encoding='ascii')
		struc.CombInstrumentID = bytes(CombInstrumentID, encoding='ascii')

		self.nRequestID += 1
		self.h.ReqQryInvestorPositionCombineDetail(self.api, byref(struc), self.nRequestID)
			
	def RegisterFensUserInfo(self, BrokerID = '', UserID = '', LoginMode = ''):
		struc = CThostFtdcFensUserInfoField()
		struc.BrokerID = bytes(BrokerID, encoding='ascii')
		struc.UserID = bytes(UserID, encoding='ascii')
		struc.LoginMode = bytes(LoginMode, encoding='ascii')

		self.nRequestID += 1
		self.h.RegisterFensUserInfo(self.api, byref(struc), self.nRequestID)
			
	def ReqRemoveParkedOrder(self, BrokerID = '', InvestorID = '', ParkedOrderID = ''):
		struc = CThostFtdcRemoveParkedOrderField()
		struc.BrokerID = bytes(BrokerID, encoding='ascii')
		struc.InvestorID = bytes(InvestorID, encoding='ascii')
		struc.ParkedOrderID = bytes(ParkedOrderID, encoding='ascii')

		self.nRequestID += 1
		self.h.ReqRemoveParkedOrder(self.api, byref(struc), self.nRequestID)
			
	def ReqBatchOrderAction(self, BrokerID = '', InvestorID = '', OrderActionRef = 0, RequestID = 0, FrontID = 0, SessionID = 0, ExchangeID = '', UserID = '', InvestUnitID = '', IPAddress = '', MacAddress = ''):
		struc = CThostFtdcInputBatchOrderActionField()
		struc.BrokerID = bytes(BrokerID, encoding='ascii')
		struc.InvestorID = bytes(InvestorID, encoding='ascii')
		struc.OrderActionRef = OrderActionRef
		struc.RequestID = RequestID
		struc.FrontID = FrontID
		struc.SessionID = SessionID
		struc.ExchangeID = bytes(ExchangeID, encoding='ascii')
		struc.UserID = bytes(UserID, encoding='ascii')
		struc.InvestUnitID = bytes(InvestUnitID, encoding='ascii')
		struc.IPAddress = bytes(IPAddress, encoding='ascii')
		struc.MacAddress = bytes(MacAddress, encoding='ascii')

		self.nRequestID += 1
		self.h.ReqBatchOrderAction(self.api, byref(struc), self.nRequestID)
			
	def ReqQryQuote(self, BrokerID = '', InvestorID = '', InstrumentID = '', ExchangeID = '', QuoteSysID = '', InsertTimeStart = '', InsertTimeEnd = ''):
		struc = CThostFtdcQryQuoteField()
		struc.BrokerID = bytes(BrokerID, encoding='ascii')
		struc.InvestorID = bytes(InvestorID, encoding='ascii')
		struc.InstrumentID = bytes(InstrumentID, encoding='ascii')
		struc.ExchangeID = bytes(ExchangeID, encoding='ascii')
		struc.QuoteSysID = bytes(QuoteSysID, encoding='ascii')
		struc.InsertTimeStart = bytes(InsertTimeStart, encoding='ascii')
		struc.InsertTimeEnd = bytes(InsertTimeEnd, encoding='ascii')

		self.nRequestID += 1
		self.h.ReqQryQuote(self.api, byref(struc), self.nRequestID)
			
	def RegisterSpi(self, pSpi):
		self.h.RegisterSpi(self.api, pSpi)
			
	def ReqParkedOrderInsert(self, BrokerID = '', InvestorID = '', InstrumentID = '', OrderRef = '', UserID = '', OrderPriceType = '', Direction = '', CombOffsetFlag = '', CombHedgeFlag = '', LimitPrice = 0, VolumeTotalOriginal = 0, TimeCondition = '', GTDDate = '', VolumeCondition = '', MinVolume = 0, ContingentCondition = '', StopPrice = 0, ForceCloseReason = '', IsAutoSuspend = 0, BusinessUnit = '', RequestID = 0, UserForceClose = 0, ExchangeID = '', ParkedOrderID = '', UserType = '', Status = '', ErrorID = 0, ErrorMsg = '', IsSwapOrder = 0, AccountID = '', CurrencyID = '', ClientID = '', InvestUnitID = '', IPAddress = '', MacAddress = ''):
		struc = CThostFtdcParkedOrderField()
		struc.BrokerID = bytes(BrokerID, encoding='ascii')
		struc.InvestorID = bytes(InvestorID, encoding='ascii')
		struc.InstrumentID = bytes(InstrumentID, encoding='ascii')
		struc.OrderRef = bytes(OrderRef, encoding='ascii')
		struc.UserID = bytes(UserID, encoding='ascii')
		struc.OrderPriceType = bytes(OrderPriceType, encoding='ascii')
		struc.Direction = bytes(Direction, encoding='ascii')
		struc.CombOffsetFlag = bytes(CombOffsetFlag, encoding='ascii')
		struc.CombHedgeFlag = bytes(CombHedgeFlag, encoding='ascii')
		struc.LimitPrice = LimitPrice
		struc.VolumeTotalOriginal = VolumeTotalOriginal
		struc.TimeCondition = bytes(TimeCondition, encoding='ascii')
		struc.GTDDate = bytes(GTDDate, encoding='ascii')
		struc.VolumeCondition = bytes(VolumeCondition, encoding='ascii')
		struc.MinVolume = MinVolume
		struc.ContingentCondition = bytes(ContingentCondition, encoding='ascii')
		struc.StopPrice = StopPrice
		struc.ForceCloseReason = bytes(ForceCloseReason, encoding='ascii')
		struc.IsAutoSuspend = IsAutoSuspend
		struc.BusinessUnit = bytes(BusinessUnit, encoding='ascii')
		struc.RequestID = RequestID
		struc.UserForceClose = UserForceClose
		struc.ExchangeID = bytes(ExchangeID, encoding='ascii')
		struc.ParkedOrderID = bytes(ParkedOrderID, encoding='ascii')
		struc.UserType = bytes(UserType, encoding='ascii')
		struc.Status = bytes(Status, encoding='ascii')
		struc.ErrorID = ErrorID
		struc.ErrorMsg = bytes(ErrorMsg, encoding='ascii')
		struc.IsSwapOrder = IsSwapOrder
		struc.AccountID = bytes(AccountID, encoding='ascii')
		struc.CurrencyID = bytes(CurrencyID, encoding='ascii')
		struc.ClientID = bytes(ClientID, encoding='ascii')
		struc.InvestUnitID = bytes(InvestUnitID, encoding='ascii')
		struc.IPAddress = bytes(IPAddress, encoding='ascii')
		struc.MacAddress = bytes(MacAddress, encoding='ascii')

		self.nRequestID += 1
		self.h.ReqParkedOrderInsert(self.api, byref(struc), self.nRequestID)
			
	def ReqQryAccountregister(self, BrokerID = '', AccountID = '', BankID = '', BankBranchID = '', CurrencyID = ''):
		struc = CThostFtdcQryAccountregisterField()
		struc.BrokerID = bytes(BrokerID, encoding='ascii')
		struc.AccountID = bytes(AccountID, encoding='ascii')
		struc.BankID = bytes(BankID, encoding='ascii')
		struc.BankBranchID = bytes(BankBranchID, encoding='ascii')
		struc.CurrencyID = bytes(CurrencyID, encoding='ascii')

		self.nRequestID += 1
		self.h.ReqQryAccountregister(self.api, byref(struc), self.nRequestID)
			
	def ReqUserLogin(self, TradingDay = '', BrokerID = '', UserID = '', Password = '', UserProductInfo = '', InterfaceProductInfo = '', ProtocolInfo = '', MacAddress = '', OneTimePassword = '', ClientIPAddress = '', LoginRemark = ''):
		struc = CThostFtdcReqUserLoginField()
		struc.TradingDay = bytes(TradingDay, encoding='ascii')
		struc.BrokerID = bytes(BrokerID, encoding='ascii')
		struc.UserID = bytes(UserID, encoding='ascii')
		struc.Password = bytes(Password, encoding='ascii')
		struc.UserProductInfo = bytes(UserProductInfo, encoding='ascii')
		struc.InterfaceProductInfo = bytes(InterfaceProductInfo, encoding='ascii')
		struc.ProtocolInfo = bytes(ProtocolInfo, encoding='ascii')
		struc.MacAddress = bytes(MacAddress, encoding='ascii')
		struc.OneTimePassword = bytes(OneTimePassword, encoding='ascii')
		struc.ClientIPAddress = bytes(ClientIPAddress, encoding='ascii')
		struc.LoginRemark = bytes(LoginRemark, encoding='ascii')

		self.nRequestID += 1
		self.h.ReqUserLogin(self.api, byref(struc), self.nRequestID)
			