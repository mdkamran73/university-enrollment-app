from flask import Flask, render_template, request
import smtplib
from email.message import EmailMessage
import os

app = Flask(__name__)

# Email Configuration (use App Password, NOT your real Gmail password)
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = os.environ.get("SENDER_EMAIL")
SENDER_PASSWORD = os.environ.get("SENDER_PASSWORD")


def send_confirmation_email(student_name, student_email, course):
    msg = EmailMessage()
    msg["Subject"] = "University Enrollment Confirmation"
    msg["From"] = SENDER_EMAIL
    msg["To"] = student_email

    msg.set_content(f"""
Hello {student_name},

🎓 Congratulations!

You have successfully enrolled in the course: {course}

Your payment has been received.
This is a demo university enrollment confirmation email.

Regards,
University Admission Team
""")

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.send_message(msg)


@app.route("/", methods=["GET", "POST"])
def enroll():
    if request.method == "POST":
        student_name = request.form["name"]
        student_email = request.form["email"]
        course = request.form["course"]

        # Simulate Payment Success
        send_confirmation_email(student_name, student_email, course)

        return render_template("success.html",
                               name=student_name,
                               email=student_email,
                               course=course)

    return render_template("enroll.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

