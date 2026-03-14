
data = [
    "DevOps involves collaboration",
    "Automation improves efficiency",
    "Python is widely used in DevOps"
]

with open("sample.txt", "w") as file:
    for line in data:
        file.write(line + "\n")

print("Data written to file successfully.")
