import streamlit as st
# Title of the webpage
st.title("This is title")
# Header
st.header("This is header")
# SubHeader
st.subheader("This is sub header")

# Text
st.text(" Hello ")

# Makrdown
st.markdown(" ### This is Makrdown ")

# Error / Colourful Text
st.success(" Successful ")

# Information
st.info("[INFO] This is an important info ")

# Warning
st.warning("Warning -- model failed")

# Error
st.error("This is an error")

# Exception
st.exception(" ZeroDivisionError()")

# get help
st.help(range)

# Writing text / Functions
 
st.write(" Boom ")

st.write(range(0,10))

# show image
from PIL import Image
img = Image.open(r"unnamed.jpg")
st.image(img, width = 300, caption = 'Car')

# # show video
# vid = open("video.mp4", "rb").read()
# st.video(vid)

# # load audio
# aud = open("song.mp3","rb").open()
# st.audio(aud, format = 'audio/mp3')

# widget / checkbox

if st.checkbox("Show/Hide"):
    st.text("showing or Hiding")

# Radio Button
status = st.radio(" What is your status ", ("Active","Inactive"))

if status == "Active":
    st.success("Yay")
else:
    st.error("Nay")
    
# Select box
gender = st.selectbox("What is your sex?",["M","F"])
st.write("You are %s" %gender)

# Multi Select
relationship = st.multiselect("What is your relationship status", ('Single','Married','Divorced','Widowed'))
st.write(" Your relationship status is (are)", relationship)

# Slider
rating = st.slider("How much do you rate this code", 0, 10)
st.write(" You rated %d" %rating)

# Button
st.button(" Do not Press")
if st.button("Do not Press, please"):
    st.write("KABoom")
    
# text input
firstName = st.text_input("Enter First Name","Type Here....")

if st.button("Sumbit"):
    st.success("Bonjour %s"%firstName)