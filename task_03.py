import os
import shutil

root_dir = os.path.join(os.path.dirname(__file__), "my_project")
dst_dir = os.path.join(os.path.dirname(__file__), "my_project", "templates")

if not os.path.exists(dst_dir):
    os.makedirs(dst_dir)

for root, dirs, files in os.walk(root_dir):
    if root.count("templates"):
        for dir_ in dirs:
            if not os.path.exists(os.path.join(dst_dir, dir_)):
                os.makedirs(os.path.join(dst_dir, dir_))
            for file in files:
                file2 = os.path.join(root, file)
                file1 = os.path.join(dst_dir, os.path.basename(root))
                if not os.path.dirname(file2) == file1:
                    shutil.copy(file2, file1)
