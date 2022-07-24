def get_users(passwd: str) -> dict:
    """Split password output by newline,
      extract user and name (1st and 5th columns),
      strip trailing commas from name,
      replace multiple commas in name with a single space
      return dict of keys = user, values = name.
    """
    passwords = (list(filter(None, passwd.splitlines())))
    words = [word.split(":") for word in passwords]

    user = []
    name = []
    for word in words:
        user.append(word[0])
        if word[4] == "":
            name.append("unknown")
        else:
            name.append(word[4].replace(",,,", "").replace(",", " "))

    return dict(zip(user, name))
