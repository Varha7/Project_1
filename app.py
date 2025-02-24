# app.py
import streamlit as st
import pandas as pd
import tempfile

# Simple function for chatbot logic (can be replaced with more complex logic)
def chatbot_response(user_input):
    user_input = user_input.lower()
    
    if "how are you" in user_input:
        return "I'm doing great, thanks for asking!"
    elif "name" in user_input:
        return "I'm a Streamlit chatbot, here to help you!"
    elif "hello" in user_input:
        return "Hello! How can I assist you today?"
    else:
        return "I'm sorry, I didn't understand that. Can you ask something else?"

# Streamlit App Title
st.title("Chatbot Widget in Streamlit")

# Initialize session state to hold messages
if 'messages' not in st.session_state:
    st.session_state['messages'] = []

# Function to display conversation history
def display_chat():
    for msg in st.session_state['messages']:
        st.write(f"**User:** {msg['user']}")
        st.write(f"**Chatbot:** {msg['bot']}")

# Text input field to type the user's message
user_input = st.text_input("You:", "")

# When the user types something, get the chatbot response and add to the history
if user_input:
    bot_response = chatbot_response(user_input)
    
    # Append user and bot messages to session state
    st.session_state['messages'].append({'user': user_input, 'bot': bot_response})
    
    # Display updated conversation history
    display_chat()

# A button to clear the chat history (optional)
if st.button("Clear Chat"):
    st.session_state['messages'] = []
    st.experimental_rerun()

file = st.file_uploader("Pick a csv file", type=["csv"])

if file is not None:
    # Read the Excel file into a pandas DataFrame
    df = pd.read_csv(file)
    
    # Display the dataframe
    st.dataframe(df)

with tempfile.NamedTemporaryFile(delete=False, mode='w', suffix='.txt') as temp_file:
        # Write the user's input to the temporary file
        temp_file.write('test')
        temp_file_path = temp_file.name  # Get the path to the temporary file

# Now offer the user the download button
with open(temp_file_path, "r") as file:
    file_content = file.read()

# Create the download button
st.download_button(
    label="Download Local Text File",  # Button label
    data=file_content,  # File content to be downloaded
    file_name="downloaded_file.txt",  # Name of the downloaded file
    mime="text/plain"  # MIME type for a text file
)

#py -m streamlit run  "D:\Python\Project_Creta\app.py" --server.address 192.168.29.150 --server.port 8502
