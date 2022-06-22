
def validate_usr(username):
    # your code here
    if username.lower()!=username: return False
    if ' ' not in username:
        if len(username) >= 4 and len(username) <= 16:
            if (username.islower() or username.isnumeric() or '_' in username):
                return True
            else:
                return False
        else:
            return False
    else:
        return False


x = validate_usr('O_nhm_0ogDabvxg')
print(x)
