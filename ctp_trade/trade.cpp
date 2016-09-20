

#include "Trade.h"
#include <string.h>
int nReq;

Trade::Trade(void)
{
	_FrontConnected = NULL;
	_FrontDisconnected = NULL;
	_HeartBeatWarning = NULL;
	_RspAuthenticate = NULL;
	_RspUserLogin = NULL;
	_RspUserLogout = NULL;
	_RspUserPasswordUpdate = NULL;
	_RspTradingAccountPasswordUpdate = NULL;
	_RspOrderInsert = NULL;
	_RspParkedOrderInsert = NULL;
	_RspParkedOrderAction = NULL;
	_RspOrderAction = NULL;
	_RspQueryMaxOrderVolume = NULL;
	_RspSettlementInfoConfirm = NULL;
	_RspRemoveParkedOrder = NULL;
	_RspRemoveParkedOrderAction = NULL;
	_RspExecOrderInsert = NULL;
	_RspExecOrderAction = NULL;
	_RspForQuoteInsert = NULL;
	_RspQuoteInsert = NULL;
	_RspQuoteAction = NULL;
	_RspLockInsert = NULL;
	_RspBatchOrderAction = NULL;
	_RspCombActionInsert = NULL;
	_RspQryOrder = NULL;
	_RspQryTrade = NULL;
	_RspQryInvestorPosition = NULL;
	_RspQryTradingAccount = NULL;
	_RspQryInvestor = NULL;
	_RspQryTradingCode = NULL;
	_RspQryInstrumentMarginRate = NULL;
	_RspQryInstrumentCommissionRate = NULL;
	_RspQryExchange = NULL;
	_RspQryProduct = NULL;
	_RspQryInstrument = NULL;
	_RspQryDepthMarketData = NULL;
	_RspQrySettlementInfo = NULL;
	_RspQryTransferBank = NULL;
	_RspQryInvestorPositionDetail = NULL;
	_RspQryNotice = NULL;
	_RspQrySettlementInfoConfirm = NULL;
	_RspQryInvestorPositionCombineDetail = NULL;
	_RspQryCFMMCTradingAccountKey = NULL;
	_RspQryEWarrantOffset = NULL;
	_RspQryInvestorProductGroupMargin = NULL;
	_RspQryExchangeMarginRate = NULL;
	_RspQryExchangeMarginRateAdjust = NULL;
	_RspQryExchangeRate = NULL;
	_RspQrySecAgentACIDMap = NULL;
	_RspQryProductExchRate = NULL;
	_RspQryProductGroup = NULL;
	_RspQryMMInstrumentCommissionRate = NULL;
	_RspQryMMOptionInstrCommRate = NULL;
	_RspQryInstrumentOrderCommRate = NULL;
	_RspQryOptionInstrTradeCost = NULL;
	_RspQryOptionInstrCommRate = NULL;
	_RspQryExecOrder = NULL;
	_RspQryForQuote = NULL;
	_RspQryQuote = NULL;
	_RspQryLock = NULL;
	_RspQryLockPosition = NULL;
	_RspQryETFOptionInstrCommRate = NULL;
	_RspQryInvestorLevel = NULL;
	_RspQryExecFreeze = NULL;
	_RspQryCombInstrumentGuard = NULL;
	_RspQryCombAction = NULL;
	_RspQryTransferSerial = NULL;
	_RspQryAccountregister = NULL;
	_RspError = NULL;
	_RtnOrder = NULL;
	_RtnTrade = NULL;
	_ErrRtnOrderInsert = NULL;
	_ErrRtnOrderAction = NULL;
	_RtnInstrumentStatus = NULL;
	_RtnBulletin = NULL;
	_RtnTradingNotice = NULL;
	_RtnErrorConditionalOrder = NULL;
	_RtnExecOrder = NULL;
	_ErrRtnExecOrderInsert = NULL;
	_ErrRtnExecOrderAction = NULL;
	_ErrRtnForQuoteInsert = NULL;
	_RtnQuote = NULL;
	_ErrRtnQuoteInsert = NULL;
	_ErrRtnQuoteAction = NULL;
	_RtnForQuoteRsp = NULL;
	_RtnCFMMCTradingAccountToken = NULL;
	_RtnLock = NULL;
	_ErrRtnLockInsert = NULL;
	_ErrRtnBatchOrderAction = NULL;
	_RtnCombAction = NULL;
	_ErrRtnCombActionInsert = NULL;
	_RspQryContractBank = NULL;
	_RspQryParkedOrder = NULL;
	_RspQryParkedOrderAction = NULL;
	_RspQryTradingNotice = NULL;
	_RspQryBrokerTradingParams = NULL;
	_RspQryBrokerTradingAlgos = NULL;
	_RspQueryCFMMCTradingAccountToken = NULL;
	_RtnFromBankToFutureByBank = NULL;
	_RtnFromFutureToBankByBank = NULL;
	_RtnRepealFromBankToFutureByBank = NULL;
	_RtnRepealFromFutureToBankByBank = NULL;
	_RtnFromBankToFutureByFuture = NULL;
	_RtnFromFutureToBankByFuture = NULL;
	_RtnRepealFromBankToFutureByFutureManual = NULL;
	_RtnRepealFromFutureToBankByFutureManual = NULL;
	_RtnQueryBankBalanceByFuture = NULL;
	_ErrRtnBankToFutureByFuture = NULL;
	_ErrRtnFutureToBankByFuture = NULL;
	_ErrRtnRepealBankToFutureByFutureManual = NULL;
	_ErrRtnRepealFutureToBankByFutureManual = NULL;
	_ErrRtnQueryBankBalanceByFuture = NULL;
	_RtnRepealFromBankToFutureByFuture = NULL;
	_RtnRepealFromFutureToBankByFuture = NULL;
	_RspFromBankToFutureByFuture = NULL;
	_RspFromFutureToBankByFuture = NULL;
	_RspQueryBankAccountMoneyByFuture = NULL;
	_RtnOpenAccountByBank = NULL;
	_RtnCancelAccountByBank = NULL;
	_RtnChangeAccountByBank = NULL;

}
void SetOnFrontConnected(Trade* spi, void* func){spi->_FrontConnected = func;}
void SetOnFrontDisconnected(Trade* spi, void* func){spi->_FrontDisconnected = func;}
void SetOnHeartBeatWarning(Trade* spi, void* func){spi->_HeartBeatWarning = func;}
void SetOnRspAuthenticate(Trade* spi, void* func){spi->_RspAuthenticate = func;}
void SetOnRspUserLogin(Trade* spi, void* func){spi->_RspUserLogin = func;}
void SetOnRspUserLogout(Trade* spi, void* func){spi->_RspUserLogout = func;}
void SetOnRspUserPasswordUpdate(Trade* spi, void* func){spi->_RspUserPasswordUpdate = func;}
void SetOnRspTradingAccountPasswordUpdate(Trade* spi, void* func){spi->_RspTradingAccountPasswordUpdate = func;}
void SetOnRspOrderInsert(Trade* spi, void* func){spi->_RspOrderInsert = func;}
void SetOnRspParkedOrderInsert(Trade* spi, void* func){spi->_RspParkedOrderInsert = func;}
void SetOnRspParkedOrderAction(Trade* spi, void* func){spi->_RspParkedOrderAction = func;}
void SetOnRspOrderAction(Trade* spi, void* func){spi->_RspOrderAction = func;}
void SetOnRspQueryMaxOrderVolume(Trade* spi, void* func){spi->_RspQueryMaxOrderVolume = func;}
void SetOnRspSettlementInfoConfirm(Trade* spi, void* func){spi->_RspSettlementInfoConfirm = func;}
void SetOnRspRemoveParkedOrder(Trade* spi, void* func){spi->_RspRemoveParkedOrder = func;}
void SetOnRspRemoveParkedOrderAction(Trade* spi, void* func){spi->_RspRemoveParkedOrderAction = func;}
void SetOnRspExecOrderInsert(Trade* spi, void* func){spi->_RspExecOrderInsert = func;}
void SetOnRspExecOrderAction(Trade* spi, void* func){spi->_RspExecOrderAction = func;}
void SetOnRspForQuoteInsert(Trade* spi, void* func){spi->_RspForQuoteInsert = func;}
void SetOnRspQuoteInsert(Trade* spi, void* func){spi->_RspQuoteInsert = func;}
void SetOnRspQuoteAction(Trade* spi, void* func){spi->_RspQuoteAction = func;}
void SetOnRspLockInsert(Trade* spi, void* func){spi->_RspLockInsert = func;}
void SetOnRspBatchOrderAction(Trade* spi, void* func){spi->_RspBatchOrderAction = func;}
void SetOnRspCombActionInsert(Trade* spi, void* func){spi->_RspCombActionInsert = func;}
void SetOnRspQryOrder(Trade* spi, void* func){spi->_RspQryOrder = func;}
void SetOnRspQryTrade(Trade* spi, void* func){spi->_RspQryTrade = func;}
void SetOnRspQryInvestorPosition(Trade* spi, void* func){spi->_RspQryInvestorPosition = func;}
void SetOnRspQryTradingAccount(Trade* spi, void* func){spi->_RspQryTradingAccount = func;}
void SetOnRspQryInvestor(Trade* spi, void* func){spi->_RspQryInvestor = func;}
void SetOnRspQryTradingCode(Trade* spi, void* func){spi->_RspQryTradingCode = func;}
void SetOnRspQryInstrumentMarginRate(Trade* spi, void* func){spi->_RspQryInstrumentMarginRate = func;}
void SetOnRspQryInstrumentCommissionRate(Trade* spi, void* func){spi->_RspQryInstrumentCommissionRate = func;}
void SetOnRspQryExchange(Trade* spi, void* func){spi->_RspQryExchange = func;}
void SetOnRspQryProduct(Trade* spi, void* func){spi->_RspQryProduct = func;}
void SetOnRspQryInstrument(Trade* spi, void* func){spi->_RspQryInstrument = func;}
void SetOnRspQryDepthMarketData(Trade* spi, void* func){spi->_RspQryDepthMarketData = func;}
void SetOnRspQrySettlementInfo(Trade* spi, void* func){spi->_RspQrySettlementInfo = func;}
void SetOnRspQryTransferBank(Trade* spi, void* func){spi->_RspQryTransferBank = func;}
void SetOnRspQryInvestorPositionDetail(Trade* spi, void* func){spi->_RspQryInvestorPositionDetail = func;}
void SetOnRspQryNotice(Trade* spi, void* func){spi->_RspQryNotice = func;}
void SetOnRspQrySettlementInfoConfirm(Trade* spi, void* func){spi->_RspQrySettlementInfoConfirm = func;}
void SetOnRspQryInvestorPositionCombineDetail(Trade* spi, void* func){spi->_RspQryInvestorPositionCombineDetail = func;}
void SetOnRspQryCFMMCTradingAccountKey(Trade* spi, void* func){spi->_RspQryCFMMCTradingAccountKey = func;}
void SetOnRspQryEWarrantOffset(Trade* spi, void* func){spi->_RspQryEWarrantOffset = func;}
void SetOnRspQryInvestorProductGroupMargin(Trade* spi, void* func){spi->_RspQryInvestorProductGroupMargin = func;}
void SetOnRspQryExchangeMarginRate(Trade* spi, void* func){spi->_RspQryExchangeMarginRate = func;}
void SetOnRspQryExchangeMarginRateAdjust(Trade* spi, void* func){spi->_RspQryExchangeMarginRateAdjust = func;}
void SetOnRspQryExchangeRate(Trade* spi, void* func){spi->_RspQryExchangeRate = func;}
void SetOnRspQrySecAgentACIDMap(Trade* spi, void* func){spi->_RspQrySecAgentACIDMap = func;}
void SetOnRspQryProductExchRate(Trade* spi, void* func){spi->_RspQryProductExchRate = func;}
void SetOnRspQryProductGroup(Trade* spi, void* func){spi->_RspQryProductGroup = func;}
void SetOnRspQryMMInstrumentCommissionRate(Trade* spi, void* func){spi->_RspQryMMInstrumentCommissionRate = func;}
void SetOnRspQryMMOptionInstrCommRate(Trade* spi, void* func){spi->_RspQryMMOptionInstrCommRate = func;}
void SetOnRspQryInstrumentOrderCommRate(Trade* spi, void* func){spi->_RspQryInstrumentOrderCommRate = func;}
void SetOnRspQryOptionInstrTradeCost(Trade* spi, void* func){spi->_RspQryOptionInstrTradeCost = func;}
void SetOnRspQryOptionInstrCommRate(Trade* spi, void* func){spi->_RspQryOptionInstrCommRate = func;}
void SetOnRspQryExecOrder(Trade* spi, void* func){spi->_RspQryExecOrder = func;}
void SetOnRspQryForQuote(Trade* spi, void* func){spi->_RspQryForQuote = func;}
void SetOnRspQryQuote(Trade* spi, void* func){spi->_RspQryQuote = func;}
void SetOnRspQryLock(Trade* spi, void* func){spi->_RspQryLock = func;}
void SetOnRspQryLockPosition(Trade* spi, void* func){spi->_RspQryLockPosition = func;}
void SetOnRspQryETFOptionInstrCommRate(Trade* spi, void* func){spi->_RspQryETFOptionInstrCommRate = func;}
void SetOnRspQryInvestorLevel(Trade* spi, void* func){spi->_RspQryInvestorLevel = func;}
void SetOnRspQryExecFreeze(Trade* spi, void* func){spi->_RspQryExecFreeze = func;}
void SetOnRspQryCombInstrumentGuard(Trade* spi, void* func){spi->_RspQryCombInstrumentGuard = func;}
void SetOnRspQryCombAction(Trade* spi, void* func){spi->_RspQryCombAction = func;}
void SetOnRspQryTransferSerial(Trade* spi, void* func){spi->_RspQryTransferSerial = func;}
void SetOnRspQryAccountregister(Trade* spi, void* func){spi->_RspQryAccountregister = func;}
void SetOnRspError(Trade* spi, void* func){spi->_RspError = func;}
void SetOnRtnOrder(Trade* spi, void* func){spi->_RtnOrder = func;}
void SetOnRtnTrade(Trade* spi, void* func){spi->_RtnTrade = func;}
void SetOnErrRtnOrderInsert(Trade* spi, void* func){spi->_ErrRtnOrderInsert = func;}
void SetOnErrRtnOrderAction(Trade* spi, void* func){spi->_ErrRtnOrderAction = func;}
void SetOnRtnInstrumentStatus(Trade* spi, void* func){spi->_RtnInstrumentStatus = func;}
void SetOnRtnBulletin(Trade* spi, void* func){spi->_RtnBulletin = func;}
void SetOnRtnTradingNotice(Trade* spi, void* func){spi->_RtnTradingNotice = func;}
void SetOnRtnErrorConditionalOrder(Trade* spi, void* func){spi->_RtnErrorConditionalOrder = func;}
void SetOnRtnExecOrder(Trade* spi, void* func){spi->_RtnExecOrder = func;}
void SetOnErrRtnExecOrderInsert(Trade* spi, void* func){spi->_ErrRtnExecOrderInsert = func;}
void SetOnErrRtnExecOrderAction(Trade* spi, void* func){spi->_ErrRtnExecOrderAction = func;}
void SetOnErrRtnForQuoteInsert(Trade* spi, void* func){spi->_ErrRtnForQuoteInsert = func;}
void SetOnRtnQuote(Trade* spi, void* func){spi->_RtnQuote = func;}
void SetOnErrRtnQuoteInsert(Trade* spi, void* func){spi->_ErrRtnQuoteInsert = func;}
void SetOnErrRtnQuoteAction(Trade* spi, void* func){spi->_ErrRtnQuoteAction = func;}
void SetOnRtnForQuoteRsp(Trade* spi, void* func){spi->_RtnForQuoteRsp = func;}
void SetOnRtnCFMMCTradingAccountToken(Trade* spi, void* func){spi->_RtnCFMMCTradingAccountToken = func;}
void SetOnRtnLock(Trade* spi, void* func){spi->_RtnLock = func;}
void SetOnErrRtnLockInsert(Trade* spi, void* func){spi->_ErrRtnLockInsert = func;}
void SetOnErrRtnBatchOrderAction(Trade* spi, void* func){spi->_ErrRtnBatchOrderAction = func;}
void SetOnRtnCombAction(Trade* spi, void* func){spi->_RtnCombAction = func;}
void SetOnErrRtnCombActionInsert(Trade* spi, void* func){spi->_ErrRtnCombActionInsert = func;}
void SetOnRspQryContractBank(Trade* spi, void* func){spi->_RspQryContractBank = func;}
void SetOnRspQryParkedOrder(Trade* spi, void* func){spi->_RspQryParkedOrder = func;}
void SetOnRspQryParkedOrderAction(Trade* spi, void* func){spi->_RspQryParkedOrderAction = func;}
void SetOnRspQryTradingNotice(Trade* spi, void* func){spi->_RspQryTradingNotice = func;}
void SetOnRspQryBrokerTradingParams(Trade* spi, void* func){spi->_RspQryBrokerTradingParams = func;}
void SetOnRspQryBrokerTradingAlgos(Trade* spi, void* func){spi->_RspQryBrokerTradingAlgos = func;}
void SetOnRspQueryCFMMCTradingAccountToken(Trade* spi, void* func){spi->_RspQueryCFMMCTradingAccountToken = func;}
void SetOnRtnFromBankToFutureByBank(Trade* spi, void* func){spi->_RtnFromBankToFutureByBank = func;}
void SetOnRtnFromFutureToBankByBank(Trade* spi, void* func){spi->_RtnFromFutureToBankByBank = func;}
void SetOnRtnRepealFromBankToFutureByBank(Trade* spi, void* func){spi->_RtnRepealFromBankToFutureByBank = func;}
void SetOnRtnRepealFromFutureToBankByBank(Trade* spi, void* func){spi->_RtnRepealFromFutureToBankByBank = func;}
void SetOnRtnFromBankToFutureByFuture(Trade* spi, void* func){spi->_RtnFromBankToFutureByFuture = func;}
void SetOnRtnFromFutureToBankByFuture(Trade* spi, void* func){spi->_RtnFromFutureToBankByFuture = func;}
void SetOnRtnRepealFromBankToFutureByFutureManual(Trade* spi, void* func){spi->_RtnRepealFromBankToFutureByFutureManual = func;}
void SetOnRtnRepealFromFutureToBankByFutureManual(Trade* spi, void* func){spi->_RtnRepealFromFutureToBankByFutureManual = func;}
void SetOnRtnQueryBankBalanceByFuture(Trade* spi, void* func){spi->_RtnQueryBankBalanceByFuture = func;}
void SetOnErrRtnBankToFutureByFuture(Trade* spi, void* func){spi->_ErrRtnBankToFutureByFuture = func;}
void SetOnErrRtnFutureToBankByFuture(Trade* spi, void* func){spi->_ErrRtnFutureToBankByFuture = func;}
void SetOnErrRtnRepealBankToFutureByFutureManual(Trade* spi, void* func){spi->_ErrRtnRepealBankToFutureByFutureManual = func;}
void SetOnErrRtnRepealFutureToBankByFutureManual(Trade* spi, void* func){spi->_ErrRtnRepealFutureToBankByFutureManual = func;}
void SetOnErrRtnQueryBankBalanceByFuture(Trade* spi, void* func){spi->_ErrRtnQueryBankBalanceByFuture = func;}
void SetOnRtnRepealFromBankToFutureByFuture(Trade* spi, void* func){spi->_RtnRepealFromBankToFutureByFuture = func;}
void SetOnRtnRepealFromFutureToBankByFuture(Trade* spi, void* func){spi->_RtnRepealFromFutureToBankByFuture = func;}
void SetOnRspFromBankToFutureByFuture(Trade* spi, void* func){spi->_RspFromBankToFutureByFuture = func;}
void SetOnRspFromFutureToBankByFuture(Trade* spi, void* func){spi->_RspFromFutureToBankByFuture = func;}
void SetOnRspQueryBankAccountMoneyByFuture(Trade* spi, void* func){spi->_RspQueryBankAccountMoneyByFuture = func;}
void SetOnRtnOpenAccountByBank(Trade* spi, void* func){spi->_RtnOpenAccountByBank = func;}
void SetOnRtnCancelAccountByBank(Trade* spi, void* func){spi->_RtnCancelAccountByBank = func;}
void SetOnRtnChangeAccountByBank(Trade* spi, void* func){spi->_RtnChangeAccountByBank = func;}

void* WINAPI CreateApi(){return CThostFtdcTraderApi::CreateFtdcTraderApi("./log/");}

void* WINAPI CreateSpi(){return new Trade();}

		void* WINAPI ReqCombActionInsert(CThostFtdcTraderApi *api ,CThostFtdcInputCombActionField *pInputCombAction, int nRequestID){api->ReqCombActionInsert(pInputCombAction,nRequestID); return 0;}
void* WINAPI RegisterFensUserInfo(CThostFtdcTraderApi *api ,CThostFtdcFensUserInfoField * pFensUserInfo){api->RegisterFensUserInfo(pFensUserInfo); return 0;}
void* WINAPI ReqForQuoteInsert(CThostFtdcTraderApi *api ,CThostFtdcInputForQuoteField *pInputForQuote, int nRequestID){api->ReqForQuoteInsert(pInputForQuote,nRequestID); return 0;}
void* WINAPI ReqQryProduct(CThostFtdcTraderApi *api ,CThostFtdcQryProductField *pQryProduct, int nRequestID){api->ReqQryProduct(pQryProduct,nRequestID); return 0;}
void* WINAPI Release(CThostFtdcTraderApi *api ){api->Release(); return 0;}
void* WINAPI ReqQryLockPosition(CThostFtdcTraderApi *api ,CThostFtdcQryLockPositionField *pQryLockPosition, int nRequestID){api->ReqQryLockPosition(pQryLockPosition,nRequestID); return 0;}
void* WINAPI ReqQrySettlementInfo(CThostFtdcTraderApi *api ,CThostFtdcQrySettlementInfoField *pQrySettlementInfo, int nRequestID){api->ReqQrySettlementInfo(pQrySettlementInfo,nRequestID); return 0;}
void* WINAPI ReqQryExchangeMarginRate(CThostFtdcTraderApi *api ,CThostFtdcQryExchangeMarginRateField *pQryExchangeMarginRate, int nRequestID){api->ReqQryExchangeMarginRate(pQryExchangeMarginRate,nRequestID); return 0;}
void* WINAPI ReqQryLock(CThostFtdcTraderApi *api ,CThostFtdcQryLockField *pQryLock, int nRequestID){api->ReqQryLock(pQryLock,nRequestID); return 0;}
void* WINAPI ReqAuthenticate(CThostFtdcTraderApi *api ,CThostFtdcReqAuthenticateField *pReqAuthenticateField, int nRequestID){api->ReqAuthenticate(pReqAuthenticateField,nRequestID); return 0;}
void* WINAPI ReqQryParkedOrderAction(CThostFtdcTraderApi *api ,CThostFtdcQryParkedOrderActionField *pQryParkedOrderAction, int nRequestID){api->ReqQryParkedOrderAction(pQryParkedOrderAction,nRequestID); return 0;}
void* WINAPI SubscribePrivateTopic(CThostFtdcTraderApi *api ,THOST_TE_RESUME_TYPE nResumeType){api->SubscribePrivateTopic(nResumeType); return 0;}
void* WINAPI ReqQryInvestorPosition(CThostFtdcTraderApi *api ,CThostFtdcQryInvestorPositionField *pQryInvestorPosition, int nRequestID){api->ReqQryInvestorPosition(pQryInvestorPosition,nRequestID); return 0;}
void* WINAPI ReqQryNotice(CThostFtdcTraderApi *api ,CThostFtdcQryNoticeField *pQryNotice, int nRequestID){api->ReqQryNotice(pQryNotice,nRequestID); return 0;}
void* WINAPI Init(CThostFtdcTraderApi *api ){api->Init(); return 0;}
void* WINAPI ReqQryExchangeRate(CThostFtdcTraderApi *api ,CThostFtdcQryExchangeRateField *pQryExchangeRate, int nRequestID){api->ReqQryExchangeRate(pQryExchangeRate,nRequestID); return 0;}
void* WINAPI ReqQryExecOrder(CThostFtdcTraderApi *api ,CThostFtdcQryExecOrderField *pQryExecOrder, int nRequestID){api->ReqQryExecOrder(pQryExecOrder,nRequestID); return 0;}
void* WINAPI ReqRemoveParkedOrder(CThostFtdcTraderApi *api ,CThostFtdcRemoveParkedOrderField *pRemoveParkedOrder, int nRequestID){api->ReqRemoveParkedOrder(pRemoveParkedOrder,nRequestID); return 0;}
void* WINAPI ReqQryAccountregister(CThostFtdcTraderApi *api ,CThostFtdcQryAccountregisterField *pQryAccountregister, int nRequestID){api->ReqQryAccountregister(pQryAccountregister,nRequestID); return 0;}
void* WINAPI ReqQryInvestorLevel(CThostFtdcTraderApi *api ,CThostFtdcQryInvestorLevelField *pQryInvestorLevel, int nRequestID){api->ReqQryInvestorLevel(pQryInvestorLevel,nRequestID); return 0;}
void* WINAPI ReqQryTradingNotice(CThostFtdcTraderApi *api ,CThostFtdcQryTradingNoticeField *pQryTradingNotice, int nRequestID){api->ReqQryTradingNotice(pQryTradingNotice,nRequestID); return 0;}
void* WINAPI ReqQryProductGroup(CThostFtdcTraderApi *api ,CThostFtdcQryProductGroupField *pQryProductGroup, int nRequestID){api->ReqQryProductGroup(pQryProductGroup,nRequestID); return 0;}
void* WINAPI ReqQryContractBank(CThostFtdcTraderApi *api ,CThostFtdcQryContractBankField *pQryContractBank, int nRequestID){api->ReqQryContractBank(pQryContractBank,nRequestID); return 0;}
void* WINAPI ReqQryInstrumentMarginRate(CThostFtdcTraderApi *api ,CThostFtdcQryInstrumentMarginRateField *pQryInstrumentMarginRate, int nRequestID){api->ReqQryInstrumentMarginRate(pQryInstrumentMarginRate,nRequestID); return 0;}
void* WINAPI ReqUserLogout(CThostFtdcTraderApi *api ,CThostFtdcUserLogoutField *pUserLogout, int nRequestID){api->ReqUserLogout(pUserLogout,nRequestID); return 0;}
void* WINAPI ReqQryInvestorPositionCombineDetail(CThostFtdcTraderApi *api ,CThostFtdcQryInvestorPositionCombineDetailField *pQryInvestorPositionCombineDetail, int nRequestID){api->ReqQryInvestorPositionCombineDetail(pQryInvestorPositionCombineDetail,nRequestID); return 0;}
void* WINAPI ReqQryEWarrantOffset(CThostFtdcTraderApi *api ,CThostFtdcQryEWarrantOffsetField *pQryEWarrantOffset, int nRequestID){api->ReqQryEWarrantOffset(pQryEWarrantOffset,nRequestID); return 0;}
void* WINAPI ReqParkedOrderAction(CThostFtdcTraderApi *api ,CThostFtdcParkedOrderActionField *pParkedOrderAction, int nRequestID){api->ReqParkedOrderAction(pParkedOrderAction,nRequestID); return 0;}
void* WINAPI ReqQryTradingAccount(CThostFtdcTraderApi *api ,CThostFtdcQryTradingAccountField *pQryTradingAccount, int nRequestID){api->ReqQryTradingAccount(pQryTradingAccount,nRequestID); return 0;}
void* WINAPI ReqQryETFOptionInstrCommRate(CThostFtdcTraderApi *api ,CThostFtdcQryETFOptionInstrCommRateField *pQryETFOptionInstrCommRate, int nRequestID){api->ReqQryETFOptionInstrCommRate(pQryETFOptionInstrCommRate,nRequestID); return 0;}
void* WINAPI ReqParkedOrderInsert(CThostFtdcTraderApi *api ,CThostFtdcParkedOrderField *pParkedOrder, int nRequestID){api->ReqParkedOrderInsert(pParkedOrder,nRequestID); return 0;}
void* WINAPI ReqQryQuote(CThostFtdcTraderApi *api ,CThostFtdcQryQuoteField *pQryQuote, int nRequestID){api->ReqQryQuote(pQryQuote,nRequestID); return 0;}
void* WINAPI ReqQueryCFMMCTradingAccountToken(CThostFtdcTraderApi *api ,CThostFtdcQueryCFMMCTradingAccountTokenField *pQueryCFMMCTradingAccountToken, int nRequestID){api->ReqQueryCFMMCTradingAccountToken(pQueryCFMMCTradingAccountToken,nRequestID); return 0;}
void* WINAPI ReqQryInvestor(CThostFtdcTraderApi *api ,CThostFtdcQryInvestorField *pQryInvestor, int nRequestID){api->ReqQryInvestor(pQryInvestor,nRequestID); return 0;}
void* WINAPI ReqQryInstrument(CThostFtdcTraderApi *api ,CThostFtdcQryInstrumentField *pQryInstrument, int nRequestID){api->ReqQryInstrument(pQryInstrument,nRequestID); return 0;}
void* WINAPI ReqQryTrade(CThostFtdcTraderApi *api ,CThostFtdcQryTradeField *pQryTrade, int nRequestID){api->ReqQryTrade(pQryTrade,nRequestID); return 0;}
void* WINAPI ReqQueryBankAccountMoneyByFuture(CThostFtdcTraderApi *api ,CThostFtdcReqQueryAccountField *pReqQueryAccount, int nRequestID){api->ReqQueryBankAccountMoneyByFuture(pReqQueryAccount,nRequestID); return 0;}
void* WINAPI GetTradingDay(CThostFtdcTraderApi *api ){api->GetTradingDay(); return 0;}
void* WINAPI ReqQryProductExchRate(CThostFtdcTraderApi *api ,CThostFtdcQryProductExchRateField *pQryProductExchRate, int nRequestID){api->ReqQryProductExchRate(pQryProductExchRate,nRequestID); return 0;}
void* WINAPI ReqQryMMOptionInstrCommRate(CThostFtdcTraderApi *api ,CThostFtdcQryMMOptionInstrCommRateField *pQryMMOptionInstrCommRate, int nRequestID){api->ReqQryMMOptionInstrCommRate(pQryMMOptionInstrCommRate,nRequestID); return 0;}
void* WINAPI ReqExecOrderAction(CThostFtdcTraderApi *api ,CThostFtdcInputExecOrderActionField *pInputExecOrderAction, int nRequestID){api->ReqExecOrderAction(pInputExecOrderAction,nRequestID); return 0;}
void* WINAPI ReqBatchOrderAction(CThostFtdcTraderApi *api ,CThostFtdcInputBatchOrderActionField *pInputBatchOrderAction, int nRequestID){api->ReqBatchOrderAction(pInputBatchOrderAction,nRequestID); return 0;}
void* WINAPI ReqQrySecAgentACIDMap(CThostFtdcTraderApi *api ,CThostFtdcQrySecAgentACIDMapField *pQrySecAgentACIDMap, int nRequestID){api->ReqQrySecAgentACIDMap(pQrySecAgentACIDMap,nRequestID); return 0;}
void* WINAPI ReqQryCFMMCTradingAccountKey(CThostFtdcTraderApi *api ,CThostFtdcQryCFMMCTradingAccountKeyField *pQryCFMMCTradingAccountKey, int nRequestID){api->ReqQryCFMMCTradingAccountKey(pQryCFMMCTradingAccountKey,nRequestID); return 0;}
void* WINAPI ReqQryTransferSerial(CThostFtdcTraderApi *api ,CThostFtdcQryTransferSerialField *pQryTransferSerial, int nRequestID){api->ReqQryTransferSerial(pQryTransferSerial,nRequestID); return 0;}
void* WINAPI ReqSettlementInfoConfirm(CThostFtdcTraderApi *api ,CThostFtdcSettlementInfoConfirmField *pSettlementInfoConfirm, int nRequestID){api->ReqSettlementInfoConfirm(pSettlementInfoConfirm,nRequestID); return 0;}
void* WINAPI ReqQryCombAction(CThostFtdcTraderApi *api ,CThostFtdcQryCombActionField *pQryCombAction, int nRequestID){api->ReqQryCombAction(pQryCombAction,nRequestID); return 0;}
void* WINAPI ReqOrderAction(CThostFtdcTraderApi *api ,CThostFtdcInputOrderActionField *pInputOrderAction, int nRequestID){api->ReqOrderAction(pInputOrderAction,nRequestID); return 0;}
void* WINAPI ReqQryInvestorProductGroupMargin(CThostFtdcTraderApi *api ,CThostFtdcQryInvestorProductGroupMarginField *pQryInvestorProductGroupMargin, int nRequestID){api->ReqQryInvestorProductGroupMargin(pQryInvestorProductGroupMargin,nRequestID); return 0;}
void* WINAPI ReqQryExchange(CThostFtdcTraderApi *api ,CThostFtdcQryExchangeField *pQryExchange, int nRequestID){api->ReqQryExchange(pQryExchange,nRequestID); return 0;}
void* WINAPI RegisterNameServer(CThostFtdcTraderApi *api ,char *pszNsAddress){api->RegisterNameServer(pszNsAddress); return 0;}
void* WINAPI ReqExecOrderInsert(CThostFtdcTraderApi *api ,CThostFtdcInputExecOrderField *pInputExecOrder, int nRequestID){api->ReqExecOrderInsert(pInputExecOrder,nRequestID); return 0;}
void* WINAPI ReqQryOptionInstrCommRate(CThostFtdcTraderApi *api ,CThostFtdcQryOptionInstrCommRateField *pQryOptionInstrCommRate, int nRequestID){api->ReqQryOptionInstrCommRate(pQryOptionInstrCommRate,nRequestID); return 0;}
void* WINAPI ReqQryBrokerTradingAlgos(CThostFtdcTraderApi *api ,CThostFtdcQryBrokerTradingAlgosField *pQryBrokerTradingAlgos, int nRequestID){api->ReqQryBrokerTradingAlgos(pQryBrokerTradingAlgos,nRequestID); return 0;}
void* WINAPI ReqQryOrder(CThostFtdcTraderApi *api ,CThostFtdcQryOrderField *pQryOrder, int nRequestID){api->ReqQryOrder(pQryOrder,nRequestID); return 0;}
void* WINAPI ReqQryParkedOrder(CThostFtdcTraderApi *api ,CThostFtdcQryParkedOrderField *pQryParkedOrder, int nRequestID){api->ReqQryParkedOrder(pQryParkedOrder,nRequestID); return 0;}
void* WINAPI ReqQryExchangeMarginRateAdjust(CThostFtdcTraderApi *api ,CThostFtdcQryExchangeMarginRateAdjustField *pQryExchangeMarginRateAdjust, int nRequestID){api->ReqQryExchangeMarginRateAdjust(pQryExchangeMarginRateAdjust,nRequestID); return 0;}
void* WINAPI ReqQuoteAction(CThostFtdcTraderApi *api ,CThostFtdcInputQuoteActionField *pInputQuoteAction, int nRequestID){api->ReqQuoteAction(pInputQuoteAction,nRequestID); return 0;}
void* WINAPI ReqFromFutureToBankByFuture(CThostFtdcTraderApi *api ,CThostFtdcReqTransferField *pReqTransfer, int nRequestID){api->ReqFromFutureToBankByFuture(pReqTransfer,nRequestID); return 0;}
void* WINAPI ReqQryExecFreeze(CThostFtdcTraderApi *api ,CThostFtdcQryExecFreezeField *pQryExecFreeze, int nRequestID){api->ReqQryExecFreeze(pQryExecFreeze,nRequestID); return 0;}
void* WINAPI RegisterSpi(CThostFtdcTraderApi *api ,CThostFtdcTraderSpi *pSpi){api->RegisterSpi(pSpi); return 0;}
void* WINAPI ReqOrderInsert(CThostFtdcTraderApi *api ,CThostFtdcInputOrderField *pInputOrder, int nRequestID){api->ReqOrderInsert(pInputOrder,nRequestID); return 0;}
void* WINAPI ReqQuoteInsert(CThostFtdcTraderApi *api ,CThostFtdcInputQuoteField *pInputQuote, int nRequestID){api->ReqQuoteInsert(pInputQuote,nRequestID); return 0;}
void* WINAPI SubscribePublicTopic(CThostFtdcTraderApi *api ,THOST_TE_RESUME_TYPE nResumeType){api->SubscribePublicTopic(nResumeType); return 0;}
void* WINAPI ReqQryOptionInstrTradeCost(CThostFtdcTraderApi *api ,CThostFtdcQryOptionInstrTradeCostField *pQryOptionInstrTradeCost, int nRequestID){api->ReqQryOptionInstrTradeCost(pQryOptionInstrTradeCost,nRequestID); return 0;}
void* WINAPI ReqLockInsert(CThostFtdcTraderApi *api ,CThostFtdcInputLockField *pInputLock, int nRequestID){api->ReqLockInsert(pInputLock,nRequestID); return 0;}
void* WINAPI ReqQryInvestorPositionDetail(CThostFtdcTraderApi *api ,CThostFtdcQryInvestorPositionDetailField *pQryInvestorPositionDetail, int nRequestID){api->ReqQryInvestorPositionDetail(pQryInvestorPositionDetail,nRequestID); return 0;}
void* WINAPI ReqQrySettlementInfoConfirm(CThostFtdcTraderApi *api ,CThostFtdcQrySettlementInfoConfirmField *pQrySettlementInfoConfirm, int nRequestID){api->ReqQrySettlementInfoConfirm(pQrySettlementInfoConfirm,nRequestID); return 0;}
void* WINAPI ReqTradingAccountPasswordUpdate(CThostFtdcTraderApi *api ,CThostFtdcTradingAccountPasswordUpdateField *pTradingAccountPasswordUpdate, int nRequestID){api->ReqTradingAccountPasswordUpdate(pTradingAccountPasswordUpdate,nRequestID); return 0;}
void* WINAPI ReqQryInstrumentCommissionRate(CThostFtdcTraderApi *api ,CThostFtdcQryInstrumentCommissionRateField *pQryInstrumentCommissionRate, int nRequestID){api->ReqQryInstrumentCommissionRate(pQryInstrumentCommissionRate,nRequestID); return 0;}
void* WINAPI ReqQryTradingCode(CThostFtdcTraderApi *api ,CThostFtdcQryTradingCodeField *pQryTradingCode, int nRequestID){api->ReqQryTradingCode(pQryTradingCode,nRequestID); return 0;}
void* WINAPI ReqQryDepthMarketData(CThostFtdcTraderApi *api ,CThostFtdcQryDepthMarketDataField *pQryDepthMarketData, int nRequestID){api->ReqQryDepthMarketData(pQryDepthMarketData,nRequestID); return 0;}
void* WINAPI ReqQryInstrumentOrderCommRate(CThostFtdcTraderApi *api ,CThostFtdcQryInstrumentOrderCommRateField *pQryInstrumentOrderCommRate, int nRequestID){api->ReqQryInstrumentOrderCommRate(pQryInstrumentOrderCommRate,nRequestID); return 0;}
void* WINAPI ReqUserPasswordUpdate(CThostFtdcTraderApi *api ,CThostFtdcUserPasswordUpdateField *pUserPasswordUpdate, int nRequestID){api->ReqUserPasswordUpdate(pUserPasswordUpdate,nRequestID); return 0;}
void* WINAPI ReqQryBrokerTradingParams(CThostFtdcTraderApi *api ,CThostFtdcQryBrokerTradingParamsField *pQryBrokerTradingParams, int nRequestID){api->ReqQryBrokerTradingParams(pQryBrokerTradingParams,nRequestID); return 0;}
void* WINAPI ReqRemoveParkedOrderAction(CThostFtdcTraderApi *api ,CThostFtdcRemoveParkedOrderActionField *pRemoveParkedOrderAction, int nRequestID){api->ReqRemoveParkedOrderAction(pRemoveParkedOrderAction,nRequestID); return 0;}
void* WINAPI ReqQryCombInstrumentGuard(CThostFtdcTraderApi *api ,CThostFtdcQryCombInstrumentGuardField *pQryCombInstrumentGuard, int nRequestID){api->ReqQryCombInstrumentGuard(pQryCombInstrumentGuard,nRequestID); return 0;}
void* WINAPI ReqUserLogin(CThostFtdcTraderApi *api ,CThostFtdcReqUserLoginField *pReqUserLoginField, int nRequestID){api->ReqUserLogin(pReqUserLoginField,nRequestID); return 0;}
void* WINAPI RegisterFront(CThostFtdcTraderApi *api ,char *pszFrontAddress){api->RegisterFront(pszFrontAddress); return 0;}
void* WINAPI ReqQryMMInstrumentCommissionRate(CThostFtdcTraderApi *api ,CThostFtdcQryMMInstrumentCommissionRateField *pQryMMInstrumentCommissionRate, int nRequestID){api->ReqQryMMInstrumentCommissionRate(pQryMMInstrumentCommissionRate,nRequestID); return 0;}
void* WINAPI ReqQryTransferBank(CThostFtdcTraderApi *api ,CThostFtdcQryTransferBankField *pQryTransferBank, int nRequestID){api->ReqQryTransferBank(pQryTransferBank,nRequestID); return 0;}
void* WINAPI Join(CThostFtdcTraderApi *api ){api->Join(); return 0;}
void* WINAPI ReqQueryMaxOrderVolume(CThostFtdcTraderApi *api ,CThostFtdcQueryMaxOrderVolumeField *pQueryMaxOrderVolume, int nRequestID){api->ReqQueryMaxOrderVolume(pQueryMaxOrderVolume,nRequestID); return 0;}
void* WINAPI ReqFromBankToFutureByFuture(CThostFtdcTraderApi *api ,CThostFtdcReqTransferField *pReqTransfer, int nRequestID){api->ReqFromBankToFutureByFuture(pReqTransfer,nRequestID); return 0;}
void* WINAPI ReqQryForQuote(CThostFtdcTraderApi *api ,CThostFtdcQryForQuoteField *pQryForQuote, int nRequestID){api->ReqQryForQuote(pQryForQuote,nRequestID); return 0;}
