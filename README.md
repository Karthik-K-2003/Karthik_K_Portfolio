🌐 Karthik's Flask Portfolio Website
----------------------------------------
A modern, responsive personal portfolio website built using Flask, TailwindCSS, HTML, and JavaScript.
This website showcases my skills, projects, experience, and includes a contact form powered by Flask-Mail / SMTP using secure environment variables.

🚀 Features
----------------------------------------
🖥️ Fully responsive UI (mobile, tablet & desktop)
🎨 Clean dark theme with teal accents
💼 Projects section with cards
🧠 Skills & Experience sections
📬 Working contact form (Flask backend)
🔐 Secure .env file for email credentials
⚡ Fast loading with optimized static assets
📂 Organized folder structure (templates + static)

🛠️ Tech Stack
----------------------------------------
1. Frontend
 - HTML5
 - Tailwind CSS
 - Custom CSS
 - JavaScript (interactions)
   
2. Backend
 - Python
 - Flask
 - Flask-Mail (SMTP integration)

3. Tools
 - Virtual Environment
 - pip (Python package manager)
 - Gmail SMTP (App Passwords)

📁 Folder Structure
----------------------------------------
Flask_Portfolio/
│
├── static/
│   ├── css/         # Custom styles
│   ├── js/          # Scripts
│   └── assets/      # Images, icons (optional if hidden in .gitignore)
│
├── templates/
│   ├── index.html   # Main portfolio page
│   ├── projects.html
│   ├── contact.html
│   └── layout.html  # Base template
│
├── app.py           # Flask application entry point
├── .env             # Email credentials (ignored in Git)
├── requirements.txt # Python dependencies
└── README.md

⚙️ Setup Instructions
-----------------------------------------
1. Clone the repository
   git clone https://github.com/yourusername/Flask_Portfolio.git
   cd Flask_Portfolio

2. Create virtual environment & activate
  python -m venv venv
  source venv/bin/activate   # Mac / Linux
  venv\Scripts\activate      # Windows

3. Install dependencies
  pip install -r requirements.txt

4. Configure environment variables
  Create a .env file in the root folder:
    MAIL_SERVER=smtp.gmail.com
    MAIL_PORT=587
    MAIL_USE_TLS=True
    MAIL_USERNAME=your_email@gmail.com
    MAIL_PASSWORD=your_app_password

5. Run the Flask server
   python app.py

6. Test the Contact Form
   Fill out the contact form → If your SMTP credentials are correct,you will receive an email 🎉
   
🖼️ Screenshots:
   <img width="1896" height="892" alt="Screenshot 2025-11-25 190950" src="https://github.com/user-attachments/assets/966c3a34-b9ba-43c2-a949-faf45d4bac0c" />

