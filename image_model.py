import google.generativeai as genai
import PIL.Image
import streamlit as st
import os

# Function to get the Gemini AI response
# Function to get the Gemini AI response
def get_gemini_response(api_key, prompt, image):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
    response = model.generate_content([prompt, image])
    return response.text

# Initialize the Streamlit app
st.set_page_config(page_title="Red Chilli AI Function DEMO") 

st.header("Gemini Application")

# Set the API key directly
api_key = "AIzaSyA-dMDZ1SipPy7MUpfkBqV8qPQEIVPTH0g"

# Set the prompt directly
prompt = "How many red chilli can be observed and other color type of chilli. Get the total of red chilli and the total other of color of chilli can be observed from the image. Determine how many percent red chilli. No need to explain anything I only need it in percent."

# File uploader to allow users to upload an image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image = None

if uploaded_file is not None:
    image = PIL.Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

# Button to submit the request
submit = st.button("Tell me about the image")

# If the submit button is clicked, configure the API key and get the Gemini AI response
if submit and image is not None:
    try:
        response = get_gemini_response(api_key, prompt, image)
        st.subheader("The Response is:")
        st.write(response)
    except Exception as e:
        st.error(f"An error occurred: {e}")
