import streamlit as st
from common import setup_page

setup_page()
with st.container(border=True):
    col1, col2 = st.columns(2)
    with col1:
        st.image("./images/placeholder.png")
    with col2:
        st.markdown("""
                    <div style="font-size:28px; font-weight:bold;">
                        Climb Phase Detection
                    </div> <br>
                    """, unsafe_allow_html=True)
        st.write("Detects whether the plane is:")
        st.markdown("""
                - Ascending
                - Neutral
                - Descending <br>
                """, unsafe_allow_html=True)
        if st.button("head over?"):
            st.switch_page("./pages/page2.py")
    