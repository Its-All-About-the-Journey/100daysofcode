import os

def clear() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')

def refresh_screen(messages: list) -> None:
    clear()

    for msg in messages:
        print(msg)