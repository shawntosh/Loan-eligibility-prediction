from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'


class LoanApplication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    applicant_income = db.Column(db.Float, nullable=False)
    coapplicant_income = db.Column(db.Float, nullable=False)
    loan_amount = db.Column(db.Float, nullable=False)
    loan_term = db.Column(db.Integer, nullable=False)
    credit_history = db.Column(db.Integer, nullable=False)
    property_valuation = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f'<LoanApplication {self.id}>'
