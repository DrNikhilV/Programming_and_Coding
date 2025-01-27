import streamlit as st
import g4f

# Set the page layout
st.set_page_config(page_title="VaathiAi", layout="wide")

# Custom CSS for styling the text input
st.markdown(
    """
    <style>
    /* Style the text input */
    .stTextInput {
        width: calc(100% - 80px); /* Adjusted width to accommodate button */
        padding: 10px;
        border: 1px solid #ccc;
        border-radius: 20px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        outline: none;
        transition: box-shadow 0.3s ease;
        resize: none; /* Prevent resizing */
        font-size: 16px; /* Adjust font size */
        margin-right: 10px; /* Space between input and button */
    }
    .stTextInput:focus {
        box-shadow: 0 0 8px rgba(0,123,255,0.6);
    }
    /* Style the send button */
    .sendButton {
        padding: 10px 20px;
        border-radius: 20px;
        background-color: #007bff; /* Blue color */
        color: #fff;
        border: none;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }
    .sendButton:hover {
        background-color: #0056b3; /* Darker shade of blue on hover */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar content
with st.sidebar:
    st.title("VaathiAI")
    if st.button("Explore VaathiAI", key="explore_button"):
        # Clear conversation history
        st.session_state.conversation = []

    st.markdown("*Today*")
    st.markdown("[New chat](#)")
    st.markdown("[Streamlit App With VaathiAI](#)")
    st.markdown("[Index Error in List](#)")
    
    st.markdown("*Previous 7 Days*")
    st.markdown("[Approximate Inference in Bayesian PR](#)")
    st.markdown("[Median Half Hypothesis Proof](#)")
    st.markdown("[Python Code: Find List Size](#)")
    st.markdown("[Focus Issues: Causes & Tasks](#)")
    st.markdown("[Student Distraction: Causes & Solutions](#)")
    st.markdown("[Corrected Operations for Points](#)")
    st.markdown("[Single Number Using HashMap](#)")
    
    st.markdown("---")
    st.button("Upgrade plan", key="upgrade_button")

# Main content
st.title("Chat with VaathiAI")

# Initialize conversation history if not present
if 'conversation' not in st.session_state:
    st.session_state.conversation = []

# Initialize temporary input if not present
if 'temp_input' not in st.session_state:
    st.session_state.temp_input = ""

# Create a text area for the user's question
question = st.text_area("Enter your question:", st.session_state.temp_input, key="chat_input", height=80, max_chars=500)

# Send button to submit the question
if st.button("Send", key="send_button"):
    if question:
        # Display the user's question
        st.session_state.conversation.append(('user', question))

        # Stream the response
        response = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": question}],
            stream=True,
        )

        response_text = ""
        for message in response:
            response_text += message

        st.session_state.conversation.append(('bot', response_text))

        # Clear the input box after processing (using JavaScript workaround)
        st.markdown("""
        <script>
        document.querySelector(".stTextInput").value = "";
        </script>
        """, unsafe_allow_html=True)

        # Update the temporary input state
        st.session_state.temp_input = ""

# Display conversation history
for role, text in reversed(st.session_state.conversation):
    if role == 'user':
        st.markdown(f"<div style='background-color: #000; color: #fff; padding: 10px; border-radius: 10px;'><strong>You:</strong> {text}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div style='background-color: #333; color: #fff; padding: 10px; border-radius: 10px;'><strong>VaathiAI:</strong> {text}</div>", unsafe_allow_html=True)