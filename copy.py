import shutil
import os

# Create a sample file
with open("Sample_file.txt", "w") as f:
    f.write("This is a simple file for shutil operations..!")

# Copy the file
shutil.copy("Sample_file.txt", "Copy_file.txt")

# Check if the copied file exists
file_copied = os.path.exists("Copy_file.txt")
print(file_copied)  # Should print: True
