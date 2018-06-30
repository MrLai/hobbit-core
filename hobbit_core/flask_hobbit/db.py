import enum

from sqlalchemy.orm import relationship
from flask import current_app

db = current_app.hobbit_manager.db

Column = db.Column
Model = db.Model
relationship = relationship


class SurrogatePK:
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    created_at = Column(
        db.DateTime, nullable=False, server_default=db.func.now())
    updated_at = Column(
        db.DateTime, nullable=False, server_default=db.func.now(),
        onupdate=db.func.now())

    def __repr__(self):
        return '<{classname}({pk}:{label!r})>'.format(
            classname=type(self).__name__, pk=self.id, label=self.label or '')


def reference_col(tablename, nullable=False, pk_name='id', **kwargs):
    return db.Column(
        db.ForeignKey('{0}.{1}'.format(tablename, pk_name)),
        nullable=nullable, **kwargs)


class EnumExt(enum.Enum):
    pass