import streamlit as st
st.subheader("Hi,Iam Translator :wave:")
st.title("LANGUAGE TRANSLATION")
st.write("welcome to applications for indian languages")
st.write("[Learn More>](https://translate.google.com)")
with st.container():
	st.write("---")
	left_column,right_column=st.columns(2)
	with left_column:
		st.header("What I Do")
		st.write("##")
		st.write(
                   """
	In our website we are providing language translation for people who:
		-are looking for  language translation.
		-Iam here to help you out with this language translation.
		-I will translate your text to text which you can understand easily.
		"""
		)
		st.write("[Reference >](https://ai4bharat.iitm.ac.in)")
import streamlit as st
from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate
from googletrans import Translator

# Create a Streamlit app title
st.title("Text-to-Text Language Translation")

# Create a text input widget
input_text = st.text_area("Enter the text you want to translate:", "")

# Create a language selection widget
# Add Indian languages to the language selection
from_lang = st.selectbox("Select the source language:", ["auto", "en", "es", "fr", "de", "ja", "zh", "hi", "kn", "ta", "te"])
to_lang = st.selectbox("Select the target language:", ["en", "es", "fr", "de", "ja", "zh", "hi", "kn", "ta", "te"])
# Create a translate button
if st.button("Translate"):
    # Initialize the translator
    translator = Translator()
    
    # Translate the input text
    if from_lang in ["hi", "kn", "ta", "te"] and to_lang in ["hi", "kn", "ta", "te"]:
        # Use the Indic language model for transliteration
        transliterated_text = transliterate(input_text, sanscript.ITRANS, to_lang)
        st.write(f"Transliterated text ({to_lang}): {transliterated_text}")
    else:
        # Use Google Translate for other language pairs
        translated_text = translator.translate(input_text, src=from_lang, dest=to_lang)
        st.write(f"Translated text ({to_lang}): {translated_text.text}")

# Create a function for each page or section
def home_page():
    st.title("Home")
    st.write("Welcome to the Home page!")

def about_page():
    st.title("About")
    st.write("This is the About page. Learn more about us here.")

def services_page():
    st.title("Services")
    st.write("Explore our services and what we offer.")

def contact_page():
    st.title("Contact")
    st.write("Contact us for more information.")

# Create a dictionary to map navigation labels to the corresponding pages
page_dict = {
    "Home": home_page,
    "About": about_page,
    "Services": services_page,
    "Contact": contact_page
}

# Create a Streamlit abovebar for navigation
st.sidebar.title("Navigation")
selected_page = st.sidebar.radio("Go to:", list(page_dict.keys()))


# Create a custom container for the top navigation bar
st.write("""
    <style>
        .topnav {
            background-color: #333;
            overflow: hidden;
        }
        .topnav a {
            float: left;
            display: block;
            color: white;
            text-align: center;
            padding: 14px 16px;
            text-decoration: none;
        }
    </style>
    <div class="topnav">
        <a href="#home">Home</a>
        <a href="#about">About</a>
        <a href="#services">Services</a>
        <a href="#contact">Contact</a>
    </div>
    """
, unsafe_allow_html=True)

# Rest of your Streamlit app code
st.title("Welcome to My Streamlit App")
st.write("This is the content of your Streamlit app.")




contact_form="""
<from action="https://formsubmit.co/MLTE.athinenirajitha8@gmail.com" method="POST">
<input type="hidden" name="_captcha"value="false">
<input type="text" name="name" placeholder="Your name" required>
<input type="email" name="email" placeholder="Your email" required>
<textarea name="message" placeholder="Your message here" required></textarea>
<button type="submit">Send</button>
</form>
"""
left_column,right_column=st.columns(2)
with left_column:
	st.markdown(contact_form,unsafe_allow_html=True)
with right_column:
	st.empty()
