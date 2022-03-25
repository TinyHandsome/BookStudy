from App.models.movie_user import MovieUser


def get_user(user_id):
    # 根据id查找
    user = MovieUser.query.get(user_id)
    if user:
        return user

    # 根据手机号查找
    user = MovieUser.query.filter(MovieUser.phone == user_id).first()
    if user:
        return user

    # 根据用户名查找
    user = MovieUser.query.filter(MovieUser.username == user_id).first()
    if user:
        return user

    return None
