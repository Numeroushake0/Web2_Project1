import json
import os

DATA_FILE = "contacts.json"

class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name: str, phone: str):
        contact = {"name": name, "phone": phone}
        self.contacts.append(contact)

    def list_contacts(self):
        return self.contacts


def load_data() -> AddressBook:
    book = AddressBook()
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, list):
                    book.contacts = data
        except (json.JSONDecodeError, IOError):
            pass  # Якщо файл пошкоджений чи неможливо прочитати — починаємо з пустої книги
    return book


def save_data(book: AddressBook):
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(book.contacts, f, ensure_ascii=False, indent=2)
    except IOError as e:
        print(f"Помилка при збереженні даних: {e}")
