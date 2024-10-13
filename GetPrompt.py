import json

data_name = 'wikigold'

path = ''
with open(path, 'r') as f:
    data = json.load(f)
for i in range(20):
    print(data[i]['prompt'])
    print('=' * 50)
    print('\n\n\n')