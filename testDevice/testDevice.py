import RPi.GPIO as GPIO
import time
import sys

import serial
from pexpect_serial import SerialSpawn
import pexpect

import chardet

# pin 6
Pin_Relay = 6


# GPIO.setmode(GPIO.BOARD)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(Pin_Relay, GPIO.OUT)

def main():
	with serial.Serial('/dev/ttyAMA0', 115200, timeout=0) as ser:
		ss = SerialSpawn(ser)
		total_cnt = 0
		success_cnt = 0
		fail_cnt = 0

		GPIO.output(Pin_Relay, GPIO.LOW)

		f = open("./logfile1.txt", 'a')

		while True:
			# try:
			# 	a = ss.expect('SCHNEIDER2 login:')
			# 	ss.sendline('root')

			# 	b = ss.expect('root@SCHNEIDER2:')
			# 	ss.sendline('poweroff')

			# 	GPIO.output(Pin_Relay, GPIO.HIGH)
			# 	time.sleep(2)
			# 	GPIO.output(Pin_Relay, GPIO.LOW)
			# 	time.sleep(2)
			# except TIMEOUT:
			# 	a = ss.expect('SCHNEIDER2 login:')
			# 	ss.sendline('root')

			# 	b = ss.expect('root@SCHNEIDER2:')
			# 	ss.sendline('poweroff')

			# 	GPIO.output(Pin_Relay, GPIO.HIGH)
			# 	time.sleep(2)
			# 	GPIO.output(Pin_Relay, GPIO.LOW)
			# 	time.sleep(2)

			# ser_bytes = ser.readline()
			# print(ser_bytes)

			start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

			ss.expect(pattern='SCHNEIDER2 login:', timeout=10000)
			ss.sendline('root')
			# print(ss.before)

			# ser_bytes = ser.readline()
			# print(ser_bytes)

			# ser_bytes = ser.readline()
			# print(ser_bytes)

			ss.expect(pattern='root@SCHNEIDER2:', timeout=10000)
			ss.sendline('poweroff')
			# print(ss.before)
			
			'''record log'''
			# data = ss.before
			# ret = chardet.detect(data)
			# print(ret)
			# s = str(data, encoding = "ascii")  
			# print(type(data))
			# print(type(s))
			# f.write(s)

			total_cnt = total_cnt + 1

			index = ss.expect(pattern=['Trying to boot from MMC1', pexpect.TIMEOUT], timeout=30)
			if(index==0):
				fail_cnt = fail_cnt + 1
				print('This test is\033[1;31m fail\033[0m!')
				ss.expect(pattern='SCHNEIDER2 login:', timeout=10000)
				ss.sendline('root')
				# print(ss.before)
				ss.expect(pattern='root@SCHNEIDER2:', timeout=10000)
				ss.sendline('poweroff')
				# print(ss.before)
				time.sleep(20)
				f.write("This test is fail!")
				f.write("\r\n")

			elif(index==1):
				success_cnt = success_cnt + 1
				print("This test is successful!")
				f.write("This test is successful!")
				f.write("\r\n")

			end_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
			print("total_cnt   :", total_cnt)
			print("success_cnt :", success_cnt)
			print("fail_cnt    :", fail_cnt)
			print("start time  :", start_time)
			print("end time    :", end_time)
			print("------------------------------------------------------\n")

			f.write("total_cnt   :" + str(total_cnt))
			f.write("\r\n")
			f.write("success_cnt :" + str(success_cnt))
			f.write("\r\n")
			f.write("fail_cnt    :" + str(fail_cnt))
			f.write("\r\n")
			f.write("start time  :" + start_time)
			f.write("\r\n")
			f.write("end time    :" + end_time)
			f.write("\r\n")
			f.write("------------------------------------------------------\r\n")
			f.write("\r\n")

			time.sleep(20)
			GPIO.output(Pin_Relay, GPIO.HIGH)
			time.sleep(5)
			GPIO.output(Pin_Relay, GPIO.LOW)

			# output = ss.read()
			# print(output)

			# ss.logfile = logFileId
			# time.sleep(2)


			# ss.logfile = sys.stdout

			# print(ss.before)

if __name__ == "__main__":
	main()