# MCSS

Multi channel sound system

This is the repository for the MCSS project. The project is a python module that compiles and parses multi channel sound system files (.mcss). The module is used to create a multi channel sound system from using .wav files and each channel can be given a tag to identify it.

## Examples of tags

Lets say we have 5 wav files that have different audio on them. We can add tags to better identify them and configure them for the application that we are using. Lets say the program has a option where you can add echo to a track and we want to put it on to chanel 3. We can add a tag to the channel and then use the tag to add the echo effect to the channel like this:

```
[["name=chanel1"], ["name=chanel2"], ["name=chanel3", "echo=true"], ["name=chanel4"], ["name=chanel5"]]
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
tags = [["name=chanel1"], ["name=chanel2"]]
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

## Installation

To install the module you need to clone the repository and then place the MCSS folder to where you want to use it.

## Licence

This project is under the GNU General Public License v3.0 - see the [LICENCE](LICENCE) file for details
