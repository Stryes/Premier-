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
st.write("Traduis"+input)
for i in range (len(list_possibilities)):
    st.button(list_possibilities[i])


import streamlit as st 
import pandas as pd 
voc=pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vTaUESVFbUnxC9q5-d-BiQXk6JD4r--bTZ3lNcryvfCeKqJq-tnz3VLhPwS_bZ5WXsRGYkOrtgkLlTU/pub?output=csv")
st.dataframe(voc)
l=voc.shape(voc)
i=hp.random.choice(range(l))
world_fr=voc["Definition"].values[i]
world_chi=voc["Pinyin"].values[i]
st.write(word_fr+""+word_chi)
