from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from flask_bootstrap import Bootstrap
from wtforms.validators import DataRequired, URL
from flask_mysqldb import MySQL

# Sets up app and relates with Bootstrap to use a quickform
app = Flask(__name__)
app.secret_key = 'torrent_under_format_uniform'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'sachin'
app.config['MYSQL_PASSWORD'] = 'pipeline'
app.config['MYSQL_DB'] = 'cafe'
Bootstrap(app)
mysql = MySQL(app)


# Creates Flask form class with fields
class CafeForm(FlaskForm):
    name = StringField('Name of the cafe', validators=[DataRequired()])
    google_maps_url = StringField("Location of cafe on Google maps(URL): ", validators=[DataRequired(), URL()])
    img_url = StringField("Picture of cafe on Google Maps(URL): ", validators=[DataRequired(), URL()])
    suburb = StringField("Suburb Name:", validators=[DataRequired()])
    pricey = SelectField("Price rating", choices=["$", "$$", "$$$"], validators=[DataRequired()])
    phone_number = StringField("Phone number of cafe")
    website = StringField("Website of the cafe(URL): ")
    menu = StringField("Menu of the cafe(URL): " )
    submit = SubmitField('Submit')


# Home page route. Reads the data in csv file and transfers it to html file as an array.
@app.route('/')
def home():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM cafe")
    cafes = cur.fetchall()
    cur.close()
    return render_template('index.html', cafes=cafes)


# Add route. Transfers form data to html to Display the form on the page.
# When form is submitted by user, function adds entered data in csv file.
@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO cafe (name, google_maps_url, img_url, suburb, pricey, phone_number, website, menu) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                    (form.name.data, form.google_maps_url.data, form.img_url.data, form.suburb.data, form.pricey.data, form.phone_number.data, form.website.data, form.menu.data))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('home'))
    return render_template('add.html', form=form)


if __name__ == "__main__":
    app.run()
