# MCSS
# Multi Channel Sound System. A file format for storing multi channel sound
# Github: https://www.github.com/0x4248/MCSS
# Author: Lewis Evans
# Licence: GNU General Public Licence v3.0

import binascii

VERSION = "1"
MAGIC_NUMBER = b"4d435353"
START_METADATA = b"0F0F990F0F"
END_METADATA = b"0F0F550F0F"
START_TAGS = b"0F0FAA0F0F"
END_TAGS = b"0F0FBB0F0F"
START_CHANNEL = b"0F0FCC0F0F"
END_CHANNEL = b"0F0FDD0F0F"


def compile_from_raw(data,tags,metadata=[]):
    """Compiles a MCSS file from raw bytes encoded in wav format.

    Args:
        data (array[bytes]): The raw bytes of the wav file.
        tags (tuple[strings]): The tags for each channel.
        metadata (array[strings], optional): The metadata for the file.

    Note:
        The tags are stored in the file in the order they are in the array and
        should look like [["example=example","other_tag=other"],["example2=example2"]]. The
        metadata is stored in the file in the order it is in the array and
        should look like ["example=example","example2=example2"].

        This also apply's to the metadata.
    """
    if len(tags) != len(data):
        raise ValueError("There must be a tag for each channel you can leave blank tags like [[], [], [], []]")
    compiled = binascii.unhexlify(MAGIC_NUMBER)
    compiled += " VERSION:".encode()+VERSION.encode()
    compiled += binascii.unhexlify(START_METADATA)
    compiled += str(metadata).encode()
    compiled += binascii.unhexlify(END_METADATA)
    compiled += binascii.unhexlify(START_TAGS)
    compiled += str(tags).encode()
    compiled += binascii.unhexlify(END_TAGS)
    for channel in data:
        compiled += binascii.unhexlify(START_CHANNEL)
        compiled += channel
        compiled += binascii.unhexlify(END_CHANNEL)
    return compiled


def extract_audio(data):
    """Extracts the audio from a MCSS file.

    Args:
        data (bytes): The raw bytes of the MCSS file.

    Returns:
        array[bytes]: The raw bytes of the wav files.
    """
    audio = []
    for channel in data.split(binascii.unhexlify(START_CHANNEL))[1:]:
        audio.append(channel.split(binascii.unhexlify(END_CHANNEL))[0])
    return audio

def extract_tags(data):
    """Extracts the tags from a MCSS file.

    Args:
        data (bytes): The raw bytes of the MCSS file.

    Returns:
        tuple[list[str], list[str]]: Two lists containing tags for each channel and metadata.
    """
    tags = []
    metadata = []
    tags_section = data.split(binascii.unhexlify(START_TAGS))[1]
    tags_data = tags_section.split(binascii.unhexlify(END_TAGS))[0].decode()
    tags_data = eval(tags_data)
    for tag_set in tags_data:
        tags.append(tag_set)
    return tags

def extract_metadata(data):
    """Extracts the metadata from a MCSS file.

    Args:
        data (bytes): The raw bytes of the MCSS file.

    Returns:
        list[str]: The metadata as a list of strings.
    """
    metadata = []
    metadata_section = data.split(binascii.unhexlify(START_METADATA))[1]
    metadata_data = metadata_section.split(binascii.unhexlify(END_METADATA))[0].decode()
    metadata_data = eval(metadata_data)
    for meta in metadata_data:
        metadata.append(meta)
    return metadata
