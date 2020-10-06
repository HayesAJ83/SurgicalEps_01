#Copyright [2020] [Alastair Hayes]
#
#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
#Unless required by applicable law or agreed to in writing, software
#distributed under the License is distributed on an "AS IS" BASIS,
#WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#See the License for the specific language governing permissions and
#limitations under the License.


import streamlit as st
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import plotly
import plotly.express as px          
import plotly.graph_objects as go    
import plotly.figure_factory as ff
import io
import requests
#px.set_mapbox_access_token(open("/Users/alastairhayes/desktop/Eponyms/ajhayes83_1.mapbox_token").read())

st.write(
        """
        <style type="text/css" media="screen">
        div[role="listbox"] ul {
            height:250px;
        }
        </style>
        """
        ,
        unsafe_allow_html=True,
    )


#----------------------------------------------------------------------------------------------#
#                                                                                              #
# Read in data                                                                                 #
#                                                                                              #
#----------------------------------------------------------------------------------------------#

#Data read and arrange
#E4P = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/Eponyms4python_Lite.csv?raw=true'
#df1 = pd.read_csv(E4P, index_col=0)
url = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/Eponyms4python_Lite.csv'
df1 = pd.read_csv(url, index_col=0)
df2 = df1.sort_values(by=['Year'],ascending=True)

#----------------------------------------------------------------------------------------------#
#                                                                                              #
#  Main                                                                                        #
# ::: Handles the navigation / routing and data loading / caching                              #                                                                                              #
#                                                                                              #
#----------------------------------------------------------------------------------------------#

def main():

#    st.sidebar.markdown('''**Advertisement**''')
#    st.sidebar.markdown('''[Advert space for Google AdSense]''')
#    st.sidebar.markdown("---")
    st.sidebar.title('Navigator')
    page = st.sidebar.radio("""Go to""",
                            ["Homepage",
                             "Surgical Eponym Explorer",
                             "Excision - App Team"])

    if page   == "Homepage":                   show_homepage()
    elif page == "Surgical Eponym Explorer":   show_explore()
    elif page == "Excision - App Team":        show_the_app_team()



#----------------------------------------------------------------------------------------------#
#                                                                                              #
#  Homepage                                                                                    #
# ::: Handles                                                                                  #                                                                                              #
#                                                                                              #
#----------------------------------------------------------------------------------------------#

def show_homepage():
    ''' Home / About page '''
    st.write('''WEB APP UNDER CONSTRUCTION''')
    st.markdown('''# SurgicalEps''')
    st.markdown('''_An Educational Web App made by Excision_''')
    st.subheader('Welcome')
    st.write('''There are a hundreds of eponyms used in daily surgical practice.
    We hope that you will find this app helpful in understanding what these terms mean, their history, and how they relate to one another using the **Eponym Explorer**.''')
    st.markdown('''We suggest starting with **Operations** of interest, or eponyms related to **Anatomy**.
    To explore their origins, check out the **Year** and **Geography** options. See **Journals** for eponyms that can be traced back to a famous publication.
    To gauge eponym usage see **Google hits**, and choose **Surgical instruments** to find eponymously named equipment.''')
    st.markdown('''We include **direct links to primary papers**, as well as useful webpages in **Wikipedia**, **Whonamedit?**, **ICD-11** and **TeachMeSurgery**. To simply search **A to Z** use the search box (below).''')
    st.markdown("---")
    st.subheader('Who is this App for?')
    st.write('''Doctors, nurses, secretaries, theatre staff, physician assistants, allied health professionals and students''')
    st.markdown("---")
    st.subheader('Disclaimer')
    st.write('''Educational purposes''')
    st.sidebar.markdown("---")
    st.sidebar.markdown('''**Latest News**''')
    st.sidebar.info("App will be launched Dec 2020")
    st.sidebar.markdown('''**About**''')
    st.sidebar.info("This App is maintained by Alastair Hayes, a Surgeon and Coder based in Edinburgh UK, supported by the App Team")
    st.sidebar.markdown('''**Contact details**''')
    st.sidebar.info("Please get in touch with any contributions or comments: surgicaleponyms@gmail.com")

#----------------------------------------------------------------------------------------------#
#                                                                                              #
#  About the team                                                                              #
# :::                                                                                          #                                                                                              #
#                                                                                              #
#----------------------------------------------------------------------------------------------#

def show_the_app_team():
    st.title("Excision - A Surgical App Development Team")
    st.markdown('''<br>We are group of General Surgeons based in Edinburgh developing app software to improve surgical **data systems**,
             **research** and **education**.''',unsafe_allow_html=True)

    st.sidebar.markdown("---")
    st.sidebar.markdown('''**Contact details**''')
    st.sidebar.info("Get in touch with any comments, queries or suggestions: surgicaleponyms@gmail.com")
    
    st.subheader("Project Lead & App Developer")
    about1 = st.checkbox("Alastair Hayes")
    if about1:
        st.markdown('''Alastair is a Specialty Training Registrar in Edinburgh with interests in Upper GI, Endocrine and Emergency General Surgery.
    His qualifications consist of BSc(Hons), MBChB, MRCS(Ed), MSc, PhD.
    He is working to develop data science and software solutions for clinical data systems, research and education in surgical practice.''')

    st.subheader("Associate Project Lead")
    about2 = st.checkbox('''Anne Ewing''')
    if about2:
        st.markdown('''Anne is a Specialty Training Registrar in Edinburgh with interests in Upper GI, Hernias and Emergency General Surgery.
    She is passionate about surgical teaching and outside work Anne is a competitive triathlete.''')
    

    st.subheader("Acknowledgements")
    st.markdown('''[Google](https://www.google.com/search/howsearchworks/?fg=1),
    [Mapbox](https://www.mapbox.com),
    [Pandas](https://pandas.pydata.org), [Plotly](https://plotly.com/python/), [PubMed&reg;](http://www.ncbi.nlm.nih.gov/pubmed),
    [Streamlit](https://www.streamlit.io)''')
    st.sidebar.markdown("---")


#----------------------------------------------------------------------------------------------#
#                                                                                              #
#  Explorer                                                                                    #
# ::: Handles the navigation                                                                   #                                                                                              #
#                                                                                              #
#----------------------------------------------------------------------------------------------#

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



#----------------------------------------------------------------------------------------------#
#                                                                                              #
#  About (1)                                                                     #
# ::: Handles                                                                                  #                                                                                              #
#                                                                                              #
#----------------------------------------------------------------------------------------------#

def exp_about():

    st.markdown(
        """
        <style type="text/css" media="screen">
        .hovertext text {
        font-size: 20px !important;}
        </style>
        """
        ,
        unsafe_allow_html=True,
    )

    #Sidebar
    st.sidebar.markdown("---")

    #Page

    st.markdown('''# About - Surgical Eponym Explorer''')
    st.markdown("""<br>Use the **Explorer** select options in the sidebar to explore eponyms related to surgery.""",
        unsafe_allow_html=True)
    st.markdown('''<br><span style="font-size:14pt;font-weight:bold;color:black;text-decoration:underline;">By Operation</span>''', unsafe_allow_html=True)
    st.write('''Here you can choose an operation type, and then access all the common eponyms related to that procedure.''')
    st.markdown('''<br><span style="font-size:14pt;font-weight:bold;color:black;text-decoration:underline;">Type of Eponym</span>''', unsafe_allow_html=True)
    st.write('''Choose from anatomical structures, clinical scores or signs, operations,
                pathology, patient positioning, research trials, incisions, instruments,
                surgical maneouvers & techniques.''')
    st.markdown('''<br><span style="font-size:14pt;font-weight:bold;color:black;text-decoration:underline;">Geographical</span>''', unsafe_allow_html=True)
    st.write('''Choose a region of the world to find eponyms. Select a country or famous city.''')
    st.markdown('''<br><span style="font-size:14pt;font-weight:bold;color:black;text-decoration:underline;">Journal of Publication</span>''', unsafe_allow_html=True)

    st.write('''In this section, journals can be selected to find which eponyms can be traced to their archives.''')
    st.markdown('''<br><span style="font-size:14pt;font-weight:bold;color:black;text-decoration:underline;">People</span>''', unsafe_allow_html=True)

    st.write('''Some famous people have been attributed to many eponyms.''')
    st.markdown('''<br><span style="font-size:14pt;font-weight:bold;color:black;text-decoration:underline;">Time Travel</span>''', unsafe_allow_html=True)

    st.write('''Explore through time using the time travel function.''')
    st.markdown('''<br><span style="font-size:14pt;font-weight:bold;color:black;text-decoration:underline;">Exam Favourites</span>''', unsafe_allow_html=True)
    st.write('''Select from those often found in exams. Explore by speciality.''')
    st.markdown('''<br><span style="font-size:14pt;font-weight:bold;color:black;text-decoration:underline;">A to Z</span>''', unsafe_allow_html=True)
    st.write('''Explore the eponym library alphabetically.''')
 


#----------------------------------------------------------------------------------------------#
#                                                                                              #
#  Surgical Operations (2)                                                                     #
# ::: Handles                                                                                  #                                                                                              #
#                                                                                              #
#----------------------------------------------------------------------------------------------#

def exp_operation():
    st.markdown(
        """
        <style type="text/css" media="screen">
        .hovertext text {
        font-size: 20px !important;}
        </style>
        """
        ,
        unsafe_allow_html=True,)
    
    #Sidebar
    st.sidebar.markdown("---")

    #Page

    url = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/Eponyms4python_Lite.csv'
    df1 = pd.read_csv(url, index_col=0)
#   df1 = pd.read_csv('/Users/alastairhayes/desktop/Eponyms/Eponyms4python_Lite.csv',dtype={'PMID':str,'Year':int})
    df2 = df1.sort_values(by=['Year'],ascending=True)
    df3 = df2.sort_values(by=['Operation'],ascending=True)  #Gives eponyms by operation alphabetically
    df4 = df3['Operation'].dropna()
    string = df4.str.cat(sep=',')
    splits = string.split(",")
    S = set(splits)
    T = np.array(list(S)).astype(object)
    U = np.sort(T)

#   st.markdown('''[Advert space for Google AdSense1]''')
    st.subheader('''First, choose operation(s) of interest:''')
    eponymByOp = st.multiselect('',options=list(U), format_func=lambda x: ' ' if x == '1' else x)
    new_df = df1.loc[df1['Operation'].str.contains('|'.join(eponymByOp)) == True]
    new_df2 = new_df.sort_values(by=['Eponym'],ascending=True)
 
    if not eponymByOp == None:
        st.subheader('''Then, search this list of relevant eponyms:''')
        Op_options = st.selectbox('',
                                  new_df2['Eponym_easy'].unique(), format_func=lambda x: ' ' if x == '1' else x)   #selectbox



#----------------------------------------------------------------------------------------------#
#                                                                                              #
#  Types (eg. Incisions, Instruments) (3)                                                      #
# ::: Handles the                                                                              #                                                                                              #
#                                                                                              #
#----------------------------------------------------------------------------------------------#

def exp_type():
    st.markdown('''[Advert space for Google AdSense2]''')
    st.subheader('''First, select type:''')
    st.sidebar.markdown("---")
    
    types = st.selectbox(""" """,
                            ["Anatomical structures",
                             "Clinical scores",
                             "Clinical signs",
                             "Operations",
                             "Pathology",
                             "Patient positioning",
                             "Research trials",
                             "Surgical incisions",
                             "Surgical instruments",
                             "Surgical maneuvers & techniques",
                             ], index=0)

    if types   == "Anatomical structures":              show_anatomical()       #1
    elif types == "Clinical scores":                    show_scores()           #2
    elif types == "Clinical signs":                     show_signs()            #3
    elif types == "Operations":                         show_opNames()          #4
    elif types == "Pathology":                          show_path()             #5
    elif types == "Patient positioning":                show_positions()        #6
    elif types == "Research trials":                    show_trials()           #7
    elif types == "Surgical incisions":                 show_cuts()             #8
    elif types == "Surgical instruments":               show_instruments()      #9
    elif types == "Surgical maneuvers & techniques":    show_maneuvers()        #10



#-------------------------------------------------------------------------------------------#
if __name__ == "__main__":
    main()
