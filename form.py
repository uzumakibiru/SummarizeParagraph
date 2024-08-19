from flask_wtf import FlaskForm
from wtforms import SubmitField
from wtforms.validators import DataRequired
from flask_ckeditor import CKEditorField

class YourText(FlaskForm):
    task=CKEditorField("Add Text",validators=[DataRequired()])
    submit=SubmitField("Summarize")

class YourREsult(FlaskForm):
    task=CKEditorField("Result",validators=[DataRequired()])
    
