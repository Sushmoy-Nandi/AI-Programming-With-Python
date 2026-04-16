import streamlit as st

st.title("Input your files (audio)",anchor=False)
st.divider()
# from directory
st.audio("audio/audio_file.mp3",loop=True)

st.divider()

audio_file = st.file_uploader("Enter your audio",
                         type=['mp3',"ogg",'flac']
                         
                         )

if audio_file:
    st.audio(audio_file)

