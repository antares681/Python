def password_validator(word):
    is_valid = True
    warning_list = []

#CHECK 1
    if not 6 <= len(word) <= 10:
       is_valid = False
       warning_list.append("Password must be between 6 and 10 characters")

#CHECK 2
    if not word.isalnum():
        is_valid = False
        warning_list.append("Password must consist only of letters and digits")

#CHECK 3
    digit_counter = 0
    for element in word:
        if element.isdigit():
            digit_counter +=1

    if digit_counter < 2:
        warning_list.append("Password must have at least 2 digits")
        is_valid = False

    if is_valid == True:
        warning_list.append("Password is valid")

    return warning_list

password = input()

print("\n".join(password_validator(password)))