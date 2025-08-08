from assistant.addressbook import AddressBook, load_data, save_data
from assistant.views import ConsoleView

def main():
    book = load_data()
    view = ConsoleView()

    while True:
        view.display_menu()
        choice = view.get_user_choice()

        if choice == '1':
            name, phone = view.input_contact_info()
            book.add_contact(name, phone)
            view.display_message(f"Контакт {name} додано.")
        
        elif choice == '2':
            contacts = book.list_contacts()
            view.display_contacts(contacts)

        elif choice == '3':
            save_data(book)
            view.display_message("Дані збережено. Вихід з програми.")
            break
        else:
            view.display_message("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
