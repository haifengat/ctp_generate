#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'HaiFeng'
__mtime__ = '2016/9/17'
"""

from ctp_data_type import *
import os

class GenerateStruct:
	def main(self):

		"""主函数"""
		fcpp = open(os.path.join(os.path.abspath('..\ctp_20160628'), 'ThostFtdcUserApiStruct.h'), 'r')
		fpy = open(os.path.join(os.path.abspath('..\..\hf_py_ctp\py_ctp'), 'ctp_struct.py'), 'w', encoding='utf-8')

		fpy.write('#!/usr/bin/env python\n')
		fpy.write('#coding:utf-8\n')
		fpy.write('from ctypes import *\n')
		fpy.write('from py_ctp.ctp_enum import *\n')

		fpy.write('\n')
		# fpy.write('structDict = {}\n')
		# fpy.write('\n')

		py_get = ''
		py_line = ''
		py_str = ''
		py_dict = ''
		py_clone = ''
		py_str_idx = 0
		py_str_format = ''

		for no, line in enumerate(fcpp):

			# 结构体申明注释
			if '///' in line and '\t' not in line:
				remark = line[3:-1]
				continue

			# 结构体变量注释
			elif '\t///' in line:
				remark = line[4:-1]
				continue

			# 结构体申明
			elif 'struct ' in line:
				content = line.split(' ')
				name = content[1].replace('\n', '')

				# struct begin
				py_line = 'class %s(Structure):\n' % name
				py_line += '\t"""%s"""\n' % remark
				py_line += '\t_fields_ = [\n'

			# 结构体变量
			elif '\t' in line and '///' not in line:
				content = line.split('\t')
				typedef = content[1]
				type_ = typedefDict[typedef]
				variable = content[2].replace(';\n', "")
				# fields
				py_line = '\t\t#%s\n' % remark
				py_line += '\t\t("%s",%s),\n' % (variable, type_)

				#
				if type_.find('c_char*') >= 0:
					#decode遇到特殊字符需处理:0xa3 -> iso-8859-1 乱玛
					py_get += "\tdef get{0}(self):\n\t\treturn str(self.{0}, 'GB2312')\n".format(variable)
					py_str_format += "str(self.{0}, 'GB2312'), ".format(variable)
					py_str += "{0}=\\'{{{1}}}\\', ".format(variable, py_str_idx)
					py_dict += "'{0}':{1},".format(variable, "str(self.{0}, 'GB2312')".format(variable))
				elif type_.find('c_char') >= 0:
					var_type = typedef[typedef.find('Ftdc') + 4:]
					py_get += "\tdef get{0}(self):\n\t\treturn {1}(ord(self.{0}))\n".format(variable, var_type)
					#如何输出enum类型的名字,而非值**某些情况下返回的值为0
					py_str_format += "'' if ord(self.{0}) == 0 else {1}(ord(self.{0})).name, ".format(variable, var_type)
					#py_str_format += "self.{0}, ".format(variable)
					py_str += "{0}={2}.{{{1}}}, ".format(variable, py_str_idx, var_type)
					py_dict += "'{0}':{1},".format(variable, "'' if ord(self.{0}) == 0 else {1}(ord(self.{0})).name".format(variable, var_type))
				else:
					py_get += "\tdef get{0}(self):\n\t\treturn self.{0}\n".format(variable)
					py_str_format += "self.{0}, ".format(variable)
					py_str += "{0}={{{1}}}, ".format(variable, py_str_idx)
					py_dict += "'{0}':{1},".format(variable, "self.{0}".format(variable))
				py_clone += "\t\tobj.{0}=self.{0}\n".format(variable)


				py_str_idx+=1
				#py_str += '{0}={{self.{0}}}, '.format(variable)

			# 结构体结束
			elif '}' in line:
				# struct end
				py_line = '\t\t]\n\n'
				py_line += py_get + '\n'
				#py_line += "\tdef __str__(self):\n\t\treturn '{0}'.format(self=self)\n\n".format(py_str[0:len(py_str)-2])
				py_line += "\tdef __str__(self):\n\t\treturn '{0}'.format({1})\n\n".format(py_str[0:len(py_str) - 2], py_str_format[0:len(py_str_format) - 2])
				py_line += "\t@property\n\tdef __dict__(self):\n\t\treturn {{{0}}}\n\n".format(py_dict[:-1])
				py_line += "\tdef clone(self):\n\t\tobj={0}()\n{1}\t\treturn obj\n\n".format(name, py_clone)

			# 结构体开始
			elif '{' in line:
				py_line = ''
				py_get = ''
				py_str = ''
				py_dict = ''
				py_clone = ''
				py_str_idx = 0
				py_str_format = ''

			# 其他
			else:
				py_line = '\n'
				continue

			fpy.write(py_line)
if __name__ == '__main__':
	GenerateStruct().main()
