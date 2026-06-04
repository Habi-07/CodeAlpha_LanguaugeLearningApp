import streamlit as st

# Title
st.title("🌍 Language Learning App")

# Sidebar navigation
menu = st.sidebar.selectbox("Choose Section", ["Vocabulary", "Grammar", "Quizzes", "Progress"])

# Local progress storage
progress = []

# Vocabulary Section
if menu == "Vocabulary":
    st.header("Daily Flashcards")
    flashcards = [
        {"word": "Bonjour", "translation": "Hello", "pronunciation": "bon-zhoor"},
        {"word": "Merci", "translation": "Thank you", "pronunciation": "mehr-see"},
        {"word": "Au revoir", "translation": "Goodbye", "pronunciation": "oh ruh-vwar"},
    ]
    for card in flashcards:
        st.subheader(card["word"])
        st.write(f"Translation: {card['translation']}")
        st.write(f"Pronunciation: {card['pronunciation']}")
        st.markdown("---")

elif menu == "Grammar":
    st.header("Basic Grammar Tips")
    st.write("1️⃣ Nouns have gender (masculine/feminine).")
    st.write("2️⃣ Verbs change with subject (je, tu, il/elle).")
    st.write("3️⃣ Adjectives agree with nouns in gender and number.")

elif menu == "Quizzes":
    st.header("Quick Quiz")
    question = "What does 'Merci' mean?"
    options = ["Hello", "Thank you", "Goodbye"]
    answer = st.radio(question, options)
    if st.button("Submit"):
        if answer == "Thank you":
            st.success("✅ Correct!")
            progress.append({"name": "User", "score": 100})
        else:
            st.error("❌ Try again!")
            progress.append({"name": "User", "score": 0})

elif menu == "Progress":
    st.header("Your Learning Progress")
    if progress:
        for entry in progress:
            st.write(f"{entry['name']} — Score: {entry['score']}")
    else:
        st.info("No progress saved yet.")
