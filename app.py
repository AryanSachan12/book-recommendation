import streamlit as st
import pickle

# Load the data and model
book_pivot = pickle.load(open("book.pkl", "rb"))
book_images = pickle.load(open("book_images.pkl", "rb"))
model = pickle.load(open("model.pkl", "rb"))

# Prepare the list of book titles
book_titles = book_images["Book-Title"].values
book_titles.sort()

# Streamlit interface
st.set_page_config(layout="wide")
st.title("Book Recommendation (Collaborative Filtering)")

# Select a book from the dropdown
selected_book = st.selectbox("Enter your favorite book", book_titles)

# Get the index of the selected book
book_index = book_pivot.index.get_loc(selected_book)

# Suggest books when the button is clicked
if st.button("Suggest"):
    distances, suggestions = model.kneighbors(
        book_pivot.iloc[book_index, :].values.reshape(1, -1), n_neighbors=7
    )

    # Display recommended books (start from 1 to skip the selected book itself)
    st.subheader("Recommended Books:")

    # Create a grid layout for the recommended books
    num_books = len(suggestions[0]) - 1  # excluding the selected book
    num_cols = 3  # Number of columns in the grid
    cols = st.columns(num_cols)  # Create columns

    # Loop through recommendations and layout the books
    for i in range(1, num_books + 1):
        recommended_book_index = suggestions[0][i]
        recommended_book = book_pivot.index[recommended_book_index]

        # Get the corresponding book image URL
        recommended_book_image_url = book_images.loc[
            book_images["Book-Title"] == recommended_book, "Image-URL-L"
        ].values[0]

        # Calculate the column index
        col = cols[i % num_cols]  # Distribute the books across the columns

        # Standardize the height of the images (set the height and maintain aspect ratio)
        with col:
            st.markdown(
                f"<div style='text-align: center;'><img src='{recommended_book_image_url}' height='300' style='width: auto; display: block; margin: 0 auto;' /></div>",
                unsafe_allow_html=True,
            )
            st.markdown(
                f"<h5 style='text-align: center; color: #333366;'>{recommended_book}</h5>",
                unsafe_allow_html=True,
            )
