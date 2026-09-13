from functions.get_files_info import get_files_info

if __name__ == "__main__":
    for dir in (".", "pkg", "/bin", "../"):
        dir_name = dir if dir != "." else "current"
        print(f"Result for {dir_name} directory:")
        print(get_files_info("calculator", dir))
