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

	def ConvertFile(self, input_file, info_only):
		# Make sure the file exists.
		if not os.path.isfile(input_file):
			raise ValueError(input_file + " not found.")

		# Split out the pieces of the input file name, and build the output file name.
		input_file_name, input_file_extension = os.path.splitext(input_file)
		if input_file_extension == ".mp4":
			output_file = input_file_name + "_new.mp4"
		else:
			output_file = input_file_name + ".mp4"

		# Is the input file supported as a conversion target?
		if any(x in input_file_extension for x in self.SupportedExtensions) or info_only:
			if info_only:
				full_command = self.ConverterName + " " + self.ConverterPreset + " --scan -i \"" + input_file + "\""
			else:
				full_command = self.ConverterName + " " + self.ConverterPreset + " -i \"" + input_file + "\" -o \"" + output_file + "\""
			
			os.system(full_command)
		else:
			raise ValueError(input_file + " is not in a format that can be converted.")	

	def GenerateScript(self):
		# Open the script file for writing, and write out the crunch-bang line for bash
		fp1 = open('rconvert.sh', 'w')
		print("#!/bin/bash", file=fp1)
		print("", file=fp1)

		# For each supported extension, find matching files, then write out a conversion line in this format:
		# HandBrakeCLI -Z "Very Fast 1080p30" -i "<inputfile>" -o "<outputfile>"
		for extension in self.SupportedExtensions:
			filenames = glob.glob('*' + extension)
			for filename in filenames:
				input_file_name, input_file_extension = os.path.splitext(filename)
				if input_file_extension == ".mp4":
					output_file = input_file_name + "_new.mp4"
				else:
					output_file = input_file_name + ".mp4"
				execCommand = self.ConverterName + " " + self.ConverterPreset + " -i \"" + filename + "\" -o \"" + output_file + "\""
				print(execCommand, file=fp1)
		fp1.close()
		os.system("chmod u+x rconvert.sh")

def main(args):
	parser = argparse.ArgumentParser()

	try:
		parser.add_argument("-f", "--file", type=str, help="name of file to convert")
		parser.add_argument("-i", "--info", help="show information about the input file, but do not convert it", action="store_true")
		parser.add_argument("-s", "--script", help="generate conversion script", action="store_true")
		args = parser.parse_args()
	except Exception as ex:
		print(ex)
		sys.exit(1)

	myRoku = CRoku('HandBrakeCLI','-Z "Very Fast 1080p30"', ['.avi','.mkv','.mov', '.mp4','.webm','.wmv'])

	try:
		if args.script:
			myRoku.GenerateScript()
			sys.exit(0)

		if args.file:
			myRoku.ConvertFile(args.file, args.info)
			sys.exit(0)
	except Exception as ex:
		print(ex)
		sys.exit(1)

	print("Not sure what you want to do...")

if __name__ == '__main__':
	sys.exit(main(sys.argv))
