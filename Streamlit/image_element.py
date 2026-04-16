import streamlit as st

st.title("Input your files",anchor=False)
st.divider()

# storage
st.image("images\OIP.jpg")

#url
st.image("https://tse4.mm.bing.net/th/id/OIP.KOOipupW_5_J2Yv5CgFH6wHaEK?rs=1&pid=ImgDetMain&o=7&rm=3")


st.divider()

images = st.file_uploader("Enter your image (at max 2)",
                         type=['jpg',"jpeg",'png'],
                         accept_multiple_files=True
                         )

print(type(images))

if images:
    if(len(images)>2):
       st.warning("You uploaded 3 photos ") 
    col = st.columns(len(images))

    for i, per_image in enumerate(images):
        with col[i]:
            st.image(per_image)



