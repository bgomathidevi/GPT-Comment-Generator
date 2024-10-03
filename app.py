import openai
import os
import streamlit as st
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Function to generate comment using GPT
def generate_comment(post_text, theme):
    prompt = f"Generate a {theme} comment on the following post:\n\n{post_text}\n\nComment:"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message['content'].strip()

# Streamlit user interface
def main():
    st.title("GPT Comment Generator")

    # Text area for user to paste the post
    post_text = st.text_area("Paste the post here:", height=200)

    # Dropdown for selecting the type of comment
    theme = st.selectbox("Select the type of comment:", 
                         ["Insightful", "Funny", "Interesting", "Appreciation","Motivation","New insights"])

    # Button to generate the comment
    if st.button("Generate Comment"):
        if post_text:
            comment = generate_comment(post_text, theme)
            st.success(f"Generated Comment: {comment}")
        else:
            st.error("Please enter a post to generate a comment.")

if __name__ == "__main__":
    main()
