from accounts.models import User

def has_admin(user):
    return user.is_admin != User.is_admin