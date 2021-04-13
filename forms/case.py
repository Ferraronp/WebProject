from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField
from wtforms import BooleanField, SubmitField
from wtforms.validators import DataRequired


class CaseForm(FlaskForm):
    # Suspect
    namesurname = StringField('Имя фамилия', validators=[DataRequired()])
    age = IntegerField('Возраст')
    weight = StringField('Вес')
    height = StringField('Рост')
    telo = StringField('Телосложение')
    nationality = StringField('Национальность')
    omens = StringField('Особые приметы')
    work = TextAreaField("Работа")
    home = StringField('Особые приметы')
    e_id = IntegerField('E-ID номер')

    # Actions
    agents = StringField('Ведущие агенты', validators=[DataRequired()])
    crime_data = TextAreaField("Данные о преступлении")
    inspection_of_scene = TextAreaField("Осмотр места происшествия")
    other_inspections = TextAreaField("Осмотр иных мест")
    surveys = TextAreaField("Опросы")
    operational_activities = TextAreaField("Оперативные мероприятия")
    wiretapping = StringField("Прослушка")
    searches_places = TextAreaField("Обыск местности")
    detention = TextAreaField("Задержание")
    searches_person = TextAreaField("Обыск задержанного лица")
    searches_all_organizations = TextAreaField("Обыск сотрудников организации")
    interrogations = TextAreaField("Допросы")
    undercover = TextAreaField("Работа под прикрытием")
    resolution = TextAreaField("Постановление агента")
    arrests = TextAreaField("Аресты")

    # Evidence
    description_evid = TextAreaField("Описание доказательства")
    proofs_evid = TextAreaField("Доказательство(ссылки на видео)")

    # Expertise
    description_expert = TextAreaField("Описание экспертиз")
    proofs_expert = TextAreaField("Доказательство(ссылки на видео)")

    # Orders
    description_order = TextAreaField("На что получены ордера")
    proofs_order = TextAreaField("Доказательство(ссылки на видео)")

    # Others
    skin_id = IntegerField('(( Номер скина ))')
    is_finished = BooleanField("Закрыто")
    submit = SubmitField('Применить')
