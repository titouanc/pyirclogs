from .irssi import irssi_parser
from .weechat import weechat_parser

PARSERS = {
    'irssi': irssi_parser(),
    'weechat': weechat_parser(),
}
