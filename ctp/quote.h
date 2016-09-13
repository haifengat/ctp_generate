
#pragma once
#define DllExport __declspec(dllexport)
#define WINAPI      __stdcall
#define WIN32_LEAN_AND_MEAN             //  从 Windows 头文件中排除极少使用的信息

#include "stddef.h"
#include <string.h>

#include "../ctp_20160628/ThostFtdcMdApi.h"
#pragma comment(lib, "../ctp_20160628/thostmduserapi.lib")

class Quote : CThostFtdcMdSpi
{
public:
	Quote(void);
	~Quote(void);
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
	typedef int (WINAPI *RspSubForQuoteRsp)(CThostFtdcSpecificInstrumentField *pSpecificInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	typedef int (WINAPI *RtnForQuoteRsp)(CThostFtdcForQuoteRspField *pForQuoteRsp);
	typedef int (WINAPI *HeartBeatWarning)(int nTimeLapse);
	typedef int (WINAPI *RspSubMarketData)(CThostFtdcSpecificInstrumentField *pSpecificInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	typedef int (WINAPI *RspUserLogin)(CThostFtdcRspUserLoginField *pRspUserLogin, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	typedef int (WINAPI *RtnDepthMarketData)(CThostFtdcDepthMarketDataField *pDepthMarketData);
	typedef int (WINAPI *RspUnSubForQuoteRsp)(CThostFtdcSpecificInstrumentField *pSpecificInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	typedef int (WINAPI *RspUnSubMarketData)(CThostFtdcSpecificInstrumentField *pSpecificInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	typedef int (WINAPI *FrontDisconnected)(int nReason);
	typedef int (WINAPI *RspUserLogout)(CThostFtdcUserLogoutField *pUserLogout, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	typedef int (WINAPI *RspError)(CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	typedef int (WINAPI *FrontConnected)();

	void *_RspSubForQuoteRsp;
	void *_RtnForQuoteRsp;
	void *_HeartBeatWarning;
	void *_RspSubMarketData;
	void *_RspUserLogin;
	void *_RtnDepthMarketData;
	void *_RspUnSubForQuoteRsp;
	void *_RspUnSubMarketData;
	void *_FrontDisconnected;
	void *_RspUserLogout;
	void *_RspError;
	void *_FrontConnected;

	virtual void OnRspSubForQuoteRsp(CThostFtdcSpecificInstrumentField *pSpecificInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
	{
		if (_RspSubForQuoteRsp)
		{
			if (pSpecificInstrument)
				((RspSubForQuoteRsp)_RspSubForQuoteRsp)(pSpecificInstrument, repare(pRspInfo), nRequestID, bIsLast);
			else
			{
				CThostFtdcSpecificInstrumentField f; memset(&f, 0, sizeof(f));
				((RspSubForQuoteRsp)_RspSubForQuoteRsp)(&f, repare(pRspInfo), nRequestID, bIsLast);
			}
		}
	}
	virtual void OnRtnForQuoteRsp(CThostFtdcForQuoteRspField *pForQuoteRsp)
	{
		{if (_RtnForQuoteRsp) ((RtnForQuoteRsp)_RtnForQuoteRsp)(pForQuoteRsp); }
	}
	virtual void OnHeartBeatWarning(int nTimeLapse) { {if (_HeartBeatWarning) ((HeartBeatWarning)_HeartBeatWarning)(nTimeLapse); } }
	virtual void OnRspSubMarketData(CThostFtdcSpecificInstrumentField *pSpecificInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
	{
		if (_RspSubMarketData)
		{
			if (pSpecificInstrument)
				((RspSubMarketData)_RspSubMarketData)(pSpecificInstrument, repare(pRspInfo), nRequestID, bIsLast);
			else
			{
				CThostFtdcSpecificInstrumentField f; memset(&f, 0, sizeof(f));
				((RspSubMarketData)_RspSubMarketData)(&f, repare(pRspInfo), nRequestID, bIsLast);
			}
		}
	}
	virtual void OnRspUserLogin(CThostFtdcRspUserLoginField *pRspUserLogin, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
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
	virtual void OnRtnDepthMarketData(CThostFtdcDepthMarketDataField *pDepthMarketData)
	{
		{if (_RtnDepthMarketData) ((RtnDepthMarketData)_RtnDepthMarketData)(pDepthMarketData); }
	}
	virtual void OnRspUnSubForQuoteRsp(CThostFtdcSpecificInstrumentField *pSpecificInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
	{
		if (_RspUnSubForQuoteRsp)
		{
			if (pSpecificInstrument)
				((RspUnSubForQuoteRsp)_RspUnSubForQuoteRsp)(pSpecificInstrument, repare(pRspInfo), nRequestID, bIsLast);
			else
			{
				CThostFtdcSpecificInstrumentField f; memset(&f, 0, sizeof(f));
				((RspUnSubForQuoteRsp)_RspUnSubForQuoteRsp)(&f, repare(pRspInfo), nRequestID, bIsLast);
			}
		}
	}
	virtual void OnRspUnSubMarketData(CThostFtdcSpecificInstrumentField *pSpecificInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
	{
		if (_RspUnSubMarketData)
		{
			if (pSpecificInstrument)
				((RspUnSubMarketData)_RspUnSubMarketData)(pSpecificInstrument, repare(pRspInfo), nRequestID, bIsLast);
			else
			{
				CThostFtdcSpecificInstrumentField f; memset(&f, 0, sizeof(f));
				((RspUnSubMarketData)_RspUnSubMarketData)(&f, repare(pRspInfo), nRequestID, bIsLast);
			}
		}
	}
	virtual void OnFrontDisconnected(int nReason) { {if (_FrontDisconnected) ((FrontDisconnected)_FrontDisconnected)(nReason); } }
	virtual void OnRspUserLogout(CThostFtdcUserLogoutField *pUserLogout, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
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

	virtual void onRspError(CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
	{
		if (_RspError)
		{
			((RspError)_RspError)(repare(pRspInfo), nRequestID, bIsLast);
		}
	}
	virtual void OnFrontConnected() { {if (_FrontConnected) ((FrontConnected)_FrontConnected)(); } }

};
