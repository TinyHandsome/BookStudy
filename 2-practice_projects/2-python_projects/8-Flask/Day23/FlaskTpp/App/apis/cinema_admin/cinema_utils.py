from App.models.cinema_admin.cinema_user_model import CinemaUser


def get_cinema_user(user_id):
    if not user_id:
        return None

    # 根据id查找
    user = CinemaUser.query.get(user_id)
    if user:
        return user

    # 根据手机号查找
    user = CinemaUser.query.filter(CinemaUser.phone == user_id).first()
    if user:
        return user

    # 根据用户名查找
    user = CinemaUser.query.filter(CinemaUser.username == user_id).first()
    if user:
        return user

    return None
