import streamlit as st

def setup_page():
    with open("images/flight_takeoff_24dp_E3E3E3_FILL0_wght400_GRAD0_opsz24.svg", "r", encoding="utf-8") as f:
        svg = f.read()
    st.markdown(
        f"""
        <style>
            .logo svg {{
                width: 45px;
                height: auto;
                margin-left: -5px;
                transform: translateY(-30px);
            }}
            .title-wrap {{
                display: flex;
                justify-content: center;
                align-items: flex-start;
                gap: 0px;
            }}
            .title-wrap h1 {{
                line-height: 1;
                margin: 0;
                transform: translateY(-50px);
            }}
        </style>
        
        <div class="title-wrap">
            <h1>Serenair</h1>
            <div class="logo">
                {svg}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )