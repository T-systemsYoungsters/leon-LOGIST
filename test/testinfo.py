import json

# data = {
#     'Deutschland' : 'Berlin',
#     'UK' : 'London',
#     'China' : 'Beijing',
#     'Kitten' : 123
# }

# with open('test_data.txt', 'w') as test_file:
#     json.dump(data, test_file)

with open('test_data.txt') as test_file:
    data = json.load(test_file)

for entry in data.items():
    print(entry)