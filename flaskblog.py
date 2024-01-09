from flask import Flask, render_template, flash, redirect, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '06a72e3c0f68f5c929f683d89ce5b1e6'

posts = [
    {
        'author': 'Naresh Shahi',
        'title': 'My Blog post',
        'content': 'I am learning Flask and this is my blog made using flask',
        'date_posted': 'January 09, 2024'

    },

    {
        'author': 'Anisha Thapa',
        'title': 'Anisha Blog post',
        'content': 'Anisha is helping Naresh creating his blog contents',
        'date_posted': 'January 09, 2024'

    },
    {
        'author': 'Naresh Shahi',
        'title': 'My Blog post 2',
        'content': 'this is my second pots',
        'date_posted': 'January 09, 2024'

    }

]

@app.route("/")
@app.route("/home")
def home():
    title = 'My blog posts'
    return render_template('home.html', posts=posts, title=title)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/add")
def add():
    a = 2
    b = 3
    total = a + b
    return render_template('add.html', a=a, b = b, total = total)

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))

    return render_template('register.html', posts=posts, title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in !', 'success')
            return redirect(url_for('home'))
        else:
             flash('Login Unsuccessful, please check your email and password', 'danger')

    return render_template('login.html', posts=posts, title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)