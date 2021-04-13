from flask import Flask, url_for, request, render_template, redirect, make_response, session, abort
from flask_login import LoginManager, login_user, login_required, logout_user, current_user

import sqlalchemy

from data import db_session
from data.users import User
from data.case import Case

from forms.user import RegisterForm
from forms.login import LoginForm
from forms.case import CaseForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)


def main():
    db_session.global_init("db/cases.db")
    db_sess = db_session.create_session()
    db_sess.commit()
    app.run()


@app.route("/")
def index():
    db_sess = db_session.create_session()
    if current_user.is_authenticated:
        news = db_sess.query(Case).filter(
            (Case.user == current_user) | (Case.is_private != True))
    else:
        news = db_sess.query(Case).filter(Case.is_private != True)
    return render_template("index.html", news=news)


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            email=form.email.data,
            about=form.about.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/new_case', methods=['GET', 'POST'])
@login_required
def add_news():
    form = CaseForm()
    db_sess = db_session.create_session()
    num = 1
    for case in db_sess.query(Case):
        num = case.id + 1
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        case = Case()
        # Suspect
        case.namesurname = form.namesurname.data
        case.age = form.age.data
        case.weight = form.weight.data
        case.height = form.height.data
        case.telo = form.telo.data
        case.nationality = form.nationality.data
        case.omens = form.omens.data
        case.work = form.work.data
        case.home = form.home.data
        case.e_id = form.e_id.data

        # Actions
        case.agents = form.agents.data
        case.crime_data = form.crime_data.data
        case.inspection_of_scene = form.inspection_of_scene.data
        case.other_inspections = form.other_inspections.data
        case.surveys = form.surveys.data
        case.operational_activities = form.operational_activities.data
        case.wiretapping = form.wiretapping.data
        case.searches_places = form.searches_places.data
        case.detention = form.detention.data
        case.searches_person = form.searches_person.data
        case.searches_all_organizations = form.searches_all_organizations.data
        case.interrogations = form.interrogations.data
        case.undercover = form.undercover.data
        case.resolution = form.resolution.data
        case.arrests = form.arrests.data

        # Evidence
        case.description_evid = form.description_evid.data
        case.proofs_evid = form.proofs_evid.data

        # Expertise
        case.description_expert = form.description_expert.data
        case.proofs_expert = form.proofs_expert.data

        # Orders
        case.description_order = form.description_order.data
        case.proofs_order = form.proofs_order.data
        case.user_id = current_user.id
        if 0 < form.skin_id.data < 312:
            case.skin_id = form.skin_id.data
        else:
            case.skin_id = 74
        case.id = 1
        for second_case in db_sess.query(Case):
            case.id = second_case.id + 1

        db_sess.add(case)
        db_sess.merge(current_user)
        db_sess.commit()
        return redirect('/')
    try:
        f = case
    except Exception:
        f = Case()
        f.skin_id = 74
    return render_template('case.html', title='Добавление дела',
                           form=form, num=num, case=f)


@app.route('/case_edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_news(id):
    form = CaseForm()
    if request.method == "GET":
        db_sess = db_session.create_session()
        case = db_sess.query(Case).filter(Case.id == id,
                                          Case.user == current_user
                                          ).first()
        if case:
            # Suspect
            form.namesurname.data = case.namesurname
            form.age.data = case.age
            form.weight.data = case.weight
            form.height.data = case.height
            form.telo.data = case.telo
            form.nationality.data = case.nationality
            form.omens.data = case.omens
            form.work.data = case.work
            form.home.data = case.home
            form.e_id.data = case.e_id

            # Actions
            form.agents.data = case.agents
            form.crime_data.data = case.crime_data
            form.inspection_of_scene.data = case.inspection_of_scene
            form.other_inspections.data = case.other_inspections
            form.surveys.data = case.surveys
            form.operational_activities.data = case.operational_activities
            form.wiretapping.data = case.wiretapping
            form.searches_places.data = case.searches_places
            form.detention.data = case.detention
            form.searches_person.data = case.searches_person
            form.searches_all_organizations.data = case.searches_all_organizations
            form.interrogations.data = case.interrogations
            form.undercover.data = case.undercover
            form.resolution.data = case.resolution
            form.arrests.data = case.arrests

            # Evidence
            form.description_evid.data = case.description_evid
            form.proofs_evid.data = case.proofs_evid

            # Expertise
            form.description_expert.data = case.description_expert
            form.proofs_expert.data = case.proofs_expert

            # Orders
            form.description_order.data = case.description_order
            form.proofs_order.data = case.proofs_order
            current_user.id = case.user_id
            form.skin_id.data = case.skin_id
            num = 1
            for second_case in db_sess.query(Case):
                num = second_case.id
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        case = db_sess.query(Case).filter(Case.id == id,
                                          Case.user == current_user
                                          ).first()
        if case:
            # Suspect
            case.namesurname = form.namesurname.data
            case.age = form.age.data
            case.weight = form.weight.data
            case.height = form.height.data
            case.telo = form.telo.data
            case.nationality = form.nationality.data
            case.omens = form.omens.data
            case.work = form.work.data
            case.home = form.home.data
            case.e_id = form.e_id.data

            # Actions
            case.agents = form.agents.data
            case.crime_data = form.crime_data.data
            case.inspection_of_scene = form.inspection_of_scene.data
            case.other_inspections = form.other_inspections.data
            case.surveys = form.surveys.data
            case.operational_activities = form.operational_activities.data
            case.wiretapping = form.wiretapping.data
            case.searches_places = form.searches_places.data
            case.detention = form.detention.data
            case.searches_person = form.searches_person.data
            case.searches_all_organizations = form.searches_all_organizations.data
            case.interrogations = form.interrogations.data
            case.undercover = form.undercover.data
            case.resolution = form.resolution.data
            case.arrests = form.arrests.data

            # Evidence
            case.description_evid = form.description_evid.data
            case.proofs_evid = form.proofs_evid.data

            # Expertise
            case.description_expert = form.description_expert.data
            case.proofs_expert = form.proofs_expert.data

            # Orders
            case.description_order = form.description_order.data
            case.proofs_order = form.proofs_order.data
            case.skin_id = form.skin_id.data
            db_sess.commit()
            return redirect('/')
        else:
            abort(404)
    return render_template('case.html',
                           title='Редактирование дела',
                           form=form,
                           num=num,
                           case=case)


@app.route('/news_delete/<int:id>', methods=['GET', 'POST'])
@login_required
def news_delete(id):
    db_sess = db_session.create_session()
    news = db_sess.query(Case).filter(Case.id == id,
                                      Case.user == current_user
                                      ).first()
    if news:
        db_sess.delete(news)
        db_sess.commit()
    else:
        abort(404)
    return redirect('/')


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


main()
