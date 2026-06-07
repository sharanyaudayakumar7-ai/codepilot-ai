from services.file_reader import get_python_files

files = get_python_files("repos/fastapi")

print(f"Total Python Files: {len(files)}")

for file in files[:10]:
    print(file)