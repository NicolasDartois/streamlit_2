import streamlit as st

def css_and_credit():
    for i in range(25):
        st.sidebar.markdown("<br>", unsafe_allow_html=True)
    st.sidebar.subheader("🎥oct23_cda_exploitation-cinématographique🎥")
    st.sidebar.markdown("_____________________")
    st.sidebar.markdown("Manon FOUQUET")
    st.sidebar.markdown("Sylvain BRAIZET")
    st.sidebar.markdown("Nicolas DARTOIS")
    
    background_image = '''
        <style>
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
        }
        .fit-img {
            width: 100%;
            height: 100%;
            object-fit: cover; /* Peut aussi être 'contain' selon le besoin */
            display: block;
        }
        </style>
        '''
    st.markdown(background_image, unsafe_allow_html=True)
