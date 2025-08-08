from abc import ABC, abstractmethod

class View(ABC):
    @abstractmethod
    def display_menu(self):
        pass

    @abstractmethod
    def get_user_choice(self):
        pass

    @abstractmethod
    def input_contact_info(self):
        pass

    @abstractmethod
    def display_message(self, message: str):
        pass

    @abstractmethod
    def display_contacts(self, contacts: list):
        pass


class ConsoleView(View):
    def display_menu(self):
        print("\nАдресна книга")
        print("1. Додати контакт")
        print("2. Переглянути контакти")
        print("3. Вийти")

    def get_user_choice(self):
        return input("Виберіть опцію (1/2/3): ")

    def input_contact_info(self):
        name = input("Введіть ім'я: ")
        phone = input("Введіть номер телефону: ")
        return name, phone

    def display_message(self, message: str):
        print(message)

    def display_contacts(self, contacts: list):
        if not contacts:
            print("Контактів поки немає.")
        else:
            print("\nСписок контактів:")
            for contact in contacts:
                print(f"Ім'я: {contact['name']}, Телефон: {contact['phone']}")
