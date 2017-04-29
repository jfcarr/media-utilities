#!/usr/bin/python3

# Example call: HandBrakeCLI -Z "Very Fast 1080p30" -i "deer.wmv" -o "deer.mp4"

import argparse
import os
import sys

parser = argparse.ArgumentParser()

try:
	parser.add_argument("-f", "--file", type=str, help="name of file to convert")
	args = parser.parse_args()
except Exception as ex:
	print(ex)
	sys.exit(1)

input_file = ""

try:
	if not args.file:
		raise ValueError("You must specify a file to convert.")
	else:
		input_file = args.file

	if not os.path.isfile(input_file):
		raise ValueError(input_file + " not found.")

	input_file_name, input_file_extension = os.path.splitext(input_file)
	output_file = input_file_name + ".mp4"

	supported_extensions = ['.wmv','.avi','.mkv','.webm']
	
	if any(x in input_file_extension for x in supported_extensions):
		full_command = "HandBrakeCLI -Z \"Very Fast 1080p30\" -i \"" + input_file + "\" -o \"" + output_file + "\""
		
		os.system(full_command)
	else:
		raise ValueError(input_file + " is not in a format that can be converted.")
		
except Exception as ex:
	print(ex)
	sys.exit(1)		

