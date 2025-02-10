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

# Review model with language, category, subcategory, product name, and review text.
class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    language = db.Column(db.String(10), nullable=False, default='EN')  # e.g., EN or HI
    category = db.Column(db.String(50), nullable=False)              # e.g., Mobiles, Cars, etc.
    subcategory = db.Column(db.String(50), nullable=False)             # e.g., Apple, Samsung, etc.
    product_name = db.Column(db.String(100), nullable=False)           # e.g., iPhone 16 Pro Max
    review_text = db.Column(db.Text, nullable=False)                   # Complete review text

# Automatically create database tables if 'reviews.db' doesn't exist.
if not os.path.exists('reviews.db'):
    with app.app_context():
        db.create_all()
        print("Database tables created successfully!")

# Home page route:
# If query parameter 'subcategory' is provided, filter reviews accordingly.
@app.route('/')
def index():
    subcategory = request.args.get('subcategory')
    if subcategory:
        reviews = Review.query.filter_by(subcategory=subcategory).all()
    else:
        reviews = Review.query.all()
    return render_template('index.html', reviews=reviews, selected_subcategory=subcategory)

# Review upload route:
# This route displays a simple upload form and handles form submission.
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
    
    # Simple inline HTML for the upload form (for simplicity, not using a separate template).
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <title>Upload Review</title>
      <link rel="stylesheet" href="/static/styles.css">
    </head>
    <body>
      <h1>Upload a New Review</h1>
      <form method="POST">
        <label for="language">Language:</label><br>
        <select name="language" id="language" required>
          <option value="EN">English</option>
          <option value="HI">Hinglish</option>
        </select><br><br>
        
        <label for="category">Category:</label><br>
        <select name="category" id="category" required>
          <option value="Mobiles">Mobiles</option>
          <option value="Cars">Cars</option>
          <option value="Monitors">Monitors</option>
          <option value="CPU">CPU</option>
          <option value="Laptops">Laptops</option>
        </select><br><br>
        
        <label for="subcategory">Subcategory:</label><br>
        <input type="text" name="subcategory" id="subcategory" placeholder="e.g., Apple" required><br><br>
        
        <label for="product_name">Product Name:</label><br>
        <input type="text" name="product_name" id="product_name" placeholder="e.g., iPhone 16 Pro Max" required><br><br>
        
        <label for="review_text">Review:</label><br>
        <textarea name="review_text" id="review_text" rows="5" placeholder="Enter review here" required></textarea><br><br>
        
        <input type="submit" value="Upload Review">
      </form>
      <p><a href="/">Back to Home</a></p>
    </body>
    </html>
    '''
    @app.route('/delete-review/<int:review_id>', methods=['POST'])
def delete_review(review_id):
    review = Review.query.get_or_404(review_id)
    db.session.delete(review)
    db.session.commit()
    flash("Review delete ho gaya!", "success")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
