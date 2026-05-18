from pathlib import Path

# filename = 'programming.txt'    #檔案被寫在上一層的目錄中

filename = Path(__file__).parent / "programming.txt"

with open(filename, "a") as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")
