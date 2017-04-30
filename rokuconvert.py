#!/usr/bin/python3

import argparse
import glob
import os
import sys

_converterName = 'HandBrakeCLI'
_converterPreset = ' -Z "Very Fast 1080p30" '
_supported_extensions = ['.avi','.mkv','.webm','.wmv']

def ConvertFile(input_file):
	if not os.path.isfile(input_file):
		raise ValueError(input_file + " not found.")

	input_file_name, input_file_extension = os.path.splitext(input_file)
	output_file = input_file_name + ".mp4"

	if any(x in input_file_extension for x in _supported_extensions):
		full_command = _converterName + _converterPreset + "-i \"" + input_file + "\" -o \"" + output_file + "\""
		
		os.system(full_command)
	else:
		raise ValueError(input_file + " is not in a format that can be converted.")	

def GenerateScript():
	fp1 = open('rconvert.sh', 'w')
	print("#!/bin/bash", file=fp1)
	print("", file=fp1)
	for extension in _supported_extensions:
		filenames = glob.glob('*' + extension)
		for filename in filenames:
			input_file_name, input_file_extension = os.path.splitext(filename)
			output_file = input_file_name + ".mp4"
			execCommand = _converterName + _converterPreset + "-i \"" + filename + "\" -o \"" + output_file + "\""
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

	try:
		if args.script:
			GenerateScript()
			sys.exit(0)

		if args.file:
			ConvertFile(args.file)
			sys.exit(0)
	except Exception as ex:
		print(ex)
		sys.exit(1)

	print("Not sure what you want to do...")
