from flask_wtf import FlaskForm
from wtforms import StringField, validators, ValidationError, HiddenField

from .models import EmailSignup

class LandingForm(FlaskForm):
    id = HiddenField('id')
    full_name = StringField('Full name', 
        render_kw={"class":"form-control","placeholder":"full name"},
        validators=[
            validators.DataRequired(
                    message='You full name is required'
            )
        ])
    email = StringField('Email', 
            render_kw={"class":"form-control", "placeholder":"your email"},
            validators=[
                validators.DataRequired(
                    message='You email is required'
                ),
            validators.Email()
        ])

    def validate_email(self, field):
        _id = self.data.get('id')
        if field.data.endswith(".edu"):
            raise ValidationError('You cannot use a school email address.')
        if _id is None:
            obj = EmailSignup.query.filter_by(email=field.data).first()
            if obj is not None:
                msg = 'This email already exists'
                raise ValidationError(msg)