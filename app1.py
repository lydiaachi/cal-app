import streamlit as st



st.title("welcom to my first app")

st.subheader("This app is doing absolutly well")

col1, col2 = st.columns(2)

with col1:
    st.number_input("How old are you",step = 1)
    st.selectbox("Title",["Mr","Mrs", "Miss"])
    st.text_input("Name")

with col2:
    st.text_area("address")
    st.selectbox("Gender",["Male","Female","others"])
    st.text_area("what do you love")
    st.sidebar.radio("Music Type", ["Afro", "hip_pop"])
    st.balloons()
    st.button("calculate")
    st.spinner("In Progress")