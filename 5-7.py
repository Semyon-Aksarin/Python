import json

profit = []
average_dict = {}
my_dict = {}
temp = []

with open('text_7.txt', 'r', encoding="utf-8") as f_obj:
    for line in f_obj:
        n = line.split()
        profit.append(int(n[2]) - int(n[3]))
        my_dict[n[0]] = int(n[2]) - int(n[3])

for i in profit:
    if i > 0:
        temp.append(i)

average_profit = sum(temp) / len(temp)
average_dict['average_profit'] = average_profit

total = [my_dict, average_dict]
print(total)

with open('file_7.json', 'w') as write_js:
    json.dump(total, write_js)

    js_str = json.dumps(total)
