import streamlit as st

image_html = f'<img src="https://github.com/NicolasDartois/streamlit_2/blob/main/images/linkedin.png?raw=true" style="width:20px; vertical-align:middle;">'

def css_and_credit():
    #st.sidebar.image("images/img_sidebar.png", use_column_width=True)
    for i in range(2):
        st.sidebar.markdown("<br>", unsafe_allow_html=True)
    st.sidebar.subheader("🎥oct23_cda_exploitation-cinématographique🎥")
    st.sidebar.markdown("_____________________")
    st.sidebar.markdown(f"{image_html} [Manon FOUQUET](https://www.linkedin.com/in/manonfouquet/)", unsafe_allow_html=True)
    st.sidebar.markdown(f"{image_html} [Sylvain BRAIZET](https://www.linkedin.com/in/sylvain-braizet-ba03ab65/)", unsafe_allow_html=True)
    st.sidebar.markdown(f"{image_html} [Nicolas DARTOIS](https://www.linkedin.com/in/nicolas-dartois/)", unsafe_allow_html=True)
    
    
    background_image = '''
        <style>
    .tab-container {
        display: flex;
        flex-direction: column;
        width: 100%;
    }
    .tab-buttons {
        display: flex;
        justify-content: center;
    }
    .tab-buttons button {
        background-color: #f1f1f1;
        border: none;
        padding: 10px 20px;
        cursor: pointer;
        transition: 0.3s;
        font-size: 16px;
    }
    .tab-buttons button:hover {
        background-color: #ddd;
    }
    .tab-buttons button.active {
        background-color: #ccc;
    }
    .tab-content {
        display: none;
        padding: 20px;
        border-top: none;
    }
    .tab-content.active {
        display: block;
    }
    .centered-content {
        display: flex;
        justify-content: center;
        align-items: center;
        width: 60%;
        min-width: 800px;
        margin-left: auto;
        margin-right: auto;
    }
    .wrapper {
        display: grid;
        grid-template-columns: 1fr 1fr 1fr 1fr 1fr;
        gap: 20px;
    }
    .plotly-chart-container {
        width: 100%;
        height: auto;
    }
    h2 {
        text-align: center;
    }
    button[title="View fullscreen"] {
        visibility: hidden;
    }
    .hidden-checkbox {
        display: none;
    }
    .hiddenText {
        display: none;
    }
    .hidden-checkbox:checked + .hiddenText {
        display: block;
    }
    .stApp {
        background-color: white;
        background-image: url("https://github.com/NicolasDartois/streamlit_2/blob/main/images/background.jpg?raw=true");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-position: center;
    }
    .box {
        background-color: white;
        padding: 20px;
        margin-top: 20px;
        margin-bottom: 20px;
        box-shadow: 0 10px 12px rgba(0, 0, 0, 0.1);
        border-radius: 10px;
        text-align: justify;
        width: 100%;
        transition: height 0.3s ease;
    }
    .fit-img {
        width: 100%;
        height: 100%;
        object-fit: cover; /* Peut aussi être 'contain' selon le besoin */
        display: block;
    }
    .centered-content a {
        display: none;
    }
        </style>
        '''
    st.markdown(background_image, unsafe_allow_html=True)
