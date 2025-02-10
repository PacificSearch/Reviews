from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Secret key for sessions and flash messages.
app.config['SECRET_KEY'] = 'your_secret_key_here'
# Configure SQLite database; this will create a file named 'reviews.db' in the root folder.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reviews.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Review model: har review record mein category, subcategory, product name, review text, aur language store hoga.
class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(50), nullable=False)       # Example: Mobiles, Cars, etc.
    subcategory = db.Column(db.String(50), nullable=False)      # Example: Apple, Samsung, etc.
    product_name = db.Column(db.String(100), nullable=False)    # Example: iPhone 16 Pro Max
    review_text = db.Column(db.Text, nullable=False)            # Complete review text
    language = db.Column(db.String(10), nullable=False, default='EN')  # Language of the review

# Automatically create database tables if the database file doesn't exist.
if not os.path.exists('reviews.db'):
    with app.app_context():
        db.create_all()
        print("Database tables created successfully!")

# Home page route: Displays all reviews.
@app.route('/')
def index():
    reviews = Review.query.all()
    return render_template('index.html', reviews=reviews)

# Upload review route: Handles the review upload form.
@app.route('/upload-review', methods=['GET', 'POST'])
def upload_review():
    if request.method == 'POST':
        # Retrieve form data.
        category = request.form.get('category')
        subcategory = request.form.get('subcategory')
        product_name = request.form.get('product_name')
        review_text = request.form.get('review_text')
        language = request.form.get('language')  # New language field

        # Check if all fields are filled.
        if not (category and subcategory and product_name and review_text and language):
            flash("Kripya sabhi fields bharen", "error")
            return redirect(url_for('upload_review'))

        # Create a new Review object.
        new_review = Review(
            category=category,
            subcategory=subcategory,
            product_name=product_name,
            review_text=review_text,
            language=language
        )
        db.session.add(new_review)
        db.session.commit()
        flash("Review safalta purvak upload ho gaya!", "success")
        return redirect(url_for('upload_review'))
    
    return render_template('upload_review.html')

if __name__ == '__main__':
    app.run(debug=True)
