import re
def get_users(passwd: str) -> dict:
    """Split password output by newline,
      extract user and name (1st and 5th columns),
      strip trailing commas from name,
      replace multiple commas in name with a single space
      return dict of keys = user, values = name.
    """


    user_to_password = {}
    lines = passwd.splitlines()
    print(lines)
    for line in lines[1:]:
        columns = line.split(':')
        user = columns[0].rstrip(',')
        if not columns[4]:
            password = 'unknown'  
        else:
            password = columns[4].rstrip(',')

        password = re.sub(r',+',' ',password)
        user_to_password[user] = password

    return user_to_password





