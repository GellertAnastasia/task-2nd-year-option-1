from src.list import List


def check_from_file(filename):
    try:
        with open(filename, "r") as file:
            numbers = file.read().strip().split()

        linked_list = List()
        for num in numbers:
            linked_list.append(int(num))

        return linked_list.is_symmetric()

    except FileNotFoundError:
        print(f"Файл {filename} не найден")
        return False
    except ValueError:
        print("Ошибка: нечисловые данные")
        return False
