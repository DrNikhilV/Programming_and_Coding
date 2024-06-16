import streamlit as st
import random

# Define the questions
questions = [
    {
        "Course": "Principles of Chemical Science",
        "Topic": "The photoelectric effect",
        "Original question": "A beam of light with an intensity of 15 W is incident on a copper plate (Φ = 7.43 x 10^-19 J). Electrons with a minimum wavelength of 3.75 x 10^-10 m are ejected from the surface of the copper. Calculate the frequency of the incident light.",
        "Solution": "7.43 * 10^-19 J"
    },
    {
        "Course": "Principles of Chemical Science",
        "Topic": "The photoelectric effect",
        "Original question": "A beam of light with an intensity of 15 W is incident on a copper plate (Φ = 7.43 x 10^-19 J). Electrons with a minimum wavelength of 3.75 x 10^-10 m are ejected from the surface of the copper. Calculate the maximum number of electrons that can be ejected by a 3.0-second pulse of the incident light.",
        "Solution": "1.8 * 10^19 electrons"
    },
    # Add more questions as needed
]

# Initialize session state variables
if 'current_question_index' not in st.session_state:
    st.session_state.current_question_index = 0
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'player_name' not in st.session_state:
    st.session_state.player_name = ""
if 'user_answer' not in st.session_state:
    st.session_state.user_answer = ""
if 'questions' not in st.session_state:
    st.session_state.questions = random.sample(questions, len(questions))

# Function to display a question
def show_question():
    if st.session_state.current_question_index < len(st.session_state.questions):
        current_question = st.session_state.questions[st.session_state.current_question_index]
        st.write(f"# {current_question['Course']}")
        st.write(f"## {current_question['Topic']}")
        st.write(current_question["Original question"])
        user_answer = st.text_input("Your Answer:", key=f'answer_{st.session_state.current_question_index}')
        submit_button = st.button("Submit Answer", key=f'submit_{st.session_state.current_question_index}')
        if submit_button:
            check_answer(user_answer)
    else:
        end_game()

# Function to check the answer
def check_answer(user_answer):
    current_question = st.session_state.questions[st.session_state.current_question_index]
    if user_answer.lower() == current_question["Solution"].lower():
        st.session_state.score += 1
        st.success("Correct! +1 point")
    else:
        st.session_state.score -= 0.25
        st.error("Incorrect! -0.25 points")
    st.session_state.current_question_index += 1
    show_question()

# Function to end the game
def end_game():
    st.write(f"# Game Over, {st.session_state.player_name}!")
    st.write(f"Your final score: {st.session_state.score:.2f}")
    st.write("Thanks for playing!")

# Streamlit UI
st.title("Quiz Game")
if st.session_state.player_name == "":
    st.session_state.player_name = st.text_input("Enter your name:")
    start_button = st.button("Start Game")
    if start_button and st.session_state.player_name:
        show_question()
    elif start_button and not st.session_state.player_name:
        st.warning("Please enter your name!")
else:
    show_question()
