from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message
from dotenv import load_dotenv
import os

app = Flask(__name__)
app.secret_key = "supersecretkey"

# load env variables
load_dotenv()

# Mail Configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv("MAIL_USERNAME")
app.config['MAIL_PASSWORD'] = os.getenv("MAIL_PASSWORD")
app.config['MAIL_DEFAULT_SENDER'] = os.getenv("MAIL_USERNAME")

mail = Mail(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contact", methods = ["POST"])
def contact():
    name = request.form["name"]
    email = request.form["email"]
    subject = request.form["subject"]
    message = request.form["message"]
    
    msg = Message(
        subject = f"Portfolio Contact: {subject}",
        recipients = [os.getenv("MAIL_USERNAME")]
    )
    
    msg.html = f"""
        <h3>New Message from Portfolio</h3>
        <p><strong>Name:</strong> {name}</p>
        <p><strong>Email:</strong> {email}</p>
        <p><strong>Subject:</strong> {subject}</p>
        <p><strong>Message:</strong><br>{message}</p>
    """
    
    try:
        mail.send(msg)
        flash("Message sent successfully!", "success")
        return redirect(url_for("home"))
    except Exception as e:
        print("Email Error:", e)
        flash("Failed to send message!", "error")
        return redirect(url_for("home"))
    
if __name__ == "__main__":
    app.run(debug = True)