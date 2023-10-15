import streamlit as st
# Set the theme
st.set_page_config(page_title="My Streamlit App", page_icon=":rocket:", layout="wide")
# Define the navigation links as dictionary
nav_links = {
    "Home": "Home",
    "About": "About",
    "Services": "Services",
    "Contact": "Contact",
}

# Create a Streamlit sidebar to display the navigation links
st.sidebar.title("Navigation")

# Create a radio button to select the page
selected_page = st.sidebar.radio("Go to", list(nav_links.keys()))



# Define content for each page
pages = {
    "Home": "Welcome to the Home Page!",
    "About": "Learn more about us on the About Page.",
    "Services": "Explore our services on the Services Page.",
    "Contact": "Contact us on the Contact Page.",
}
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



contact_form="""
<from action="https://formsubmit.co/MLTE.samalasania@gmail.com" method="POST">
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

