import streamlit as st
name=st.text_input("Your name")
st.write ("Hello"+name)


genre = st.radio(
    "What's your favorite movie genre",
    [":rainbow[Comedy]", "***Drama***", "Documentary :movie_camera:"],
    captions = ["Laugh out loud.", "HIHIIHIH AHHAHAH.", "Never stop learning."])

if genre == ':rainbow[Comedy]':
    st.write('You selected comedy.')
else:
    st.write("You didn\'t select comedy.")

input="lapin"
list_possibilities=["rabbit","raco","rhyme","rogue"]
correct_answer="rabbit"
traduis: lapin 
for i in range (len(list-possibilities)):
    st.button(list-possibilities[i])



