#Copyright [2020] [EXCISION LIMITED]
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


#----------------------------------------------------------------------------------------------#
#                                                                                              #
#  Main                                                                                        #
# ::: Handles the navigation / routing and data loading / caching                              #                                                                                              #
#                                                                                              #
#----------------------------------------------------------------------------------------------#

def main():
#   st.sidebar.markdown('''[Advert space for Google AdSense]''')
    st.write(
        """
        <style type="text/css" media="screen">
        div[role="listbox"] ul {
            height:200px;
        }
        </style>
        """
        ,unsafe_allow_html=True,)
    
    st.sidebar.title('Navigator')
    page = st.sidebar.radio("""Go to""",
                            ["Homepage",
                             "Surgical Eponym Explorer",
                             "App Design Team"])

    if page   == "Homepage":                   show_homepage()
    elif page == "Surgical Eponym Explorer":   show_explore()
    elif page == "App Design Team":            show_the_app_team()


#----------------------------------------------------------------------------------------------#
#                                                                                              #
#  Homepage                                                                                    #
# ::: Handles                                                                                  #                                                                                              #
#                                                                                              #
#----------------------------------------------------------------------------------------------#

def show_homepage():
    ''' Home / About page '''
    st.write('''# UNDER CONSTRUCTION''')
    st.markdown('''# SurgicalEps''')
    st.markdown('''_An Educational Web App designed by **Excision**_''')
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
    st.sidebar.info("This App is maintained by Alastair Hayes, a Surgeon and Programer, supported by the wider Excision team")
    st.sidebar.markdown('''**Contact details**''')
    st.sidebar.info("Please get in touch with any contributions or comments: surgicaleponyms@gmail.com")

#----------------------------------------------------------------------------------------------#
#                                                                                              #
#  About the team                                                                              #
# :::                                                                                          #                                                                                              #
#                                                                                              #
#----------------------------------------------------------------------------------------------#

def show_the_app_team():
    st.title("App Design Team")
    st.markdown('''The team consists of a group of General Surgeons based in Edinburgh who are motivated to develop software to improve surgical **data systems**,
             **research** and **education**.''')
    st.markdown('''To meet these aims, a company called **Excision** was founded in 2020, and **SurgicalEps** Web App was one of the initial projects.''',unsafe_allow_html=True)

    st.sidebar.markdown("---")
    st.sidebar.markdown('''**Contact details**''')
    st.sidebar.info("Get in touch with any comments, queries or suggestions about this App: surgicaleponyms@gmail.com")
    
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
#  About (1)                                                                                   #
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
    df1 = pd.read_csv(url, dtype={'PMID':str,'Year':int,})
    df2 = df1.sort_values(by=['Year'],ascending=True)
    df3 = df2.sort_values(by=['Operation'],ascending=True)  #Gives eponyms by operation alphabetically
    df4 = df3['Operation'].dropna()
    string = df4.str.cat(sep=',')
    splits = string.split(",")
    S = set(splits)
    T = np.array(list(S)).astype(object)
    U = np.sort(T)
#   st.markdown('''[Advert space for Google AdSense1]''')
    st.subheader('''First, choose operations of interest:''')
    eponymByOp = st.multiselect('',options=list(U), format_func=lambda x: ' ' if x == '1' else x)
    new_df = df1.loc[df1['Operation'].str.contains('|'.join(eponymByOp)) == True]
    new_df2 = new_df.sort_values(by=['Eponym'],ascending=True)
 
    if not eponymByOp == None:
        st.subheader('''Then, search list of related eponyms:''')
        Op_options = st.selectbox('',
                                  new_df2['Eponym_easy'].unique(), format_func=lambda x: ' ' if x == '1' else x)   #selectbox

        df_ep_info2 = new_df[new_df['Eponym_easy'].str.match(Op_options)]
        ep_yr = df_ep_info2['Year'].to_string(index=False)

        if not df_ep_info2['Who'].isnull().all():
            st.write('_Who_:',df_ep_info2['Who'].to_string(index=False))

        if not df_ep_info2['Year_str'].isnull().all():
            st.write('_When_:',df_ep_info2['Year_str'].to_string(index=False))

        if not df_ep_info2['Where'].isnull().all():
            st.write('_Where_:', df_ep_info2['Where'].to_string(index=False))
    
        description = df_ep_info2['Description'].to_string(index=False)
        history = df_ep_info2['History'].to_string(index=False)

        if not df_ep_info2['Description'].isnull().all():
            st.markdown(description, unsafe_allow_html=True)
        if not df_ep_info2['History'].isnull().all():
            st.write('**_History_**:', history)
            st.markdown("---")

        if not df_ep_info2['Who'].isnull().all():
            st.write('**External links**')
        ref_link = df_ep_info2['Pubmed'].to_string(index=False)
        if not df_ep_info2['Pubmed'].isnull().all():
           st.markdown(f"[PubMed.gov]({ref_link})")

        wiki_link = df_ep_info2['Wiki_link'].to_string(index=False)
        if not df_ep_info2['Wiki_link'].isnull().all():
            st.markdown(f"[wikipedia.org]({wiki_link})")

        wni_link = df_ep_info2['WNI_link'].to_string(index=False)
        if not df_ep_info2['WNI_link'].isnull().all():
           st.markdown(f"[whonamedit.com]({wni_link})")

        icd_link = df_ep_info2['ICD11_link'].to_string(index=False)
        if not df_ep_info2['ICD11_link'].isnull().all():
           st.markdown(f"[Internatinal Classification of Diseases 11th Revision]({icd_link})")


#----------------------------------------------------------------------------------------------#
#                                                                                              #
#  Types (eg. Incisions, Instruments) (3)                                                      #
# ::: Handles the                                                                              #                                                                                              #
#                                                                                              #
#----------------------------------------------------------------------------------------------#

def exp_type():
    #st.markdown('''[Advert space for Google AdSense2]''')
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


#1
def show_anatomical():
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

    url = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/Eponyms4python_Lite.csv'
    df = pd.read_csv(url, dtype={'PMID':str,'Year':int})
    df1 = df.rename(columns={"Eponym": "Eponym_OLD", "Eponym_easy": "Eponym"})
    Anat_df = df1[(df1['Type'].str.match('Structures'))]
    if not Anat_df['Type'].isnull().all():
        Table = ff.create_table(Anat_df.drop(['Alphabet','CityOfEponym_A1','ISO_country_A1','Author_1_Role','WhoNamedIt',
                    'Author_1', 'Author_2','Pubmed_results','Google_results','Operation','GxP','Log2_GxP','Societies',
                    'ICD11','WNI_link', 'Reference', 'Wiki_link','PMID','Type','Journal','History','ICD11_link','Year',
                    'CountryOfEponym_A1','Class','Subclass','Description','Sex_A1','Lat_A1','Long_A1'],
                             axis=1).sort_values(by=['Eponym_OLD'],
                                                 ascending=True).reindex(columns=['Eponym']).reset_index(drop=True))

    worldMap = st.checkbox('''Show anatomical eponyms on world map''', value=False)
    if worldMap:
        Year = st.slider('Time traveler function - Year:', 1560, 2020, value=2020)
#       mapbox_access_token = open('https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/ajhayes83_1mapbox_token.txt').read()  
        mapbox_access_token = 'pk.eyJ1IjoiYWpoYXllczgzIiwiYSI6ImNrY2pqM2lvMDB4Z24ydG8zdDl0NTYwbTUifQ.2DKVfTAaE77XAXMpDeq_Pg'
        dfT = Anat_df.sort_values(by=['Year'],ascending=True)
        time_df = Anat_df.loc[Anat_df['Year'] <= Year]
        site_lat = time_df['Lat_A1']                           
        site_lon = time_df['Long_A1']           
        text = time_df['Eponym'] + ', ' + time_df['CityOfEponym_A1'] + ', ' + time_df['Year'].astype(str)
        locations_name = time_df['Eponym']
        fig = go.Figure()
        fig.add_trace(go.Scattermapbox(
                lat=site_lat,lon=site_lon,
                mode='markers',
                marker=go.scattermapbox.Marker(
                    color='yellow',
                    opacity=0.7,
                    size=12,
                ),
                text=text,
            hoverinfo='text'
            ))
        fig.update_layout(
            autosize=True,
            hovermode='closest',
            showlegend=False,
            width=1100,
            height=570,
            mapbox=dict(
                accesstoken=mapbox_access_token,
                bearing=0,
                center=dict(lat=25,lon=8),
                pitch=0,
                zoom=1.08,
                style='dark'),
            )
        fig.update_layout(margin=dict(l=2, r=2, t=0, b=0))
        st.write(fig) 
    st.subheader('''Then, search list of named anatomical structures:''')
    Anat_options2 = st.selectbox('', Anat_df['Eponym'].unique(), format_func=lambda x: ' ' if x == '1' else x)
    Anat_options2_info = Anat_df[Anat_df['Eponym'].str.match(Anat_options2)]



#2
def show_scores():
    st.markdown(
        """
        <style type="text/css" media="screen">
        div[role="listbox"] ul {height:430px}
        </style>
        """
        ,
        unsafe_allow_html=True,
    )

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

    url = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/Eponyms4python_Lite.csv'
    df = pd.read_csv(url, dtype={'PMID':str,'Year':int})
    Scores_df = df[(df['Type'].str.match('Scores'))]
    if not Scores_df['Type'].isnull().all():
        Table = ff.create_table(Scores_df.drop(['Alphabet','CityOfEponym_A1','ISO_country_A1','Author_1_Role','WhoNamedIt',
                    'Author_1', 'Author_2','Pubmed_results', 'Google_results','Operation','GxP', 'Log2_GxP','Societies',
                    'ICD11','WNI_link', 'Reference', 'Wiki_link','PMID', 'Type','Journal','History','ICD11_link','Year',
                    'CountryOfEponym_A1','Class','Subclass','Description','Sex_A1','Lat_A1','Long_A1'],
                             axis=1).sort_values(by=['Eponym'],
                                                 ascending=True).reindex(columns=['Eponym']).reset_index(drop=True))




#-------------------------------------------------------------------------------------------#
if __name__ == "__main__":
    main()
