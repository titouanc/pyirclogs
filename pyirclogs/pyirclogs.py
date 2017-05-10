from .parsers import PARSERS


def parse(lines, parser='irssi', encoding='utf-8'):
    def decode_line(line):
        return line.decode(encoding).strip()

    if isinstance(parser, str) or isinstance(parser, unicode):
        parser = PARSERS[parser]
    return parser(map(decode_line, lines))


def parse_file(filename, *args, **kwargs):
    return parse(open(filename, 'rb'), *args, **kwargs)
