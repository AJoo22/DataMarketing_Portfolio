import streamlit as st

# Set up the title of the app
st.title('Simple Streamlit App')

# Text input for user name
user_name = st.text_input('Enter your name:', '')

# Button to greet the user
if st.button('Greet'):
    # Display a greeting message when the button is clicked
    st.write(f'Hello {user_name}, welcome to our Streamlit app!')

# Run this with `streamlit run your_script_name.py`
