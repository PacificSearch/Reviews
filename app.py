from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Secret key for sessions and flash messages.
app.config['SECRET_KEY'] = 'your_secret_key_here'
# SQLite database configuration; this will create 'reviews.db' in the root folder.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reviews.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Review model: Har review ek record ke roop mein store hoga.
class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(50), nullable=False)       # e.g., Mobiles, Cars, etc.
    subcategory = db.Column(db.String(50), nullable=False)      # e.g., Apple, Samsung, etc.
    product_name = db.Column(db.String(100), nullable=False)    # e.g., iPhone 16 Pro Max
    review_text = db.Column(db.Text, nullable=False)            # Review ka pura text
    language = db.Column(db.String(10), nullable=False, default='EN')  # New field for language

# Automatically create database tables if 'reviews.db' does not exist.
if not os.path.exists('reviews.db'):
    with app.app_context():
        db.create_all()
        print("Database tables created successfully!")

# Home page route: Saare reviews display karega along with filter panel.
@app.route('/')
def index():
    reviews = Review.query.all()
    return render_template('index.html', reviews=reviews)

# Upload review route: Form se review upload karega.
@app.route('/upload-review', methods=['GET', 'POST'])
def upload_review():
    if request.method == 'POST':
        category = request.form.get('category')
        subcategory = request.form.get('subcategory')
        product_name = request.form.get('product_name')
        review_text = request.form.get('review_text')
        language = request.form.get('language')  # New field from form

        if not (category and subcategory and product_name and review_text and language):
            flash("Kripya sabhi fields bharen", "error")
            return redirect(url_for('upload_review'))

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

# New route for filtering reviews by subcategory.
@app.route('/filter')
def filter_reviews():
    subcategory = request.args.get('subcategory')
    if subcategory:
        filtered_reviews = Review.query.filter_by(subcategory=subcategory).all()
    else:
        filtered_reviews = []
    return render_template('filtered.html', reviews=filtered_reviews, subcategory=subcategory)

if __name__ == '__main__':
    app.run(debug=True)
