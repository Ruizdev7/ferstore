from datetime import datetime

from ferstore_app import db


class Employee(db.Model):
    __tablename__ = "tbl_employee"
    ccn_employee = db.Column(db.Integer, primary_key=True)
    ccn_type_id = db.Column(db.Integer, db.ForeignKey("tbl_type_id.ccn_type_id"))
    number_id_employee = db.Column(db.BigInteger, nullable=False, unique=True)
    first_name_employee = db.Column(db.String(30), nullable=False)
    middle_name_employee = db.Column(db.String(30), nullable=True)
    first_last_name_employee = db.Column(db.String(30), nullable=False)
    second_last_name_employee = db.Column(db.String(30), nullable=True)
    full_name_employee = db.Column(db.String(200), nullable=False)
    date_birth_employee = db.Column(db.Date, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    auto_perceived_gender = db.Column(
        db.Integer, db.ForeignKey("tbl_auto_perceived_gender.ccn_auto_perceived_gender")
    )
    employee_personal_email = db.Column(db.String(100), nullable=False)
    employee_personal_cellphone = db.Column(db.BigInteger, nullable=False)
    informed_consent_law_1581 = db.Column(db.String(10), nullable=False)
    image = db.Column(db.String(255), nullable=True)
    employee_password = db.Column(db.String(300), nullable=False)

    def __init__(
        self,
        ccn_employee,
        ccn_type_id,
        number_id_employee,
        first_name_employee,
        middle_name_employee,
        first_last_name_employee,
        second_last_name_employee,
        date_birth_employee,
        age,
        age_range,
        auto_perceived_gender,
        employee_personal_email,
        employee_personal_cellphone,
        informed_consent_law_1581,
        image,
        employee_password,
    ):
        self.ccn_employee = ccn_employee
        self.ccn_type_id = ccn_type_id
        self.number_id_employee = number_id_employee
        self.first_name_employee = first_name_employee
        self.middle_name_employee = middle_name_employee
        self.first_last_name_employee = first_last_name_employee
        self.second_last_name_employee = second_last_name_employee
        self.full_name_employee = f"{first_name_employee} {middle_name_employee} {first_last_name_employee} {second_last_name_employee}"
        self.date_birth_employee = date_birth_employee
        self.age = age
        self.age_range = age_range
        self.auto_perceived_gender = auto_perceived_gender
        self.employee_personal_email = employee_personal_email
        self.employee_personal_cellphone = employee_personal_cellphone
        self.informed_consent_law_1581 = informed_consent_law_1581
        self.image = image
        self.employee_password = employee_password

    def choice_query():
        return Employee.query

    def __repr__(self):
        return f"Employee: {self.full_name_employee}"
