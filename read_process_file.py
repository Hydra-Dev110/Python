
with open("sample.txt", "r") as file:
    lines = file.readlines()

line_count = len(lines)
word_count = sum(len(line.split()) for line in lines)

print("Number of lines:", line_count)
print("Number of words:", word_count)
