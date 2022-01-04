# Media Utilities

## convert-to-mp4

### Description

The only consistently supported file format (for video files on flash drives) on the Roku 3+ is .mp4.  This format can also be quickly transcoded by Plex.

This script provides a couple of quick ways to convert various video files to .mp4 format.  This assumes you're using Linux, as it relies on `chmod`.

### Requirements

* Python 3
  * argparse package for Python 3 (`pip3 install argparse`)
* Latest version of [Handbrake](https://handbrake.fr/)

### Usage

Convert a single file like this:

```bash
convert-to-mp4.py -f <input_file>
```

Get info about an input file, but don't convert it, like this:

```bash
convert-to-mp4.py -f <input_file> -i
```

Generate a script (video-convert.sh) to convert all supported file formats in the current directory like this:

```bash
convert-to-mp4.py -s
```

## slice-video

### Description

Extracts a slice of an input video.

### Requirements

* Python 3
  * argparse package for Python 3 (`pip3 install argparse`)
* ffmpeg

### Usage

Example, extracting a video slice from source.mp4, starting at 5 seconds into the input video, and ending at 27 seconds into the input video:

```bash
slice-video.py -f source.mp4 -s 00:00:05 -e 00:00:27
```

The output will be written to source_output.mp4.
