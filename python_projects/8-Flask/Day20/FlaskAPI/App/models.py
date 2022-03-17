from App.ext import db


class BaseModel(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    def save(self):

        try:
            db.session.add(self)
            db.session.commit()
            return True
        except Exception as e:
            print(e)
            return False


class Goods(BaseModel):
    g_name = db.Column(db.String(64))
    g_price = db.Column(db.Float, default=0)
