import shutil
import os
from datetime import datetime

# Set the source directory to back up and where to store the backup
source_dir = "E:/Python programming/source_folder"    # ✅ Replace with your source folder path
backup_dir = "E:/Python programming/backup_folder"    # ✅ Replace with your backup folder path

# Create timestamp
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

# Create full backup file path
backup_file = os.path.join(backup_dir, f"backup_{timestamp}.zip")

# Make the backup zip
shutil.make_archive(backup_file.replace('.zip', ''), 'zip', source_dir)

print(f"Backup created at: {backup_file}")
