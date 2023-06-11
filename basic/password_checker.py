username = input("Introduce tu nombre de usurario, por favor: ")
password = input("Introduce tu contraseña, por favor: ")
password_hidden = len(password) * "*"
password_length = len((str(password)))

print(f"Hi! {username}, your password {password_hidden} is {password_length} letters long")