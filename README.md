# roku-media-conversion

## Description

The only consistently supported file format (for video files on flash drives) on the Roku 3+ is .mp4.  This script provides a couple of quick ways to convert various video files to .mp4 format.  (You'll need to install `Python 3` and the latest version of [Handbrake](https://handbrake.fr/) before using it.  This also assumes you're using Linux, as it relies on `chmod`.

## Usage

Convert a single file like this:

```bash
rokuconvert.py -f <input_file>
```

Generate a script (rconvert.sh) to convert all supported file formats in the current directory like this:

```bash
rokuconvert.py -s
```
