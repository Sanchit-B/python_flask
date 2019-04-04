from flask import Flask, render_template
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['Secret_Key'] = '9561546aa9bde13ad6308c83538b4ec8'

posts = [
	{
		"author":"sanchit",
		"title":"Blog Post 1",
		"content":"first post content",
		"date_posted": "04/04/2019"
	},
	{
		"author":"sanchit bansal",
		"title":"Blog Post 2",
		"content":"second post content",
		"date_posted": "05/03/2019"
	},
	{
		"author":"sam",
		"title":"Blog Post 3",
		"content":"third post content",
		"date_posted": "06/04/2019"
	}
]




@app.route('/')
@app.route("/home")
def home():
	return render_template('home.html', posts=posts)

@app.route("/about")
def about():
	return render_template('about.html')

@app.route("/register")
def register():
	form = RegisterForm()
	return render_template('register.html', form=form)

@app.route("/Login")
def Login():
	form = LoginForm()
	return render_template("login.html", form=form)

if __name__ == "__main__":
	app.run(debug=True)