import os
import create_user
    
if __name__ == "__main__":
    user = create_user.get_user()
    if create_user.has_user(user):
        print("E-mail já cadastrado seu filho da puta! Tenta outro desgraça!!!")
    else:
        create_user.insert_user(user)