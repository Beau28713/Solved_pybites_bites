import re


def get_users(passwd: str) -> dict:
    """Split password output by newline,
      extract user and name (1st and 5th columns),
      strip trailing commas from name,
      replace multiple commas in name with a single space
      return dict of keys = user, values = name.
    """
    user_value = {}
    for ele in passwd.splitlines()[1:]:
        user = ele.split(":")[0]
        name = re.sub(r",+", r" ", ele.split(":")[4]).strip()
        user_value[user] = name or "unknown"

    return user_value