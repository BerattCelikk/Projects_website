from flask import Flask, redirect , render_template,abort,request, url_for
import os

app = Flask(__name__)

projects = [
    {
        "title":"King Size AWS",
        "description":"This project offers an introduction to Amazon Web Services (AWS), including certification guidance and cloud fundamentals, presented through a web-based interface.",
        "link":"https://kingsizeaws.great-site.net/?i=1",
        "technologies": ["HTML", "CSS", "Bootstrap", "AWS"],
        "image":"images/awsfoto.png"
    },
    {
    "title": "Audi Water Consumption Dashboard",
    "description": "A comprehensive digital twin solution for monitoring and optimizing water consumption in Audi production facilities. Features anomaly detection, trend analysis, and simulation capabilities.",
    "link": "https://audi-real.onrender.com/",
    "technologies": ["Python", "Dash", "Plotly", "Pandas", "Digital Twin"],
    "image": "images/proje2resim2.png"
    },
    {
    "title": "Car Rental Management System",
    "description": "A comprehensive system for managing car rentals, including features for booking, inventory management, and customer relationship management.",
    "link": "https://github.com/BerattCelikk/DATABASE_PROJECT",
    "technologies": ["Python", "Flask", "HTML", "CSS"],
    "image": "images/proje3.png"
    },
    {
        "title": "Grails Tracking Carbon Emissions",
        "description": "Rotterdam University Grails - Tracking Carbon Emission Analysis and Predictions",
        "link": "https://github.com/BerattCelikk/Grails_Tracking_Carbon_Emissions",
        "technologies": ["Python", "Machine Learning", "Pandas", "Matplotlib", "Scikit-learn", "Seaborn","Tkinter"],
        "image": "images/proje4.png"
    },
    {
        "title": "Advanced Matrix Calculator",
        "description": "A comprehensive web application for matrix calculations including operations (+, -, *), special matrix checks (idempotent, nilpotent, etc.), and properties analysis (trace, symmetry).",
        "link": "https://matrix-calculator-10wo.onrender.com/",
        "technologies": ["Python", "Flask", "NumPy", "JavaScript", "HTML5", "CSS3"],
        "image": "images/matrixphoto.png"
    }

]
@app.route('/')
def index():
    return render_template("index.html", projects=projects)

@app.route("/projects/<int:project_id>")
def project_detail(project_id):
    if 0 <= project_id < len(projects):
        return render_template("project_detail.html", project=projects[project_id])
    else:
        abort(404)
        
        
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
