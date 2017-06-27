#!usr/bin/env python
# -*- coding: utf-8 -*

import sys
import os
import datetime

class RecordType:
	SENSOR_FILL_RECORD_TYPE = 0
  	SENSOR_INIT_RECORD_TYPE = 1
	SENSOR_START_RECORD_TYPE = 2
	SENSOR_HYDRTDATA_RECORD_TYPE = 3
	SENSOR_CALIB_RECORD_TYPE = 4
	SENSOR_STOP_RECORD_TYPE = 5
	SENSOR_EA_RECORD_TYPE = 6
	SENSOR_BLOCK_INIT_RECORD_TYPE = 7
	SENSOR_STABLEDATA_RECORD_TYPE = 8
	SENSOR_STABLE_NOCALIB_DATA_RECORD_TYPE = 9
	SENSOR_CAL0DATA_RECORD_TYPE = 10
	SENSOR_CAL1DATA_RECORD_TYPE = 11
	
class HistoryAnalyzer(object):
	"""
	analyze history data of PDM.
	"""
	FILE_HEAD_SIZE = 28
	SETTING_DATA_MASK = 1
	PUMP_DATA_MASK = 2
	SENSOR_DATA_MASK = 4
	HISTORY_RECORD_HEAD_SIZE = 12
	
	def __init__(self, file_name):
		self.file_name = file_name
		#self.device_id = 0
		#self.account_id = 0
		#self.whole_data = []
		#self.sensor_data = []
		#self.setting_data = []
		#self.pump_data = []
		print "Construct"
		print file_name
		try:
			history_file = open(file_name, 'rb')
		except IOError:
			print "IO Error"
			return
		
		file_buffer = history_file.read(-1);
		#file_size = len(file_buffer)
		#self.whole_data = list(file_buffer)
		self.whole_data = file_buffer
		history_file.close()
		
		if len(self.whole_data) < self.FILE_HEAD_SIZE:
			print "file is too small"
			return
		self.file_version = self.whole_data[0:6]
		print self.file_version
		
		# 版本判断
		if self.file_version == "MTD01a":
			pass
			
		# 后续处理
		# 提取设备ID
		offset = 6
		self.device_id = ord(self.whole_data[offset]) + \
						(ord(self.whole_data[offset+1]) << 8) + \
						(ord(self.whole_data[offset+2]) << 16) + \
						(ord(self.whole_data[offset+3]) << 24);				
		print "device_id:", self.device_id
		offset += 4
						
		# 提取账户ID
		self.account_id = ord(self.whole_data[offset]) + \
						(ord(self.whole_data[offset+1]) << 8) + \
						(ord(self.whole_data[offset+2]) << 16) + \
						(ord(self.whole_data[offset+3]) << 24);
		print "account_id:", self.account_id
		offset += 4
		
		# 提取数据类型
		self.data_type = ord(self.whole_data[offset]) + \
						(ord(self.whole_data[offset+1]) << 8);
		print "data_type:", self.data_type
		offset += 2
		
		# 提取设备设置数据长度
		self.setting_data_size = ord(self.whole_data[offset]) + \
						(ord(self.whole_data[offset+1]) << 8) + \
						(ord(self.whole_data[offset+2]) << 16) + \
						(ord(self.whole_data[offset+3]) << 24);
		print "setting_data_size:", self.setting_data_size
		offset += 4	
		
		# 提取泵数据长度
		self.pump_data_size = ord(self.whole_data[offset]) + \
						(ord(self.whole_data[offset+1]) << 8) + \
						(ord(self.whole_data[offset+2]) << 16) + \
						(ord(self.whole_data[offset+3]) << 24);
		print "pump_data_size:", self.pump_data_size
		offset += 4	
		
		# 提取传感器数据长度
		self.sensor_data_size = ord(self.whole_data[offset]) + \
						(ord(self.whole_data[offset+1]) << 8) + \
						(ord(self.whole_data[offset+2]) << 16) + \
						(ord(self.whole_data[offset+3]) << 24);
		print "sensor_data_size:", self.sensor_data_size
		offset += 4			
		
		# 提取设备设置数据
		if self.data_type & self.SETTING_DATA_MASK:
			self.setting_data = \
				self.whole_data[offset:(offset + self.setting_data_size)]
			offset += self.setting_data_size
		
		# 提取泵数据
		if self.data_type & self.PUMP_DATA_MASK:
			self.pump_data = \
				self.whole_data[offset:(offset + self.pump_data_size)]
			offset += self.pump_data_size
		
		# 提取传感器数据
		if self.data_type & self.SENSOR_DATA_MASK:
			self.sensor_data = \
				self.whole_data[offset:(offset + self.sensor_data_size)]
			offset += self.sensor_data_size

	def rawRecord(self, type):
		index = 0
		data_size = 0
		head_flag = 0
		data_ref = ''
		raw_record = ''
		#print dir(self)
		if "sensor" == type:
			if 'sensor_data' in dir(self):
				data_size = len(self.sensor_data)
				head_flag = 0xBB
				data_ref = self.sensor_data
			else:
				return
		elif "pump" == type:
			if 'pump_data' in dir(self):
				data_size = len(self.pump_data)
				head_flag = 0xAA
				data_ref = self.pump_data				
			else:
				return
		else:
			return;
		
		while index < data_size:
			if (head_flag == ord(data_ref[index+0])):
				raw_record_size = ord(data_ref[index+1])
				yield data_ref[index:(index+raw_record_size)]
				index += raw_record_size
			else:
				raise StopIteration()
	
	def glucoseRecord(self):
		for record in self.rawRecord("sensor"):
			record_type = ord(record[2])
			offset = 6
			year = (ord(record[offset]) << 8) + ord(record[offset + 1])
			month = ord(record[offset+2])
			day = ord(record[offset+3])
			hour = ord(record[offset+4])
			minute = ord(record[offset+5])
			#timeinterval = 
			if record_type == RecordType.SENSOR_HYDRTDATA_RECORD_TYPE or \
			   record_type == RecordType.SENSOR_STABLEDATA_RECORD_TYPE or \
			   record_type == RecordType.SENSOR_STABLE_NOCALIB_DATA_RECORD_TYPE or \
			   record_type == RecordType.SENSOR_CAL0DATA_RECORD_TYPE or \
			   record_type == RecordType.SENSOR_CAL1DATA_RECORD_TYPE:
				#print len(record)
				
				offset = self.HISTORY_RECORD_HEAD_SIZE
				num = (ord(record[offset]) << 8) + ord(record[offset+1]);
				offset += 2
				calib_ratio = (ord(record[offset]) << 8) + ord(record[offset+1]);
				bg_unit = (calib_ratio >> 14) & 0x03
				calib_ratio = calib_ratio & 0x3fff
				offset += 2
				#print record_type, num, bg_unit, calib_ratio
				
				dt = datetime.datetime(year,month,day,hour,minute)
				#print dt.strftime("%Y-%m-%d %H:%M:%S"),record_type, num, bg_unit, calib_ratio
				#datetime.datetime()
				i = num
				while i > 0:
					point_dt = dt + datetime.timedelta(minutes=(i-1)*2)
					sensor_signal = (ord(record[offset + (i-1)*2]) << 8) + \
							ord(record[offset+(i-1)*2+1]);
					#print point_dt.strftime("%Y-%m-%d %H:%M:%S"),record_type, sensor_signal, bg_unit, calib_ratio
					yield point_dt.strftime("%Y-%m-%d %H:%M:%S"),record_type, sensor_signal, bg_unit, calib_ratio
					i = i - 1
					
if __name__ == '__main__':
	print "test 001"
	#print HistoryAnalyzer.__doc__
	if 2 == len(sys.argv):
		print os.path.join(os.getcwd(), sys.argv[1])  
	else:
		print "input file name"
		sys.exit(0)	
	file_name = os.path.join(os.getcwd(), sys.argv[1])
	#str = "sdfef"
	ana = HistoryAnalyzer(file_name)
	#ana.rawRecord("sensor")
	#print list(str)
	#for record in ana.rawRecord("sensor"):
	#	print list(record)
	for record in ana.glucoseRecord():
		print record