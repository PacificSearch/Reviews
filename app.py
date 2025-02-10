from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Secret key for sessions and flash messages.
app.config['SECRET_KEY'] = 'your_secret_key_here'
# Configure SQLite database; 'reviews.db' will be created in the root folder.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reviews.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Review model: stores language, category, subcategory, product name, and review text.
class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    language = db.Column(db.String(10), nullable=False, default='EN')
    category = db.Column(db.String(50), nullable=False)
    subcategory = db.Column(db.String(50), nullable=False)
    product_name = db.Column(db.String(100), nullable=False)
    review_text = db.Column(db.Text, nullable=False)

# Automatically create database tables if 'reviews.db' doesn't exist.
if not os.path.exists('reviews.db'):
    with app.app_context():
        db.create_all()
        print("Database tables created successfully!")

# Home page route: displays all reviews; supports filtering by subcategory via query parameter.
@app.route('/')
def index():
    subcategory = request.args.get('subcategory')
    if subcategory:
        reviews = Review.query.filter_by(subcategory=subcategory).all()
    else:
        reviews = Review.query.all()
    return render_template('index.html', reviews=reviews, selected_subcategory=subcategory)

# Review upload route: shows the upload form and handles review submission.
@app.route('/upload-review', methods=['GET', 'POST'])
def upload_review():
    if request.method == 'POST':
        language = request.form.get('language')
        category = request.form.get('category')
        subcategory = request.form.get('subcategory')
        product_name = request.form.get('product_name')
        review_text = request.form.get('review_text')
        if not (language and category and subcategory and product_name and review_text):
            flash("Kripya sabhi fields bharen", "error")
            return redirect(url_for('upload_review'))
        new_review = Review(
            language=language,
            category=category,
            subcategory=subcategory,
            product_name=product_name,
            review_text=review_text
        )
        db.session.add(new_review)
        db.session.commit()
        flash("Review safalta purvak upload ho gaya!", "success")
        return redirect(url_for('upload_review'))
    return render_template('upload_review.html')

# DELETE ROUTE: Delete a review by its ID.
@app.route('/delete-review/<int:review_id>', methods=['POST'])
def delete_review(review_id):
    review = Review.query.get_or_404(review_id)
    db.session.delete(review)
    db.session.commit()
    flash("Review delete ho gaya!", "success")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
