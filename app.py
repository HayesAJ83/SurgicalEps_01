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
    st.sidebar.title('Navigator')
    page = st.sidebar.selectbox('',#'Go to',
                            ["Surgical Eponym Explorer",
                             "App Design Team"])

    if page == "Surgical Eponym Explorer":   show_explore()
    elif page == "App Design Team":          show_the_app_team()


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
   # st.sidebar.title("**Explorer**")
    exp = st.sidebar.radio('',#'Select',
                                ["About This App",
                                 "By Operation",
                                 "Type of Eponym",
                                 "Geographical",
                                 "Journal of Publication",
                                 "Famous People",
                                 "Time Travel",
                                 "Exam Favourites",
                                 ])
    if   exp == "About This App":           exp_about()             #1
    elif exp == "By Operation":             exp_operation()         #2
    elif exp == "Type of Eponym":           exp_type()              #3
    elif exp == "Geographical":             exp_geography()         #4         
    elif exp == "Journal of Publication":   exp_journals()          #5
    elif exp == "Famous People":            exp_people()            #6
    elif exp == "Time Travel":              exp_year()              #7
    elif exp == "Exam Favourites":          exp_exam()              #8

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
        unsafe_allow_html=True)

    st.markdown(
        """
        <style type="text/css" media="screen">
        div[role="listbox"] ul {
            height:110px;
        }
        </style>
        """
        ,
        unsafe_allow_html=True)




    #Page
    st.write('''_UNDER CONSTRUCTION_''')
    st.markdown('''# SurgicalEps''')
    st.markdown('''_An Educational Web App from Excision Ltd_''')

    st.markdown("---")
    st.subheader('Introduction')
    st.markdown(' ')
#   st.markdown('''<br><span style="font-size:14pt;font-weight:bold;color:black;text-decoration:underline;">Introduction</span>''', unsafe_allow_html=True)
    st.write('''There are a hundreds of eponyms used in daily surgical practice.
    We hope that you will find this app helpful in understanding what these terms mean, their history,
    and how they relate to one another. We include direct links to primary papers, as well as useful webpages in Wikipedia, Whonamedit?, ICD-11 and TeachMeSurgery.''')

    st.markdown("---")
    st.subheader('How To Use This App')
    st.markdown(' ')
    st.markdown('''<span style="font-size:12pt;color:black;font-weight:bold;">By Operation:</span><span style="font-size:12pt;color:black;"> Here you
                   can choose an operation type (eg. Oesophagectomy), and then access all the common eponyms related to that procedure.</span>''',
                unsafe_allow_html=True)
    st.markdown('''<span style="font-size:12pt;color:black;font-weight:bold;">Type of Eponym:</span><span style="font-size:12pt;color:black;"> Choose from anatomical structures, clinical scores or signs, operations,
                pathology, patient positioning, research trials, incisions, instruments, surgical maneouvers & techniques.</span>''',
                unsafe_allow_html=True)
    st.markdown('''<span style="font-size:12pt;color:black;font-weight:bold;">Geographical:</span><span style="font-size:12pt;color:black;"> Choose a region of the world to find eponyms.
                Select a country or famous city.</span>''',
                unsafe_allow_html=True)
    st.markdown('''<span style="font-size:12pt;color:black;font-weight:bold;">Journal of Publication:</span><span style="font-size:12pt;color:black;"> In this section, journals can be selected to
                find which eponyms can be traced to their archives.</span>''',
                unsafe_allow_html=True)
    st.markdown('''<span style="font-size:12pt;color:black;font-weight:bold;">Famous People:</span><span style="font-size:12pt;color:black;"> Some famous people have
                been attributed to many eponyms.</span>''',
                unsafe_allow_html=True)
    st.markdown('''<span style="font-size:12pt;color:black;font-weight:bold;">Time Travel:</span><span style="font-size:12pt;color:black;"> Explore
                through time using the time travel function.</span>''',
                unsafe_allow_html=True)
    st.markdown('''<span style="font-size:12pt;color:black;font-weight:bold;">Exam Favourites:</span><span style="font-size:12pt;color:black;"> Select from those often found in exams.
                Explore by speciality.</span>''',
                unsafe_allow_html=True)
 
    st.markdown("---")
    st.subheader('Who is this App for?')
    st.markdown(' ')
    st.write('''Doctors, nurses, secretaries, theatre staff, physician assistants, allied health professionals and students''')

    st.markdown("---")
    st.subheader('Disclaimer')
    st.markdown(' ')
    st.write('''Educational purposes''')
    
    st.sidebar.markdown("---")
    st.sidebar.markdown('''**Latest News**''')
    st.sidebar.info("App will be launched Jan 2021")


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

    st.markdown(
        """
        <style type="text/css" media="screen">
        div[role="listbox"] ul {
            height:250px;
        }
        </style>
        """
        ,unsafe_allow_html=True,)

    ScreenSize = st.selectbox('Screen size',
                     options=['Smartphone - portrait',
                              'Smartphone - landscape',
                              'Tablet','13-inch','15-inch','27-inch'])

    if   ScreenSize == "Smartphone - portrait":  Screen_width =  400; Screen_height = 600
    if   ScreenSize == "Smartphone - landscape": Screen_width =  400; Screen_height = 600
    if   ScreenSize == "15-inch":                Screen_width = 1100; Screen_height = 500
    if   ScreenSize == "27-inch":                Screen_width = 1100; Screen_height = 500
    st.markdown("---")

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
    st.subheader('''Choose operations of interest:''')
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
    ScreenSize = st.selectbox('Screen size',
                     options=['Smartphone - portrait','Smartphone - landscape',
                              'Tablet / Laptop / Desktop'])

    if   ScreenSize == "Smartphone - portrait":  Screen_width =  400; Screen_height = 600
    if   ScreenSize == "Smartphone - landscape": Screen_width = 1100; Screen_height = 500
    st.markdown("---")
    
    st.subheader('''First, Select Type:''')
#    st.sidebar.markdown("---")
    
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
        font-size: 16px !important;}
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
                    'ICD11','WNI_link', 'Reference', 'Wiki_link','PMID','Type','ExamFav','Journal','History','ICD11_link','Year',
                    'CountryOfEponym_A1','Class','Subclass','Description','Sex_A1','Lat_A1','Long_A1'],
                             axis=1).sort_values(by=['Eponym_OLD'],
                                                 ascending=True).reindex(columns=['Eponym']).reset_index(drop=True))

    worldMap = st.checkbox('''Show on world map - Smartphone''', value=False)
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
                    size=5,
                ),
                text=text,
            hoverinfo='text'
            ))
        fig.update_layout(
            autosize=True,
            hovermode='closest',
            showlegend=False,
            width=345,
            height=230,
            mapbox=dict(
                accesstoken=mapbox_access_token,
                bearing=0,
                center=dict(lat=35,lon=8),
                pitch=0,
                zoom=-0.50,
                style='dark'),
            )
        fig.update_layout(margin=dict(l=2, r=2, t=0, b=0))
        st.write(fig)

    worldMap1 = st.checkbox('''Show on world map - Widescreen''', value=False)
    if worldMap1:
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
            width=700,
            height=400,
            mapbox=dict(
                accesstoken=mapbox_access_token,
                bearing=0,
                center=dict(lat=25,lon=8),
                pitch=0,
                zoom=0.90,
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


#----------------------------------------------------------------------------------------------#
#                                                                                              #
#  Geographical Origins (4)                                                                    #
# ::: Handles the                                                                              #                                                                                              #
#                                                                                              #
#----------------------------------------------------------------------------------------------#

def exp_geography():
    st.markdown(
        """
        <style type="text/css" media="screen">
        div[role="listbox"] ul {height:150px}
        </style>
        """
        ,
        unsafe_allow_html=True,
    )

#   st.markdown('''[Advert space for Google AdSense3]''')
    ScreenSize = st.radio('Screen size',
                     options=['Smartphone - portrait',
                              'Smartphone - landscape',
                              'Tablet / Laptop / Desktop',])

    if ScreenSize == "Smartphone - portrait":
        st.subheader('''Type in box for geographical location:''')
        options1 = st.selectbox(' ', [" ",
                                 "   ",
                                 "All",
                                 "Argentina",
                                 "Austria",
                                 "Brazil",
                                 "Canada",
                                 "Chicago",
                                 "Denmark",
                                 "Edinburgh",
                                 "Europe",
                                 "France",
                                 "Germany",
                                 "Hawaii",
                                 "Ireland",
                                 "Italy",
                                 "Japan",
                                 "London",
                                 "Netherlands",
                                 "New York City",
                                 "North America",
                                 "Paris",
                                 "Poland",
                                 "South America",
                                 "Sweden",
                                 "Switzerland",
                                 "UK",
                                 "United Kingdom",
                                 "USA",
                                 "World",
                                 ])


        Year = st.slider('Use the red dot slider to travel back in time:', 1560, 2020, value=2020)
        url = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/Eponyms4python_Lite.csv'
        df1 = pd.read_csv(url, dtype={'PMID':str,'Year':int})
        df2 = df1.sort_values(by=['Year'],ascending=True)
#    mapbox_access_token = open("/Users/alastairhayes/desktop/Eponyms/ajhayes83_1.mapbox_token").read()  
        mapbox_access_token = 'pk.eyJ1IjoiYWpoYXllczgzIiwiYSI6ImNrY2pqM2lvMDB4Z24ydG8zdDl0NTYwbTUifQ.2DKVfTAaE77XAXMpDeq_Pg'
        df3 = df2.sort_values(by=['CountryOfEponym_A1'],ascending=True)  #Gives eponyms by operation alphabetically
        dfT = df3.sort_values(by=['Year'],ascending=True)
        time_df = dfT.loc[dfT['Year'] <= Year]
        site_lat = time_df['Lat_A1']            #df3['Lat_A1']                
        site_lon = time_df['Long_A1']           #df3['Long_A1']
        text = time_df['Eponym_easy'] + ', ' + time_df['CityOfEponym_A1'] + ', ' + time_df['Year'].astype(str)
        locations_name = time_df['Eponym_easy'] #df3['Eponym_easy']

        if   options1 == " ":              lat_country  = 20.00;  lon_country  =  8.0; zoom_country = -0.40; markersize = 4; Screen_width =  340; Screen_height = 260
        if   options1 == "london":         lat_country  = 51.52;  lon_country  = -0.1; zoom_country =  9.80; markersize = 18; Screen_width =  340; Screen_height = 480
        if   options1 == "london":         lat_country  = 51.52;  lon_country  = -0.1; zoom_country =  9.80; markersize = 18
        if   options1 == "Paris":          lat_country  = 48.85;  lon_country  = 2.36; zoom_country = 10.40; markersize = 18
        if   options1 == "World":          lat_country  = 25.00;  lon_country  =  8.0; zoom_country =  1.08; markersize = 12
        if   options1 == "All":            lat_country  = 25.00;  lon_country  =  8.0; zoom_country =  1.08;  markersize = 12
        if   options1 == "Europe":         lat_country  = 54.00;  lon_country  = 10.0; zoom_country =  2.85; markersize = 12
        if   options1 == "Austria":        lat_country  = 47.20;  lon_country  = 13.4; zoom_country =  6.50; markersize = 16
        if   options1 == "Denmark":        lat_country  = 56.00;  lon_country  =  9.8; zoom_country =  4.00; markersize = 16
        if   options1 == "France":         lat_country  = 47.00;  lon_country  =  4.0; zoom_country =  4.50; markersize = 16
        if   options1 == "Germany":        lat_country  = 51.25;  lon_country  = 10.5; zoom_country =  5.20; markersize = 16
        if   options1 == "Ireland":        lat_country  = 53.50;  lon_country  = -6.2; zoom_country = 5.0; markersize = 16
        if   options1 == "Italy":          lat_country  = 41.50;  lon_country  = 14.0; zoom_country = 4.0; markersize = 16
        if   options1 == "Japan":          lat_country  = 37.40;  lon_country  = 135.0;zoom_country = 4.4; markersize = 16
        if   options1 == "Netherlands":    lat_country  = 52.00;  lon_country  =  5.0; zoom_country = 4.8; markersize = 16
        if   options1 == "Poland":         lat_country  = 52.00;  lon_country  = 19.0; zoom_country = 4.0; markersize = 16
        if   options1 == "Sweden":         lat_country  = 62.50;  lon_country  = 18.5; zoom_country = 3.0; markersize = 16
        if   options1 == "Switzerland":    lat_country  = 47.00;  lon_country  =  8.0; zoom_country = 4.5; markersize = 16
        if   options1 == "UK":             lat_country  = 53.00;  lon_country  = -3.2; zoom_country = 3.8; markersize = 18
        if   options1 == "Edinburgh":      lat_country  = 55.80;  lon_country  = -3.2; zoom_country = 6.8; markersize = 18
        if   options1 == "London":         lat_country  = 51.52;  lon_country  = -0.1; zoom_country = 9.8; markersize = 18
        if   options1 == "North America":  lat_country  = 52.00;  lon_country  = -100; zoom_country = 1.8; markersize = 10
        if   options1 == "Canada":         lat_country  = 59.00;  lon_country  = -95.0;zoom_country = 2.5; markersize = 16
        if   options1 == "USA":            lat_country  = 37.00;  lon_country  = -113;   zoom_country = 2.9; markersize = 16
        if   options1 == "Chicago":        lat_country  = 42.00;  lon_country  = -88.0;  zoom_country = 8.0; markersize = 18
        if   options1 == "New York":       lat_country  = 40.80;  lon_country  = -73.9;  zoom_country = 9.8; markersize = 18
        if   options1 == "Hawaii":         lat_country  = 20.50;  lon_country  = -157.4; zoom_country = 6.1; markersize = 18
        if   options1 == "South America":  lat_country  =-28.00;  lon_country  = -65.0;  zoom_country = 1.8; markersize = 12
        if   options1 == "Argentina":      lat_country  =-40.00;  lon_country  = -65.0;  zoom_country = 2.5; markersize = 16
        if   options1 == "Brazil":         lat_country  =-10.00;  lon_country  = -55.0;  zoom_country = 3.0; markersize = 16

        fig3 = go.Figure()
        fig3.add_trace(go.Scattermapbox(
                lat=site_lat,
                lon=site_lon,
                mode='markers',
                marker=go.scattermapbox.Marker(
                    size=markersize,
                    color='yellow', #'rgb(255, 0, 0)',
                    opacity=0.7
                ),
                text=text,
                hoverinfo='text',
            ))

        fig3.update_layout(
            autosize=True,
            hovermode='closest',
            showlegend=False,
            width=Screen_width,
            height=Screen_height,
            mapbox=dict(
                accesstoken=mapbox_access_token,
                bearing=0,
                center=dict(lat=lat_country,lon=lon_country),
                pitch=0,
                zoom=zoom_country,
                style='satellite-streets'), #'dark'
        )
        fig3.update_layout(margin=dict(l=2, r=2, t=0, b=0))
        st.write(fig3)
        st.write('''To **zoom in**: first click on the map then use **=** key. Use **-** key to pan out.''')

        df4 = df3.sort_values(by=['Eponym'],ascending=True)
        Geo_options = st.selectbox('', df4['Eponym_easy'].unique())



    if ScreenSize == "Smartphone - landscape":
        st.subheader('''Type in box for geographical location:''')
        options1 = st.selectbox(' ', [" ",
                                 "   ",
                                 "All",
                                 "Argentina",
                                 "Austria",
                                 "UK",
                                 "United Kingdom",
                                 "USA",
                                 "World",
                                 ])


        Year = st.slider('Use the red dot slider to travel back in time:', 1560, 2020, value=2020)
        url = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/Eponyms4python_Lite.csv'
        df1 = pd.read_csv(url, dtype={'PMID':str,'Year':int})
        df2 = df1.sort_values(by=['Year'],ascending=True)
        mapbox_access_token = 'pk.eyJ1IjoiYWpoYXllczgzIiwiYSI6ImNrY2pqM2lvMDB4Z24ydG8zdDl0NTYwbTUifQ.2DKVfTAaE77XAXMpDeq_Pg'
        df3 = df2.sort_values(by=['CountryOfEponym_A1'],ascending=True)  #Gives eponyms by operation alphabetically
        dfT = df3.sort_values(by=['Year'],ascending=True)
        time_df = dfT.loc[dfT['Year'] <= Year]
        site_lat = time_df['Lat_A1']            #df3['Lat_A1']                
        site_lon = time_df['Long_A1']           #df3['Long_A1']
        text = time_df['Eponym_easy'] + ', ' + time_df['CityOfEponym_A1'] + ', ' + time_df['Year'].astype(str)
        locations_name = time_df['Eponym_easy'] #df3['Eponym_easy']

        if   options1 == " ":              lat_country  = 30.00;  lon_country  =  10.0; zoom_country = 0.55; markersize = 6; Screen_width =  600; Screen_height = 330
        if   options1 == "london":         lat_country  = 51.52;  lon_country  = -0.1; zoom_country =  9.80; markersize = 6; Screen_width =  600; Screen_height = 330


        fig3 = go.Figure()
        fig3.add_trace(go.Scattermapbox(
                lat=site_lat,
                lon=site_lon,
                mode='markers',
                marker=go.scattermapbox.Marker(
                    size=markersize,
                    color='yellow', #'rgb(255, 0, 0)',
                    opacity=0.7
                ),
                text=text,
                hoverinfo='text',
                ))

        fig3.update_layout(
                autosize=True,
                hovermode='closest',
                showlegend=False,
                width=Screen_width,
                height=Screen_height,
        mapbox=dict(
                accesstoken=mapbox_access_token,
                bearing=0,
                center=dict(lat=lat_country,lon=lon_country),
                pitch=0,
                zoom=zoom_country,
                style='satellite-streets'), #'dark'
            )
        fig3.update_layout(margin=dict(l=2, r=2, t=0, b=0))
        st.write(fig3)
        st.write('''To **zoom in**: first click on the map then use **=** key. Use **-** key to pan out.''')

        df4 = df3.sort_values(by=['Eponym'],ascending=True)
        Geo_options = st.selectbox('', df4['Eponym_easy'].unique())










    if ScreenSize == "Tablet / Laptop / Desktop":                
        st.subheader('''Type in box for geographical location:''')
        options1 = st.selectbox(' ', [" ",
                                 "   ",
                                 "All",
                                 "Argentina",
                                 "Austria",
                                 "UK",
                                 "United Kingdom",
                                 "USA",
                                 "World",
                                 ])


        Year = st.slider('Use the red dot slider to travel back in time:', 1560, 2020, value=2020)
        url = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/Eponyms4python_Lite.csv'
        df1 = pd.read_csv(url, dtype={'PMID':str,'Year':int})
        df2 = df1.sort_values(by=['Year'],ascending=True)
        mapbox_access_token = 'pk.eyJ1IjoiYWpoYXllczgzIiwiYSI6ImNrY2pqM2lvMDB4Z24ydG8zdDl0NTYwbTUifQ.2DKVfTAaE77XAXMpDeq_Pg'
        df3 = df2.sort_values(by=['CountryOfEponym_A1'],ascending=True)  #Gives eponyms by operation alphabetically
        dfT = df3.sort_values(by=['Year'],ascending=True)
        time_df = dfT.loc[dfT['Year'] <= Year]
        site_lat = time_df['Lat_A1']            #df3['Lat_A1']                
        site_lon = time_df['Long_A1']           #df3['Long_A1']
        text = time_df['Eponym_easy'] + ', ' + time_df['CityOfEponym_A1'] + ', ' + time_df['Year'].astype(str)
        locations_name = time_df['Eponym_easy'] #df3['Eponym_easy']

        if   options1 == " ":              lat_country  = 30.00;  lon_country  =  10.0; zoom_country = 0.45; markersize = 6; Screen_width =  700; Screen_height = 450
        if   options1 == "london":         lat_country  = 51.52;  lon_country  = -0.1; zoom_country =  9.80; markersize = 5; Screen_width =  700; Screen_height = 450


        fig3 = go.Figure()
        fig3.add_trace(go.Scattermapbox(
                lat=site_lat,
                lon=site_lon,
                mode='markers',
                marker=go.scattermapbox.Marker(
                    size=markersize,
                    color='yellow', #'rgb(255, 0, 0)',
                    opacity=0.7
                ),
                text=text,
                hoverinfo='text',
                ))

        fig3.update_layout(
                autosize=True,
                hovermode='closest',
                showlegend=False,
                width=Screen_width,
                height=Screen_height,
        mapbox=dict(
                accesstoken=mapbox_access_token,
                bearing=0,
                center=dict(lat=lat_country,lon=lon_country),
                pitch=0,
                zoom=zoom_country,
                style='satellite-streets'), #'dark'
            )
        fig3.update_layout(margin=dict(l=2, r=2, t=0, b=0))
        st.write(fig3)
        st.write('''To **zoom in**: first click on the map then use **=** key. Use **-** key to pan out.''')

        df4 = df3.sort_values(by=['Eponym'],ascending=True)
        Geo_options = st.selectbox('', df4['Eponym_easy'].unique())

   
#'open-street-map','white-bg','carto-positron','carto-darkmatter','stamen- terrain','stamen-watercolor', 'basic', 'streets',
    #'outdoors', 'light', 'dark',
    #'satellite', 'satellite-streets'

#----------------------------------------------------------------------------------------------#
#                                                                                              #
#  Exam (8)                                                                                    #
# ::: Handles the                                                                              #                                                                                              #
#                                                                                              #
#----------------------------------------------------------------------------------------------#
def exp_exam():

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
    ExamF_df = df[(df['ExamFav'].str.match('Yes'))]
    if not ExamF_df['ExamFav'].isnull().all():
        Table = ff.create_table(ExamF_df.drop(['Alphabet','CityOfEponym_A1','ISO_country_A1','Author_1_Role','WhoNamedIt',
                    'Author_1', 'Author_2','Pubmed_results', 'Google_results','Operation','GxP', 'Log2_GxP','Societies',
                    'ICD11','WNI_link', 'Reference', 'Wiki_link','PMID', 'Type','Journal','History','ICD11_link','Year',
                    'CountryOfEponym_A1','Class','Subclass','Description','Sex_A1','Lat_A1','Long_A1'],
                             axis=1).sort_values(by=['Eponym'],
                                                 ascending=True).reindex(columns=['Eponym']).reset_index(drop=True))



#-------------------------------------------------------------------------------------------#
if __name__ == "__main__":
    main()
