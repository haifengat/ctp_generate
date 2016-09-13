

#include "Quote.h"
#include <string.h>
int nReq;

Quote::Quote(void)
{
	_FrontConnected = NULL;
	_FrontDisconnected = NULL;
	_HeartBeatWarning = NULL;
	_RspUserLogin = NULL;
	_RspUserLogout = NULL;
	_RspError = NULL;
	_RspSubMarketData = NULL;
	_RspUnSubMarketData = NULL;
	_RspSubForQuoteRsp = NULL;
	_RspUnSubForQuoteRsp = NULL;
	_RtnDepthMarketData = NULL;
	_RtnForQuoteRsp = NULL;

}
void SetOnFrontConnected(Quote* spi, void* func){spi->_FrontConnected = func;}
void SetOnFrontDisconnected(Quote* spi, void* func){spi->_FrontDisconnected = func;}
void SetOnHeartBeatWarning(Quote* spi, void* func){spi->_HeartBeatWarning = func;}
void SetOnRspUserLogin(Quote* spi, void* func){spi->_RspUserLogin = func;}
void SetOnRspUserLogout(Quote* spi, void* func){spi->_RspUserLogout = func;}
void SetOnRspError(Quote* spi, void* func){spi->_RspError = func;}
void SetOnRspSubMarketData(Quote* spi, void* func){spi->_RspSubMarketData = func;}
void SetOnRspUnSubMarketData(Quote* spi, void* func){spi->_RspUnSubMarketData = func;}
void SetOnRspSubForQuoteRsp(Quote* spi, void* func){spi->_RspSubForQuoteRsp = func;}
void SetOnRspUnSubForQuoteRsp(Quote* spi, void* func){spi->_RspUnSubForQuoteRsp = func;}
void SetOnRtnDepthMarketData(Quote* spi, void* func){spi->_RtnDepthMarketData = func;}
void SetOnRtnForQuoteRsp(Quote* spi, void* func){spi->_RtnForQuoteRsp = func;}

void* WINAPI CreateApi(){return CThostFtdcMdApi::CreateFtdcMdApi("./log/");}

void* WINAPI CreateSpi(){return new Trade();}

		void* WINAPI ReqUserLogin(CThostFtdcMdApi *api ,CThostFtdcReqUserLoginField *pReqUserLoginField, int nRequestID){api->ReqUserLogin(pReqUserLoginField,nRequestID); return 0;}
void* WINAPI RegisterFensUserInfo(CThostFtdcMdApi *api ,CThostFtdcFensUserInfoField * pFensUserInfo){api->RegisterFensUserInfo(pFensUserInfo); return 0;}
void* WINAPI UnSubscribeMarketData(CThostFtdcMdApi *api ,char *ppInstrumentID[], int nCount){api->UnSubscribeMarketData(ppInstrumentID,nCount); return 0;}
void* WINAPI ReqUserLogout(CThostFtdcMdApi *api ,CThostFtdcUserLogoutField *pUserLogout, int nRequestID){api->ReqUserLogout(pUserLogout,nRequestID); return 0;}
void* WINAPI SubscribeMarketData(CThostFtdcMdApi *api ,char *ppInstrumentID[], int nCount){api->SubscribeMarketData(ppInstrumentID,nCount); return 0;}
void* WINAPI RegisterFront(CThostFtdcMdApi *api ,char *pszFrontAddress){api->RegisterFront(pszFrontAddress); return 0;}
void* WINAPI UnSubscribeForQuoteRsp(CThostFtdcMdApi *api ,char *ppInstrumentID[], int nCount){api->UnSubscribeForQuoteRsp(ppInstrumentID,nCount); return 0;}
void* WINAPI Join(CThostFtdcMdApi *api ){api->Join(); return 0;}
void* WINAPI SubscribeForQuoteRsp(CThostFtdcMdApi *api ,char *ppInstrumentID[], int nCount){api->SubscribeForQuoteRsp(ppInstrumentID,nCount); return 0;}
void* WINAPI RegisterNameServer(CThostFtdcMdApi *api ,char *pszNsAddress){api->RegisterNameServer(pszNsAddress); return 0;}
void* WINAPI Release(CThostFtdcMdApi *api ){api->Release(); return 0;}
void* WINAPI GetTradingDay(CThostFtdcMdApi *api ){api->GetTradingDay(); return 0;}
void* WINAPI RegisterSpi(CThostFtdcMdApi *api ,CThostFtdcMdSpi *pSpi){api->RegisterSpi(pSpi); return 0;}
void* WINAPI Init(CThostFtdcMdApi *api ){api->Init(); return 0;}
