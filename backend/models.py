from flask_sqlalchemy import SQLAlchemy

# Initialize SQLAlchemy
db = SQLAlchemy()

# Define a MenuItem model
class MenuItem(db.Model):
    __tablename__ = "menu_items"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)  # e.g., "Drink", "Main", "Dessert"
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text)

    def __repr__(self):
        return f"<MenuItem {self.name} - {self.category}>"

# Define a User model
class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    preferences = db.Column(db.Text)  # e.g., "vegetarian, spicy"

    def __repr__(self):
        return f"<User {self.username}>"

# Define a Recommendation model
class Recommendation(db.Model):
    __tablename__ = "recommendations"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    menu_item_id = db.Column(db.Integer, db.ForeignKey("menu_items.id"), nullable=False)

    user = db.relationship("User", backref="recommendations")
    menu_item = db.relationship("MenuItem", backref="recommendations")

    def __repr__(self):
        return f"<Recommendation User {self.user_id} -> Item {self.menu_item_id}>"