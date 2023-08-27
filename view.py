import text


def menu():
    for i, item in enumerate(text.main_menu):
        if i == 0:
            print(item)
        else:
            print(f"\t{i}.{item}")
        while True:
            choice = input(text.input_choice)
            if choice.isdigit() and 0 < int(choice) < len(text.input_choice):
                return int(choice)
            print(text.input_menu_error)


def print_massage(msg: str):
    print("\n" + "=" * len(msg))
    print(msg)
    print("=" * len(msg) + "\n")


def show_book(book: dict, msg: str):
    if book:
        max_len = [len(max(item, key=len)) for item in zip(*book.values)]
        print("\n" + "=" * (sum(max_len) + 8))
        for i, contact in book.items():
            print(
                f"{i:>3}, {contact[0]:< {max_len[0]}}{contact[1]:{max_len[1]}}{contact[2]:{max_len[2]}}"
            )
        print("=" * (sum(max_len) + 8) + "\n")
    else:
        print_massage(msg)


def input_contact(msg) -> list[str]:
    new = []
    for item in msg:
        new.append(input(item))
    return new


def input_request(msg: str) -> str:
    return input(msg)
