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
st.set_page_config(page_title="Red Chilli AI Function Demo") 

st.header("Red Chilli AI Function DEMO")

# Set the API key directly
api_key = "AIzaSyCDArjAnWftMGMiQXwVPwfQWDWN09EKMZE"

# Set the prompt directly
prompt = "How many red chilli can be observed and other color type of chilli. Get the total of red chilli and the total other of color of chilli can be observed from the image. Determine how many percent red chilli. No need to explain anything I only need it in percent. If there's NO CHILLI observed, then just say 0%. Make sure it's concise!"

# File uploader to allow users to upload multiple images
uploaded_files = st.file_uploader("Choose images...", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

# Button to submit the request
submit = st.button("Analyze Images")

# Process each uploaded image if submit button is clicked
if submit and uploaded_files:
    for idx, uploaded_file in enumerate(uploaded_files):
        try:
            # Load the image and display it
            image = PIL.Image.open(uploaded_file)
            st.image(image, caption=f"Uploaded Image {idx + 1}", use_column_width=True)

            # Get the Gemini AI response for each image
            response = get_gemini_response(api_key, prompt, image)
            st.subheader(f"Response for Image {idx + 1}:")
            st.write(response)
        except Exception as e:
            st.error(f"An error occurred with Image {idx + 1}: {e}")
