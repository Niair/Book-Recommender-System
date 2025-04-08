# Book-Recommender-System
### Discover books you'll love based on your favorite reads. A visually engaging, machine learning-powered book recommendation app built with Streamlit.

---

## 📖 Project Overview

**BookBuddy** is a personalized content-based book recommender system developed using **Streamlit**, **Scikit-learn**, and **RapidFuzz**. It analyzes user-selected book titles and recommends similar books based on TF-IDF vector similarity, while showcasing book cover images for an intuitive user experience.

The app offers a sleek, responsive interface with sidebar navigation, image previews, and stylized book cards. It is modular, scalable, and designed to be deployed online.

---

## 🌟 App Features

### 🏠 Home
- Clean, modern landing page with call-to-action and featured image.
- Introduces app features and navigation guide.

### 🔍 Book Recommendations
- **Searchable dropdown** with fuzzy matching to find book titles.
- Recommends **5 similar books** with title, author, and book cover image.
- Uses **TF-IDF + Cosine Similarity** on user-book matrix.

### 🏆 Top Books
- Displays **Top 50 Most Popular Books** based on user ratings.
- Includes metadata: Title, Author, Average Rating, Number of Votes.
- Book covers and summary cards enhance visual appeal.

### ℹ️ About Us
- Brief overview of the app’s purpose and motivation.

### ✉️ Contact Us
- Form for users to send queries or feedback.

---

## 🛠️ Technical Stack

| Component      | Description                                      |
|----------------|--------------------------------------------------|
| **Frontend**   | Streamlit, HTML, CSS, Custom Themes              |
| **Backend**    | Python, Scikit-learn, Pandas, NumPy              |
| **ML Model**   | TF-IDF Vectorizer, Cosine Similarity Matrix      |
| **Image Logic**| Book cover URLs integrated from dataset          |
| **UX**         | RapidFuzz + FuzzyWuzzy for enhanced search       |

---

## 🔧 How It Works

### 💡 Recommendation Logic:
1. User selects a book title via fuzzy search dropdown.
2. The app fetches precomputed similarity scores from the TF-IDF matrix.
3. It returns the top 5 most similar books.
4. Displays recommendations in responsive columns with:
   - Title
   - Author
   - Cover Image

### 📊 Top Books Logic:
- Popular books loaded from a separate precomputed `popular.pkl` file.
- Sorted by number of ratings and average rating.

---

## 🗂️ Files & Directory Structure

```
bookbuddy/
│
├── app.py                      # Main Streamlit application
├── data/
│   ├── books.pkl               # Metadata with image URLs
│   ├── pt.pkl                  # Pivot table of users vs. books
│   ├── similarity_scores.pkl   # Cosine similarity matrix
│   └── popular.pkl             # Top 50 popular books
├── notebooks/
├── requirements.txt           # Required Python libraries
└── README.md                  # Project documentation
```

---

## 📸 App Preview

### 🔍 Recommendations Page

<img src="https://via.placeholder.com/600x250.png?text=Recommendation+Example" width="600"/>

---

### 🏆 Top Books Page

<img src="https://via.placeholder.com/600x250.png?text=Top+Books+Example" width="600"/>

---

## ▶️ Installation & Usage

### ✅ Prerequisites
- Python 3.7+
- pip / conda

### 💻 Setup
```bash
git clone https://github.com/yourusername/bookbuddy.git
cd bookbuddy
pip install -r requirements.txt
streamlit run app.py
```

---

## 🌐 Deployment

You can deploy this app on:

- **Streamlit Community Cloud** (1-click deploy)
- **Render**, **Heroku**, **Vercel** (using FastAPI wrapper if needed)
- **Docker** for containerized hosting
