from functions.get_file_content import get_file_content

paths = ("lorem.txt", "main.py", "pkg/calculator.py", "/bin/cat", "pkg/does_not_exist.py")

for fp in paths:
    result = get_file_content("calculator", fp)

    if fp == "lorem.txt":
        print(f"lorem.txt length: {len(result)}")
        print(f"lorem.txt truncated: {'truncated' in result}")
    else:
        print(result)
