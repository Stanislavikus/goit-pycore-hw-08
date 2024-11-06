import pickle

class AddressBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone):
        self.contacts[name] = phone

    def remove_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]

    def get_contact(self, name):
        return self.contacts.get(name)

    def list_contacts(self):
        return self.contacts

    @staticmethod
    def load_data(filename="addressbook.pkl"):
        try:
            with open(filename, "rb") as file:
                return pickle.load(file)
        except FileNotFoundError:
            # Якщо файл не знайдено, повертаємо новий об'єкт AddressBook
            return AddressBook()

    def save_data(self, filename="addressbook.pkl"):
        with open(filename, "wb") as file:
            pickle.dump(self, file)

def main():
    print("Програма запущена.")  # Додано для перевірки запуску програми
    address_book = AddressBook.load_data()

    # Основний цикл програми
    while True:
        print("Введіть команду (add, remove, list, exit): ")  # Додано для перевірки циклу
        command = input().strip().lower()

        if command == "add":
            name = input("Введіть ім'я: ")
            phone = input("Введіть номер телефону: ")
            address_book.add_contact(name, phone)
            print(f"Контакт {name} додано.")

        elif command == "remove":
            name = input("Введіть ім'я для видалення: ")
            address_book.remove_contact(name)
            print(f"Контакт {name} видалено.")

        elif command == "list":
            print("Контакти:")
            for name, phone in address_book.list_contacts().items():
                print(f"{name}: {phone}")

        elif command == "exit":
            # Зберігаємо дані перед виходом
            address_book.save_data()
            print("Дані збережено. До побачення!")
            break

        else:
            print("Невідома команда. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
