import streamlit as st
st.set_page_config(page_title="Favorite Things")
st.title("Fav Things")
place=st.text_input("Favorite Place")
dish=st.text_input("Favorite Dish")
name=st.text_input("Favorite Book")
hobbies=st.multiselect("Select your hobbies:",["Reading","Playing","Watching","Dancing","Cooking","Gaming","Photography","Singing","Coding","Traveling","Listening to Music","Practicing Yoga"])
#Use session state to avoid reset
if "show" not in st.session_state:
    st.session_state.show=False
if st.button("Show My Selection"):
    st.session_state.show=True
if st.session_state.show:
    if not all([place,dish,name]):
        st.error("Please fill all the fields")
    else:
        col1,col2=st.columns(2)
        with col1:
            st.header("You have picked")
            st.write("Place:",place)
            st.write("Dish:",dish)
            st.write("Book:",name)
        with col2:
            st.header("Your hobbies")
            if hobbies:
                for h in hobbies:
                    st.write(h)
            else:
                st.write("No hobbies selected")

