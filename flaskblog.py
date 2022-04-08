from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm


app = Flask(__name__)

app.config['SECRET_KEY'] = '66294800a89b651b6fb0293af3823f76'

posts = [
    {
        'author': 'xtar',
        'title': 'Hello Flask!',
        'content': 'This is my fist flask blog!',
        'date_posted': '2022.4.6'
    },
    {
        'author': 'xtar',
        'title': 'Hello again!',
        'content': 'This is my second flask blog!',
        'date_posted': '2022.4.7'
    },
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='about')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", 'success')
        return redirect(url_for('home')) # url_for对象是函数名
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)
