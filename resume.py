from flask import Flask , render_template , url_for , request , redirect
import random
# me = {


resume = Flask (__name__)



me = {
	"first_name":"Hamza",
	"last_name":"Rdaideh",
	"description": "Hi, my name is Hamza Rdaideh. I live in Amman, Jordan.I am a Programmer. I have graduated from AlZaytoonah University, Faculty of Science and IT.",
	"social_links": [
			{"site":"Facebook","url":"https://web.facebook.com/hamza.alradaideh/"}, 
			{"site": "GitHub", "url": "https://github.com/HamzaMohammadRdaideh"},
			{"site": "Twiiter", "url": "https://twitter.com/Hamza11289384?s=09"},
			{"site": "Linkedin", "url": "https://www.linkedin.com/in/hamza-rdaideh-b072381b7/?lipi=urn%3Ali%3Apage%3Ad_flagship3_feed%3BLJ2Z8xi8Q8KUmcciPYWuMA%3D%3D'"}

	],
	"age": 24,
	"avatarURL": "https://media.squawka.com/images/en/2020/07/08150337/1150497_1150497_PA-11477570-2-scaled.jpg",
	"email": "rdaidehhamza@gmail.com",
	"skills": [	{"number": "1","course" : "Python","year":"2020","uni":"HTU "},
				{"number": "2","course" : "Java","year":"2019","uni":"ZUJ"},
				{"number": "3","course" : "HTML","year":"2018","uni":"ZUJ"},
				{"number": "4","course" : "Flask","year":"2020","uni":"HTU"},
				{"number": "5","course" : "SQL","year":"2017","uni":"ZUJ"}		
		],
				
	"projects": [
		{"name":"Tic-Tac-Toe", "description":"A description for the project", "tags":["functions", "control structures", "game"]},
		{"name":"Battle of Teams", "description":"A description for the project", "tags":["functions", "OOP"]},
		{"name":"Resume", "description":"A description for the project", "tags":["flask", "web application", "HTTP routes"]}
	],
		"favourite_quotes": [
		{"quote":"Patience you must have my young Padawan.", "author":"Hesham"},
		{"quote":"The more a thing tends to be permanent, the more it tends to be lifeless.", "author":"Reema"},
		{"quote":"Logic will get you from A to Z; imagination will get you everywhere.", "author":"Albert"}
	]
}





@resume.route('/')
def homepage():
    menu = [
        {"title":"Personal inormation", "url":url_for("me_html")},
        {"title":"Skills", "url":url_for("skill_html")},
        {"title":"Projects", "url":url_for("project_html")},
        {"title":"Quote", "url":url_for("favourite_html")}
        ]
    return render_template("home.html", menu=menu , me=me)


@resume.route('/me')
def me_html():
    return render_template('me.html' , me=me , social_links = me.get('social_links') , go_home=url_for("homepage") , pic = url_for('static' , filename='resume/image/manu.jpg'))


@resume.route('/editme')
def editme():
	pass



@resume.route('/project')
def project_html():
    return render_template('projects.html' , me=me , go_home=url_for("homepage"))



@resume.route('/skill')
def skill_html():
    return render_template('skills.html' , me=me , go_home=url_for("homepage"))


@resume.route('/ff')
def favourite_html():
	
	return render_template('favourite.html' , me=me , go_home=url_for("homepage"))


@resume.route('/add_quote', methods=["GET", "POST"])
def add_quote():
	if request.method == 'GET':
		return render_template("add_quote.html")
	else:
		newquote = request.form['new_quote']
		newauthor = request.form['new_author']
		me['favourite_quotes'].append({'quote':newquote,'author':newauthor})
		return redirect(url_for("favourite_html"))


@resume.route('/del_quote', methods=["GET", "POST"])
def del_quote():
	if request.method == 'GET':
		return render_template("del_quote.html", me = me)
	else:
		quotenumber = int(request.form['quote_number'])
		me['favourite_quotes'].pop(quotenumber)
		return redirect(url_for("favourite_html"))



if __name__ == "__main__":
    resume.run(debug=True)