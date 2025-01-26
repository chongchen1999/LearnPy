from collections import OrderedDict

# Create an OrderedDict
d = OrderedDict()

# Insert items in a specific order
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4
d['qq'] = 5
d['mahuateng'] = 6
d['leijun'] = 7
d['musk'] = 8
d['01'] = 9

# Iterate over the OrderedDict
for key in d:
    print(key, d[key])

import json

# Convert the OrderedDict to a JSON string
json_string = json.dumps(d)
print(json_string)