from datetime import datetime
from logging import getLogger
import re

logger = getLogger(__name__)

nick = '([^<-][^ >]+)_*'
date = '\[(\d{2}:\d{2}(\.\d{2})?)\]'
msg = re.compile(date + '\s+<(@|\+|)' + nick + '>\s+(.*)')
action = re.compile(date + '\s+?\*\s+(@|\+|)' + nick + ' (.*)')


def mirc_parser(msg=msg):
    def parse_mirc(iterlines):
        for line in iterlines:
            is_action = True
            m = action.match(line)
            if not m:
                m = msg.match(line)
                is_action = False
            if m:
                time = None
                if len(m.group(1)) == 5:
                    time = datetime.strptime(m.group(1), '%H:%M')
                elif len(m.group(1)) == 8:
                    time = datetime.strptime(m.group(1), '%H:%M.%S')
                else:
                    assert 0==1, "Error parsing time"
                yield {
                    'time': time,
                    'action': is_action,
                    'op': m.group(3),
                    'nick': m.group(4),
                    'text': m.group(5)
                }
                continue
        logger.debug("Skip " + line)

    return parse_mirc
