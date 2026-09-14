from functions.write_file import write_file


args = (
        ("lorem.txt", "wait, this isn't lorem ipsum"),
        ("pkg/morelorem.txt", "lorem ipsum dolor sit amet"),
        ("/tmp/temp.txt", "this should not be allowed"),
    )

for fp, content in args:
    result = write_file("calculator", fp, content)
    print(result)
