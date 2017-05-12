from collections import namedtuple

from .parsers import PARSERS

# Force map to be lazy
from sys import version_info
if version_info.major < 3:
    from itertools import imap as map

Message = namedtuple('Message', ['time', 'nick', 'op', 'text', 'action'])


def parse(lines, parser='irssi'):
    if isinstance(parser, str) or isinstance(parser, unicode):
        parser = PARSERS[parser]
    return map(lambda d: Message(**d), parser(lines))


def parse_file(filename, parser='irssi', encoding='utf-8'):
    def decode_line(line):
        return line.decode(encoding).strip()

    lines = map(decode_line, open(filename, 'rb'))
    return parse(lines, parser=parser)
