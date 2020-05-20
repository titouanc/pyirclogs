from datetime import datetime
from logging import getLogger
import re

logger = getLogger(__name__)

nick = '([^<-][^ ]*?)_*'
date = '(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})'
modechars = '(@|\+|~|&|%|)'
msg = re.compile(date + '\s+?' + modechars + nick + '\s+(.*)')
action = re.compile(date + '\s+?\*\s+' + modechars + nick + ' (.*)')


def weechat_parser(msg=msg):
    def parse_weechat(iterlines):
        for line in iterlines:
            is_action = True
            m = action.match(line)
            if not m:
                m = msg.match(line)
                is_action = False
            if m:
                yield {
                    'time': datetime.strptime(m.group(1), '%Y-%m-%d %H:%M:%S'),
                    'action': is_action,
                    'op': m.group(2),
                    'nick': m.group(3),
                    'text': m.group(4)
                }
                continue
        logger.debug("Skip " + line)

    return parse_weechat
