import streamlit as st               #[v 0.67.1]
import pandas as pd                  #[v 1.0.4]
import numpy as np                   #[v 1.18.5]

def main():

    st.sidebar.title('Navigator')
    page = st.sidebar.radio("""Go to""",
                            ["Homepage",
                             "Surgical Eponym Explorer ©",
                             "App Team"])

    if page   == "Homepage":                   show_homepage()
    elif page == "Surgical Eponym Explorer ©": show_explore()
    elif page == "App Team":                   show_the_app_team()


def show_homepage():
    ''' Home / About page '''
    st.markdown('''# Learning Surgical Eponyms App''')
    st.subheader('Welcome')
    st.sidebar.info("This App is maintained by Alastair Hayes, a Surgeon and Coder based in Edinburgh UK, supported by the App Team")
    st.sidebar.markdown('''**Contact details**''')
    st.sidebar.info("Please get in touch with any contributions or comments: surgicaleponyms@gmail.com")


def show_explore():
    st.sidebar.markdown("---")
    st.sidebar.title("**Explorer**")
    exp = st.sidebar.radio('Select',
                                ["About",
                                 "By Operation",
                                 "Type of Eponym",
                                 "Geographical",
                                 "Journal of Publication",
                                 "People",
                                 "Time Travel",
                                 "Exam Favourites",
                                 "A to Z",
                                 ])
    if   exp == "About":                    exp_about()             #1
    elif exp == "By Operation":             exp_operation()         #2
    elif exp == "Type of Eponym":           exp_type()              #3
    elif exp == "Geographical":             exp_geography()         #4         
    elif exp == "Journal of Publication":   exp_journals()          #5
    elif exp == "People":                   exp_people()            #6
    elif exp == "Time Travel":              exp_year()              #7
    elif exp == "Exam Favourites":          exp_exam()              #8
    elif exp == "A to Z":                   exp_A2Z()               #9


def show_the_app_team():
    st.title("Surgical App Development Team")
    st.markdown('''<br>We are group of General Surgeons based in Edinburgh developing app software to improve surgical **data systems**,
             **research** and **education**.''',unsafe_allow_html=True)

#-----------------------------------------------------------------------------------------------#

if __name__ == "__main__":
    main()
