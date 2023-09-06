from datetime import datetime

from ferstore_app import db


class Customer(db.Model):
    __tablename__ = "tbl_customer"
    ccn_customer = db.Column(db.Integer, primary_key=True)
    ccn_type_id = db.Column(db.Integer, db.ForeignKey("tbl_type_id.ccn_type_id"))
    number_id_customer = db.Column(db.BigInteger, nullable=False, unique=True)
    first_name_customer = db.Column(db.String(60), nullable=False)
    middle_name_customer = db.Column(db.String(60), nullable=True)
    first_last_name_customer = db.Column(db.String(60), nullable=False)
    second_last_name_customer = db.Column(db.String(60), nullable=True)
    birthday_customer = db.Column(db.Date, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    auto_perceived_gender = db.Column(
        db.Integer, db.ForeignKey("tbl_auto_perceived_gender.ccn_auto_perceived_gender")
    )
    email_customer = db.Column(db.String(100), nullable=False)
    cellphone_customer = db.Column(db.BigInteger, nullable=False)
    informed_consent_law_1581 = db.Column(db.String(10), nullable=False)
    profile_picture_customer = db.Column(db.String(255), nullable=True)
    password_customer = db.Column(db.String(300), nullable=False)

    def __init__(
        self,
        ccn_customer,
        ccn_type_id,
        number_id_customer,
        first_name_customer,
        middle_name_customer,
        first_last_name_customer,
        second_last_name_customer,
        birthday_customer,
        age,
        auto_perceived_gender,
        email_customer,
        cellphone_customer,
        informed_consent_law_1581,
        profile_picture_customer,
        password_customer,
    ):
        self.ccn_customer = ccn_customer
        self.ccn_type_id = ccn_type_id
        self.number_id_customer = number_id_customer
        self.first_name_customer = first_name_customer
        self.middle_name_customer = middle_name_customer
        self.first_last_name_customer = first_last_name_customer
        self.second_last_name_customer = second_last_name_customer
        self.birthday_customer = birthday_customer
        self.age = age
        self.auto_perceived_gender = auto_perceived_gender
        self.email_customer = email_customer
        self.cellphone_customer = cellphone_customer
        self.informed_consent_law_1581 = informed_consent_law_1581
        self.profile_picture_customer = profile_picture_customer
        self.password_customer = password_customer

    def choice_query():
        return Customer.query

    def __repr__(self):
        return f"Customer: {self.number_id_customer}"
