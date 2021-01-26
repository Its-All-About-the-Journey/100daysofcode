LETTER = "./Input/Letters/starting_letter.txt"
RECIPIENTS = "./Input/Names/invited_names.txt"
OUTPUT_LETTER = "./Output/ReadyToSend"
NAME_FIELD = "[name]"

def load(file: str) -> str:
    try:
        with open(file) as file_in:
            text = file_in.read()
    except:
        raise Exception(f"Could not load file: {file}")

    return text

def dump(file: str, content: str) -> None:
    try:
        with open(file, "w") as file_in:
            file_in.write(content)
    except:
        raise Exception(f"Could not write file: {file}")


if __name__ == "__main__":

    # load letter
    letter = load(LETTER)

    # load recipients
    recipients = load(RECIPIENTS).splitlines()

    for recipient in recipients:
        dump(
            f"{OUTPUT_LETTER}/{recipient}.txt",
            letter.replace(NAME_FIELD, recipient)
        )
