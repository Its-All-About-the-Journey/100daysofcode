def calculate(n: float, **kwargs: object) -> float:
    print(f"kwargs type: {type(kwargs)}")
    print(f"kwargs:\n{kwargs}")

    n += kwargs.get("add")
    n *= kwargs.get("multiply")

    return n


if __name__ == "__main__":
    print(f"Results: {calculate(5, add=5, multiply=2)}")
