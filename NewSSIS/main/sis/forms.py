from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length

class StudentForm(FlaskForm):
    id_number = StringField("ID Number",
                            validators=[DataRequired(), Length(max=9)])
    first_name = StringField("First name", validators=[DataRequired()])
    last_name = StringField("Last name", validators=[DataRequired()])
    course = SelectField("Course", choices=[])
    year_level = SelectField("Year Level", choices=[1, 2, 3, 4, 5])
    gender = SelectField("Gender",
                         choices=["Male", "Female", 
                                  "Other"])
    add = SubmitField("Add")

class SearchForm(FlaskForm):
    search_by = SelectField("Search by", 
                            choices=["ID Number", "First name",
                                     "Last name", "Course", 
                                     "Year Level", "Gender"])
    this = StringField("This", validators=[DataRequired()])
    search = SubmitField("Search")

class CourseSearchForm(FlaskForm):
    search_by = SelectField("Search by", 
                            choices=["Course code", 
                                     "Course name",
                                     "College"])
    this = StringField("This", validators=[DataRequired()])
    search = SubmitField("Search")

class CourseForm(FlaskForm):
    course_code = StringField("Course code", validators=[DataRequired()])
    course_name = StringField("Course name", validators=[DataRequired()])
    college = SelectField("College", choices=[])
    add = SubmitField("Add")

class CollegeSearchForm(FlaskForm):
    search_by = SelectField("Search by", 
                            choices=["College code", 
                                     "College name"])
    this = StringField("This", validators=[DataRequired()])
    search = SubmitField("Search")

class CollegeForm(FlaskForm):
    college_code = StringField("College code", validators=[DataRequired()])
    college_name = StringField("College name", validators=[DataRequired()])
    add = SubmitField("Add")

class CollegeSearchForm(FlaskForm):
    search_by = SelectField("Search by", 
                            choices=["College code", 
                                     "College name"])
    this = StringField("This", validators=[DataRequired()])
    search = SubmitField("Search")
