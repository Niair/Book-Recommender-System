import streamlit as st
import pandas as pd
import numpy as np
import pickle
from rapidfuzz import process
from streamlit_option_menu import option_menu
from fuzzywuzzy import process

# Load pickled models and data
books_df = pickle.load(open('data/books.pkl', 'rb'))
pt = pickle.load(open('data/pt.pkl', 'rb'))
similarity_scores = pickle.load(open('data/similarity_scores.pkl', 'rb'))
popular_df = pickle.load(open('data/popular.pkl', 'rb'))

# App Config
st.set_page_config(page_title="Book Recommender", layout="wide")

# Custom CSS Styling
st.markdown("""
    <style>
        body {
            background-color: #272A35;
        }
        .main {
            background-color: #272A35;
            color: #A1B1CC;
        }
        h1, h2, h3, h4, h5, h6, .stText, .stMarkdown, .stButton>button {
            color: #A1B1CC;
        }
        .stButton>button {
            background-color: #0E7EC0;
            color: white;
            border: none;
            padding: 0.6em 1.2em;
            border-radius: 8px;
        }
        .stButton>button:hover {
            background-color: #0c6fb0;
        }
        .stImage img {
            border-radius: 10px;
        }
        .book-card {
            background-color: #1e212b;
            padding: 1rem;
            border-radius: 10px;
            box-shadow: 0 0 8px rgba(208, 219, 238, 0.15);
            margin-bottom: 1rem;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar Navigation
with st.sidebar:
    st.markdown("<h4 style='margin-bottom:0;'>📚 Navigation</h4><hr>", unsafe_allow_html=True)
    selected = option_menu(
        menu_title=None,
        options=["Home", "Recommendations", "Top Books", "About Us", "Contact Us"],
        icons=["house", "book", "trophy", "info-circle", "envelope"],
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "#1e212b"},
            "icon": {"color": "#D0DBEE", "font-size": "20px"},
            "nav-link": {
                "font-size": "16px",
                "text-align": "left",
                "margin": "5px",
                "padding": "10px 15px",
                "--hover-color": "#0E7EC0",
                "color": "#A1B1CC"
            },
            "nav-link-selected": {
                "background-color": "#0E7EC0",
                "color": "white",
                "font-weight": "bold",
                "border-radius": "5px",
            },
        }
    )

# ------------------ Main Pages ------------------

if selected == "Home":
    st.title("📚 Welcome to BookBuddy")
    st.subheader("Your Personal Book Recommendation Companion")

    st.markdown("""
    <p style='color:#848B9B; font-size:16px;'>
    Discover books you'll love based on your favorite reads. Whether you're into fiction, fantasy, history, or science – we’ve got something tailored just for you!
    </p>
    """, unsafe_allow_html=True)

    st.image("https://images.unsplash.com/photo-1512820790803-83ca734da794", caption="Find your next read!", use_container_width=True)

    st.markdown("### 🔍 Start Exploring:")
    st.markdown("- Head to **Recommendations** to get personalized book suggestions")
    st.markdown("- Check out our **Top Books** page for trending reads")
    st.markdown("- Learn more in **About Us** or **Contact Us**")

elif selected == "Recommendations":
    st.title("📖 Get Book Recommendations")
    st.subheader("🔍 Find similar books based on what you love")

    all_titles = list(pt.index)

    def get_fuzzy_options(user_input):
        if user_input.strip():
            return [match[0] for match in process.extract(user_input, all_titles, limit=50)]
        else:
            return all_titles  # show all books if no input

    # Single searchable selectbox with fuzzy matching
    selected_title = st.selectbox(
        "Search or select a book:",
        options=get_fuzzy_options(""),  # Start with all books
        index=0,
        key="book_search"
    )

    # Update options dynamically based on input
    if "book_search" in st.session_state:
        user_input = st.session_state["book_search"]
        st.session_state.book_search_options = get_fuzzy_options(user_input)

    if st.button("Recommend"):
        if not selected_title:
            st.warning("Please select a book.")
        else:
            st.success(f"📚 Recommendations for **{selected_title}**:")

            book_index = np.where(pt.index == selected_title)[0][0]
            similar_items = sorted(
                list(enumerate(similarity_scores[book_index])),
                key=lambda x: x[1],
                reverse=True
            )[1:6]

            for idx, sim in similar_items:
                recommended_title = pt.index[idx]
                temp_df = books_df[books_df['Book-Title'] == recommended_title].drop_duplicates('Book-Title')

                if not temp_df.empty:
                    rec = temp_df.iloc[0]
                    cols = st.columns([1, 4])
                    with cols[0]:
                        st.image(rec['Image-URL-M'], width=100)
                    with cols[1]:
                        st.markdown(
                            f"<div class='book-card'><strong>{rec['Book-Title']}</strong><br>by {rec['Book-Author']}</div>",
                            unsafe_allow_html=True
                        )
elif selected == "Top Books":
    st.title("🏆 Top 50 Books Loved by Readers")
    st.subheader("🔥 Trending Now")
    
    for i in range(len(popular_df)):
      book = popular_df.iloc[i]
      cols = st.columns([1, 4])
      with cols[0]:
            st.image(book['Image-URL-M'], width=100)
      with cols[1]:
            st.markdown(
                  f"<div class='book-card'><strong>{book['Book-Title']}</strong><br>"
                  f"by {book['Book-Author']}<br>"
                  f"⭐ Rating: {book['avg_rating']} | 🗳️ Votes: {book['num_ratings']}</div>",
                  unsafe_allow_html=True
            )
      
      # Add a small gap between book entries
      st.markdown("<br>", unsafe_allow_html=True)

elif selected == "About Us":
    st.title("ℹ️ About Us")
    st.markdown("""
    <p style='color:#A1B1CC; font-size:16px;'>
    BookBuddy is a personalized recommendation platform built with ❤️ for all book lovers. Our system learns your preferences and suggests reads you'll truly enjoy!
    </p>
    """, unsafe_allow_html=True)

elif selected == "Contact Us":
    st.title("✉️ Contact Us")
    st.markdown("""
    <p style='color:#A1B1CC; font-size:16px;'>
    We'd love to hear from you! Reach out with suggestions, issues, or just to say hello.
    </p>
    """, unsafe_allow_html=True)

    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        submitted = st.form_submit_button("Send")
        if submitted:
            st.success("Thanks for reaching out! We’ll get back to you soon.")
