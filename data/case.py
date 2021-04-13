import datetime
import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Case(SqlAlchemyBase):
    __tablename__ = 'case'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)

    # Suspect
    namesurname = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    age = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    weight = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    height = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    telo = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    nationality = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    omens = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    work = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    home = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    e_id = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)

    # Actions
    agents = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    crime_data = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    inspection_of_scene = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    other_inspections = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    surveys = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    operational_activities = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    wiretapping = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    searches_places = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    detention = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    searches_person = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    searches_all_organizations = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    interrogations = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    undercover = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    resolution = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    arrests = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    # Evidence
    description_evid = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    proofs_evid = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    # Expertise
    description_expert = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    proofs_expert = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    # Orders
    description_order = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    proofs_order = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    # Others
    created_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                     default=datetime.datetime.now)
    is_finished = sqlalchemy.Column(sqlalchemy.Boolean, default=False)
    is_private = sqlalchemy.Column(sqlalchemy.Boolean, default=False)
    skin_id = sqlalchemy.Column(sqlalchemy.Integer, default=74, nullable=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("users.id"))
    user = orm.relation('User')
