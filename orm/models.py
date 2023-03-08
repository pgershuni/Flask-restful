from orm.db_session import ORMBase
from sqlalchemy_serializer import SerializerMixin
import sqlalchemy as sa


class User(ORMBase, SerializerMixin):
    __tablename__ = 'users'

    id = sa.Column(sa.Integer, autoincrement=True, primary_key=True)
    name = sa.Column(sa.String)
    surname = sa.Column(sa.String)
