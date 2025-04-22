# 📚 Book Recommendation System (Collaborative Filtering) 📚

Welcome to the **Book Recommendation System**! This application recommends books based on your favorite book selection using **Collaborative Filtering** and the **k-Nearest Neighbors** algorithm. It leverages a machine learning model to find similar books and present them in an easy-to-use interface with book cover images.

## 🚀 [Live Demo](https://aryansachan12-book-recommendation-app-wimb48.streamlit.app/) <- Click to see it in action!

## 🌟 Features

- **Interactive Book Selection**: Select your favorite book from a dropdown list.
- **Smart Recommendations**: Get personalized book recommendations based on the chosen book using collaborative filtering.
- **Book Covers**: Each recommended book is displayed with its cover image for easy identification and visual appeal.

---

## 🛠️ Technologies Used

- **Streamlit**: Interactive web app framework.
- **Pickle**: For loading pre-trained models and book data.
- **k-Nearest Neighbors (k-NN)**: Collaborative filtering algorithm used to find similar books.
- **Pandas**: For efficient data handling and manipulation.

---

## 📥 Installation

### Prerequisites

Ensure you have the following installed:

- Python 3.7+ (recommended)
- pip (Python package installer)

### Steps to Run the Project Locally

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/book-recommendation-system.git
   ```

2. **Navigate to the project directory**:

   ```bash
   cd book-recommendation-system
   ```

3. **Install the required dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Streamlit app**:

   ```bash
   streamlit run app.py
   ```

   This will open the app in your default web browser.

---

## 📂 Project Files

- **app.py**: Main file that powers the Streamlit app, showing book recommendations.
- **book.pkl**: Pickled file containing the book pivot data used for collaborative filtering.
- **book_images.pkl**: Pickled file containing the image URLs for book covers.
- **model.pkl**: Pickled k-NN model used to generate book recommendations.

---

## 🔍 How It Works

1. **Select a Book**: Choose your favorite book from the dropdown.
2. **Recommendation**: The system uses **k-NN** to find similar books based on your selection.
3. **Display**: The recommended books are shown in a grid layout, each with its cover image.
4. **Interact**: Select a different book and get updated recommendations in real-time.

---

## 🤝 Contributing

We welcome contributions! If you'd like to improve or add features to the project, feel free to:

1. Fork the repository.
2. Make your changes.
3. Open a pull request with a description of your changes.

---

## 📬 Contact

Feel free to reach out for questions or feedback via email:  
[aryansachan2004@gmail.com](mailto:aryansachan2004@gmail.com)
