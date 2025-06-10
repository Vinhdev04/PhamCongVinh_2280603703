print("Enter text: ");
lines =[]
while True:
    line = input()
    if line.lower() == 'done':
        break
    lines.append(line)
print("\nAfter convert: ")
for line in lines:
    print(line.upper())