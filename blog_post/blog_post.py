import mechanize
import string

#submitting new blog post
def post():
	#execute other functions
	title, category, entry = parse_txt_file()
	username, password = login()
	
	#create new browser class instance
	browser = mechanize.Browser()
	browser.set_handle_robots(False)
	
	#nagivate to page and login
	browser.open("http://blog.whackandblite.com")
	browser.follow_link(text="Login", nr=0)
	browser.select_form(name="admin_login")
	browser.form["admin_username"] = username
	browser.form["admin_password"] = password
	browser.submit()
	
	#submit post
	browser.select_form(name="new_entry")
	browser.form["title"] = title
	browser.form["category"] = category
	browser.form["entry"] = entry
	browser.submit()

#parsing blog post text file
def parse_txt_file():
	source = raw_input("Location of text file for post: ")
	target = open(source, 'r')
	title = target.readline().rstrip('\n')
	category = target.readline().rstrip('\n')
	
	#turning '\n' into '<br />'
	raw_entry = target.read()
	clean_entry = ""
	for x in raw_entry:
		if x == "\n":
			x = "<br />"
		clean_entry += x
		
	entry = clean_entry
	return title, category, entry

#login information
def login():
	print "\nLogin"
	username = raw_input("Username: ")
	password = raw_input("Password: ")
	return username, password

post()
	