#!/usr/bin/python3

# ffmpeg example:
#  ffmpeg -i input_file.mp4 -acodec copy -vcodec copy -ss 00:11:23 -t 00:00:53 output_file.mp4

import argparse
from datetime import time
import os
import sys

def convert_to_timestamp(seconds):
	min, sec = divmod(seconds, 60)
	hour, min = divmod(min, 60)

	return "%02d:%02d:%02d" % (hour, min, sec)

def total_seconds(hour, minute, second):
	return int(hour)*60*60 + int(minute)*60 + int(second)

if __name__ == '__main__':
	parser = argparse.ArgumentParser()

	parser.add_argument("-f", "--file", type=str, help="Name of input file to slice.")
	parser.add_argument("-s", "--start", type=str, help="Start position for the slice, formatted as HH:MM:SS.  This is optional: if it's not specified, the slice will begin at the beginning of the input file.")
	parser.add_argument("-e", "--end", type=str, help="End position for the slice, formatted as HH:MM:SS.  This is optional: if it's not specified, the slice will end at the end of the input file.")

	args = parser.parse_args()

	if not args.file:
		print("File argument is required.")
		sys.exit(-1)

	split_start = args.start if args.start else "00:00:00"
	split_length = ""

	if args.end:
		hour,minute,second = split_start.split(':')
		start_seconds = total_seconds(hour, minute, second)

		hour,minute,second = args.end.split(':')
		end_seconds = total_seconds(hour, minute, second)

		split_length = convert_to_timestamp(end_seconds - start_seconds)

	length_arg = f"-t {split_length}" if split_length else ""
	output_file = f"{os.path.splitext(args.file)[0]}_output{os.path.splitext(args.file)[1]}"

	cmd_string = f"ffmpeg -i {args.file} -acodec copy -vcodec copy -ss {split_start} {length_arg} {output_file}"

	os.system(cmd_string)
