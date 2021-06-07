from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField,\
    IntegerField, RadioField, SelectField
from wtforms.validators import input_required, Email, Optional

states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

class AddSnackForm(FlaskForm):
    email = StringField("Email", validators=[Email()])
    name = StringField("Snack Name" , validators=[input_required(message="Snack name can't be blank")])
    price = FloatField("Price in USD")
    quantity = IntegerField("How many?")
    is_healthy = BooleanField("This is a healthy snack")

    # category = RadioField("Category", choices=[("ic", "Ice Cream"), ("chips", "Potato chips"),
    #                                            ("sweets", "Candy/Sweets") ])

    category = SelectField("Category", choices=[("ic", "Ice Cream"), ("chips", "Potato chips"),
                                               ("sweets", "Candy/Sweets")])

class EmployeeForm(FlaskForm):

    name = StringField("Employee Name")
    state = SelectField("state", choices=[(st, st) for st in states])
    dept_code = SelectField("Department Code")
