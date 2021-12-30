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
