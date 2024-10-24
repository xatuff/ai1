import google.generativeai as genai
import PIL.Image
import streamlit as st
import os

# Function to get the Gemini AI response
def get_gemini_response(api_key, prompt, image):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
    response = model.generate_content([prompt, image])
    return response.text

# Initialize the Streamlit app
st.set_page_config(page_title="Gemini Vision Bot Demo")

st.header("Gemini Application")

# Input field for the Google API Key
api_key = st.text_input("Enter your Gemini API Key: ", type="password")

# Input prompt from the user
prompt = st.text_input("Input Prompt (e.g., 'What is in this photo?'): ", key="input")

# File uploader to allow users to upload an image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image = None

if uploaded_file is not None:
    image = PIL.Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

# Button to submit the request
submit = st.button("Tell me about the image")

# If the submit button is clicked, configure the API key and get the Gemini AI response
if submit and api_key and image is not None:
    try:
        response = get_gemini_response(api_key, prompt, image)
        st.subheader("The Response is:")
        st.write(response)
    except Exception as e:
        st.error(f"An error occurred: {e}")
