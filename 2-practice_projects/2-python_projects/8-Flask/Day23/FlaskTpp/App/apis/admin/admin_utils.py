from App.models.admin.admin_user_model import AdminUser


def get_admin_user(user_id):
    if not user_id:
        return None

    # 根据id查找
    user = AdminUser.query.get(user_id)
    if user:
        return user

    # 根据用户名查找
    user = AdminUser.query.filter(AdminUser.username == user_id).first()
    if user:
        return user

    return None
