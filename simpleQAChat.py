import streamlit as st

# Define simple FAQ pairs
faqs = {
    "What is your name?": "I am a chatbot created for this demonstration.",
    "How can I help you?": "I can answer your questions or assist with basic tasks.",
    "Where are you located?": "I exist online and can help from anywhere!",
}

# Streamlit Interface
st.title("Simple FAQ Chatbot")

user_input = st.text_input("Ask me anything:")

if user_input:
    response = faqs.get(user_input, "Sorry, I didn’t understand that.")
    st.write(f"**Bot:** {response}")
