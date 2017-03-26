# pyirclogs

A python lib to read your irc logs.

* Iterator based
* Flexible parsers


## Example

```python
from itertools import chain
from pyirclogs import parse_file

logs = list(chain(
    parse_file('awesomechan-irssi.log', parser='irssi'),
    parse_file('awesomechan-weechat.log', parser='weechat')
))

for msg in logs:
    print(msg)
```

