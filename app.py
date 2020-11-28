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
    His qualifications include FRCSEd (Gen Surg) & PhD.''')
        st.markdown('''He is working to develop data science and software solutions for clinical data systems, research and education in surgical practice.''')

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
                                ["About this App",
                                 "By Operation",
                                 "Type of Eponym",
                                 "World Maps",
                                 "Journal of Publication",
                                 "Famous People",
                                 "Time Travel",
                                 "Exam Favourites",
                                 ])
    if   exp == "About this App":           exp_about()             #1
    elif exp == "By Operation":             exp_operation()         #2
    elif exp == "Type of Eponym":           exp_type()              #3
    elif exp == "World Maps":               exp_geography()         #4         
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
        """<style type="text/css" media="screen">
        .hovertext text {font-size: 20px !important;}
        </style>""",unsafe_allow_html=True)

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
    eponymByOp = st.multiselect('Select from operations:',options=list(U), format_func=lambda x: ' ' if x == '1' else x)
    new_df = df1.loc[df1['Operation'].str.contains('|'.join(eponymByOp)) == True]
    new_df2 = new_df.sort_values(by=['Eponym'],ascending=True)
 
    if not eponymByOp == None:
        Op_options = st.selectbox('Related eponyms:',
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
    types = st.selectbox('First, select type of eponym from list:',["Anatomical structures",
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
    Anat_options2 = st.selectbox('Then, search list of named structures:', Anat_df['Eponym'].unique(), format_func=lambda x: ' ' if x == '1' else x)
    Anat_options2_info = Anat_df[Anat_df['Eponym'].str.match(Anat_options2)]

#2
def show_scores():
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
    Scores_options2 = st.selectbox('Then, search list of clinical scores:', Scores_df['Eponym'].unique())
    Scores_options2_info = Scores_df[Scores_df['Eponym'].str.match(Scores_options2)]

#3
def show_signs():
    url = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/Eponyms4python_Lite.csv'
    df = pd.read_csv(url, dtype={'PMID':str,'Year':int})
    Sign_df = df[(df['Type'].str.match('Signs'))]
    if not Sign_df['Type'].isnull().all():
        Table = ff.create_table(Sign_df.drop(['Alphabet','CityOfEponym_A1','ISO_country_A1','Author_1_Role','WhoNamedIt',
                    'Author_1', 'Author_2','Pubmed_results', 'Google_results','Operation','GxP', 'Log2_GxP','Societies',
                    'ICD11','WNI_link', 'Reference', 'Wiki_link','PMID', 'Type','Journal','History','ICD11_link','Year',
                    'CountryOfEponym_A1','Class','Subclass','Description','Sex_A1','Lat_A1','Long_A1'],
                             axis=1).sort_values(by=['Eponym'],
                                                 ascending=True).reindex(columns=['Eponym']).reset_index(drop=True))
    Sign_options2 = st.selectbox('Then, search list of clinical signs:', Sign_df['Eponym'].unique())
    Sign_options2_info = Sign_df[Sign_df['Eponym'].str.match(Sign_options2)]

#4
def show_opNames():
    url = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/Eponyms4python_Lite.csv'
    df = pd.read_csv(url, dtype={'PMID':str,'Year':int})
    OpName_df = df[(df['Type'].str.match('Operations'))]
    if not OpName_df['Type'].isnull().all():
        Table = ff.create_table(OpName_df.drop(['Alphabet','CityOfEponym_A1','ISO_country_A1','Author_1_Role',
                    'WhoNamedIt','Author_1', 'Author_2','Pubmed_results', 'Google_results','Operation',
                    'GxP', 'Log2_GxP','Societies','ICD11','WNI_link', 'Reference', 'Wiki_link','PMID', 'Type',
                    'Journal','History','ICD11_link','Year', 'CountryOfEponym_A1','Class','Subclass','Description',
                    'Sex_A1','Lat_A1','Long_A1'],
                             axis=1).sort_values(by=['Eponym'],
                                                 ascending=True).reindex(columns=['Eponym']).reset_index(drop=True))
    OpName_options2 = st.selectbox('Then, search list of named operations:', OpName_df['Eponym'].unique())
    OpName_options2_info = OpName_df[OpName_df['Eponym'].str.match(OpName_options2)]

#5
def show_path():
    url = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/Eponyms4python_Lite.csv'
    df = pd.read_csv(url, dtype={'PMID':str,'Year':int})
    Path_df = df[(df['Type'].str.match('Pathology'))]
    if not Path_df['Type'].isnull().all():
        Table = ff.create_table(Path_df.drop(['Alphabet','CityOfEponym_A1','ISO_country_A1','Author_1_Role',
                    'WhoNamedIt','Author_1', 'Author_2','Pubmed_results', 'Google_results','Operation','GxP',
                    'Log2_GxP','Societies','ICD11','WNI_link', 'Reference', 'Wiki_link','PMID', 'Type','Journal',
                    'History','ICD11_link','Year', 'CountryOfEponym_A1','Class','Subclass','Description',
                    'Sex_A1','Lat_A1','Long_A1'],
                             axis=1).sort_values(by=['Eponym'],
                                                 ascending=True).reindex(columns=['Eponym']).reset_index(drop=True))
    Paths_options2 = st.selectbox('Then, choose from eponymous pathological term:', Path_df['Eponym'].unique())
    Paths_options2_info = Path_df[Path_df['Eponym'].str.match(Paths_options2)]

#6
def show_positions():
    url = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/Eponyms4python_Lite.csv'
    df = pd.read_csv(url, dtype={'PMID':str,'Year':int})
    Positions_df = df[(df['Type'].str.match('Positions'))]
    if not Positions_df['Type'].isnull().all():
        Table = ff.create_table(Positions_df.drop(['Alphabet','CityOfEponym_A1','ISO_country_A1','Author_1_Role',
                    'WhoNamedIt','Author_1', 'Author_2','Pubmed_results', 'Google_results','Operation','GxP',
                    'Log2_GxP','Societies','ICD11','WNI_link', 'Reference', 'Wiki_link','PMID', 'Type','Journal',
                    'History','ICD11_link','Year', 'CountryOfEponym_A1','Class','Subclass','Description',
                    'Sex_A1','Lat_A1','Long_A1'],
                             axis=1).sort_values(by=['Eponym'],
                                                 ascending=True).reindex(columns=['Eponym']).reset_index(drop=True))
    Positions_options2 = st.selectbox('Choose named patient position:', Positions_df['Eponym'].unique())
    Positions_options2_info = Positions_df[Positions_df['Eponym'].str.match(Positions_options2)]

#7
def show_trials():
    url = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/Eponyms4python_Lite.csv'
    df = pd.read_csv(url, dtype={'PMID':str,'Year':int})
    Trial_df = df[(df['Type'].str.match('Trials'))]
    if not Trial_df['Type'].isnull().all():
        Table = ff.create_table(Trial_df.drop(['Alphabet','CityOfEponym_A1','ISO_country_A1','Author_1_Role','WhoNamedIt',
                    'Author_1', 'Author_2','Pubmed_results', 'Google_results','Operation','GxP', 'Log2_GxP','Societies',
                    'ICD11','WNI_link', 'Reference', 'Wiki_link','PMID', 'Type','Journal','History','ICD11_link','Year',
                    'CountryOfEponym_A1','Class','Subclass','Description','Sex_A1','Lat_A1','Long_A1'],
                             axis=1).sort_values(by=['Eponym'],
                                                 ascending=True).reindex(columns=['Eponym']).reset_index(drop=True))
    Trial_options2 = st.selectbox('Then, search list of eponymous research trials:', Trial_df['Eponym'].unique())
    Trial_options2_info = Trial_df[Trial_df['Eponym'].str.match(Trial_options2)]

#8
def show_cuts():
    url = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/Eponyms4python_Lite.csv'
    df = pd.read_csv(url, dtype={'PMID':str,'Year':int})
    Cuts_df = df[(df['Type'].str.match('Incisions'))]
    if not Cuts_df['Type'].isnull().all():
        Table = ff.create_table(Cuts_df.drop(['Alphabet','CityOfEponym_A1','ISO_country_A1','Author_1_Role',
                    'WhoNamedIt','Author_1', 'Author_2','Pubmed_results', 'Google_results','Operation','GxP',
                    'Log2_GxP','Societies','ICD11','WNI_link', 'Reference', 'Wiki_link','PMID', 'Type','Journal',
                    'History','ICD11_link','Year', 'CountryOfEponym_A1','Class','Subclass','Description',
                    'Sex_A1','Lat_A1','Long_A1'],
                             axis=1).sort_values(by=['Eponym'],
                                                 ascending=True).reindex(columns=['Eponym']).reset_index(drop=True))
    Cuts_options2 = st.selectbox('Choose from list of incisions:', Cuts_df['Eponym'].unique())
    Cuts_options2_info = Cuts_df[Cuts_df['Eponym'].str.match(Cuts_options2)]

#9    
def show_instruments():
    url = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/Eponyms4python_Lite.csv'
    df = pd.read_csv(url, dtype={'PMID':str,'Year':int})
    Instrum_df = df[(df['Type'].str.match('Instruments'))]
    if not Instrum_df['Type'].isnull().all():
        Table = ff.create_table(Instrum_df.drop(['Alphabet','CityOfEponym_A1','ISO_country_A1','Author_1_Role',
                    'WhoNamedIt','Author_1', 'Author_2','Pubmed_results', 'Google_results','Operation','GxP',
                    'Log2_GxP','Societies','ICD11','WNI_link', 'Reference', 'Wiki_link','PMID', 'Type','Journal',
                    'History','ICD11_link','Year', 'CountryOfEponym_A1','Class','Subclass','Description',
                    'Sex_A1','Lat_A1','Long_A1'],
                             axis=1).sort_values(by=['Eponym'],
                                                 ascending=True).reindex(columns=['Eponym']).reset_index(drop=True))
    Instrum_options2 = st.selectbox('Choose from list of surgical instruments:', Instrum_df['Eponym'].unique())
    Instrum_options2_info = Instrum_df[Instrum_df['Eponym'].str.match(Instrum_options2)]


#10
def show_maneuvers():
    url = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/Eponyms4python_Lite.csv'
    df = pd.read_csv(url, dtype={'PMID':str,'Year':int})
    Maneuv_df = df[(df['Type'].str.match('Surgical Maneuvers & Techniques'))]
    if not Maneuv_df['Type'].isnull().all():
        Table = ff.create_table(Maneuv_df.drop(['Alphabet','CityOfEponym_A1','ISO_country_A1','Author_1_Role',
                    'WhoNamedIt','Author_1', 'Author_2','Pubmed_results','Google_results','Operation','GxP',
                    'Log2_GxP','Societies','ICD11','WNI_link', 'Reference', 'Wiki_link','PMID', 'Type','Journal',
                    'History','ICD11_link','Year', 'CountryOfEponym_A1','Class','Subclass','Description',
                    'Sex_A1','Lat_A1','Long_A1'],
                             axis=1).sort_values(by=['Eponym'],
                                                 ascending=True).reindex(columns=['Eponym']).reset_index(drop=True))
    Maneuv_options2 = st.selectbox('Choose from list of surgical maneuvers or techniques:', Maneuv_df['Eponym'].unique())
    Maneuv_options2_info = Maneuv_df[Maneuv_df['Eponym'].str.match(Maneuv_options2)]


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
        div[role="listbox"] ul {height:55px}
        </style>
        """
        ,
        unsafe_allow_html=True,
    )
#   st.markdown('''[Advert space for Google AdSense3]''')
    ScreenSize = st.radio('Select screen size:',
                     options=['Smartphone',
                              'Desktop / Laptop / Tablet',],index=0)

    if ScreenSize == "Smartphone":
        portrait1 = st.selectbox('Choose map Location:',
                                ["World","  ",
                                 "Argentina","Austria","Brazil","Canada",
                                 "Denmark","Edinburgh","England","Europe",
                                 "France","Germany","Hawaii",
                                 "Ireland","Italy","Japan","London",
                                 "Netherlands","New York City","North America",
                                 "Paris","Poland",
                                 "South America","Sweden","Switzerland",
                                 "UK","United Kingdom","USA"])

        Year = st.slider('Travel back in time:', 1560, 2020, value=2020)
        url = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/Eponyms4python_Lite.csv'
        df1 = pd.read_csv(url, dtype={'PMID':str,'Year':int})
        df2 = df1.sort_values(by=['Year'],ascending=True)
#       mapbox_access_token = open("/Users/alastairhayes/desktop/Eponyms/ajhayes83_1.mapbox_token").read()  
        mapbox_access_token = 'pk.eyJ1IjoiYWpoYXllczgzIiwiYSI6ImNrY2pqM2lvMDB4Z24ydG8zdDl0NTYwbTUifQ.2DKVfTAaE77XAXMpDeq_Pg'
        df3 = df2.sort_values(by=['CountryOfEponym_A1'],ascending=True)  #Gives eponyms by operation alphabetically
        dfT = df3.sort_values(by=['Year'],ascending=True)
        time_df = dfT.loc[dfT['Year'] <= Year]
        site_lat = time_df['Lat_A1']                            
        site_lon = time_df['Long_A1']
        text = time_df['Eponym_easy'] + ', ' + time_df['CityOfEponym_A1'] + ', ' + time_df['Year'].astype(str)
        locations_name = time_df['Eponym_easy']

        if portrait1 == " ":         lat_1 = 40.00; lon_1 =   0.0; zoom_country = -0.45; markersize = 4; Screen_width =  350; Screen_height = 260;
        if portrait1 == "Argentina": lat_1 =-40.00; lon_1 = -65.0; zoom_country =   2.4; markersize = 6; Screen_width =  350; Screen_height = 260;
        if portrait1 == "Austria":   lat_1 = 47.20; lon_1 =  13.4; zoom_country =  5.50; markersize = 8; Screen_width =  350; Screen_height = 260;
        if portrait1 == "Brazil":    lat_1 =-10.00; lon_1 = -55.0; zoom_country =   2.0; markersize = 9; Screen_width =  350; Screen_height = 260;
        if portrait1 == "Canada":    lat_1 = 59.00; lon_1 = -97.0; zoom_country =   1.4; markersize = 9; Screen_width =  350; Screen_height = 260;
        if portrait1 == "Denmark":   lat_1 = 56.00; lon_1 =   9.8; zoom_country =  4.00; markersize = 8; Screen_width =  350; Screen_height = 260;
        if portrait1 == "Europe":    lat_1 = 54.00; lon_1 =  10.0; zoom_country =  1.80; markersize = 6; Screen_width =  350; Screen_height = 260;
        if portrait1 == "Edinburgh": lat_1 = 55.92; lon_1 =  -3.2; zoom_country =  7.20; markersize = 9; Screen_width =  350; Screen_height = 260;
        if portrait1 == "England":   lat_1 = 52.80; lon_1 =  -3.0; zoom_country =  4.30; markersize = 9; Screen_width =  350; Screen_height = 260
        if portrait1 == "France":    lat_1 = 47.00; lon_1 =   4.0; zoom_country =  4.50; markersize = 8; Screen_width =  350; Screen_height = 260;
        if portrait1 == "Germany":   lat_1 = 51.25; lon_1 =  10.2; zoom_country =  3.80; markersize = 8; Screen_width =  350; Screen_height = 260;
        if portrait1 == "Hawaii":    lat_1 = 20.50; lon_1 =-157.4; zoom_country =   5.0; markersize = 9; Screen_width =  350; Screen_height = 260;
        if portrait1 == "Ireland":   lat_1 = 53.50; lon_1 =  -6.2; zoom_country =   5.0; markersize = 8; Screen_width =  350; Screen_height = 260; 
        if portrait1 == "Italy":     lat_1 = 41.50; lon_1 =  14.0; zoom_country =   3.6; markersize = 8; Screen_width =  350; Screen_height = 260;
        if portrait1 == "Japan":     lat_1 = 37.40; lon_1 = 135.0; zoom_country =   4.4; markersize = 8; Screen_width =  350; Screen_height = 260;
        if portrait1 == "London":         lat_1 = 51.54;  lon_1 =  -0.1; zoom_country =  8.20; markersize = 9; Screen_width =  350; Screen_height = 260;
        if portrait1 == "Netherlands":    lat_1 = 52.00;  lon_1 =   5.0; zoom_country =   4.8; markersize = 8; Screen_width =  350; Screen_height = 260;
        if portrait1 == "New York City":  lat_1 = 40.78;  lon_1 = -74.0; zoom_country =  8.20; markersize = 9; Screen_width =  350; Screen_height = 260;
        if portrait1 == "North America":  lat_1 = 52.00;  lon_1 =  -100; zoom_country =   1.8; markersize = 9; Screen_width =  350; Screen_height = 260;
        if portrait1 == "Paris":          lat_1 = 48.86;  lon_1 =  2.35; zoom_country =  10.2; markersize = 9; Screen_width =  350; Screen_height = 260;
        if portrait1 == "Poland":         lat_1 = 52.00;  lon_1 =  19.0; zoom_country =   4.0; markersize = 8; Screen_width =  350; Screen_height = 260;
        if portrait1 == "South America":  lat_1 =-28.00;  lon_1 = -65.0; zoom_country =   1.8; markersize = 6; Screen_width =  350; Screen_height = 260;
        if portrait1 == "Sweden":         lat_1 = 62.50;  lon_1 =  18.5; zoom_country =   3.0; markersize = 8; Screen_width =  350; Screen_height = 260;
        if portrait1 == "Switzerland":    lat_1 = 47.00;  lon_1 =   8.0; zoom_country =   4.5; markersize = 8; Screen_width =  350; Screen_height = 260;
        if portrait1 == "UK":             lat_1 = 54.40;  lon_1 =  -3.2; zoom_country =  3.55; markersize = 9; Screen_width =  350; Screen_height = 260;
        if portrait1 == "USA":            lat_1 = 39.00;  lon_1 =   -96; zoom_country =  2.05; markersize = 9; Screen_width =  350; Screen_height = 260;
        if portrait1 == "World":          lat_1 = 40.00;  lon_1 =   0.0; zoom_country = -0.45; markersize = 4; Screen_width =  350; Screen_height = 260;

        figG3 = go.Figure()
        figG3.add_trace(go.Scattermapbox(lat=site_lat,lon=site_lon,mode='markers',
                marker=go.scattermapbox.Marker(size=markersize,color='yellow',opacity=0.7),
                text=text,hoverinfo='text',))

        figG3.update_layout(
                autosize=True,hovermode='closest',showlegend=False,width=Screen_width,height=Screen_height,
                mapbox=dict(accesstoken=mapbox_access_token,bearing=0,center=dict(lat=lat_1,lon=lon_1),
                pitch=5,zoom=zoom_country,style='satellite-streets'))
        figG3.update_layout(margin=dict(l=2, r=2, t=0, b=0))
        st.write(figG3)
        st.markdown('''<span style="font-size:8pt;color:black;">If the map does not locate correctly, press 'Zoom in' on the top right corner.</span>''',
                unsafe_allow_html=True)

    if ScreenSize == "Desktop / Laptop / Tablet":                
        options3 = st.selectbox('Choose map location:',
                                ["World"," ","  ",
                                 "Argentina","Austria","Brazil","Canada",
                                 "Denmark","Edinburgh","England","Europe",
                                 "France","Germany","Hawaii",
                                 "Ireland","Italy","Japan","London",
                                 "Netherlands","New York City","North America",
                                 "Paris","Poland",
                                 "South America","Sweden","Switzerland",
                                 "UK","United Kingdom","USA",])

        Year = st.slider('Travel back in time:', 1560, 2020, value=2020)
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

        if   options3 == " ":              lat_3 = 35.00; lon_3 =  10.0; zoom_country = 0.44; markersize = 6; Screen_width =  700; Screen_height = 440
        if   options3 == "Argentina":      lat_3 =-39.00; lon_3 = -65.0; zoom_country = 2.30; markersize =10; Screen_width =  700; Screen_height = 440
        if   options3 == "Austria":        lat_3 = 47.20; lon_3 =  13.4; zoom_country = 5.80; markersize =11; Screen_width =  700; Screen_height = 440
        if   options3 == "Brazil":         lat_3 =-10.00; lon_3 = -55.0; zoom_country = 2.50; markersize =11; Screen_width =  700; Screen_height = 440
        if   options3 == "Canada":         lat_3 = 61.00; lon_3 = -94.0; zoom_country = 1.90; markersize =10; Screen_width =  700; Screen_height = 440
        if   options3 == "Denmark":        lat_3 = 56.00; lon_3 =  9.70; zoom_country = 5.00; markersize =10; Screen_width =  700; Screen_height = 440
        if   options3 == "Edinburgh":      lat_3 = 55.92; lon_3 =  -3.2; zoom_country = 9.20; markersize =12; Screen_width =  700; Screen_height = 440
        if   options3 == "England":        lat_3 = 52.80; lon_3 =  -3.0; zoom_country = 5.05; markersize =11; Screen_width =  700; Screen_height = 440
        if   options3 == "Europe":         lat_3 = 54.40; lon_3 =  10.0; zoom_country = 2.50; markersize = 6; Screen_width =  700; Screen_height = 440
        if   options3 == "France":         lat_3 = 47.00; lon_3 =   3.0; zoom_country = 4.50; markersize =10; Screen_width =  700; Screen_height = 440
        if   options3 == "Germany":        lat_3 = 51.30; lon_3 =  10.2; zoom_country = 4.50; markersize =11; Screen_width =  700; Screen_height = 440
        if   options3 == "Hawaii":         lat_3 = 20.50; lon_3 =-157.3; zoom_country = 5.50; markersize = 9; Screen_width =  700; Screen_height = 440
        if   options3 == "Ireland":        lat_3 = 53.50; lon_3 =  -6.2; zoom_country = 5.00; markersize = 9; Screen_width =  700; Screen_height = 440
        if   options3 == "Italy":          lat_3 = 41.80; lon_3 =  14.0; zoom_country = 4.50; markersize =11; Screen_width =  700; Screen_height = 440
        if   options3 == "Japan":          lat_3 = 37.70; lon_3 = 135.5; zoom_country = 3.45; markersize =11; Screen_width =  700; Screen_height = 440
        if   options3 == "London":         lat_3 = 51.54; lon_3 =  -0.1; zoom_country = 8.96; markersize =12; Screen_width =  700; Screen_height = 440
        if   options3 == "Netherlands":    lat_3 = 52.20; lon_3 =   5.0; zoom_country = 6.00; markersize =11; Screen_width =  700; Screen_height = 440
        if   options3 == "New York City":  lat_3 = 40.78; lon_3 = -73.9; zoom_country = 9.00; markersize =11; Screen_width =  700; Screen_height = 440
        if   options3 == "North America":  lat_3 = 51.00; lon_3 =  -103; zoom_country = 1.75; markersize = 9; Screen_width =  700; Screen_height = 440
        if   options3 == "Paris":          lat_3 = 48.86; lon_3 =  2.35; zoom_country = 10.2; markersize =12; Screen_width =  700; Screen_height = 440
        if   options3 == "Poland":         lat_3 = 52.50; lon_3 =  19.0; zoom_country =  5.0; markersize =12; Screen_width =  700; Screen_height = 440
        if   options3 == "South America":  lat_3 =-21.80; lon_3 = -65.0; zoom_country = 1.75; markersize =11; Screen_width =  700; Screen_height = 440
        if   options3 == "Sweden":         lat_3 = 62.85; lon_3 =  18.5; zoom_country = 3.15; markersize =11; Screen_width =  700; Screen_height = 440
        if   options3 == "Switzerland":    lat_3 = 47.00; lon_3 =   8.0; zoom_country =  6.0; markersize =11; Screen_width =  700; Screen_height = 440
        if   options3 == "UK":             lat_3 = 54.45; lon_3 =  -3.2; zoom_country = 4.00; markersize = 9; Screen_width =  700; Screen_height = 440
        if   options3 == "United Kingdom": lat_3 = 54.45; lon_3 =  -3.2; zoom_country = 4.00; markersize = 9; Screen_width =  700; Screen_height = 440
        if   options3 == "USA":            lat_3 = 39.00; lon_3 =-101.0; zoom_country = 1.95; markersize =10; Screen_width =  700; Screen_height = 440
        if   options3 == "World":          lat_3 = 35.00; lon_3 =  10.0; zoom_country = 0.44; markersize = 6; Screen_width =  700; Screen_height = 440
               
        figG3 = go.Figure()
        figG3.add_trace(go.Scattermapbox(
                lat=site_lat,lon=site_lon,mode='markers',
                marker=go.scattermapbox.Marker(
                    size=markersize,color='yellow',opacity=0.7),
                text=text,hoverinfo='text',
                ))
        figG3.update_layout(
                autosize=True,hovermode='closest',showlegend=False,
                width=Screen_width,height=Screen_height,
                mapbox=dict(accesstoken=mapbox_access_token,bearing=0,center=dict(lat=lat_3,lon=lon_3),
                pitch=5,zoom=zoom_country,
                style='satellite-streets'))
        figG3.update_layout(margin=dict(l=2, r=2, t=0, b=0))
        st.write(figG3)
        st.markdown('''<span style="font-size:10pt;color:black;">If map does not locate correctly, press 'Zoom in' on the top right corner.</span>''',
                unsafe_allow_html=True)

        #'open-street-map','white-bg','carto-positron','carto-darkmatter','stamen- terrain','stamen-watercolor',
        #'basic', 'streets','outdoors', 'light', 'dark','satellite', 'satellite-streets'


#----------------------------------------------------------------------------------------------#
#                                                                                              #
#  Journals (5)                                                                                 #
# ::: Handles                                                                                  #                                                                                              #
#                                                                                              #
#----------------------------------------------------------------------------------------------#

def exp_journals():
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

    #st.markdown('''[Advert space for Google AdSense4]''')
    ScreenSize = st.radio('Select screen size:',
                     options=['Smartphone',
                              'Desktop / Laptop / Tablet'],index=0)

#    st.write('''Click on a journal name to find related eponyms:''')
#    st.write('''**Zoom in** by clicking on journal name. **Zoom out** by clicking the center of the circle.''')

    url_J = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/Eponyms4python_Lite4Journals.csv'
    dfY = pd.read_csv(url_J)
    dfY1 = dfY.dropna()
    dfY1["JOURNALS"] = "JOURNALS"

    df1 = pd.read_csv(url_J)
    df2 = df1.sort_values(by=['journal'],ascending=True)
    df3 = df2['journal'].dropna()
    string = df3.str.cat(sep=',')
    splits = string.split(",")
    S = set(splits)
    T = np.array(list(S)).astype(object)
    U = np.sort(T)

    if ScreenSize == "Smartphone":
        jrnls = st.multiselect('Select from journals:',options=list(U), format_func=lambda x: ' ' if x == '1' else x)
        new_jrnls1 = df1.loc[df1['journal'].str.contains('|'.join(jrnls)) == True]
        new_jrnls2 = new_jrnls1.sort_values(by=['eponym'],ascending=True)
        if not jrnls == None:
            J_options = st.selectbox('Related eponyms:',
                                  new_jrnls2['eponym'].unique(), format_func=lambda x: ' ' if x == '1' else x)

            df_ep_info2 = new_jrnls1[new_jrnls1['eponym'].str.match(J_options)]
            
            if not df_ep_info2['year_str'].isnull().all():
                st.write('_When_:',df_ep_info2['year_str'].to_string(index=False))

            if not df_ep_info2['Who'].isnull().all():
                st.write('_Who_:',df_ep_info2['Who'].to_string(index=False))

            if not df_ep_info2['journal_name'].isnull().all():
                st.write('_Journal_:',df_ep_info2['journal_name'].to_string(index=False))


    if ScreenSize == "Desktop / Laptop / Tablet":
        figJDLT = px.sunburst(dfY1, path=['JOURNALS',
                                          'journal', 'year', 'eponym'],
                      values='Log10 Google hits',color='Log2 Google hits',hover_data=['eponym'],
                      color_continuous_scale='RdBu', #inferno,thermal,Magma,Cividis,deep,Viridis,icefire,ylgnbu,'portland','agsunset'
                      width=750, height=550)
        figJDLT.update_layout(margin=dict(l=0, r=0, t=0, b=0))
        figJDLT.update_traces(hovertemplate=None, hoverinfo='skip')
        st.write(figJDLT)


#----------------------------------------------------------------------------------------------#
#                                                                                              #
#  Exam (8)                                                                                    #
# ::: Handles the                                                                              #                                                                                              #
#                                                                                              #
#----------------------------------------------------------------------------------------------#
def exp_exam():
    url = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/Eponyms4python_Lite.csv'
    df = pd.read_csv(url, dtype={'PMID':str,'Year':int})
    df1 = df['ExamSpec'].dropna()
    string = df1.str.cat(sep=',')
    splits = string.split(",")
    S = set(splits)
    T = np.array(list(S)).astype(object)
    U = np.sort(T)
    exams = st.multiselect('Select from specialties:',options=list(U),
                           format_func=lambda x: ' ' if x == '1' else x,
                           default=['General Surgery','Bariatrics','Breast','Colorectal',
                                    'Endocrine','Gynaecology','HPB','Hernia','Neurosurgery',
                                    'Oesophagogastric','Paediatrics','Plastics',
                                    'Trauma','Urology','Vascular'])
    new_exams1 = df.loc[df['ExamSpec'].str.contains('|'.join(exams)) == True]
    new_exams2 = new_exams1.sort_values(by=['Eponym'],ascending=True)

    if not exams == None:
        Ex_options = st.selectbox('Related eponyms:',
                                  new_exams2['Eponym'].unique(), format_func=lambda x: ' ' if x == '1' else x)

        df_ep_info2 = new_exams1[new_exams1['Eponym'].str.match(Ex_options)]
            
        if not df_ep_info2['Year_str'].isnull().all():
            st.write('_When_:',df_ep_info2['Year_str'].to_string(index=False))

        if not df_ep_info2['Who'].isnull().all():
            st.write('_Who_:',df_ep_info2['Who'].to_string(index=False))



#-------------------------------------------------------------------------------------------#
if __name__ == "__main__":
    main()
