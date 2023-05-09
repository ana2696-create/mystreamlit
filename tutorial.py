import streamlit as st
st.title('Onlei Technologies')
st.set_page_config(page_title='My Streamlit',page_icon='random')
st.image(https://onleitechnologies.com/wp-content/uploads/2021/12/Untitled_design__6_-removebg-preview-1-150x84.png'')
st.header('By Anamika Yadav')
mymenu=st.sidebar.selectbox('MY MENU',('Home','Fill Form','Downloads'))
if (mymenu=='HOME'):
    st.markdown('<center><h1>WELCOME TO ONLEI TECHNOLOGIES </h1></center>')
    st.video("https://www.youtube.com/watch?v=q1jM0kIFL78")

elif (mymenu=='Fill FORM'):
    with st.form("MY FORM"):
        name=st.text_input("Enter Name")
        dob=st.date_input("Select Date Of Birth")
        marks=st.slider("Choose marks")
        k=st.form_submit_button("Submit Form")
        if k:
            st.write("Name:",name," DOB:",dob," Marks:",marks)


elif (mymenu=="Downloads"):
    st.header("Downloads")
    st.download_button("Download Now","Hello! Friends, this is anamika who is creating this file from onlei technologies.","onlei.txt")
    
