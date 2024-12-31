from flask_wtf.file import FileAllowed, FileField, FileRequired
from flask_wtf.form import FlaskForm
from wtforms.fields.simple import SubmitField
from wtforms import StringField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Email, Length

# 화일을 업로드하기 위한 form, EXCEL 화일만 가능함
class UploadImageForm(FlaskForm):
    image = FileField(
        validators=[FileRequired("해당하는 추정화일을 선택해 주세요."),
        FileAllowed(["xlsx","xls"], "지원되지 않는 이미지 형식입니다."),]
    )
    submit = SubmitField("업로드")

class UploadMissionForm(FlaskForm):
    mission_statement = TextAreaField(
        "사명선언서",
        validators=[
            DataRequired(message="사명선언서는 필수입니다."),
            Length(max=5000, message="최대 5,000자입니다.")
        ],
    )
    roll_statement = TextAreaField(
        "역할별원칙",
        validators=[
            Length(max=10000, message="최대 10,000자입니다.")
        ],
    )
    extra_statement = TextAreaField(
        "부칙",
        validators=[
            Length(max=10000, message="최대 10,000자입니다.")
        ],
    )
    submit = SubmitField("등록")

class Roll_position(FlaskForm):
    roll = TextAreaField(
        "역할",
        validators=[
            Length(max=5000, message="최대 5,000자입니다.")
        ],
    )
    area_avility = TextAreaField(
        "잘하는일",
        validators=[
            Length(max=5000, message="최대 5,000자입니다.")
        ],
    )
    area_concern = TextAreaField(
        "잘하고 싶은일",
        validators=[
            Length(max=5000, message="최대 5,000자입니다.")
        ],
    )
    area_weakness = TextAreaField(
        "약점",
        validators=[
            Length(max=5000, message="최대 5,000자입니다.")
        ],
    )
    submit = SubmitField("업로드")

class Question_answer(FlaskForm):
    NO1 = TextAreaField(
        "1번답",
        validators=[
            Length(max=5000, message="최대 5,000자입니다.")
        ],
    )
    NO2 = TextAreaField(
        "2번답",
        validators=[
            Length(max=5000, message="최대 5,000자입니다.")
        ],
    )
    NO3 = TextAreaField(
        "3번답",
        validators=[
            Length(max=5000, message="최대 5,000자입니다.")
        ],
    )
    NO4 = TextAreaField(
        "4번답",
        validators=[
            Length(max=5000, message="최대 5,000자입니다.")
        ],
    )
    NO5 = TextAreaField(
        "5번답",
        validators=[
            Length(max=5000, message="최대 5,000자입니다.")
        ],
    )
    NO6 = TextAreaField(
        "6번답",
        validators=[
            Length(max=5000, message="최대 5,000자입니다.")
        ],
    )
    submit = SubmitField("업로드")