#!/usr/bin/python3

# Example call: HandBrakeCLI -Z "Very Fast 1080p30" -i "deer.wmv" -o "deer.mp4"

import argparse
import glob
import os
import sys

supported_extensions = ['.avi','.mkv','.webm','.wmv']

def ConvertFile(filename):
	if not os.path.isfile(input_file):
		raise ValueError(input_file + " not found.")

	input_file_name, input_file_extension = os.path.splitext(input_file)
	output_file = input_file_name + ".mp4"

	if any(x in input_file_extension for x in supported_extensions):
		full_command = "HandBrakeCLI -Z \"Very Fast 1080p30\" -i \"" + input_file + "\" -o \"" + output_file + "\""
		
		os.system(full_command)
	else:
		raise ValueError(input_file + " is not in a format that can be converted.")	

def GenerateScript():
	fp1 = open('rconvert.sh', 'w')
	print("#!/bin/bash", file=fp1)
	print("", file=fp1)
	for extension in supported_extensions:
		filenames = glob.glob('*' + extension)
		for filename in filenames:
			input_file_name, input_file_extension = os.path.splitext(filename)
			output_file = input_file_name + ".mp4"
			execCommand = "HandBrakeCLI -Z \"Very Fast 1080p30\" -i \"" + filename + "\" -o \"" + output_file + "\""
			print(execCommand, file=fp1)
	fp1.close()
	sys.exit(0)

parser = argparse.ArgumentParser()

try:
	parser.add_argument("-f", "--file", type=str, help="name of file to convert")
	parser.add_argument("-s", "--script", help="generate conversion script", action="store_true")
	args = parser.parse_args()
except Exception as ex:
	print(ex)
	sys.exit(1)

if args.script:
	GenerateScript()

input_file = ""

try:
	if not args.file:
		raise ValueError("You must specify a file to convert.")
	else:
		input_file = args.file

	ConvertFile(input_file)
		
except Exception as ex:
	print(ex)
	sys.exit(1)		

