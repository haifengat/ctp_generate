
#pragma once
#define DllExport __declspec(dllexport)
#define WINAPI      __stdcall
#define WIN32_LEAN_AND_MEAN             //  从 Windows 头文件中排除极少使用的信息

#include "stddef.h"
#include <string.h>

#include "../ctp_20160628/ThostFtdcTraderApi.h"
#pragma comment(lib, "../ctp_20160628/thosttraderapi.lib")

class Trade: CThostFtdcTraderSpi
{
public:
	Trade(void);
	~Trade(void);
	//针对收到空反馈的处理
	CThostFtdcRspInfoField rif;
	CThostFtdcRspInfoField* repare(CThostFtdcRspInfoField *pRspInfo)
	{
		if (pRspInfo == NULL)
		{
			memset(&rif, 0, sizeof(rif));
			return &rif;
		}
		else
			return pRspInfo;
	}
	typedef int (WINAPI *RtnRepealFromFutureToBankByFutureManual)(CThostFtdcRspRepealField *pRspRepeal);
	typedef int (WINAPI *ErrRtnExecOrderAction)(CThostFtdcExecOrderActionField *pExecOrderAction, CThostFtdcRspInfoField *pRspInfo);
	typedef int (WINAPI *HeartBeatWarning)(int nTimeLapse);
	typedef int (WINAPI *RspQryBrokerTradingAlgos)(CThostFtdcBrokerTradingAlgosField *pBrokerTradingAlgos, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	typedef int (WINAPI *RspQryExecOrder)(CThostFtdcExecOrderField *pExecOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	typedef int (WINAPI *RtnCFMMCTradingAccountToken)(CThostFtdcCFMMCTradingAccountTokenField *pCFMMCTradingAccountToken);
	typedef int (WINAPI *RspQryCombAction)(CThostFtdcCombActionField *pCombAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	typedef int (WINAPI *RtnRepealFromFutureToBankByBank)(CThostFtdcRspRepealField *pRspRepeal);
	typedef int (WINAPI *RspQryContractBank)(CThostFtdcContractBankField *pContractBank, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	typedef int (WINAPI *ErrRtnOrderInsert)(CThostFtdcInputOrderField *pInputOrder, CThostFtdcRspInfoField *pRspInfo);
	typedef int (WINAPI *RspQryInvestorPositionCombineDetail)(CThostFtdcInvestorPositionCombineDetailField *pInvestorPositionCombineDetail, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	typedef int (WINAPI *RspQryExecFreeze)(CThostFtdcExecFreezeField *pExecFreeze, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	typedef int (WINAPI *RspTradingAccountPasswordUpdate)(CThostFtdcTradingAccountPasswordUpdateField *pTradingAccountPasswordUpdate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	typedef int (WINAPI *RtnErrorConditionalOrder)(CThostFtdcErrorConditionalOrderField *pErrorConditionalOrder);
	typedef int (WINAPI *RspQryInvestorProductGroupMargin)(CThostFtdcInvestorProductGroupMarginField *pInvestorProductGroupMargin, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	typedef int (WINAPI *RspQryMMOptionInstrCommRate)(CThostFtdcMMOptionInstrCommRateField *pMMOptionInstrCommRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	typedef int (WINAPI *ErrRtnQueryBankBalanceByFuture)(CThostFtdcReqQueryAccountField *pReqQueryAccount, CThostFtdcRspInfoField *pRspInfo);
	typedef int (WINAPI *RspQryParkedOrderAction)(CThostFtdcParkedOrderActionField *pParkedOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	typedef int (WINAPI *RspQryTransferBank)(CThostFtdcTransferBankField *pTransferBank, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	typedef int (WINAPI *RtnOrder)(CThostFtdcOrderField *pOrder);
	typedef int (WINAPI *RspQryProductGroup)(CThostFtdcProductGroupField *pProductGroup, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	typedef int (WINAPI *ErrRtnCombActionInsert)(CThostFtdcInputCombActionField *pInputCombAction, CThostFtdcRspInfoField *pRspInfo);
	typedef int (WINAPI *RtnFromFutureToBankByBank)(CThostFtdcRspTransferField *pRspTransfer);
	typedef int (WINAPI *RspRemoveParkedOrderAction)(CThostFtdcRemoveParkedOrderActionField *pRemoveParkedOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	typedef int (WINAPI *ErrRtnRepealFutureToBankByFutureManual)(CThostFtdcReqRepealField *pReqRepeal, CThostFtdcRspInfoField *pRspInfo);
	typedef int (WINAPI *RtnExecOrder)(CThostFtdcExecOrderField *pExecOrder);
	typedef int (WINAPI *ErrRtnRepealBankToFutureByFutureManual)(CThostFtdcReqRepealField *pReqRepeal, CThostFtdcRspInfoField *pRspInfo);
	typedef int (WINAPI *RspLockInsert)(CThostFtdcInputLockField *pInputLock, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	typedef int (WINAPI *RtnQueryBankBalanceByFuture)(CThostFtdcNotifyQueryAccountField *pNotifyQueryAccount);
	typedef int (WINAPI *ErrRtnQuoteInsert)(CThostFtdcInputQuoteField *pInputQuote, CThostFtdcRspInfoField *pRspInfo);
	typedef int (WINAPI *ErrRtnExecOrderInsert)(CThostFtdcInputExecOrderField *pInputExecOrder, CThostFtdcRspInfoField *pRspInfo);
	typedef int (WINAPI *RtnTrade)(CThostFtdcTradeField *pTrade);
	typedef int (WINAPI *RspFromBankToFutureByFuture)(CThostFtdcReqTransferField *pReqTransfer, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	typedef int (WINAPI *RspExecOrderInsert)(CThostFtdcInputExecOrderField *pInputExecOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	typedef int (WINAPI *RspForQuoteInsert)(CThostFtdcInputForQuoteField *pInputForQuote, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	typedef int (WINAPI *RtnRepealFromFutureToBankByFuture)(CThostFtdcRspRepealField *pRspRepeal);
	typedef int (WINAPI *RspQryCFMMCTradingAccountKey)(CThostFtdcCFMMCTradingAccountKeyField *pCFMMCTradingAccountKey, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	typedef int (WINAPI *RspQryCombInstrumentGuard)(CThostFtdcCombInstrumentGuardField *pCombInstrumentGuard, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	typedef int (WINAPI *RspQryDepthMarketData)(CThostFtdcDepthMarketDataField *pDepthMarketData, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	typedef int (WINAPI *RspQrySecAgentACIDMap)(CThostFtdcSecAgentACIDMapField *pSecAgentACIDMap, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	typedef int (WINAPI *RtnCombAction)(CThostFtdcCombActionField *pCombAction);
	typedef int (WINAPI *RspUserLogin)(CThostFtdcRspUserLoginField *pRspUserLogin, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	typedef int (WINAPI *RspSettlementInfoConfirm)(CThostFtdcSettlementInfoConfirmField *pSettlementInfoConfirm, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	typedef int (WINAPI *RtnInstrumentStatus)(CThostFtdcInstrumentStatusField *pInstrumentStatus);
	typedef int (WINAPI *RspQryTransferSerial)(CThostFtdcTransferSerialField *pTransferSerial, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	typedef int (WINAPI *RspExecOrderAction)(CThostFtdcInputExecOrderActionField *pInputExecOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	typedef int (WINAPI *RtnRepealFromBankToFutureByFutureManual)(CThostFtdcRspRepealField *pRspRepeal);
	typedef int (WINAPI *RspQryTradingNotice)(CThostFtdcTradingNoticeField *pTradingNotice, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	typedef int (WINAPI *RspQryTrade)(CThostFtdcTradeField *pTrade, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	typedef int (WINAPI *RspQueryMaxOrderVolume)(CThostFtdcQueryMaxOrderVolumeField *pQueryMaxOrderVolume, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	typedef int (WINAPI *RspQueryBankAccountMoneyByFuture)(CThostFtdcReqQueryAccountField *pReqQueryAccount, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	typedef int (WINAPI *RtnFromFutureToBankByFuture)(CThostFtdcRspTransferField *pRspTransfer);
	typedef int (WINAPI *ErrRtnQuoteAction)(CThostFtdcQuoteActionField *pQuoteAction, CThostFtdcRspInfoField *pRspInfo);
	typedef int (WINAPI *RtnCancelAccountByBank)(CThostFtdcCancelAccountField *pCancelAccount);
	typedef int (WINAPI *RspQryLock)(CThostFtdcLockField *pLock, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	typedef int (WINAPI *RspCombActionInsert)(CThostFtdcInputCombActionField *pInputCombAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	typedef int (WINAPI *RspQryParkedOrder)(CThostFtdcParkedOrderField *pParkedOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	typedef int (WINAPI *RspQryBrokerTradingParams)(CThostFtdcBrokerTradingParamsField *pBrokerTradingParams, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	typedef int (WINAPI *ErrRtnBankToFutureByFuture)(CThostFtdcReqTransferField *pReqTransfer, CThostFtdcRspInfoField *pRspInfo);
	typedef int (WINAPI *RspQryInstrumentCommissionRate)(CThostFtdcInstrumentCommissionRateField *pInstrumentCommissionRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	typedef int (WINAPI *RspQryInstrumentOrderCommRate)(CThostFtdcInstrumentOrderCommRateField *pInstrumentOrderCommRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	typedef int (WINAPI *RtnRepealFromBankToFutureByFuture)(CThostFtdcRspRepealField *pRspRepeal);
	typedef int (WINAPI *RspQryETFOptionInstrCommRate)(CThostFtdcETFOptionInstrCommRateField *pETFOptionInstrCommRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	typedef int (WINAPI *RspParkedOrderInsert)(CThostFtdcParkedOrderField *pParkedOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	typedef int (WINAPI *RspQuoteAction)(CThostFtdcInputQuoteActionField *pInputQuoteAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	typedef int (WINAPI *RspQryInstrument)(CThostFtdcInstrumentField *pInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	typedef int (WINAPI *RspUserPasswordUpdate)(CThostFtdcUserPasswordUpdateField *pUserPasswordUpdate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	typedef int (WINAPI *RspParkedOrderAction)(CThostFtdcParkedOrderActionField *pParkedOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	typedef int (WINAPI *RspQryEWarrantOffset)(CThostFtdcEWarrantOffsetField *pEWarrantOffset, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	typedef int (WINAPI *RspAuthenticate)(CThostFtdcRspAuthenticateField *pRspAuthenticateField, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	typedef int (WINAPI *RspFromFutureToBankByFuture)(CThostFtdcReqTransferField *pReqTransfer, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	typedef int (WINAPI *FrontConnected)();
	typedef int (WINAPI *RspQryInvestor)(CThostFtdcInvestorField *pInvestor, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	typedef int (WINAPI *RspQryForQuote)(CThostFtdcForQuoteField *pForQuote, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	typedef int (WINAPI *RspQryAccountregister)(CThostFtdcAccountregisterField *pAccountregister, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	typedef int (WINAPI *RspQryTradingCode)(CThostFtdcTradingCodeField *pTradingCode, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	typedef int (WINAPI *RspQryQuote)(CThostFtdcQuoteField *pQuote, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	typedef int (WINAPI *ErrRtnLockInsert)(CThostFtdcInputLockField *pInputLock, CThostFtdcRspInfoField *pRspInfo);
	typedef int (WINAPI *RspQryOptionInstrTradeCost)(CThostFtdcOptionInstrTradeCostField *pOptionInstrTradeCost, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	typedef int (WINAPI *RspQryOrder)(CThostFtdcOrderField *pOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	typedef int (WINAPI *RspQryTradingAccount)(CThostFtdcTradingAccountField *pTradingAccount, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	typedef int (WINAPI *RspError)(CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	typedef int (WINAPI *RspQryExchangeMarginRate)(CThostFtdcExchangeMarginRateField *pExchangeMarginRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	typedef int (WINAPI *RspQryExchangeMarginRateAdjust)(CThostFtdcExchangeMarginRateAdjustField *pExchangeMarginRateAdjust, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	typedef int (WINAPI *FrontDisconnected)(int nReason);
	typedef int (WINAPI *RspQryExchangeRate)(CThostFtdcExchangeRateField *pExchangeRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	typedef int (WINAPI *RspQrySettlementInfoConfirm)(CThostFtdcSettlementInfoConfirmField *pSettlementInfoConfirm, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	typedef int (WINAPI *RspQueryCFMMCTradingAccountToken)(CThostFtdcQueryCFMMCTradingAccountTokenField *pQueryCFMMCTradingAccountToken, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	typedef int (WINAPI *RspQuoteInsert)(CThostFtdcInputQuoteField *pInputQuote, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	typedef int (WINAPI *RspQryOptionInstrCommRate)(CThostFtdcOptionInstrCommRateField *pOptionInstrCommRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	typedef int (WINAPI *RtnBulletin)(CThostFtdcBulletinField *pBulletin);
	typedef int (WINAPI *RtnQuote)(CThostFtdcQuoteField *pQuote);
	typedef int (WINAPI *RspQryProduct)(CThostFtdcProductField *pProduct, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	typedef int (WINAPI *RtnRepealFromBankToFutureByBank)(CThostFtdcRspRepealField *pRspRepeal);
	typedef int (WINAPI *RspOrderInsert)(CThostFtdcInputOrderField *pInputOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	typedef int (WINAPI *RtnFromBankToFutureByFuture)(CThostFtdcRspTransferField *pRspTransfer);
	typedef int (WINAPI *RtnOpenAccountByBank)(CThostFtdcOpenAccountField *pOpenAccount);
	typedef int (WINAPI *RspBatchOrderAction)(CThostFtdcInputBatchOrderActionField *pInputBatchOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	typedef int (WINAPI *ErrRtnBatchOrderAction)(CThostFtdcBatchOrderActionField *pBatchOrderAction, CThostFtdcRspInfoField *pRspInfo);
	typedef int (WINAPI *RtnFromBankToFutureByBank)(CThostFtdcRspTransferField *pRspTransfer);
	typedef int (WINAPI *RspRemoveParkedOrder)(CThostFtdcRemoveParkedOrderField *pRemoveParkedOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	typedef int (WINAPI *ErrRtnOrderAction)(CThostFtdcOrderActionField *pOrderAction, CThostFtdcRspInfoField *pRspInfo);
	typedef int (WINAPI *RspQryLockPosition)(CThostFtdcLockPositionField *pLockPosition, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	typedef int (WINAPI *RspQryNotice)(CThostFtdcNoticeField *pNotice, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	typedef int (WINAPI *RspQryInvestorLevel)(CThostFtdcInvestorLevelField *pInvestorLevel, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	typedef int (WINAPI *RspQryMMInstrumentCommissionRate)(CThostFtdcMMInstrumentCommissionRateField *pMMInstrumentCommissionRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	typedef int (WINAPI *RspQryExchange)(CThostFtdcExchangeField *pExchange, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	typedef int (WINAPI *RspUserLogout)(CThostFtdcUserLogoutField *pUserLogout, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	typedef int (WINAPI *RtnTradingNotice)(CThostFtdcTradingNoticeInfoField *pTradingNoticeInfo);
	typedef int (WINAPI *RspQrySettlementInfo)(CThostFtdcSettlementInfoField *pSettlementInfo, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	typedef int (WINAPI *RspQryInvestorPosition)(CThostFtdcInvestorPositionField *pInvestorPosition, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	typedef int (WINAPI *ErrRtnFutureToBankByFuture)(CThostFtdcReqTransferField *pReqTransfer, CThostFtdcRspInfoField *pRspInfo);
	typedef int (WINAPI *ErrRtnForQuoteInsert)(CThostFtdcInputForQuoteField *pInputForQuote, CThostFtdcRspInfoField *pRspInfo);
	typedef int (WINAPI *RspQryProductExchRate)(CThostFtdcProductExchRateField *pProductExchRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	typedef int (WINAPI *RtnChangeAccountByBank)(CThostFtdcChangeAccountField *pChangeAccount);
	typedef int (WINAPI *RspQryInvestorPositionDetail)(CThostFtdcInvestorPositionDetailField *pInvestorPositionDetail, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	typedef int (WINAPI *RspOrderAction)(CThostFtdcInputOrderActionField *pInputOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	typedef int (WINAPI *RtnLock)(CThostFtdcLockField *pLock);
	typedef int (WINAPI *RtnForQuoteRsp)(CThostFtdcForQuoteRspField *pForQuoteRsp);
	typedef int (WINAPI *RspQryInstrumentMarginRate)(CThostFtdcInstrumentMarginRateField *pInstrumentMarginRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);

	void *_RtnRepealFromFutureToBankByFutureManual;
	void *_ErrRtnExecOrderAction;
	void *_HeartBeatWarning;
	void *_RspQryBrokerTradingAlgos;
	void *_RspQryExecOrder;
	void *_RtnCFMMCTradingAccountToken;
	void *_RspQryCombAction;
	void *_RtnRepealFromFutureToBankByBank;
	void *_RspQryContractBank;
	void *_ErrRtnOrderInsert;
	void *_RspQryInvestorPositionCombineDetail;
	void *_RspQryExecFreeze;
	void *_RspTradingAccountPasswordUpdate;
	void *_RtnErrorConditionalOrder;
	void *_RspQryInvestorProductGroupMargin;
	void *_RspQryMMOptionInstrCommRate;
	void *_ErrRtnQueryBankBalanceByFuture;
	void *_RspQryParkedOrderAction;
	void *_RspQryTransferBank;
	void *_RtnOrder;
	void *_RspQryProductGroup;
	void *_ErrRtnCombActionInsert;
	void *_RtnFromFutureToBankByBank;
	void *_RspRemoveParkedOrderAction;
	void *_ErrRtnRepealFutureToBankByFutureManual;
	void *_RtnExecOrder;
	void *_ErrRtnRepealBankToFutureByFutureManual;
	void *_RspLockInsert;
	void *_RtnQueryBankBalanceByFuture;
	void *_ErrRtnQuoteInsert;
	void *_ErrRtnExecOrderInsert;
	void *_RtnTrade;
	void *_RspFromBankToFutureByFuture;
	void *_RspExecOrderInsert;
	void *_RspForQuoteInsert;
	void *_RtnRepealFromFutureToBankByFuture;
	void *_RspQryCFMMCTradingAccountKey;
	void *_RspQryCombInstrumentGuard;
	void *_RspQryDepthMarketData;
	void *_RspQrySecAgentACIDMap;
	void *_RtnCombAction;
	void *_RspUserLogin;
	void *_RspSettlementInfoConfirm;
	void *_RtnInstrumentStatus;
	void *_RspQryTransferSerial;
	void *_RspExecOrderAction;
	void *_RtnRepealFromBankToFutureByFutureManual;
	void *_RspQryTradingNotice;
	void *_RspQryTrade;
	void *_RspQueryMaxOrderVolume;
	void *_RspQueryBankAccountMoneyByFuture;
	void *_RtnFromFutureToBankByFuture;
	void *_ErrRtnQuoteAction;
	void *_RtnCancelAccountByBank;
	void *_RspQryLock;
	void *_RspCombActionInsert;
	void *_RspQryParkedOrder;
	void *_RspQryBrokerTradingParams;
	void *_ErrRtnBankToFutureByFuture;
	void *_RspQryInstrumentCommissionRate;
	void *_RspQryInstrumentOrderCommRate;
	void *_RtnRepealFromBankToFutureByFuture;
	void *_RspQryETFOptionInstrCommRate;
	void *_RspParkedOrderInsert;
	void *_RspQuoteAction;
	void *_RspQryInstrument;
	void *_RspUserPasswordUpdate;
	void *_RspParkedOrderAction;
	void *_RspQryEWarrantOffset;
	void *_RspAuthenticate;
	void *_RspFromFutureToBankByFuture;
	void *_FrontConnected;
	void *_RspQryInvestor;
	void *_RspQryForQuote;
	void *_RspQryAccountregister;
	void *_RspQryTradingCode;
	void *_RspQryQuote;
	void *_ErrRtnLockInsert;
	void *_RspQryOptionInstrTradeCost;
	void *_RspQryOrder;
	void *_RspQryTradingAccount;
	void *_RspError;
	void *_RspQryExchangeMarginRate;
	void *_RspQryExchangeMarginRateAdjust;
	void *_FrontDisconnected;
	void *_RspQryExchangeRate;
	void *_RspQrySettlementInfoConfirm;
	void *_RspQueryCFMMCTradingAccountToken;
	void *_RspQuoteInsert;
	void *_RspQryOptionInstrCommRate;
	void *_RtnBulletin;
	void *_RtnQuote;
	void *_RspQryProduct;
	void *_RtnRepealFromBankToFutureByBank;
	void *_RspOrderInsert;
	void *_RtnFromBankToFutureByFuture;
	void *_RtnOpenAccountByBank;
	void *_RspBatchOrderAction;
	void *_ErrRtnBatchOrderAction;
	void *_RtnFromBankToFutureByBank;
	void *_RspRemoveParkedOrder;
	void *_ErrRtnOrderAction;
	void *_RspQryLockPosition;
	void *_RspQryNotice;
	void *_RspQryInvestorLevel;
	void *_RspQryMMInstrumentCommissionRate;
	void *_RspQryExchange;
	void *_RspUserLogout;
	void *_RtnTradingNotice;
	void *_RspQrySettlementInfo;
	void *_RspQryInvestorPosition;
	void *_ErrRtnFutureToBankByFuture;
	void *_ErrRtnForQuoteInsert;
	void *_RspQryProductExchRate;
	void *_RtnChangeAccountByBank;
	void *_RspQryInvestorPositionDetail;
	void *_RspOrderAction;
	void *_RtnLock;
	void *_RtnForQuoteRsp;
	void *_RspQryInstrumentMarginRate;

virtual void OnRtnRepealFromFutureToBankByFutureManual (CThostFtdcRspRepealField *pRspRepeal)
{
	if (_RtnRepealFromFutureToBankByFutureManual) ((RtnRepealFromFutureToBankByFutureManual)_RtnRepealFromFutureToBankByFutureManual)(pRspRepeal);
}
virtual void OnErrRtnExecOrderAction (CThostFtdcExecOrderActionField *pExecOrderAction, CThostFtdcRspInfoField *pRspInfo)
{
	if (_ErrRtnExecOrderAction) ((ErrRtnExecOrderAction)_ErrRtnExecOrderAction)(pExecOrderAction, pRspInfo);
}
virtual void OnHeartBeatWarning (int nTimeLapse) {if (_HeartBeatWarning) ((HeartBeatWarning)_HeartBeatWarning)(nTimeLapse);}
virtual void OnRspQryBrokerTradingAlgos (CThostFtdcBrokerTradingAlgosField *pBrokerTradingAlgos, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
	if (_RspQryBrokerTradingAlgos)
				{
					if (pBrokerTradingAlgos)
						((RspQryBrokerTradingAlgos)_RspQryBrokerTradingAlgos)(pBrokerTradingAlgos, repare(pRspInfo), nRequestID, bIsLast);
					else
					{
						CThostFtdcBrokerTradingAlgosField f; memset(&f, 0, sizeof(f));
						((RspQryBrokerTradingAlgos)_RspQryBrokerTradingAlgos)(&f, repare(pRspInfo), nRequestID, bIsLast);
					}
				}
}
virtual void OnRspQryExecOrder (CThostFtdcExecOrderField *pExecOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
	if (_RspQryExecOrder)
				{
					if (pExecOrder)
						((RspQryExecOrder)_RspQryExecOrder)(pExecOrder, repare(pRspInfo), nRequestID, bIsLast);
					else
					{
						CThostFtdcExecOrderField f; memset(&f, 0, sizeof(f));
						((RspQryExecOrder)_RspQryExecOrder)(&f, repare(pRspInfo), nRequestID, bIsLast);
					}
				}
}
virtual void OnRtnCFMMCTradingAccountToken (CThostFtdcCFMMCTradingAccountTokenField *pCFMMCTradingAccountToken)
{
	if (_RtnCFMMCTradingAccountToken) ((RtnCFMMCTradingAccountToken)_RtnCFMMCTradingAccountToken)(pCFMMCTradingAccountToken);
}
virtual void OnRspQryCombAction (CThostFtdcCombActionField *pCombAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
	if (_RspQryCombAction)
				{
					if (pCombAction)
						((RspQryCombAction)_RspQryCombAction)(pCombAction, repare(pRspInfo), nRequestID, bIsLast);
					else
					{
						CThostFtdcCombActionField f; memset(&f, 0, sizeof(f));
						((RspQryCombAction)_RspQryCombAction)(&f, repare(pRspInfo), nRequestID, bIsLast);
					}
				}
}
virtual void OnRtnRepealFromFutureToBankByBank (CThostFtdcRspRepealField *pRspRepeal)
{
	if (_RtnRepealFromFutureToBankByBank) ((RtnRepealFromFutureToBankByBank)_RtnRepealFromFutureToBankByBank)(pRspRepeal);
}
virtual void OnRspQryContractBank (CThostFtdcContractBankField *pContractBank, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
	if (_RspQryContractBank)
				{
					if (pContractBank)
						((RspQryContractBank)_RspQryContractBank)(pContractBank, repare(pRspInfo), nRequestID, bIsLast);
					else
					{
						CThostFtdcContractBankField f; memset(&f, 0, sizeof(f));
						((RspQryContractBank)_RspQryContractBank)(&f, repare(pRspInfo), nRequestID, bIsLast);
					}
				}
}
virtual void OnErrRtnOrderInsert (CThostFtdcInputOrderField *pInputOrder, CThostFtdcRspInfoField *pRspInfo)
{
	if (_ErrRtnOrderInsert) ((ErrRtnOrderInsert)_ErrRtnOrderInsert)(pInputOrder, pRspInfo);
}
virtual void OnRspQryInvestorPositionCombineDetail (CThostFtdcInvestorPositionCombineDetailField *pInvestorPositionCombineDetail, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
	if (_RspQryInvestorPositionCombineDetail)
				{
					if (pInvestorPositionCombineDetail)
						((RspQryInvestorPositionCombineDetail)_RspQryInvestorPositionCombineDetail)(pInvestorPositionCombineDetail, repare(pRspInfo), nRequestID, bIsLast);
					else
					{
						CThostFtdcInvestorPositionCombineDetailField f; memset(&f, 0, sizeof(f));
						((RspQryInvestorPositionCombineDetail)_RspQryInvestorPositionCombineDetail)(&f, repare(pRspInfo), nRequestID, bIsLast);
					}
				}
}
virtual void OnRspQryExecFreeze (CThostFtdcExecFreezeField *pExecFreeze, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
	if (_RspQryExecFreeze)
				{
					if (pExecFreeze)
						((RspQryExecFreeze)_RspQryExecFreeze)(pExecFreeze, repare(pRspInfo), nRequestID, bIsLast);
					else
					{
						CThostFtdcExecFreezeField f; memset(&f, 0, sizeof(f));
						((RspQryExecFreeze)_RspQryExecFreeze)(&f, repare(pRspInfo), nRequestID, bIsLast);
					}
				}
}
virtual void OnRspTradingAccountPasswordUpdate (CThostFtdcTradingAccountPasswordUpdateField *pTradingAccountPasswordUpdate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
	if (_RspTradingAccountPasswordUpdate)
				{
					if (pTradingAccountPasswordUpdate)
						((RspTradingAccountPasswordUpdate)_RspTradingAccountPasswordUpdate)(pTradingAccountPasswordUpdate, repare(pRspInfo), nRequestID, bIsLast);
					else
					{
						CThostFtdcTradingAccountPasswordUpdateField f; memset(&f, 0, sizeof(f));
						((RspTradingAccountPasswordUpdate)_RspTradingAccountPasswordUpdate)(&f, repare(pRspInfo), nRequestID, bIsLast);
					}
				}
}
virtual void OnRtnErrorConditionalOrder (CThostFtdcErrorConditionalOrderField *pErrorConditionalOrder)
{
	if (_RtnErrorConditionalOrder) ((RtnErrorConditionalOrder)_RtnErrorConditionalOrder)(pErrorConditionalOrder);
}
virtual void OnRspQryInvestorProductGroupMargin (CThostFtdcInvestorProductGroupMarginField *pInvestorProductGroupMargin, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
	if (_RspQryInvestorProductGroupMargin)
				{
					if (pInvestorProductGroupMargin)
						((RspQryInvestorProductGroupMargin)_RspQryInvestorProductGroupMargin)(pInvestorProductGroupMargin, repare(pRspInfo), nRequestID, bIsLast);
					else
					{
						CThostFtdcInvestorProductGroupMarginField f; memset(&f, 0, sizeof(f));
						((RspQryInvestorProductGroupMargin)_RspQryInvestorProductGroupMargin)(&f, repare(pRspInfo), nRequestID, bIsLast);
					}
				}
}
virtual void OnRspQryMMOptionInstrCommRate (CThostFtdcMMOptionInstrCommRateField *pMMOptionInstrCommRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
	if (_RspQryMMOptionInstrCommRate)
				{
					if (pMMOptionInstrCommRate)
						((RspQryMMOptionInstrCommRate)_RspQryMMOptionInstrCommRate)(pMMOptionInstrCommRate, repare(pRspInfo), nRequestID, bIsLast);
					else
					{
						CThostFtdcMMOptionInstrCommRateField f; memset(&f, 0, sizeof(f));
						((RspQryMMOptionInstrCommRate)_RspQryMMOptionInstrCommRate)(&f, repare(pRspInfo), nRequestID, bIsLast);
					}
				}
}
virtual void OnErrRtnQueryBankBalanceByFuture (CThostFtdcReqQueryAccountField *pReqQueryAccount, CThostFtdcRspInfoField *pRspInfo)
{
	if (_ErrRtnQueryBankBalanceByFuture) ((ErrRtnQueryBankBalanceByFuture)_ErrRtnQueryBankBalanceByFuture)(pReqQueryAccount, pRspInfo);
}
virtual void OnRspQryParkedOrderAction (CThostFtdcParkedOrderActionField *pParkedOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
	if (_RspQryParkedOrderAction)
				{
					if (pParkedOrderAction)
						((RspQryParkedOrderAction)_RspQryParkedOrderAction)(pParkedOrderAction, repare(pRspInfo), nRequestID, bIsLast);
					else
					{
						CThostFtdcParkedOrderActionField f; memset(&f, 0, sizeof(f));
						((RspQryParkedOrderAction)_RspQryParkedOrderAction)(&f, repare(pRspInfo), nRequestID, bIsLast);
					}
				}
}
virtual void OnRspQryTransferBank (CThostFtdcTransferBankField *pTransferBank, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
	if (_RspQryTransferBank)
				{
					if (pTransferBank)
						((RspQryTransferBank)_RspQryTransferBank)(pTransferBank, repare(pRspInfo), nRequestID, bIsLast);
					else
					{
						CThostFtdcTransferBankField f; memset(&f, 0, sizeof(f));
						((RspQryTransferBank)_RspQryTransferBank)(&f, repare(pRspInfo), nRequestID, bIsLast);
					}
				}
}
virtual void OnRtnOrder (CThostFtdcOrderField *pOrder)
{
	if (_RtnOrder) ((RtnOrder)_RtnOrder)(pOrder);
}
virtual void OnRspQryProductGroup (CThostFtdcProductGroupField *pProductGroup, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
	if (_RspQryProductGroup)
				{
					if (pProductGroup)
						((RspQryProductGroup)_RspQryProductGroup)(pProductGroup, repare(pRspInfo), nRequestID, bIsLast);
					else
					{
						CThostFtdcProductGroupField f; memset(&f, 0, sizeof(f));
						((RspQryProductGroup)_RspQryProductGroup)(&f, repare(pRspInfo), nRequestID, bIsLast);
					}
				}
}
virtual void OnErrRtnCombActionInsert (CThostFtdcInputCombActionField *pInputCombAction, CThostFtdcRspInfoField *pRspInfo)
{
	if (_ErrRtnCombActionInsert) ((ErrRtnCombActionInsert)_ErrRtnCombActionInsert)(pInputCombAction, pRspInfo);
}
virtual void OnRtnFromFutureToBankByBank (CThostFtdcRspTransferField *pRspTransfer)
{
	if (_RtnFromFutureToBankByBank) ((RtnFromFutureToBankByBank)_RtnFromFutureToBankByBank)(pRspTransfer);
}
virtual void OnRspRemoveParkedOrderAction (CThostFtdcRemoveParkedOrderActionField *pRemoveParkedOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
	if (_RspRemoveParkedOrderAction)
				{
					if (pRemoveParkedOrderAction)
						((RspRemoveParkedOrderAction)_RspRemoveParkedOrderAction)(pRemoveParkedOrderAction, repare(pRspInfo), nRequestID, bIsLast);
					else
					{
						CThostFtdcRemoveParkedOrderActionField f; memset(&f, 0, sizeof(f));
						((RspRemoveParkedOrderAction)_RspRemoveParkedOrderAction)(&f, repare(pRspInfo), nRequestID, bIsLast);
					}
				}
}
virtual void OnErrRtnRepealFutureToBankByFutureManual (CThostFtdcReqRepealField *pReqRepeal, CThostFtdcRspInfoField *pRspInfo)
{
	if (_ErrRtnRepealFutureToBankByFutureManual) ((ErrRtnRepealFutureToBankByFutureManual)_ErrRtnRepealFutureToBankByFutureManual)(pReqRepeal, pRspInfo);
}
virtual void OnRtnExecOrder (CThostFtdcExecOrderField *pExecOrder)
{
	if (_RtnExecOrder) ((RtnExecOrder)_RtnExecOrder)(pExecOrder);
}
virtual void OnErrRtnRepealBankToFutureByFutureManual (CThostFtdcReqRepealField *pReqRepeal, CThostFtdcRspInfoField *pRspInfo)
{
	if (_ErrRtnRepealBankToFutureByFutureManual) ((ErrRtnRepealBankToFutureByFutureManual)_ErrRtnRepealBankToFutureByFutureManual)(pReqRepeal, pRspInfo);
}
virtual void OnRspLockInsert (CThostFtdcInputLockField *pInputLock, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
	if (_RspLockInsert)
				{
					if (pInputLock)
						((RspLockInsert)_RspLockInsert)(pInputLock, repare(pRspInfo), nRequestID, bIsLast);
					else
					{
						CThostFtdcInputLockField f; memset(&f, 0, sizeof(f));
						((RspLockInsert)_RspLockInsert)(&f, repare(pRspInfo), nRequestID, bIsLast);
					}
				}
}
virtual void OnRtnQueryBankBalanceByFuture (CThostFtdcNotifyQueryAccountField *pNotifyQueryAccount)
{
	if (_RtnQueryBankBalanceByFuture) ((RtnQueryBankBalanceByFuture)_RtnQueryBankBalanceByFuture)(pNotifyQueryAccount);
}
virtual void OnErrRtnQuoteInsert (CThostFtdcInputQuoteField *pInputQuote, CThostFtdcRspInfoField *pRspInfo)
{
	if (_ErrRtnQuoteInsert) ((ErrRtnQuoteInsert)_ErrRtnQuoteInsert)(pInputQuote, pRspInfo);
}
virtual void OnErrRtnExecOrderInsert (CThostFtdcInputExecOrderField *pInputExecOrder, CThostFtdcRspInfoField *pRspInfo)
{
	if (_ErrRtnExecOrderInsert) ((ErrRtnExecOrderInsert)_ErrRtnExecOrderInsert)(pInputExecOrder, pRspInfo);
}
virtual void OnRtnTrade (CThostFtdcTradeField *pTrade)
{
	if (_RtnTrade) ((RtnTrade)_RtnTrade)(pTrade);
}
virtual void OnRspFromBankToFutureByFuture (CThostFtdcReqTransferField *pReqTransfer, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
	if (_RspFromBankToFutureByFuture)
				{
					if (pReqTransfer)
						((RspFromBankToFutureByFuture)_RspFromBankToFutureByFuture)(pReqTransfer, repare(pRspInfo), nRequestID, bIsLast);
					else
					{
						CThostFtdcReqTransferField f; memset(&f, 0, sizeof(f));
						((RspFromBankToFutureByFuture)_RspFromBankToFutureByFuture)(&f, repare(pRspInfo), nRequestID, bIsLast);
					}
				}
}
virtual void OnRspExecOrderInsert (CThostFtdcInputExecOrderField *pInputExecOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
	if (_RspExecOrderInsert)
				{
					if (pInputExecOrder)
						((RspExecOrderInsert)_RspExecOrderInsert)(pInputExecOrder, repare(pRspInfo), nRequestID, bIsLast);
					else
					{
						CThostFtdcInputExecOrderField f; memset(&f, 0, sizeof(f));
						((RspExecOrderInsert)_RspExecOrderInsert)(&f, repare(pRspInfo), nRequestID, bIsLast);
					}
				}
}
virtual void OnRspForQuoteInsert (CThostFtdcInputForQuoteField *pInputForQuote, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
	if (_RspForQuoteInsert)
				{
					if (pInputForQuote)
						((RspForQuoteInsert)_RspForQuoteInsert)(pInputForQuote, repare(pRspInfo), nRequestID, bIsLast);
					else
					{
						CThostFtdcInputForQuoteField f; memset(&f, 0, sizeof(f));
						((RspForQuoteInsert)_RspForQuoteInsert)(&f, repare(pRspInfo), nRequestID, bIsLast);
					}
				}
}
virtual void OnRtnRepealFromFutureToBankByFuture (CThostFtdcRspRepealField *pRspRepeal)
{
	if (_RtnRepealFromFutureToBankByFuture) ((RtnRepealFromFutureToBankByFuture)_RtnRepealFromFutureToBankByFuture)(pRspRepeal);
}
virtual void OnRspQryCFMMCTradingAccountKey (CThostFtdcCFMMCTradingAccountKeyField *pCFMMCTradingAccountKey, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
	if (_RspQryCFMMCTradingAccountKey)
				{
					if (pCFMMCTradingAccountKey)
						((RspQryCFMMCTradingAccountKey)_RspQryCFMMCTradingAccountKey)(pCFMMCTradingAccountKey, repare(pRspInfo), nRequestID, bIsLast);
					else
					{
						CThostFtdcCFMMCTradingAccountKeyField f; memset(&f, 0, sizeof(f));
						((RspQryCFMMCTradingAccountKey)_RspQryCFMMCTradingAccountKey)(&f, repare(pRspInfo), nRequestID, bIsLast);
					}
				}
}
virtual void OnRspQryCombInstrumentGuard (CThostFtdcCombInstrumentGuardField *pCombInstrumentGuard, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
	if (_RspQryCombInstrumentGuard)
				{
					if (pCombInstrumentGuard)
						((RspQryCombInstrumentGuard)_RspQryCombInstrumentGuard)(pCombInstrumentGuard, repare(pRspInfo), nRequestID, bIsLast);
					else
					{
						CThostFtdcCombInstrumentGuardField f; memset(&f, 0, sizeof(f));
						((RspQryCombInstrumentGuard)_RspQryCombInstrumentGuard)(&f, repare(pRspInfo), nRequestID, bIsLast);
					}
				}
}
virtual void OnRspQryDepthMarketData (CThostFtdcDepthMarketDataField *pDepthMarketData, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
	if (_RspQryDepthMarketData)
				{
					if (pDepthMarketData)
						((RspQryDepthMarketData)_RspQryDepthMarketData)(pDepthMarketData, repare(pRspInfo), nRequestID, bIsLast);
					else
					{
						CThostFtdcDepthMarketDataField f; memset(&f, 0, sizeof(f));
						((RspQryDepthMarketData)_RspQryDepthMarketData)(&f, repare(pRspInfo), nRequestID, bIsLast);
					}
				}
}
virtual void OnRspQrySecAgentACIDMap (CThostFtdcSecAgentACIDMapField *pSecAgentACIDMap, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
	if (_RspQrySecAgentACIDMap)
				{
					if (pSecAgentACIDMap)
						((RspQrySecAgentACIDMap)_RspQrySecAgentACIDMap)(pSecAgentACIDMap, repare(pRspInfo), nRequestID, bIsLast);
					else
					{
						CThostFtdcSecAgentACIDMapField f; memset(&f, 0, sizeof(f));
						((RspQrySecAgentACIDMap)_RspQrySecAgentACIDMap)(&f, repare(pRspInfo), nRequestID, bIsLast);
					}
				}
}
virtual void OnRtnCombAction (CThostFtdcCombActionField *pCombAction)
{
	if (_RtnCombAction) ((RtnCombAction)_RtnCombAction)(pCombAction);
}
virtual void OnRspUserLogin (CThostFtdcRspUserLoginField *pRspUserLogin, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
	if (_RspUserLogin)
				{
					if (pRspUserLogin)
						((RspUserLogin)_RspUserLogin)(pRspUserLogin, repare(pRspInfo), nRequestID, bIsLast);
					else
					{
						CThostFtdcRspUserLoginField f; memset(&f, 0, sizeof(f));
						((RspUserLogin)_RspUserLogin)(&f, repare(pRspInfo), nRequestID, bIsLast);
					}
				}
}
virtual void OnRspSettlementInfoConfirm (CThostFtdcSettlementInfoConfirmField *pSettlementInfoConfirm, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
	if (_RspSettlementInfoConfirm)
				{
					if (pSettlementInfoConfirm)
						((RspSettlementInfoConfirm)_RspSettlementInfoConfirm)(pSettlementInfoConfirm, repare(pRspInfo), nRequestID, bIsLast);
					else
					{
						CThostFtdcSettlementInfoConfirmField f; memset(&f, 0, sizeof(f));
						((RspSettlementInfoConfirm)_RspSettlementInfoConfirm)(&f, repare(pRspInfo), nRequestID, bIsLast);
					}
				}
}
virtual void OnRtnInstrumentStatus (CThostFtdcInstrumentStatusField *pInstrumentStatus)
{
	if (_RtnInstrumentStatus) ((RtnInstrumentStatus)_RtnInstrumentStatus)(pInstrumentStatus);
}
virtual void OnRspQryTransferSerial (CThostFtdcTransferSerialField *pTransferSerial, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
	if (_RspQryTransferSerial)
				{
					if (pTransferSerial)
						((RspQryTransferSerial)_RspQryTransferSerial)(pTransferSerial, repare(pRspInfo), nRequestID, bIsLast);
					else
					{
						CThostFtdcTransferSerialField f; memset(&f, 0, sizeof(f));
						((RspQryTransferSerial)_RspQryTransferSerial)(&f, repare(pRspInfo), nRequestID, bIsLast);
					}
				}
}
virtual void OnRspExecOrderAction (CThostFtdcInputExecOrderActionField *pInputExecOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
	if (_RspExecOrderAction)
				{
					if (pInputExecOrderAction)
						((RspExecOrderAction)_RspExecOrderAction)(pInputExecOrderAction, repare(pRspInfo), nRequestID, bIsLast);
					else
					{
						CThostFtdcInputExecOrderActionField f; memset(&f, 0, sizeof(f));
						((RspExecOrderAction)_RspExecOrderAction)(&f, repare(pRspInfo), nRequestID, bIsLast);
					}
				}
}
virtual void OnRtnRepealFromBankToFutureByFutureManual (CThostFtdcRspRepealField *pRspRepeal)
{
	if (_RtnRepealFromBankToFutureByFutureManual) ((RtnRepealFromBankToFutureByFutureManual)_RtnRepealFromBankToFutureByFutureManual)(pRspRepeal);
}
virtual void OnRspQryTradingNotice (CThostFtdcTradingNoticeField *pTradingNotice, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
	if (_RspQryTradingNotice)
				{
					if (pTradingNotice)
						((RspQryTradingNotice)_RspQryTradingNotice)(pTradingNotice, repare(pRspInfo), nRequestID, bIsLast);
					else
					{
						CThostFtdcTradingNoticeField f; memset(&f, 0, sizeof(f));
						((RspQryTradingNotice)_RspQryTradingNotice)(&f, repare(pRspInfo), nRequestID, bIsLast);
					}
				}
}
virtual void OnRspQryTrade (CThostFtdcTradeField *pTrade, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
	if (_RspQryTrade)
				{
					if (pTrade)
						((RspQryTrade)_RspQryTrade)(pTrade, repare(pRspInfo), nRequestID, bIsLast);
					else
					{
						CThostFtdcTradeField f; memset(&f, 0, sizeof(f));
						((RspQryTrade)_RspQryTrade)(&f, repare(pRspInfo), nRequestID, bIsLast);
					}
				}
}
virtual void OnRspQueryMaxOrderVolume (CThostFtdcQueryMaxOrderVolumeField *pQueryMaxOrderVolume, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
	if (_RspQueryMaxOrderVolume)
				{
					if (pQueryMaxOrderVolume)
						((RspQueryMaxOrderVolume)_RspQueryMaxOrderVolume)(pQueryMaxOrderVolume, repare(pRspInfo), nRequestID, bIsLast);
					else
					{
						CThostFtdcQueryMaxOrderVolumeField f; memset(&f, 0, sizeof(f));
						((RspQueryMaxOrderVolume)_RspQueryMaxOrderVolume)(&f, repare(pRspInfo), nRequestID, bIsLast);
					}
				}
}
virtual void OnRspQueryBankAccountMoneyByFuture (CThostFtdcReqQueryAccountField *pReqQueryAccount, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
	if (_RspQueryBankAccountMoneyByFuture)
				{
					if (pReqQueryAccount)
						((RspQueryBankAccountMoneyByFuture)_RspQueryBankAccountMoneyByFuture)(pReqQueryAccount, repare(pRspInfo), nRequestID, bIsLast);
					else
					{
						CThostFtdcReqQueryAccountField f; memset(&f, 0, sizeof(f));
						((RspQueryBankAccountMoneyByFuture)_RspQueryBankAccountMoneyByFuture)(&f, repare(pRspInfo), nRequestID, bIsLast);
					}
				}
}
virtual void OnRtnFromFutureToBankByFuture (CThostFtdcRspTransferField *pRspTransfer)
{
	if (_RtnFromFutureToBankByFuture) ((RtnFromFutureToBankByFuture)_RtnFromFutureToBankByFuture)(pRspTransfer);
}
virtual void OnErrRtnQuoteAction (CThostFtdcQuoteActionField *pQuoteAction, CThostFtdcRspInfoField *pRspInfo)
{
	if (_ErrRtnQuoteAction) ((ErrRtnQuoteAction)_ErrRtnQuoteAction)(pQuoteAction, pRspInfo);
}
virtual void OnRtnCancelAccountByBank (CThostFtdcCancelAccountField *pCancelAccount)
{
	if (_RtnCancelAccountByBank) ((RtnCancelAccountByBank)_RtnCancelAccountByBank)(pCancelAccount);
}
virtual void OnRspQryLock (CThostFtdcLockField *pLock, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
	if (_RspQryLock)
				{
					if (pLock)
						((RspQryLock)_RspQryLock)(pLock, repare(pRspInfo), nRequestID, bIsLast);
					else
					{
						CThostFtdcLockField f; memset(&f, 0, sizeof(f));
						((RspQryLock)_RspQryLock)(&f, repare(pRspInfo), nRequestID, bIsLast);
					}
				}
}
virtual void OnRspCombActionInsert (CThostFtdcInputCombActionField *pInputCombAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
	if (_RspCombActionInsert)
				{
					if (pInputCombAction)
						((RspCombActionInsert)_RspCombActionInsert)(pInputCombAction, repare(pRspInfo), nRequestID, bIsLast);
					else
					{
						CThostFtdcInputCombActionField f; memset(&f, 0, sizeof(f));
						((RspCombActionInsert)_RspCombActionInsert)(&f, repare(pRspInfo), nRequestID, bIsLast);
					}
				}
}
virtual void OnRspQryParkedOrder (CThostFtdcParkedOrderField *pParkedOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
	if (_RspQryParkedOrder)
				{
					if (pParkedOrder)
						((RspQryParkedOrder)_RspQryParkedOrder)(pParkedOrder, repare(pRspInfo), nRequestID, bIsLast);
					else
					{
						CThostFtdcParkedOrderField f; memset(&f, 0, sizeof(f));
						((RspQryParkedOrder)_RspQryParkedOrder)(&f, repare(pRspInfo), nRequestID, bIsLast);
					}
				}
}
virtual void OnRspQryBrokerTradingParams (CThostFtdcBrokerTradingParamsField *pBrokerTradingParams, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
	if (_RspQryBrokerTradingParams)
				{
					if (pBrokerTradingParams)
						((RspQryBrokerTradingParams)_RspQryBrokerTradingParams)(pBrokerTradingParams, repare(pRspInfo), nRequestID, bIsLast);
					else
					{
						CThostFtdcBrokerTradingParamsField f; memset(&f, 0, sizeof(f));
						((RspQryBrokerTradingParams)_RspQryBrokerTradingParams)(&f, repare(pRspInfo), nRequestID, bIsLast);
					}
				}
}
virtual void OnErrRtnBankToFutureByFuture (CThostFtdcReqTransferField *pReqTransfer, CThostFtdcRspInfoField *pRspInfo)
{
	if (_ErrRtnBankToFutureByFuture) ((ErrRtnBankToFutureByFuture)_ErrRtnBankToFutureByFuture)(pReqTransfer, pRspInfo);
}
virtual void OnRspQryInstrumentCommissionRate (CThostFtdcInstrumentCommissionRateField *pInstrumentCommissionRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
	if (_RspQryInstrumentCommissionRate)
				{
					if (pInstrumentCommissionRate)
						((RspQryInstrumentCommissionRate)_RspQryInstrumentCommissionRate)(pInstrumentCommissionRate, repare(pRspInfo), nRequestID, bIsLast);
					else
					{
						CThostFtdcInstrumentCommissionRateField f; memset(&f, 0, sizeof(f));
						((RspQryInstrumentCommissionRate)_RspQryInstrumentCommissionRate)(&f, repare(pRspInfo), nRequestID, bIsLast);
					}
				}
}
virtual void OnRspQryInstrumentOrderCommRate (CThostFtdcInstrumentOrderCommRateField *pInstrumentOrderCommRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
	if (_RspQryInstrumentOrderCommRate)
				{
					if (pInstrumentOrderCommRate)
						((RspQryInstrumentOrderCommRate)_RspQryInstrumentOrderCommRate)(pInstrumentOrderCommRate, repare(pRspInfo), nRequestID, bIsLast);
					else
					{
						CThostFtdcInstrumentOrderCommRateField f; memset(&f, 0, sizeof(f));
						((RspQryInstrumentOrderCommRate)_RspQryInstrumentOrderCommRate)(&f, repare(pRspInfo), nRequestID, bIsLast);
					}
				}
}
virtual void OnRtnRepealFromBankToFutureByFuture (CThostFtdcRspRepealField *pRspRepeal)
{
	if (_RtnRepealFromBankToFutureByFuture) ((RtnRepealFromBankToFutureByFuture)_RtnRepealFromBankToFutureByFuture)(pRspRepeal);
}
virtual void OnRspQryETFOptionInstrCommRate (CThostFtdcETFOptionInstrCommRateField *pETFOptionInstrCommRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
	if (_RspQryETFOptionInstrCommRate)
				{
					if (pETFOptionInstrCommRate)
						((RspQryETFOptionInstrCommRate)_RspQryETFOptionInstrCommRate)(pETFOptionInstrCommRate, repare(pRspInfo), nRequestID, bIsLast);
					else
					{
						CThostFtdcETFOptionInstrCommRateField f; memset(&f, 0, sizeof(f));
						((RspQryETFOptionInstrCommRate)_RspQryETFOptionInstrCommRate)(&f, repare(pRspInfo), nRequestID, bIsLast);
					}
				}
}
virtual void OnRspParkedOrderInsert (CThostFtdcParkedOrderField *pParkedOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
	if (_RspParkedOrderInsert)
				{
					if (pParkedOrder)
						((RspParkedOrderInsert)_RspParkedOrderInsert)(pParkedOrder, repare(pRspInfo), nRequestID, bIsLast);
					else
					{
						CThostFtdcParkedOrderField f; memset(&f, 0, sizeof(f));
						((RspParkedOrderInsert)_RspParkedOrderInsert)(&f, repare(pRspInfo), nRequestID, bIsLast);
					}
				}
}
virtual void OnRspQuoteAction (CThostFtdcInputQuoteActionField *pInputQuoteAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
	if (_RspQuoteAction)
				{
					if (pInputQuoteAction)
						((RspQuoteAction)_RspQuoteAction)(pInputQuoteAction, repare(pRspInfo), nRequestID, bIsLast);
					else
					{
						CThostFtdcInputQuoteActionField f; memset(&f, 0, sizeof(f));
						((RspQuoteAction)_RspQuoteAction)(&f, repare(pRspInfo), nRequestID, bIsLast);
					}
				}
}
virtual void OnRspQryInstrument (CThostFtdcInstrumentField *pInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
	if (_RspQryInstrument)
				{
					if (pInstrument)
						((RspQryInstrument)_RspQryInstrument)(pInstrument, repare(pRspInfo), nRequestID, bIsLast);
					else
					{
						CThostFtdcInstrumentField f; memset(&f, 0, sizeof(f));
						((RspQryInstrument)_RspQryInstrument)(&f, repare(pRspInfo), nRequestID, bIsLast);
					}
				}
}
virtual void OnRspUserPasswordUpdate (CThostFtdcUserPasswordUpdateField *pUserPasswordUpdate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
	if (_RspUserPasswordUpdate)
				{
					if (pUserPasswordUpdate)
						((RspUserPasswordUpdate)_RspUserPasswordUpdate)(pUserPasswordUpdate, repare(pRspInfo), nRequestID, bIsLast);
					else
					{
						CThostFtdcUserPasswordUpdateField f; memset(&f, 0, sizeof(f));
						((RspUserPasswordUpdate)_RspUserPasswordUpdate)(&f, repare(pRspInfo), nRequestID, bIsLast);
					}
				}
}
virtual void OnRspParkedOrderAction (CThostFtdcParkedOrderActionField *pParkedOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
	if (_RspParkedOrderAction)
				{
					if (pParkedOrderAction)
						((RspParkedOrderAction)_RspParkedOrderAction)(pParkedOrderAction, repare(pRspInfo), nRequestID, bIsLast);
					else
					{
						CThostFtdcParkedOrderActionField f; memset(&f, 0, sizeof(f));
						((RspParkedOrderAction)_RspParkedOrderAction)(&f, repare(pRspInfo), nRequestID, bIsLast);
					}
				}
}
virtual void OnRspQryEWarrantOffset (CThostFtdcEWarrantOffsetField *pEWarrantOffset, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
	if (_RspQryEWarrantOffset)
				{
					if (pEWarrantOffset)
						((RspQryEWarrantOffset)_RspQryEWarrantOffset)(pEWarrantOffset, repare(pRspInfo), nRequestID, bIsLast);
					else
					{
						CThostFtdcEWarrantOffsetField f; memset(&f, 0, sizeof(f));
						((RspQryEWarrantOffset)_RspQryEWarrantOffset)(&f, repare(pRspInfo), nRequestID, bIsLast);
					}
				}
}
virtual void OnRspAuthenticate (CThostFtdcRspAuthenticateField *pRspAuthenticateField, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
	if (_RspAuthenticate)
				{
					if (pRspAuthenticateField)
						((RspAuthenticate)_RspAuthenticate)(pRspAuthenticateField, repare(pRspInfo), nRequestID, bIsLast);
					else
					{
						CThostFtdcRspAuthenticateField f; memset(&f, 0, sizeof(f));
						((RspAuthenticate)_RspAuthenticate)(&f, repare(pRspInfo), nRequestID, bIsLast);
					}
				}
}
virtual void OnRspFromFutureToBankByFuture (CThostFtdcReqTransferField *pReqTransfer, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
	if (_RspFromFutureToBankByFuture)
				{
					if (pReqTransfer)
						((RspFromFutureToBankByFuture)_RspFromFutureToBankByFuture)(pReqTransfer, repare(pRspInfo), nRequestID, bIsLast);
					else
					{
						CThostFtdcReqTransferField f; memset(&f, 0, sizeof(f));
						((RspFromFutureToBankByFuture)_RspFromFutureToBankByFuture)(&f, repare(pRspInfo), nRequestID, bIsLast);
					}
				}
}
virtual void OnFrontConnected () {if (_FrontConnected) ((FrontConnected)_FrontConnected)();}
virtual void OnRspQryInvestor (CThostFtdcInvestorField *pInvestor, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
	if (_RspQryInvestor)
				{
					if (pInvestor)
						((RspQryInvestor)_RspQryInvestor)(pInvestor, repare(pRspInfo), nRequestID, bIsLast);
					else
					{
						CThostFtdcInvestorField f; memset(&f, 0, sizeof(f));
						((RspQryInvestor)_RspQryInvestor)(&f, repare(pRspInfo), nRequestID, bIsLast);
					}
				}
}
virtual void OnRspQryForQuote (CThostFtdcForQuoteField *pForQuote, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
	if (_RspQryForQuote)
				{
					if (pForQuote)
						((RspQryForQuote)_RspQryForQuote)(pForQuote, repare(pRspInfo), nRequestID, bIsLast);
					else
					{
						CThostFtdcForQuoteField f; memset(&f, 0, sizeof(f));
						((RspQryForQuote)_RspQryForQuote)(&f, repare(pRspInfo), nRequestID, bIsLast);
					}
				}
}
virtual void OnRspQryAccountregister (CThostFtdcAccountregisterField *pAccountregister, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
	if (_RspQryAccountregister)
				{
					if (pAccountregister)
						((RspQryAccountregister)_RspQryAccountregister)(pAccountregister, repare(pRspInfo), nRequestID, bIsLast);
					else
					{
						CThostFtdcAccountregisterField f; memset(&f, 0, sizeof(f));
						((RspQryAccountregister)_RspQryAccountregister)(&f, repare(pRspInfo), nRequestID, bIsLast);
					}
				}
}
virtual void OnRspQryTradingCode (CThostFtdcTradingCodeField *pTradingCode, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
	if (_RspQryTradingCode)
				{
					if (pTradingCode)
						((RspQryTradingCode)_RspQryTradingCode)(pTradingCode, repare(pRspInfo), nRequestID, bIsLast);
					else
					{
						CThostFtdcTradingCodeField f; memset(&f, 0, sizeof(f));
						((RspQryTradingCode)_RspQryTradingCode)(&f, repare(pRspInfo), nRequestID, bIsLast);
					}
				}
}
virtual void OnRspQryQuote (CThostFtdcQuoteField *pQuote, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
	if (_RspQryQuote)
				{
					if (pQuote)
						((RspQryQuote)_RspQryQuote)(pQuote, repare(pRspInfo), nRequestID, bIsLast);
					else
					{
						CThostFtdcQuoteField f; memset(&f, 0, sizeof(f));
						((RspQryQuote)_RspQryQuote)(&f, repare(pRspInfo), nRequestID, bIsLast);
					}
				}
}
virtual void OnErrRtnLockInsert (CThostFtdcInputLockField *pInputLock, CThostFtdcRspInfoField *pRspInfo)
{
	if (_ErrRtnLockInsert) ((ErrRtnLockInsert)_ErrRtnLockInsert)(pInputLock, pRspInfo);
}
virtual void OnRspQryOptionInstrTradeCost (CThostFtdcOptionInstrTradeCostField *pOptionInstrTradeCost, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
	if (_RspQryOptionInstrTradeCost)
				{
					if (pOptionInstrTradeCost)
						((RspQryOptionInstrTradeCost)_RspQryOptionInstrTradeCost)(pOptionInstrTradeCost, repare(pRspInfo), nRequestID, bIsLast);
					else
					{
						CThostFtdcOptionInstrTradeCostField f; memset(&f, 0, sizeof(f));
						((RspQryOptionInstrTradeCost)_RspQryOptionInstrTradeCost)(&f, repare(pRspInfo), nRequestID, bIsLast);
					}
				}
}
virtual void OnRspQryOrder (CThostFtdcOrderField *pOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
	if (_RspQryOrder)
				{
					if (pOrder)
						((RspQryOrder)_RspQryOrder)(pOrder, repare(pRspInfo), nRequestID, bIsLast);
					else
					{
						CThostFtdcOrderField f; memset(&f, 0, sizeof(f));
						((RspQryOrder)_RspQryOrder)(&f, repare(pRspInfo), nRequestID, bIsLast);
					}
				}
}
virtual void OnRspQryTradingAccount (CThostFtdcTradingAccountField *pTradingAccount, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
	if (_RspQryTradingAccount)
				{
					if (pTradingAccount)
						((RspQryTradingAccount)_RspQryTradingAccount)(pTradingAccount, repare(pRspInfo), nRequestID, bIsLast);
					else
					{
						CThostFtdcTradingAccountField f; memset(&f, 0, sizeof(f));
						((RspQryTradingAccount)_RspQryTradingAccount)(&f, repare(pRspInfo), nRequestID, bIsLast);
					}
				}
}

			virtual void onRspError(CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
			{
				if (_RspError)
				{
					((RspError)_RspError)(repare(pRspInfo), nRequestID, bIsLast);
				}
			}
virtual void OnRspQryExchangeMarginRate (CThostFtdcExchangeMarginRateField *pExchangeMarginRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
	if (_RspQryExchangeMarginRate)
				{
					if (pExchangeMarginRate)
						((RspQryExchangeMarginRate)_RspQryExchangeMarginRate)(pExchangeMarginRate, repare(pRspInfo), nRequestID, bIsLast);
					else
					{
						CThostFtdcExchangeMarginRateField f; memset(&f, 0, sizeof(f));
						((RspQryExchangeMarginRate)_RspQryExchangeMarginRate)(&f, repare(pRspInfo), nRequestID, bIsLast);
					}
				}
}
virtual void OnRspQryExchangeMarginRateAdjust (CThostFtdcExchangeMarginRateAdjustField *pExchangeMarginRateAdjust, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
	if (_RspQryExchangeMarginRateAdjust)
				{
					if (pExchangeMarginRateAdjust)
						((RspQryExchangeMarginRateAdjust)_RspQryExchangeMarginRateAdjust)(pExchangeMarginRateAdjust, repare(pRspInfo), nRequestID, bIsLast);
					else
					{
						CThostFtdcExchangeMarginRateAdjustField f; memset(&f, 0, sizeof(f));
						((RspQryExchangeMarginRateAdjust)_RspQryExchangeMarginRateAdjust)(&f, repare(pRspInfo), nRequestID, bIsLast);
					}
				}
}
virtual void OnFrontDisconnected (int nReason) {if (_FrontDisconnected) ((FrontDisconnected)_FrontDisconnected)(nReason);}
virtual void OnRspQryExchangeRate (CThostFtdcExchangeRateField *pExchangeRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
	if (_RspQryExchangeRate)
				{
					if (pExchangeRate)
						((RspQryExchangeRate)_RspQryExchangeRate)(pExchangeRate, repare(pRspInfo), nRequestID, bIsLast);
					else
					{
						CThostFtdcExchangeRateField f; memset(&f, 0, sizeof(f));
						((RspQryExchangeRate)_RspQryExchangeRate)(&f, repare(pRspInfo), nRequestID, bIsLast);
					}
				}
}
virtual void OnRspQrySettlementInfoConfirm (CThostFtdcSettlementInfoConfirmField *pSettlementInfoConfirm, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
	if (_RspQrySettlementInfoConfirm)
				{
					if (pSettlementInfoConfirm)
						((RspQrySettlementInfoConfirm)_RspQrySettlementInfoConfirm)(pSettlementInfoConfirm, repare(pRspInfo), nRequestID, bIsLast);
					else
					{
						CThostFtdcSettlementInfoConfirmField f; memset(&f, 0, sizeof(f));
						((RspQrySettlementInfoConfirm)_RspQrySettlementInfoConfirm)(&f, repare(pRspInfo), nRequestID, bIsLast);
					}
				}
}
virtual void OnRspQueryCFMMCTradingAccountToken (CThostFtdcQueryCFMMCTradingAccountTokenField *pQueryCFMMCTradingAccountToken, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
	if (_RspQueryCFMMCTradingAccountToken)
				{
					if (pQueryCFMMCTradingAccountToken)
						((RspQueryCFMMCTradingAccountToken)_RspQueryCFMMCTradingAccountToken)(pQueryCFMMCTradingAccountToken, repare(pRspInfo), nRequestID, bIsLast);
					else
					{
						CThostFtdcQueryCFMMCTradingAccountTokenField f; memset(&f, 0, sizeof(f));
						((RspQueryCFMMCTradingAccountToken)_RspQueryCFMMCTradingAccountToken)(&f, repare(pRspInfo), nRequestID, bIsLast);
					}
				}
}
virtual void OnRspQuoteInsert (CThostFtdcInputQuoteField *pInputQuote, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
	if (_RspQuoteInsert)
				{
					if (pInputQuote)
						((RspQuoteInsert)_RspQuoteInsert)(pInputQuote, repare(pRspInfo), nRequestID, bIsLast);
					else
					{
						CThostFtdcInputQuoteField f; memset(&f, 0, sizeof(f));
						((RspQuoteInsert)_RspQuoteInsert)(&f, repare(pRspInfo), nRequestID, bIsLast);
					}
				}
}
virtual void OnRspQryOptionInstrCommRate (CThostFtdcOptionInstrCommRateField *pOptionInstrCommRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
	if (_RspQryOptionInstrCommRate)
				{
					if (pOptionInstrCommRate)
						((RspQryOptionInstrCommRate)_RspQryOptionInstrCommRate)(pOptionInstrCommRate, repare(pRspInfo), nRequestID, bIsLast);
					else
					{
						CThostFtdcOptionInstrCommRateField f; memset(&f, 0, sizeof(f));
						((RspQryOptionInstrCommRate)_RspQryOptionInstrCommRate)(&f, repare(pRspInfo), nRequestID, bIsLast);
					}
				}
}
virtual void OnRtnBulletin (CThostFtdcBulletinField *pBulletin)
{
	if (_RtnBulletin) ((RtnBulletin)_RtnBulletin)(pBulletin);
}
virtual void OnRtnQuote (CThostFtdcQuoteField *pQuote)
{
	if (_RtnQuote) ((RtnQuote)_RtnQuote)(pQuote);
}
virtual void OnRspQryProduct (CThostFtdcProductField *pProduct, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
	if (_RspQryProduct)
				{
					if (pProduct)
						((RspQryProduct)_RspQryProduct)(pProduct, repare(pRspInfo), nRequestID, bIsLast);
					else
					{
						CThostFtdcProductField f; memset(&f, 0, sizeof(f));
						((RspQryProduct)_RspQryProduct)(&f, repare(pRspInfo), nRequestID, bIsLast);
					}
				}
}
virtual void OnRtnRepealFromBankToFutureByBank (CThostFtdcRspRepealField *pRspRepeal)
{
	if (_RtnRepealFromBankToFutureByBank) ((RtnRepealFromBankToFutureByBank)_RtnRepealFromBankToFutureByBank)(pRspRepeal);
}
virtual void OnRspOrderInsert (CThostFtdcInputOrderField *pInputOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
	if (_RspOrderInsert)
				{
					if (pInputOrder)
						((RspOrderInsert)_RspOrderInsert)(pInputOrder, repare(pRspInfo), nRequestID, bIsLast);
					else
					{
						CThostFtdcInputOrderField f; memset(&f, 0, sizeof(f));
						((RspOrderInsert)_RspOrderInsert)(&f, repare(pRspInfo), nRequestID, bIsLast);
					}
				}
}
virtual void OnRtnFromBankToFutureByFuture (CThostFtdcRspTransferField *pRspTransfer)
{
	if (_RtnFromBankToFutureByFuture) ((RtnFromBankToFutureByFuture)_RtnFromBankToFutureByFuture)(pRspTransfer);
}
virtual void OnRtnOpenAccountByBank (CThostFtdcOpenAccountField *pOpenAccount)
{
	if (_RtnOpenAccountByBank) ((RtnOpenAccountByBank)_RtnOpenAccountByBank)(pOpenAccount);
}
virtual void OnRspBatchOrderAction (CThostFtdcInputBatchOrderActionField *pInputBatchOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
	if (_RspBatchOrderAction)
				{
					if (pInputBatchOrderAction)
						((RspBatchOrderAction)_RspBatchOrderAction)(pInputBatchOrderAction, repare(pRspInfo), nRequestID, bIsLast);
					else
					{
						CThostFtdcInputBatchOrderActionField f; memset(&f, 0, sizeof(f));
						((RspBatchOrderAction)_RspBatchOrderAction)(&f, repare(pRspInfo), nRequestID, bIsLast);
					}
				}
}
virtual void OnErrRtnBatchOrderAction (CThostFtdcBatchOrderActionField *pBatchOrderAction, CThostFtdcRspInfoField *pRspInfo)
{
	if (_ErrRtnBatchOrderAction) ((ErrRtnBatchOrderAction)_ErrRtnBatchOrderAction)(pBatchOrderAction, pRspInfo);
}
virtual void OnRtnFromBankToFutureByBank (CThostFtdcRspTransferField *pRspTransfer)
{
	if (_RtnFromBankToFutureByBank) ((RtnFromBankToFutureByBank)_RtnFromBankToFutureByBank)(pRspTransfer);
}
virtual void OnRspRemoveParkedOrder (CThostFtdcRemoveParkedOrderField *pRemoveParkedOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
	if (_RspRemoveParkedOrder)
				{
					if (pRemoveParkedOrder)
						((RspRemoveParkedOrder)_RspRemoveParkedOrder)(pRemoveParkedOrder, repare(pRspInfo), nRequestID, bIsLast);
					else
					{
						CThostFtdcRemoveParkedOrderField f; memset(&f, 0, sizeof(f));
						((RspRemoveParkedOrder)_RspRemoveParkedOrder)(&f, repare(pRspInfo), nRequestID, bIsLast);
					}
				}
}
virtual void OnErrRtnOrderAction (CThostFtdcOrderActionField *pOrderAction, CThostFtdcRspInfoField *pRspInfo)
{
	if (_ErrRtnOrderAction) ((ErrRtnOrderAction)_ErrRtnOrderAction)(pOrderAction, pRspInfo);
}
virtual void OnRspQryLockPosition (CThostFtdcLockPositionField *pLockPosition, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
	if (_RspQryLockPosition)
				{
					if (pLockPosition)
						((RspQryLockPosition)_RspQryLockPosition)(pLockPosition, repare(pRspInfo), nRequestID, bIsLast);
					else
					{
						CThostFtdcLockPositionField f; memset(&f, 0, sizeof(f));
						((RspQryLockPosition)_RspQryLockPosition)(&f, repare(pRspInfo), nRequestID, bIsLast);
					}
				}
}
virtual void OnRspQryNotice (CThostFtdcNoticeField *pNotice, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
	if (_RspQryNotice)
				{
					if (pNotice)
						((RspQryNotice)_RspQryNotice)(pNotice, repare(pRspInfo), nRequestID, bIsLast);
					else
					{
						CThostFtdcNoticeField f; memset(&f, 0, sizeof(f));
						((RspQryNotice)_RspQryNotice)(&f, repare(pRspInfo), nRequestID, bIsLast);
					}
				}
}
virtual void OnRspQryInvestorLevel (CThostFtdcInvestorLevelField *pInvestorLevel, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
	if (_RspQryInvestorLevel)
				{
					if (pInvestorLevel)
						((RspQryInvestorLevel)_RspQryInvestorLevel)(pInvestorLevel, repare(pRspInfo), nRequestID, bIsLast);
					else
					{
						CThostFtdcInvestorLevelField f; memset(&f, 0, sizeof(f));
						((RspQryInvestorLevel)_RspQryInvestorLevel)(&f, repare(pRspInfo), nRequestID, bIsLast);
					}
				}
}
virtual void OnRspQryMMInstrumentCommissionRate (CThostFtdcMMInstrumentCommissionRateField *pMMInstrumentCommissionRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
	if (_RspQryMMInstrumentCommissionRate)
				{
					if (pMMInstrumentCommissionRate)
						((RspQryMMInstrumentCommissionRate)_RspQryMMInstrumentCommissionRate)(pMMInstrumentCommissionRate, repare(pRspInfo), nRequestID, bIsLast);
					else
					{
						CThostFtdcMMInstrumentCommissionRateField f; memset(&f, 0, sizeof(f));
						((RspQryMMInstrumentCommissionRate)_RspQryMMInstrumentCommissionRate)(&f, repare(pRspInfo), nRequestID, bIsLast);
					}
				}
}
virtual void OnRspQryExchange (CThostFtdcExchangeField *pExchange, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
	if (_RspQryExchange)
				{
					if (pExchange)
						((RspQryExchange)_RspQryExchange)(pExchange, repare(pRspInfo), nRequestID, bIsLast);
					else
					{
						CThostFtdcExchangeField f; memset(&f, 0, sizeof(f));
						((RspQryExchange)_RspQryExchange)(&f, repare(pRspInfo), nRequestID, bIsLast);
					}
				}
}
virtual void OnRspUserLogout (CThostFtdcUserLogoutField *pUserLogout, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
	if (_RspUserLogout)
				{
					if (pUserLogout)
						((RspUserLogout)_RspUserLogout)(pUserLogout, repare(pRspInfo), nRequestID, bIsLast);
					else
					{
						CThostFtdcUserLogoutField f; memset(&f, 0, sizeof(f));
						((RspUserLogout)_RspUserLogout)(&f, repare(pRspInfo), nRequestID, bIsLast);
					}
				}
}
virtual void OnRtnTradingNotice (CThostFtdcTradingNoticeInfoField *pTradingNoticeInfo)
{
	if (_RtnTradingNotice) ((RtnTradingNotice)_RtnTradingNotice)(pTradingNoticeInfo);
}
virtual void OnRspQrySettlementInfo (CThostFtdcSettlementInfoField *pSettlementInfo, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
	if (_RspQrySettlementInfo)
				{
					if (pSettlementInfo)
						((RspQrySettlementInfo)_RspQrySettlementInfo)(pSettlementInfo, repare(pRspInfo), nRequestID, bIsLast);
					else
					{
						CThostFtdcSettlementInfoField f; memset(&f, 0, sizeof(f));
						((RspQrySettlementInfo)_RspQrySettlementInfo)(&f, repare(pRspInfo), nRequestID, bIsLast);
					}
				}
}
virtual void OnRspQryInvestorPosition (CThostFtdcInvestorPositionField *pInvestorPosition, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
	if (_RspQryInvestorPosition)
				{
					if (pInvestorPosition)
						((RspQryInvestorPosition)_RspQryInvestorPosition)(pInvestorPosition, repare(pRspInfo), nRequestID, bIsLast);
					else
					{
						CThostFtdcInvestorPositionField f; memset(&f, 0, sizeof(f));
						((RspQryInvestorPosition)_RspQryInvestorPosition)(&f, repare(pRspInfo), nRequestID, bIsLast);
					}
				}
}
virtual void OnErrRtnFutureToBankByFuture (CThostFtdcReqTransferField *pReqTransfer, CThostFtdcRspInfoField *pRspInfo)
{
	if (_ErrRtnFutureToBankByFuture) ((ErrRtnFutureToBankByFuture)_ErrRtnFutureToBankByFuture)(pReqTransfer, pRspInfo);
}
virtual void OnErrRtnForQuoteInsert (CThostFtdcInputForQuoteField *pInputForQuote, CThostFtdcRspInfoField *pRspInfo)
{
	if (_ErrRtnForQuoteInsert) ((ErrRtnForQuoteInsert)_ErrRtnForQuoteInsert)(pInputForQuote, pRspInfo);
}
virtual void OnRspQryProductExchRate (CThostFtdcProductExchRateField *pProductExchRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
	if (_RspQryProductExchRate)
				{
					if (pProductExchRate)
						((RspQryProductExchRate)_RspQryProductExchRate)(pProductExchRate, repare(pRspInfo), nRequestID, bIsLast);
					else
					{
						CThostFtdcProductExchRateField f; memset(&f, 0, sizeof(f));
						((RspQryProductExchRate)_RspQryProductExchRate)(&f, repare(pRspInfo), nRequestID, bIsLast);
					}
				}
}
virtual void OnRtnChangeAccountByBank (CThostFtdcChangeAccountField *pChangeAccount)
{
	if (_RtnChangeAccountByBank) ((RtnChangeAccountByBank)_RtnChangeAccountByBank)(pChangeAccount);
}
virtual void OnRspQryInvestorPositionDetail (CThostFtdcInvestorPositionDetailField *pInvestorPositionDetail, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
	if (_RspQryInvestorPositionDetail)
				{
					if (pInvestorPositionDetail)
						((RspQryInvestorPositionDetail)_RspQryInvestorPositionDetail)(pInvestorPositionDetail, repare(pRspInfo), nRequestID, bIsLast);
					else
					{
						CThostFtdcInvestorPositionDetailField f; memset(&f, 0, sizeof(f));
						((RspQryInvestorPositionDetail)_RspQryInvestorPositionDetail)(&f, repare(pRspInfo), nRequestID, bIsLast);
					}
				}
}
virtual void OnRspOrderAction (CThostFtdcInputOrderActionField *pInputOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
	if (_RspOrderAction)
				{
					if (pInputOrderAction)
						((RspOrderAction)_RspOrderAction)(pInputOrderAction, repare(pRspInfo), nRequestID, bIsLast);
					else
					{
						CThostFtdcInputOrderActionField f; memset(&f, 0, sizeof(f));
						((RspOrderAction)_RspOrderAction)(&f, repare(pRspInfo), nRequestID, bIsLast);
					}
				}
}
virtual void OnRtnLock (CThostFtdcLockField *pLock)
{
	if (_RtnLock) ((RtnLock)_RtnLock)(pLock);
}
virtual void OnRtnForQuoteRsp (CThostFtdcForQuoteRspField *pForQuoteRsp)
{
	if (_RtnForQuoteRsp) ((RtnForQuoteRsp)_RtnForQuoteRsp)(pForQuoteRsp);
}
virtual void OnRspQryInstrumentMarginRate (CThostFtdcInstrumentMarginRateField *pInstrumentMarginRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
	if (_RspQryInstrumentMarginRate)
				{
					if (pInstrumentMarginRate)
						((RspQryInstrumentMarginRate)_RspQryInstrumentMarginRate)(pInstrumentMarginRate, repare(pRspInfo), nRequestID, bIsLast);
					else
					{
						CThostFtdcInstrumentMarginRateField f; memset(&f, 0, sizeof(f));
						((RspQryInstrumentMarginRate)_RspQryInstrumentMarginRate)(&f, repare(pRspInfo), nRequestID, bIsLast);
					}
				}
}

};
