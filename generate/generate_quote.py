#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'HaiFeng'
__mtime__ = '2016/9/1'
"""
import os

#from generate.generate_enum import GenerateEnum

class Generate:

	def __init__(self):
		self.cbNames = []
		self.cbArgs_dict = {}

		self.fcName_dict = []
		self.fcArgs_dict = {}


		self.ApiName = 'CThostFtdcMdApi'

		self.fcpp = open(os.path.join(os.path.abspath('..\ctp_20160628'), 'ThostFtdcMdApi.h'), 'r')

		self.fquote_h = open(os.path.join(os.path.abspath('..\ctp'), 'quote.h'), 'w', encoding='utf-8')

		self.fquote_p = open(os.path.join(os.path.abspath('..\ctp'), 'quote.cpp'), 'w', encoding='utf-8')

		self.fquote_d = open(os.path.join(os.path.abspath('..\ctp'), 'define.def'), 'w', encoding='utf-8')

		self.fquote_py = open(os.path.join(os.path.abspath('..\py_ctp'), 'quote.py'), 'w', encoding='utf-8')


	def processCallBack(self, line):
		orignalLine = line
		line = line.replace('\tvirtual void ', '')  # 删除行首的无效内容
		line = line.replace('{};\n', '')  # 删除行尾的无效内容

		content = line.split('(')
		cbName = content[0]  # 回调函数名称*Onxxxx

		self.cbNames.append(cbName)

		cbArgs = content[1]  # 回调函数参数
		if cbArgs[-1] == ' ':
			cbArgs = cbArgs.replace(') ', '')
		else:
			cbArgs = cbArgs.replace(')', '')
		self.cbArgs_dict[cbName] = cbArgs


	def processFunction(self, line):

		#line = line.replace('\tvirtual int ', '')  # 删除行首的无效内容
		line = line.replace(') = 0;\n', '')  # 删除行尾的无效内容
		content = line.split('(')
		fcName = content[0].split(' ')[-1].replace('*', '')  # 回调函数名称

		self.fcName_dict.append(fcName)

		fcArgs = content[1]  # 回调函数参数
		fcArgs = fcArgs.replace(')', '')

		self.fcArgs_dict[fcName] = fcArgs

	def WriteH(self):

		self.fquote_h.write('')
		self.fquote_h.write("""
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
	}\n""")

		vars = ''
		typedef = ''
		virtual = ''
		for cbName in self.cbArgs_dict:
			cbArgs = self.cbArgs_dict[cbName]
			cbArgsList = cbArgs.split(', ')  # 将每个参数转化为列表

			cbArgsTypeList = []
			cbArgsValueList = []

			for arg in cbArgsList:  # 开始处理参数
				content = arg.split(' ')
				if len(content) > 1:
					cbArgsTypeList.append(content[0])  # 参数类型列表
					cbArgsValueList.append(content[1].replace('*', ''))  # 参数数据列表

			cb = cbName[2:]

			# 生成.h文件中的on部分
			if 'OnRspError' in cbName:
				on_line = """
			virtual void onRspError(CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
			{
				if (_RspError)
				{
					((RspError)_RspError)(repare(pRspInfo), nRequestID, bIsLast);
				}
			}\n"""
			elif 'OnRsp' in cbName:
				cnt = """if (_{0})
				{{
					if ({2})
						(({0})_{0})({2}, repare(pRspInfo), nRequestID, bIsLast);
					else
					{{
						{1} f; memset(&f, 0, sizeof(f));
						(({0})_{0})(&f, repare(pRspInfo), nRequestID, bIsLast);
					}}
				}}""".format(cb, cbArgsTypeList[0], cbArgsValueList[0])

				on_line = 'virtual void {0} ({1})\n{{\n\t{2}\n}}\n'.format(cbName, cbArgs, cnt)
			elif 'OnRtn' in cbName:
				cnt = """{{if (_{0}) (({0})_{0})({1});}}""".format(cb, cbArgsValueList[0])
				on_line = 'virtual void {0} ({1})\n{{\n\t{2}\n}}\n'.format(cbName, cbArgs, cnt)
			elif 'OnErrRtn' in cbName:
				on_line = 'virtual void ' + cbName + '(dict data, dict error) {};\n'
			else:
				cnt = """{{if (_{0}) (({0})_{0})({1});}}""".format(cb, '' if len(cbArgsValueList) == 0 else cbArgsValueList[0])
				on_line = 'virtual void {0} ({1}) {{{2}}}\n'.format(cbName, cbArgs, cnt)

			if on_line != '':
				# typedef int (WINAPI *RspUserLogin)(CThostFtdcRspUserLoginField *pRspUserLogin, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
				typedef += '\ttypedef int (WINAPI *{0})({1});\n'.format(cb, cbArgs)

				# void* _FrontConnected;
				vars += '\tvoid *_{0};\n'.format(cb)

				# virtual void OnFrontConnected(){ if (_FrontConnected) ((FrontConnected)_FrontConnected)(); }
				virtual += on_line

		self.fquote_h.write(typedef)
		self.fquote_h.write('\n')
		self.fquote_h.write(vars)
		self.fquote_h.write('\n')
		self.fquote_h.write(virtual)
		self.fquote_h.write('\n')
		self.fquote_h.write('};\n')

	def WriteCpp(self):

		initCb = ''
		#SetFunction(api, func){spi.xxx = xxx
		setf = ''
		for cbName in self.cbNames:
			cb = cbName[2:]
			# set
			setf += 'void Set{0}(Quote* spi, void* func){{spi->_{1} = func;}}\n'.format(cbName, cb)
			initCb += '\t_{0} = NULL;\n'.format(cb)

		self.fquote_p.write('')
		self.fquote_p.write("""

#include "Quote.h"
#include <string.h>
int nReq;

Quote::Quote(void)
{{
{0}
}}
""".format(initCb))

		self.fquote_p.write(setf)

		self.fquote_p.write("""
void* WINAPI CreateApi(){return CThostFtdcMdApi::CreateFtdcMdApi("./log/");}

void* WINAPI CreateSpi(){return new Quote();}

		""")


		for fcName in self.fcArgs_dict:
			fcArgs = self.fcArgs_dict[fcName]
			fcArgsList = fcArgs.split(', ')  # 将每个参数转化为列表

			fcArgsTypeList = []
			fcArgsValueList = []

			for arg in fcArgsList:  # 开始处理参数
				content = arg.replace('*', '').split(' ', 1)
				if len(content) > 1:
					fcArgsTypeList.append(content[0])  # 参数类型列表
					fcArgsValueList.append(content[1].replace(' ',''))  # 参数数据列表
			params = ''
			for p in fcArgsValueList:
				p = p.replace('[', '').replace(']', '')
				params += p if params == '' else ',' + p

			#if line.find(' int ') >= 0:
			#	self.Voids += 'void* WINAPI {0}({1} *api {2}){{return (void *)api->{0}({3});}}\n'.format(fcName, self.ApiName, '' if fcArgs == '' else ',' + fcArgs, params)
			#else:
			self.fquote_p.write('void* WINAPI {0}({1} *api {2}){{api->{0}({3}); return 0;}}\n'.format(fcName, self.ApiName, '' if fcArgs == '' else ',' + fcArgs, params))


	def WriteDef(self):
		# define.def
		self.fquote_d.write('LIBRARY\nEXPORTS\n')
		self.fquote_d.write('\tCreateApi\n')
		self.fquote_d.write('\tCreateSpi\n')

		for fcName in self.fcName_dict:
			self.fquote_d.write('\t{0}\n'.format(fcName))

		for cb in self.cbNames:
			self.fquote_d.write('\tSet{0}\n'.format(cb))


	def WritePyQuote(self):
		#structs and fields
		fstruct = open('..\py_ctp\ctp_struct.py', 'r', encoding='utf-8')
		struct_dict = {}
		struct_init_dict = {}
		struct = ''
		m = __import__('py_ctp.ctp_struct')
		for line in fstruct.readlines():
			if line.find('Structure') >= 0:
				key = line.split(' ')[1].split('(')[0]
				c = getattr(getattr(m, 'ctp_struct'), key)
				o = c()
				struct_dict[key] = o._fields_


		self.fquote_py.write(
		"""
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
		self.nRequestID = 0
""")
		funcs = []
		funcs.append("""
	def {0}(self{1}):
		self.api = self.h.{0}({1})
		return self.api\n""".format("CreateApi",""))
		funcs.append("""
	def {0}(self{1}):
		self.spi = self.h.{0}({1})
		return self.spi\n""".format("CreateSpi",""))

		type_dict = {'int': 'c_int32', 'char': 'c_char_p', 'double': 'c_double', 'short': 'c_int32', 'string': 'c_char_p', 'bool': 'c_bool'}

		for fcName in self.fcArgs_dict:
			fcArgs = self.fcArgs_dict[fcName]
			fcArgsList = fcArgs.split(', ')  # 将每个参数转化为列表

			fcArgsTypeList = []
			fcArgsValueList = []

			for arg in fcArgsList:  # 开始处理参数
				content = arg.replace('*', '').split(' ', 1)
				if len(content) > 1:
					fcArgsTypeList.append(content[0])  # 参数类型列表
					fcArgsValueList.append(content[1].replace(' ', ''))  # 参数数据列表

			#对合约订阅与要的特别处理
			if fcName.find('Subscribe') == 0 or fcName.find('Subscribe') == 2:
				func = '''
	def {0}(self, pInstrumentID):
		self.h.{0}.argtypes = [c_void_p , c_char_p*1, c_int32]
		self.h.{0}.restype = c_void_p
		self.h.{0}(self.api, (c_char_p*1)(bytes(pInstrumentID, encoding = 'ascii')), 1)\n'''.format(fcName)
			else:
				#类型声明时的argtypes用
				types = ''
				#def同行参数
				params = ''
				#调用时的参数名
				values = ''
				struct_init = ''
				#for type in fcArgsTypeList:
				for i in range(len(fcArgsTypeList)):
					type = fcArgsTypeList[i]
					args = fcArgsValueList[i].replace('[', '').replace(']', '')
					if type in type_dict.keys():
						types += ' , ' + type_dict[type]

# CThostFtdcReqUserLoginField *pReqUserLoginField, int nRequestID =>,pReqUserLoginField,nRequestID
						if type == 'char':
							values += ', ' + "bytes({0}, encoding='ascii')".format(args)
						else:
							values += ', ' + args
						params += ', ' + args
					else: #非基础类型的参数
						if type in struct_dict.keys():
							struct_init = '\n\t\tstruc = {0}()\n'.format(type)
							for field in struct_dict[type]:
								tt = str(field[1]).split('.')[-1].split('\'')[0]

								if tt.find('c_char') >= 0:
									params += ", {0} = ''".format(field[0])
								else:
									params += ', {0} = 0'.format(field[0])
								#合成structure bytes('9999', encoding='ascii')
								struct_init += '\t\tstruc.{0} = {1}\n'.format(field[0], field[0] if tt.find('c_char') < 0 else "bytes({0}, encoding='ascii')".format(field[0]))
							#构造struct的语句
							struct_init_dict[fcName] = struct_init
							values += ', byref({0})'.format('struc')
						else:
							values += ', {0}'.format(args)
							params += ', ' + args
						types += ' , c_void_p'


				line = '''\t\tself.h.{0}.argtypes = [c_void_p{1}]
		self.h.{0}.restype = c_void_p\n'''.format(fcName, types)
				self.fquote_py.write(line)

				#处理参数为Structure的情况:加入structu构造,去掉reqid
				if fcName in struct_init_dict.keys():
					func = '''
	def {0}(self{1}):{3}
		self.nRequestID += 1
		self.h.{0}(self.api{2}, self.nRequestID)
			'''.format(fcName, params.replace(', nRequestID', ''), values.replace(', nRequestID', ''), struct_init_dict[fcName])
				else:
					func = '''
	def {0}(self{1}):
		self.h.{0}(self.api{2})
			'''.format(fcName, params, values)

			funcs.append(func)

		cbRegs = []
		cb__Funcs = []
		cbFuncs = []
		#响应函数
		for cbName in self.cbArgs_dict:
			cbArgs = self.cbArgs_dict[cbName]
			cbArgsList = cbArgs.split(', ')  # 将每个参数转化为列表

			cbArgsTypeList = []
			cbArgsValueList = []


			for arg in cbArgsList:  # 开始处理参数
				content = arg.split(' ')
				if len(content) > 1:
					cbArgsTypeList.append(content[0])  # 参数类型列表
					cbArgsValueList.append(content[1].replace('*', ''))  # 参数数据列表

			paramtype = ''
			params = ''
			params__ = ''
			param_trans = ''

			for t in cbArgsTypeList:
				paramtype += ', ' + (type_dict[t] if t in type_dict.keys() else 'POINTER({0})'.format(t))
				#在响应参数中加入参数的类型,方便之后的调用(可查类型)
				param = cbArgsValueList[cbArgsTypeList.index(t)]
				params__ += ', ' + param
				#if params == '':
				#	params += '{0} = {1}'.format(param, t)
				#else:
				params += ', {0} = {1}'.format(param, t)
#def __OnRspSubMarketData(self, pSpecificInstrument, pRspInfo, nRequestID, bIsLast):
#self.OnRspSubMarketData(POINTER(CThostFtdcSpecificInstrumentField).from_param(pSpecificInstrument).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents, nRequestID, bIsLast)
				ref = param
				if t not in type_dict:
					ref = 'POINTER({0}).from_param({1}).contents'.format(t, param)
				param_trans += ref if param_trans == '' else (', ' + ref)

			line = """
		self.h.Set{0}.argtypes = [c_void_p, c_void_p]
		self.h.Set{0}.restype = c_void_p
		self.ev{0} = CFUNCTYPE(c_void_p{1})(self.__{0})
		self.h.Set{0}(self.spi, self.ev{0})
""".format(cbName, paramtype)
			cbRegs.append(line)

			cb__Funcs.append("""
	def __{0}(self{1}):
		self.{0}({2})
	""".format(cbName, params__, param_trans))

			cbFuncs.append("""
	def {0}(self{1}):
			print('{0}:{1}')
	""".format(cbName, params))

		self.fquote_py.write('''
		# restore work directory
		os.chdir(cur_path)

''')
		############### 以上为__init__函数内容

		# 事件注册函数
		self.fquote_py.write('''
	def RegCB(self):
		"""在createapi, createspi后调用"""
''')

		for reg in cbRegs:
			self.fquote_py.write(reg)

		#回调函数
		for func in cb__Funcs:
			self.fquote_py.write(func)
		for func in cbFuncs:
			self.fquote_py.write(func)

		# 主调函数
		for func in funcs:
			self.fquote_py.write(func)


	def run(self):
		for line in self.fcpp:
			if "\tvirtual void On" in line:
				self.processCallBack(line)
			# elif "\tvirtual int" in line:
			elif '= 0;' in line:
				# virtual void RegisterFront(char *pszFrontAddress) = 0;
				# ==>
				# DllExport void* WINAPI
				self.processFunction(line)
		self.WriteH()
		self.WriteCpp()
		self.WriteDef()  # define.def
		self.WritePyQuote()

if __name__ == '__main__':
	#构建quote  cb, func
	g = Generate()
	g.run()

	#e = GenerateEnum()
	#e.main()

	from generate.generate_struct import GenerateStruct
	s = GenerateStruct()
	s.main()

	#os.remove('ctp_data_type.py') #,from xxx struct放在此函数内解决::删除后会造成eneratestruct无法运行,因为要import datatype.py

