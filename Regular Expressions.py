import re

phoneNumberRegex = re.compile(r'/d{4}')
mo = phoneNumberRegex.search('My number is 503-894-1880')
mo.group(0)