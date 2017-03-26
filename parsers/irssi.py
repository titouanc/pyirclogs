import re
from dateutil import parser
from logging import getLogger

logger = getLogger(__name__)

log_opened = re.compile(r'--- Log opened (.+)')
day_changed = re.compile(r'--- Day changed (.+)')
nick = '([^ ]+?)_*'
msg = re.compile(r'(\d{2}):(\d{2}) <(@|\+| )%s> (.*)' % nick)
action = re.compile(r'(\d{2}):(\d{2})  \* %s (.*)' % nick)


def irssi_parser(log_opened=log_opened, day_changed=day_changed,
                 msg=msg, action=action):
    def parse_irssi(iterlines):
        for line in iterlines:
            m = log_opened.match(line)
            if not m:
                m = day_changed.match(line)
            if m:
                today = parser.parse(m.group(1)).replace(second=0)
                continue

            m = action.match(line)
            if m:
                yield {
                    'action': True,
                    'op': None,
                    'nick': m.group(3),
                    'text': m.group(4),
                    'time': today.replace(minute=int(m.group(2)),
                                          hour=int(m.group(1))),
                }
                continue

            m = msg.match(line)
            if m:
                yield {
                    'action': False,
                    'op': m.group(3),
                    'nick': m.group(4),
                    'text': m.group(5),
                    'time': today.replace(minute=int(m.group(2)),
                                          hour=int(m.group(1))),
                }
                continue
            logger.debug("Skip " + line)
    return parse_irssi
