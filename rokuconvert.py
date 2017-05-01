#!/usr/bin/python3

import argparse
import glob
import os
import sys

class CRoku:
	def __init__(self, _converterName, _converterPreset, _supported_extensions):
		self.ConverterName = _converterName
		self.ConverterPreset = _converterPreset
		self.SupportedExtensions = _supported_extensions

	def ConvertFile(self, input_file):
		if not os.path.isfile(input_file):
			raise ValueError(input_file + " not found.")

		input_file_name, input_file_extension = os.path.splitext(input_file)
		output_file = input_file_name + ".mp4"

		if any(x in input_file_extension for x in self.SupportedExtensions):
			full_command = self.ConverterName + " " + self.ConverterPreset + " -i \"" + input_file + "\" -o \"" + output_file + "\""
			
			os.system(full_command)
		else:
			raise ValueError(input_file + " is not in a format that can be converted.")	

	def GenerateScript(self):
		fp1 = open('rconvert.sh', 'w')
		print("#!/bin/bash", file=fp1)
		print("", file=fp1)
		for extension in self.SupportedExtensions:
			filenames = glob.glob('*' + extension)
			for filename in filenames:
				input_file_name, input_file_extension = os.path.splitext(filename)
				output_file = input_file_name + ".mp4"
				execCommand = self.ConverterName + " " + self.ConverterPreset + " -i \"" + filename + "\" -o \"" + output_file + "\""
				print(execCommand, file=fp1)
		fp1.close()
		os.system("chmod u+x rconvert.sh")

if __name__ == '__main__':
	parser = argparse.ArgumentParser()

	try:
		parser.add_argument("-f", "--file", type=str, help="name of file to convert")
		parser.add_argument("-s", "--script", help="generate conversion script", action="store_true")
		args = parser.parse_args()
	except Exception as ex:
		print(ex)
		sys.exit(1)

	myRoku = CRoku('HandBrakeCLI','-Z "Very Fast 1080p30"', ['.avi','.mkv','.mov','.webm','.wmv'])

	try:
		if args.script:
			myRoku.GenerateScript()
			sys.exit(0)

		if args.file:
			myRoku.ConvertFile(args.file)
			sys.exit(0)
	except Exception as ex:
		print(ex)
		sys.exit(1)

	print("Not sure what you want to do...")
