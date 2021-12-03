import os
import functions
    
if __name__ == "__main__":
    user = functions.get_user()
    if functions.has_user(user):
        print("E-mail já cadastrado seu filho da puta! Tenta outro desgraça!!!")
    else:
        functions.insert_user(user)