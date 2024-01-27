from flask import Flask, render_template
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.fastmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'berny@fastmail.com'
app.config['MAIL_PASSWORD'] = 'w5enmhucdzy93yfj'
app.config['MAIL_USE_TLS'] =  False
app.config['MAIL_USE_SSL'] = True    

    

mail = Mail(app)


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/contact.html")
def contact():
    return render_template('contact.html')


x = 0    

@app.route("/submit_form", methods=["GET","POST"])

def email_form():
    
    msg = Message(subject='Hello from the other side!', sender='noreply@demo.com', recipients=['berny@fastmail.com'])
    msg.body = "Test"
    mail.send(msg)
    
    return render_template('contact.html')

