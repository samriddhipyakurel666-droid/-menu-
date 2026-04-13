from flask import Flask, render_template
from database import init_db, db
from models import MenuItem, User, Recommendation

app = Flask(__name__, template_folder="../frontend")

# Database configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///menu.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize database
init_db(app)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)