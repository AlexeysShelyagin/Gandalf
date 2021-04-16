#import json

#data = json.loads( open('Data.json', 'r').read() )

#print(data)

from datetime import datetime
t = datetime.now().time()
print(t)
print(t.minute)
print(t.second)