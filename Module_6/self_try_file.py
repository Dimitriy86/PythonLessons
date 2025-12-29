# Визначення власного класу винятку
# class AgeVerificationError(Exception):
#     def __init__(self, message="Age doesn't meet the minimum requirement"):
#         self.message = message
#         super().__init__(self.message)


# def verify_age(age: int):
#     if age < 18:
#         raise AgeVerificationError('Person is under 18 years old')


# if __name__ == "__main__":
    # Обробка винятку
    # try:
    #     verify_age(16)  # Змініть вік для різних результатів
    # except AgeVerificationError as e:
    #     print(f"Exception: {e}")
    # else:
    #     print("Age verified, person is an adult.")

# ------------------------------------------------------------------------------------

class NameTooShortError(Exception):
    pass

class NameStartsFromLowError(Exception):
    pass

def enter_name():
    name = input("Enter name: ")
    if len(name) < 3:
        raise NameTooShortError("Name is too short, need more than 2 symbols.")
    if not name[0].isupper():
        raise NameStartsFromLowError("Name shoud start from capital letter.")
    return name

if __name__ == "__main__":
    try:
        name = enter_name()
        print(f"Hello, {name}")
    except (NameTooShortError, NameStartsFromLowError) as e:
        print(e)
