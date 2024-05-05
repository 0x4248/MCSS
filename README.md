# MCSS

Multi channel sound system

> This project meets the [Open Source File Format Standard](https://www.github.com/0x4248/OSFFS).

This is the repository for the MCSS project. The project is a python module that compiles and parses multi channel sound system files (.mcss). The module is used to create a multi channel sound system from using .wav files and each channel can be given a tag to identify it.

## Examples of tags

Lets say we have 5 wav files that have different audio on them. We can add tags to better identify them and configure them for the application that we are using. Lets say the program has a option where you can add echo to a track and we want to put it on to channel 3. We can add a tag to the channel and then use the tag to add the echo effect to the channel like this:

```
[["name=channel1"], ["name=channel2"], ["name=channel3", "echo=true"], ["name=channel4"], ["name=channel5"]]
```

Adding tags is optional to leave a `.mcss` file tags blank just put 

```
[[], [], [], [], []]
```

## Metadata

Exactly the same as normal metadata you would put on a file.

Example:

```
["title=Song", "artist=Artist", "album=Album", "year=Year", "genre=Genre"]
```

This is optional to leave a `.mcss` file metadata blank just put 

```
[]
```

by default MCSS will leave the metadata blank if you don't specify any.

## Usage

To use the module you need to import it into your python file like this:

```python
import MCSS
```

Then you can use the module like this:

```python
audio_1 = open("audio_1.wav", "rb").read()
audio_2 = open("audio_2.wav", "rb").read()
tags = [["name=channel1"], ["name=channel2"]]
metadata = ["title=My Multi Channel Song"]
mcss_file = MCSS.compile([audio_1, audio_2], tags, metadata)
open("song.mcss", "wb").write(mcss_file)
```

You can extract tags and metadata from a `.mcss` file like this:

```python
mcss_file = open("song.mcss", "rb").read()
tags = MCSS.extract_tags(mcss_file)
metadata = MCSS.extract_metadata(mcss_file)
```

You can extract audio from a `.mcss` file like this:

```python
mcss_file = open("song.mcss", "rb").read()
audio = MCSS.extract_audio(mcss_file)
```

When you extract the audio it will be in a list of bytes objects. You can then write the audio to a file like this:

```python
audio = MCSS.extract_audio(mcss_file)
open("audio_1.wav", "wb").write(audio[0])
open("audio_2.wav", "wb").write(audio[1])
```

## File format

This file format is used to store multi channel sound data and is used by MCSS.

### File structure

The magic identifier lets other programs know its a MCSS file. The File then has a `VERSION:` part this is the version of the file format. Then the start metadata number is placed in the file and the mata data is placed in a python like list `["title=My Multi Channel Song","artist=John Doe"]`. This is then followed by a end metadata number. Then the start tags number is placed in the file with the tags like this `[["name=channel1"], ["name=channel2"]]. This is then followed by a end tags number. Then for each channel there is a start channel number with audio data (commonly in WAV) and then a end channel number. The end of the file is defined where there is no more data.

### Magic numbers

There are `6` amount of magic numbers in this file format.

| Magic number             | Description             |
| ------------------------ | ----------------------- |
| `4d435353`               | Magic identifier        |
| `0F0F990F0F`             | Start metadata          |
| `0F0F550F0F`             | End metadata            |
| `0F0FAA0F0F`             | Start tags              |
| `0F0FBB0F0F`             | End tags                |
| `0F0FCC0F0F`             | Start channel           |
| `0F0FDD0F0F`             | End channel             |

## Installation

To install the module you need to clone the repository and then place the MCSS folder to where you want to use it.

## Pre-requisites

This module requires Python 3.6 or higher to run.

## Licence

This project is under the GNU General Public License v3.0 - see the [LICENCE](LICENCE) file for details
