import uuid

MOVIE_USER = "movie_user"
ADMIN_USER = "admin_user"
CINEMA_USER = "cinema_user"


def generate_token(prefix=None):
    token = prefix + uuid.uuid4().hex
    return token


def generate_movie_user_token():
    return generate_token(prefix=MOVIE_USER)


def generate_admin_user_token():
    return generate_token(prefix=ADMIN_USER)


def generate_cinema_user_token():
    return generate_token(prefix=CINEMA_USER)
