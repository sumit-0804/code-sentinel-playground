USERS = {1: {"name": "Ada"}, 2: {"name": "Linus"}}


def find_user(user_id):
    if user_id not in USERS:
        return None
    return USERS[user_id]


def _normalize(name):
    return name.strip().lower()
