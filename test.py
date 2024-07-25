import os
from collections import defaultdict

def categorize_files_by_type(folder_path):
    
    if not os.path.exists(folder_path):
        raise FileNotFoundError(f"The folder path '{folder_path}' does not exist.")
    if not os.path.isdir(folder_path):
        raise NotADirectoryError(f"The path '{folder_path}' is not a directory.")
    
    file_dict = defaultdict(list)
    
    for root, _, files in os.walk(folder_path):
        for file in files:
            full_path = os.path.join(root, file)
            file_ext = os.path.splitext(file)[1] or ""
            file_dict[file_ext].append(full_path)
    
    return dict(file_dict)

result = categorize_files_by_type(r"D:\Desktop\TestTask\1p")
print(result)
