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
st.set_page_config(page_title="Chilli AI Analysis")

st.header("Chilli AI Function Demo")

# Set the API key directly
api_key = "AIzaSyCDArjAnWftMGMiQXwVPwfQWDWN09EKMZE"

# Primary ComboBox to select analysis type
analysis_type = st.selectbox("Select Analysis Type:", ["Color Detection", "Plant Health"])

# Set prompt based on ComboBox selections
prompt = ""
show_color_options = analysis_type == "Color Detection"

if show_color_options:
    # Secondary ComboBox for color-specific options if "Color Detection" is selected
    color_option = st.selectbox("Select Chilli Color:", ["Red Chilli", "Green Chilli"])

    if color_option == "Red Chilli":
        prompt = (
            "How many red chilli can be observed and other color type of chilli. "
            "Get the total of red chilli and the total other of color of chilli can be observed from the image. "
            "Determine and write how many percent red chilli. Then write:  If it's more than (75%) write, "
            "\"Plants is Harvestable\". Else, \"Plant is Not Harvestable yet\". "
            "The Writting response from you should be ONLY like this and REMEMBER if <75%, PLANT IS NOT HARVESTABLE: 25%. Plant is not harvestable yet. "
            "If there's NO CHILLI observed, then just say 0%. Make sure it's concise!"
        )
    elif color_option == "Green Chilli":
        prompt = (
            "How many green chilli can be observed and other color type of chilli. "
            "Get the total of green chilli and the total other of color of chilli can be observed from the image. "
            "Determine and write how many percent green chilli. Then write:  If it's more than (75%) write, "
            "\"Plants is Harvestable\". Else, \"Plant is Not Harvestable yet\". "
            "The Writting response from you should be ONLY like this and REMEMBER if <75%, PLANT IS NOT HARVESTABLE: 25%. Plant is not harvestable yet."
            "If there's NO CHILLI observed, then just say 0%. Make sure it's concise!"
        )

else:
    # Prompt for "Plant Health" selection
    prompt = (
        "Determine the chilli and other factors of the chilli plant here, "
        "is the chilli plant here in good shape or in good health? "
        "If not, recommend me next steps in order to take care of this plant"
    )

# File uploader to allow users to upload multiple images
uploaded_files = st.file_uploader("Choose images...", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

# Place the buttons in a row


# Add the "Analyze Images" button in the first column

    st.button("Analyze Images")

# Add the redirect button in the second column

    st.markdown(
        """
        <a href="http://localhost/website/gemini2/retrievealldata.php" target="_blank" style="
            display: inline-block; 
            padding: 10px 10px; 
            background-color: #4CAF50; 
            color: white; 
            text-align: center; 
            text-decoration: none; 
            border-radius: 4px; 
            font-size: 13px; 
            font-weight: bold;">
            Go to Retrieve All Data!
        </a>
        """, unsafe_allow_html=True
    )




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
