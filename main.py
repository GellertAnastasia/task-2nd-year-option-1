from src.list import List
from src.read_and_check_file import check_from_file


if __name__ == "__main__":
    result = check_from_file('test.txt')
    print(result)