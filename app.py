from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# SECRET_KEY zaroori hai flash messages aur security ke liye.
app.config['SECRET_KEY'] = 'your_secret_key_here'

# SQLite database configuration; yeh file 'reviews.db' naam se banegi.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reviews.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# SQLAlchemy ka object banaya
db = SQLAlchemy(app)

# Review model: Har review ek record ke roop mein store hoga.
class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(50), nullable=False)       # Jaise: Mobiles, Cars, etc.
    subcategory = db.Column(db.String(50), nullable=False)      # Jaise: Apple, Samsung, etc.
    product_name = db.Column(db.String(100), nullable=False)    # Jaise: iPhone 16 Pro Max
    review_text = db.Column(db.Text, nullable=False)            # Review ka pura text

# Home Page Route: Saare reviews ko display karega.
@app.route('/')
def index():
    reviews = Review.query.all()  # Database se saare reviews le aata hai.
    return render_template('index.html', reviews=reviews)

# Upload Review Route: Yahan form se review upload kiya jayega.
@app.route('/upload-review', methods=['GET', 'POST'])
def upload_review():
    if request.method == 'POST':
        # Form se data nikalna
        category = request.form.get('category')
        subcategory = request.form.get('subcategory')
        product_name = request.form.get('product_name')
        review_text = request.form.get('review_text')
        
        # Agar koi field empty hai to flash message dikhayein
        if not (category and subcategory and product_name and review_text):
            flash("Kripya sabhi fields bharen", "error")
            return redirect(url_for('upload_review'))
        
        # Naya Review object banayein aur database mein add karein
        new_review = Review(
            category=category,
            subcategory=subcategory,
            product_name=product_name,
            review_text=review_text
        )
        db.session.add(new_review)
        db.session.commit()
        flash("Review safalta purvak upload ho gaya!", "success")
        return redirect(url_for('upload_review'))
    
    # GET request ke liye upload_review.html render karein.
    return render_template('upload_review.html')

if __name__ == '__main__':
    # Pehli baar run karte waqt database create karne ke liye, neeche ki line ko uncomment kar dein:
    # db.create_all()
    app.run(debug=True)
