#!/usr/bin/python3

import argparse
import glob
import os
import sys

class CConverter:
	def __init__(self, _converter_name, _converter_preset, _supported_extensions):
		self.converter_name = _converter_name
		self.converter_preset = _converter_preset
		self.supported_extensions = _supported_extensions

	def convert_file(self, input_file, info_only):
		# Make sure the file exists.
		if not os.path.isfile(input_file):
			raise ValueError(f"{input_file} not found.")

		# Split out the pieces of the input file name, and build the output file name.
		input_file_name, input_file_extension = os.path.splitext(input_file)
		if input_file_extension == ".mp4":
			output_file = f"{input_file_name}_new.mp4"
		else:
			output_file = f"{input_file_name}.mp4"

		# Is the input file supported as a conversion target?
		if any(x in input_file_extension for x in self.supported_extensions) or info_only:
			if info_only:
				full_command = f"{self.converter_name} {self.converter_preset} --scan -i \"{input_file}\""
			else:
				full_command = f"{self.converter_name} {self.converter_preset} -i \"{input_file}\" -o \"{output_file}\""
			
			os.system(full_command)
		else:
			raise ValueError(f"{input_file} is not in a format that can be converted.")	

	def generate_script(self, reconvert):
		# Open the script file for writing, and write out the crunch-bang line for bash
		fp1 = open('video-convert.sh', 'w')
		print("#!/bin/bash", file=fp1)
		print("", file=fp1)

		# For each supported extension, find matching files, then write out a conversion line in this format:
		# HandBrakeCLI -Z "Very Fast 1080p30" -i "<inputfile>" -o "<outputfile>"
		for extension in self.supported_extensions:
			filenames = glob.glob(f"*{extension}")
			for filename in filenames:
				input_file_name, input_file_extension = os.path.splitext(filename)
				output_file = ""
				if input_file_extension == ".mp4":
					if reconvert == True:
						output_file = f"{input_file_name}_new.mp4"
				else:
					output_file = f"{input_file_name}.mp4"
				if not output_file == "":
					execCommand = f"{self.converter_name} {self.converter_preset} -i \"{filename}\" -o \"{output_file}\""
					print(execCommand, file=fp1)
		fp1.close()
		os.system("chmod u+x video-convert.sh")

def main(args):
	parser = argparse.ArgumentParser()

	try:
		parser.add_argument("-f", "--file", type=str, help="name of file to convert")
		parser.add_argument("-i", "--info", help="show information about the input file, but do not convert it", action="store_true")
		parser.add_argument("-s", "--script", help="generate conversion script", action="store_true")
		parser.add_argument("-sx", "--scriptnomp4", help="generate conversion script WITHOUT .mp4 reconversion", action="store_true")
		args = parser.parse_args()
	except Exception as ex:
		print(ex)
		sys.exit(1)

	my_converter = CConverter('HandBrakeCLI','-Z "Very Fast 1080p30"', ['.3gp','.flv','.avi','.AVI','m4v','.mkv','.mov', '.mp4','.mpg','.ogv','.webm','.wmv'])

	try:
		if args.script:
			my_converter.generate_script(True)
			sys.exit(0)

		if args.scriptnomp4:
			my_converter.generate_script(False)
			sys.exit(0)

		if args.file:
			my_converter.convert_file(args.file, args.info)
			sys.exit(0)
	except Exception as ex:
		print(ex)
		sys.exit(1)

	print("Not sure what you want to do...")

if __name__ == '__main__':
	sys.exit(main(sys.argv))
