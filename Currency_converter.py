with open('demo.txt') as f:
    a = f.readlines()

parsed_dict = {}
for row in a:
    parsed = row.split('\t')
    parsed_dict[parsed[0]] = parsed[1]

print(parsed_dict)
amount = int(input("Enter the amount: "))
print("Enter the name of currency you want to convert \nAvailable Options:")
[print(i) for i in parsed_dict.keys()]


