def add(*args: int) -> int:
    print(f"args type: {type(args)}")
    print(f"args: {args}")
    return sum(args)


if __name__ == "__main__":
    print(f"The sum is: {add(1, 2, 3, 4, 5)}")
