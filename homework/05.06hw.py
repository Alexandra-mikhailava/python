login = input("Введите ваш логин: ")
def decorator(func):
    def wrapper_decorator(*args, **kwargs):
        if login != "admin":
           return "У вас нет доступа"
        value = func(*args, **kwargs)
        return value
    return wrapper_decorator
@decorator
def bank_account(balance):
    return balance
result = bank_account("10.000")
print(result)
