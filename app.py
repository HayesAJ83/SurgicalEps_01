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
pd.options.display.max_colwidth = 1000000
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
# :::                                                                                          #
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
                                 "Explore By Disease",
                                 "Explore By Journal",
                                 "Explore By Operation",
                                 "Explore By Speciality",
                                 "Explore By Type of Eponym",
                                 "Exam Favourites",
                                 "Find Famous People",
                                 "Explore With World Maps",
                                 "Search Full Database",
                                 ])
    if   exp == "About this App":           exp_about()             #1
    elif exp == "Explore By Operation":     exp_operation()         #2
 #   elif exp == "Explore By Type of Eponym":exp_type()              #3
    elif exp == "Explore With World Maps":  exp_geography()         #4         
    elif exp == "Explore By Journal":       exp_journals()          #5
    elif exp == "Find Famous People":       exp_people()            #6
    elif exp == "Exam Favourites":     exp_exam()              #8
    elif exp == "Explore By Disease":       exp_dis()               #9
    elif exp == "Explore By Speciality":    exp_spec()              #9
    elif exp == "Search Full Database":       exp_A2Z()              #10

#----------------------------------------------------------------------------------------------#
#                                                                                              #
#  About (1)                                                                                   #
# ::: Handles                                                                                  #                                                                                              
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
    #st.markdown('''<br><span style="font-size:14pt;font-weight:bold;color:black;text-decoration:underline;">Introduction</span>''', unsafe_allow_html=True)
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
        """<style type="text/css" media="screen">.hovertext text {font-size: 20px !important;}
        </style>""",unsafe_allow_html=True,)

    st.subheader("Eponyms Related to Particular Operations") 

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

        if not df_ep_info2['Who_B'].isnull().all():
            st.write('_Who_:',df_ep_info2['Who_B'].to_string(index=False))

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

        if not df_ep_info2['Who_B'].isnull().all():
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
    st.subheader("Eponyms Categorised Into Different Types") 
    types = st.selectbox('First, select type of eponym:',["Anatomical structures",
                             "Clinical scores",
                             "Clinical signs",
                             "Operations",
                             "Pathology",
                             "Patient positioning",
                             "Research trials",
                             "Statistical tests",
                             "Surgical incisions",
                             "Surgical instruments",
                             "Surgical maneuvers & techniques",
                             "Syndromes",
                             ], index=0)

    if types   == "Anatomical structures":              show_anatomical()       #1
    elif types == "Clinical scores":                    show_scores()           #2
    elif types == "Clinical signs":                     show_signs()            #3
    elif types == "Syndromes":                          show_synd()             #3
    elif types == "Operations":                         show_opNames()          #4
    elif types == "Pathology":                          show_path()             #5
    elif types == "Patient positioning":                show_positions()        #6
    elif types == "Research trials":                    show_trials()           #7
    elif types == "Statistical tests":                  show_stats()            #8
    elif types == "Surgical incisions":                 show_cuts()             #9
    elif types == "Surgical instruments":               show_instruments()      #10
    elif types == "Surgical maneuvers & techniques":    show_maneuvers()        #11

#1
def show_anatomical():
    url = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/Eponyms4python_Lite.csv'
    df = pd.read_csv(url, dtype={'PMID':str,'Year':int})
    df1 = df.rename(columns={"Eponym": "Eponym_OLD", "Eponym_easy": "Eponym"})
    Anat_df = df1[(df1['Type'].str.match('Anatomy'))]
    if not Anat_df['Type'].isnull().all():
        Table = ff.create_table(Anat_df.drop(['Alphabet','CityOfEponym_A1','ISO_country_A1','Author_1_Role','WhoNamedIt',
                    'Author_1', 'Author_2','Pubmed_results','Google_results','Operation','GxP','Log2_GxP','Societies',
                    'ICD11','WNI_link', 'Reference', 'Wiki_link','PMID','Type','ExamFav','journal','History','ICD11_link','Year',
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
                    'ICD11','WNI_link', 'Reference', 'Wiki_link','PMID', 'Type','journal','History','ICD11_link','Year',
                    'CountryOfEponym_A1','Class','Subclass','Description','Sex_A1','Lat_A1','Long_A1'],
                             axis=1).sort_values(by=['Eponym'],
                                                 ascending=True).reindex(columns=['Eponym']).reset_index(drop=True))
    Scores_options2 = st.radio('Then, search list of clinical scores:', Scores_df['Eponym'].unique())
    Scores_options2_info = Scores_df[Scores_df['Eponym'].str.match(Scores_options2)]

#3
def show_signs():
    url = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/Eponyms4python_Lite.csv'
    df = pd.read_csv(url, dtype={'PMID':str,'Year':int})
    Sign_df = df[(df['Type'].str.match('Signs'))]
    if not Sign_df['Type'].isnull().all():
        Table = ff.create_table(Sign_df.drop(['Alphabet','CityOfEponym_A1','ISO_country_A1','Author_1_Role','WhoNamedIt',
                    'Author_1', 'Author_2','Pubmed_results', 'Google_results','Operation','GxP', 'Log2_GxP','Societies',
                    'ICD11','WNI_link', 'Reference', 'Wiki_link','PMID', 'Type','journal','History','ICD11_link','Year',
                    'CountryOfEponym_A1','Class','Subclass','Description','Sex_A1','Lat_A1','Long_A1'],
                             axis=1).sort_values(by=['Eponym'],
                                                 ascending=True).reindex(columns=['Eponym']).reset_index(drop=True))
    Sign_options2 = st.selectbox('Then, search list of clinical signs:', Sign_df['Eponym'].unique())
    Sign_options2_info = Sign_df[Sign_df['Eponym'].str.match(Sign_options2)]


#3
def show_synd():
    url = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/Eponyms4python_Lite.csv'
    df = pd.read_csv(url, dtype={'PMID':str,'Year':int})
    Synd_df = df[(df['Type'].str.match('Syndromes'))]
    if not Synd_df['Type'].isnull().all():
        Table = ff.create_table(Synd_df.drop(['Alphabet','CityOfEponym_A1','ISO_country_A1','Author_1_Role','WhoNamedIt',
                    'Author_1', 'Author_2','Pubmed_results', 'Google_results','Operation','GxP', 'Log2_GxP','Societies',
                    'ICD11','WNI_link', 'Reference', 'Wiki_link','PMID', 'Type','journal','History','ICD11_link','Year',
                    'CountryOfEponym_A1','Class','Subclass','Description','Sex_A1','Lat_A1','Long_A1'],
                             axis=1).sort_values(by=['Eponym'],
                                                 ascending=True).reindex(columns=['Eponym']).reset_index(drop=True))
   # Synd_options2 = st.selectbox('Then, search list of syndromes:', Synd_df['Eponym'].unique())
    Synd_options2 = st.selectbox('Then, search list of syndromes:', Synd_df['Eponym'].unique())
    Synd_options2_info = Synd_df[Synd_df['Eponym'].str.match(Synd_options2)]

#4
def show_opNames():
    url = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/Eponyms4python_Lite.csv'
    df = pd.read_csv(url, dtype={'PMID':str,'Year':int})
    OpName_df = df[(df['Type'].str.match('Operations'))]
    if not OpName_df['Type'].isnull().all():
        Table = ff.create_table(OpName_df.drop(['Alphabet','CityOfEponym_A1','ISO_country_A1','Author_1_Role',
                    'WhoNamedIt','Author_1', 'Author_2','Pubmed_results', 'Google_results','Operation',
                    'GxP', 'Log2_GxP','Societies','ICD11','WNI_link', 'Reference', 'Wiki_link','PMID', 'Type',
                    'journal','History','ICD11_link','Year', 'CountryOfEponym_A1','Class','Subclass','Description',
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
                    'Log2_GxP','Societies','ICD11','WNI_link', 'Reference', 'Wiki_link','PMID', 'Type','journal',
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
                    'Log2_GxP','Societies','ICD11','WNI_link', 'Reference', 'Wiki_link','PMID', 'Type','journal',
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
                    'ICD11','WNI_link', 'Reference', 'Wiki_link','PMID', 'Type','journal','History','ICD11_link','Year',
                    'CountryOfEponym_A1','Class','Subclass','Description','Sex_A1','Lat_A1','Long_A1'],
                             axis=1).sort_values(by=['Eponym'],
                                                 ascending=True).reindex(columns=['Eponym']).reset_index(drop=True))
    Trial_options2 = st.selectbox('Then, search list of eponymous research trials:', Trial_df['Eponym'].unique())
    Trial_options2_info = Trial_df[Trial_df['Eponym'].str.match(Trial_options2)]

#8
def show_stats():
    url = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/Eponyms4python_Lite.csv'
    df = pd.read_csv(url, dtype={'PMID':str,'Year':int})
    Stats_df = df[(df['Type'].str.match('Statistics'))]
    if not Stats_df['Type'].isnull().all():
        Table = ff.create_table(Stats_df.drop(['Alphabet','CityOfEponym_A1','ISO_country_A1','Author_1_Role','WhoNamedIt',
                    'Author_1', 'Author_2','Pubmed_results', 'Google_results','Operation','GxP', 'Log2_GxP','Societies',
                    'ICD11','WNI_link', 'Reference', 'Wiki_link','PMID', 'Type','journal','History','ICD11_link','Year',
                    'CountryOfEponym_A1','Class','Subclass','Description','Sex_A1','Lat_A1','Long_A1'],
                             axis=1).sort_values(by=['Eponym'],
                                                 ascending=True).reindex(columns=['Eponym']).reset_index(drop=True))
    Stats_options2 = st.selectbox('Then, search list of eponymous statistical tests:', Stats_df['Eponym'].unique())
    Stats_options2_info = Stats_df[Stats_df['Eponym'].str.match(Stats_options2)]

#9
def show_cuts():
    url = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/Eponyms4python_Lite.csv'
    df = pd.read_csv(url, dtype={'PMID':str,'Year':int})
    Cuts_df = df[(df['Type'].str.match('Incisions'))]
    if not Cuts_df['Type'].isnull().all():
        Table = ff.create_table(Cuts_df.drop(['Alphabet','CityOfEponym_A1','ISO_country_A1','Author_1_Role',
                    'WhoNamedIt','Author_1', 'Author_2','Pubmed_results', 'Google_results','Operation','GxP',
                    'Log2_GxP','Societies','ICD11','WNI_link', 'Reference', 'Wiki_link','PMID', 'Type','journal',
                    'History','ICD11_link','Year', 'CountryOfEponym_A1','Class','Subclass','Description',
                    'Sex_A1','Lat_A1','Long_A1'],
                             axis=1).sort_values(by=['Eponym'],
                                                 ascending=True).reindex(columns=['Eponym']).reset_index(drop=True))
    Cuts_options2 = st.selectbox('Choose from list of incisions:', Cuts_df['Eponym'].unique())
    Cuts_options2_info = Cuts_df[Cuts_df['Eponym'].str.match(Cuts_options2)]

#10    
def show_instruments():
    url = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/Eponyms4python_Lite.csv'
    df = pd.read_csv(url, dtype={'PMID':str,'Year':int})
    Instrum_df = df[(df['Type'].str.match('Instruments'))]
    if not Instrum_df['Type'].isnull().all():
        Table = ff.create_table(Instrum_df.drop(['Alphabet','CityOfEponym_A1','ISO_country_A1','Author_1_Role',
                    'WhoNamedIt','Author_1', 'Author_2','Pubmed_results', 'Google_results','Operation','GxP',
                    'Log2_GxP','Societies','ICD11','WNI_link', 'Reference', 'Wiki_link','PMID', 'Type','journal',
                    'History','ICD11_link','Year', 'CountryOfEponym_A1','Class','Subclass','Description',
                    'Sex_A1','Lat_A1','Long_A1'],
                             axis=1).sort_values(by=['Eponym'],
                                                 ascending=True).reindex(columns=['Eponym']).reset_index(drop=True))
    Instrum_options2 = st.selectbox('Choose from list of surgical instruments:', Instrum_df['Eponym'].unique())
    Instrum_options2_info = Instrum_df[Instrum_df['Eponym'].str.match(Instrum_options2)]


#11
def show_maneuvers():
    url = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/Eponyms4python_Lite.csv'
    df = pd.read_csv(url, dtype={'PMID':str,'Year':int})
    Maneuv_df = df[(df['Type'].str.match('Surgical Maneuvers & Techniques'))]
    if not Maneuv_df['Type'].isnull().all():
        Table = ff.create_table(Maneuv_df.drop(['Alphabet','CityOfEponym_A1','ISO_country_A1','Author_1_Role',
                    'WhoNamedIt','Author_1', 'Author_2','Pubmed_results','Google_results','Operation','GxP',
                    'Log2_GxP','Societies','ICD11','WNI_link', 'Reference', 'Wiki_link','PMID', 'Type','journal',
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
        """<style type="text/css" media="screen">div[role="listbox"] ul {height:55px}
        </style>""",unsafe_allow_html=True,)

    ScreenSize = st.radio('1st) Select screen size:',
                     options=['Smartphone',
                              'Desktop / Laptop / Tablet',],index=0)

    if ScreenSize == "Smartphone":
        min_yrs, max_yrs = st.slider("2nd) Choose time window:", 1520, 2040, [1560, 2021])
        url = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/Eponyms4python_Lite.csv'
        df1 = pd.read_csv(url, dtype={'PMID':str,'Year':int})
        df2 = df1.sort_values(by=['Year'],ascending=True)
#       mapbox_access_token = open("/Users/alastairhayes/desktop/Eponyms/ajhayes83_1.mapbox_token").read()  
        mapbox_access_token = 'pk.eyJ1IjoiYWpoYXllczgzIiwiYSI6ImNrY2pqM2lvMDB4Z24ydG8zdDl0NTYwbTUifQ.2DKVfTAaE77XAXMpDeq_Pg'
        df3 = df2.sort_values(by=['CountryOfEponym_A1'],ascending=True)  #Gives eponyms by operation alphabetically
        dfT = df3.sort_values(by=['Year'],ascending=True)
        time_df = dfT.loc[(dfT['Year'] >= min_yrs) & (dfT['Year'] <= max_yrs)]
        site_lat = time_df['Lat_A1']                            
        site_lon = time_df['Long_A1']
        text = time_df['Eponym_easy'] + ', ' + time_df['CityOfEponym_A1'] + ', ' + time_df['Year'].astype(str)
        locations_name = time_df['Eponym_easy']

        figG3 = go.Figure()
        figG3.add_trace(go.Scattermapbox(lat=site_lat,lon=site_lon,mode='markers',
                marker=go.scattermapbox.Marker(size=4,color='yellow',opacity=0.6),
                text=text,hoverinfo='text',))

        figG3.update_layout(
                autosize=True,hovermode='closest',showlegend=False,width=350,height=250,
                mapbox=dict(accesstoken=mapbox_access_token,bearing=0,center=dict(lat=38,lon=0),
                pitch=5,zoom=-0.45,style='dark'))
        figG3.update_layout(margin=dict(l=2, r=2, t=0, b=0))
        st.write(figG3)
        st.markdown('''<span style="font-size:10pt;color:black;">Use smartphone touchscreen to zoom in and out of map.</span>''',
                unsafe_allow_html=True)

    if ScreenSize == "Desktop / Laptop / Tablet":

        mapbox_access_token = 'pk.eyJ1IjoiYWpoYXllczgzIiwiYSI6ImNrY2pqM2lvMDB4Z24ydG8zdDl0NTYwbTUifQ.2DKVfTAaE77XAXMpDeq_Pg'
        url = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/Eponyms4python_Lite.csv'
        df1 = pd.read_csv(url, dtype={'PMID':str,'Year':int})
        df2 = df1.sort_values(by=['Year'],ascending=True)
        spec_df = df2['Topic'].dropna()
        string = spec_df.str.cat(sep=',')
        splits = string.split(",")
        S = set(splits)
        T = np.array(list(S)).astype(object)
        U = np.sort(T)
        journal_spec = st.multiselect("2nd) Optional - choose specific specialties. Default 'Choose an option' shows all.",options=list(U),
                           format_func=lambda x: ' ' if x == '1' else x,
                           #default=['Academic','Anaesthetics','Bariatrics','Breast','Cardiothoracics','Colorectal','Emergency Surgery','Endocrine','ENT',
                           #         'General Surgery','Gynaecology','HPB','Hernia','Laparoscopic Surgery','Maxillofacial','Neurosurgery',
                           #         'Oesophagogastric','Orthopaedics','Paediatrics','Plastics','Transplant','Trauma','Urology','Vascular',]
                                          )

        min_yrs, max_yrs = st.slider("3rd) Optional - define a time window:", 1550, 2050, [1550, 2021])

        new_geo1 = df2.loc[df2['Topic'].str.contains('|'.join(journal_spec)) == True]
        new_geo2 = new_geo1.sort_values(by=['Year'],ascending=True)
        new_geo2T = new_geo2.loc[(new_geo2['Year'] >= min_yrs) & (new_geo2['Year'] <= max_yrs)]
        site_lat = new_geo2T['Lat_A1']            #df3['Lat_A1']                
        site_lon = new_geo2T['Long_A1']           #df3['Long_A1']
        text = new_geo2T['Eponym_easy'] + ', ' + new_geo2T['CityOfEponym_A1'] + ', ' + new_geo2T['Year'].astype(str)
        locations_name = new_geo2T['Eponym_easy'] #df3['Eponym_easy']

        options3 = st.selectbox("4th) Type continent, country or city to geolocate. Type over previous, don't try to delete. 'World' returns default. ",
                                ["World"," ","  ",
                                 "Argentina","Austria","Brazil","Canada",
                                 "Denmark","Edinburgh","England","Europe",
                                 "France","Germany","Hawaii",'India',
                                 "Ireland","Italy","Japan","London",
                                 "Netherlands","New York City","North America",
                                 "Paris","Poland",
                                 "South America","Sweden","Switzerland",
                                 "UK","United Kingdom","USA",])

        if   options3 == " ":              lat_3 = 35.00; lon_3 =  11.0; zoom_country = 0.47; markersize =6.5; Screen_width =  700; Screen_height = 440
        if   options3 == "Argentina":      lat_3 =-39.00; lon_3 = -65.0; zoom_country = 2.30; markersize =10; Screen_width =  700; Screen_height = 440
        if   options3 == "Austria":        lat_3 = 47.20; lon_3 =  13.4; zoom_country = 5.80; markersize =11; Screen_width =  700; Screen_height = 440
        if   options3 == "Brazil":         lat_3 =-10.00; lon_3 = -55.0; zoom_country = 2.50; markersize =11; Screen_width =  700; Screen_height = 440
        if   options3 == "Canada":         lat_3 = 61.00; lon_3 = -94.0; zoom_country = 1.90; markersize =10; Screen_width =  700; Screen_height = 440
        if   options3 == "Denmark":        lat_3 = 56.00; lon_3 =  9.70; zoom_country = 5.00; markersize =10; Screen_width =  700; Screen_height = 440
        if   options3 == "Edinburgh":      lat_3 = 55.92; lon_3 =  -3.2; zoom_country = 9.20; markersize =12; Screen_width =  700; Screen_height = 440
        if   options3 == "England":        lat_3 = 52.80; lon_3 =  -3.0; zoom_country = 5.05; markersize =11; Screen_width =  700; Screen_height = 440
        if   options3 == "Europe":         lat_3 = 54.40; lon_3 =  10.0; zoom_country = 2.50; markersize = 8; Screen_width =  700; Screen_height = 440
        if   options3 == "France":         lat_3 = 47.00; lon_3 =   3.0; zoom_country = 4.50; markersize =10; Screen_width =  700; Screen_height = 440
        if   options3 == "Germany":        lat_3 = 51.30; lon_3 =  10.2; zoom_country = 4.50; markersize =11; Screen_width =  700; Screen_height = 440
        if   options3 == "Hawaii":         lat_3 = 20.50; lon_3 =-157.3; zoom_country = 5.50; markersize = 9; Screen_width =  700; Screen_height = 440
        if   options3 == "India":          lat_3 = 22.00; lon_3 =  80.0; zoom_country = 3.00; markersize = 9; Screen_width =  700; Screen_height = 440
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
        if   options3 == "Sweden":         lat_3 = 62.85; lon_3 =  18.5; zoom_country = 3.12; markersize =11; Screen_width =  700; Screen_height = 440
        if   options3 == "Switzerland":    lat_3 = 47.00; lon_3 =   8.0; zoom_country =  6.0; markersize =11; Screen_width =  700; Screen_height = 440
        if   options3 == "UK":             lat_3 = 54.45; lon_3 =  -3.2; zoom_country = 4.00; markersize = 9; Screen_width =  700; Screen_height = 440
        if   options3 == "United Kingdom": lat_3 = 54.45; lon_3 =  -3.2; zoom_country = 4.00; markersize = 9; Screen_width =  700; Screen_height = 440
        if   options3 == "USA":            lat_3 = 39.00; lon_3 =-101.0; zoom_country = 1.95; markersize =10; Screen_width =  700; Screen_height = 440
        if   options3 == "World":          lat_3 = 35.00; lon_3 =  11.0; zoom_country = 0.47; markersize =6.5; Screen_width =  700; Screen_height = 440
               
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
                style='dark'))#dark satellite-streets
        figG3.update_layout(margin=dict(l=2, r=2, t=0, b=0))
        st.write(figG3)
        st.markdown('''<span style="font-size:10pt;color:black;">If map does not locate correctly, press 'Zoom in' on the top right corner.</span>''',
                unsafe_allow_html=True)


       # url = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/Eponyms4python_Lite.csv'
        new_geo2T["WORLD"] = "WORLD"
        figJDLT = px.sunburst(new_geo2T,path=['WORLD',
            'Continent_A1','CountryOfEponym_A1','CityOfEponym_A1','Eponym_easy'],
                              #values='Log10_GxP',
                              color='Log10_GxP',
                              hover_data=['Eponym'],
                              color_continuous_scale='viridis',#'RdBu'
                                  )
        figJDLT.update_layout(margin=dict(l=0, r=0, t=0, b=0),width=680,height=500)
        figJDLT.update_traces(hovertemplate=None,hoverinfo='skip') 
        st.write(figJDLT)


#----------------------------------------------------------------------------------------------#
#                                                                                              #
#  Journals (5)                                                                                #
# ::: Handles                                                                                  #                                                                                              #
#                                                                                              #
#----------------------------------------------------------------------------------------------#

def exp_journals():
    #st.markdown('''[Advert space for Google AdSense4]''')
    ScreenSize = st.radio('1st) Select screen size:',options=['Smartphone','Desktop / Laptop / Tablet'],index=0)
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
        jrnls = st.multiselect('2nd) Select journals:',options=list(U), format_func=lambda x: ' ' if x == '1' else x)
        new_jrnls1 = df1.loc[df1['journal'].str.contains('|'.join(jrnls)) == True]
        new_jrnls2 = new_jrnls1.sort_values(by=['eponym'],ascending=True)
        if not jrnls == None:
            J_options = st.selectbox('3rd) Search eponyms from selected journals:',
                                  new_jrnls2['eponym'].unique(), format_func=lambda x: ' ' if x == '1' else x)

            df_ep_info2 = new_jrnls1[new_jrnls1['eponym'].str.match(J_options)]
            journal = df_ep_info2['journal_name'].to_string(index=False)
            if not df_ep_info2['journal_name'].isnull().all():
                st.write(journal, unsafe_allow_html=True)
                
            if not df_ep_info2['year_str'].isnull().all():
                st.write('_When_:',df_ep_info2['year_str'].to_string(index=False))

            if not df_ep_info2['Who'].isnull().all():
                st.write('_Authors_:',df_ep_info2['Who'].to_string(index=False))


    if ScreenSize == "Desktop / Laptop / Tablet":
        types = st.radio('2nd) Choose specialties:',["All","Selected",])

        if types == 'All':
            min_yrs, max_yrs = st.slider("3rd) Choose time window:", 1700, 2030, [1700, 2021])
            url_J = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/Eponyms4python_Lite4Journals.csv'
            dfY = pd.read_csv(url_J)
            dfY1 = dfY.dropna()
            dfY1["JOURNALS"] = "JOURNALS"
            dfT = dfY1.sort_values(by=['year'],ascending=True)
            time_df = dfT.loc[(dfT['year'] >= min_yrs) & (dfT['year'] <= max_yrs)]
            time_spec_df = time_df['specialty'].dropna()
            string = time_spec_df.str.cat(sep=',')
            splits = string.split(",")
            S = set(splits)
            T = np.array(list(S)).astype(object)
            U = np.sort(T)
            figJDLT = px.sunburst(time_df,path=['JOURNALS','journal_short','year','eponym'],
                              #values='Log10 Google hits',
                                  color='Log2 Google hits',hover_data=['eponym'],
                              color_continuous_scale='RdBu'
                                  )
            figJDLT.update_layout(margin=dict(l=0, r=0, t=0, b=0),width=680,height=500)
            figJDLT.update_traces(hovertemplate=None,hoverinfo='skip') 
            st.write(figJDLT)

       #     jrnls = st.multiselect('2nd) Select journals:',options=list(U), format_func=lambda x: ' ' if x == '1' else x)
       #     new_jrnls1 = df1.loc[df1['journal'].str.contains('|'.join(jrnls)) == True] #str.contains('|'.join(jrnls)) == True]
       #     new_jrnls2 = new_jrnls1.sort_values(by=['eponym'],ascending=True)
       #     if not jrnls == None:
       #         J_options = st.selectbox('Eponyms in journals:',
       #                           new_jrnls2['eponym'].unique(), format_func=lambda x: ' ' if x == '1' else x)
       #         df_ep_info2 = new_jrnls1[new_jrnls1['eponym'].str.match(J_options)]
       #         journal = df_ep_info2['journal_name'].to_string(index=False)
       #     if not df_ep_info2['journal_name'].isnull().all():
       #         st.write(journal, unsafe_allow_html=True) 
       #     if not df_ep_info2['year_str'].isnull().all():
       #         st.write('_When_:',df_ep_info2['year_str'].to_string(index=False))
       #     if not df_ep_info2['Who'].isnull().all():
       #        st.write('_Authors_:',df_ep_info2['Who'].to_string(index=False))

        if types == 'Selected':
            url_J = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/Eponyms4python_Lite4Journals.csv'
            dfY = pd.read_csv(url_J)
            dfY1 = dfY.dropna()
            dfY1["JOURNALS"] = "JOURNALS"
            df2 = dfY1.sort_values(by=['year'],ascending=True)
            spec_df = df2['specialty'].dropna()
            string = spec_df.str.cat(sep=',')
            splits = string.split(",")
            S = set(splits)
            T = np.array(list(S)).astype(object)
            U = np.sort(T)
            journal_spec = st.multiselect('Specilaties of interest - pick and choose',options=list(U),
                           format_func=lambda x: ' ' if x == '1' else x,
                           default=['Anaesthetics','Bariatrics','Breast','Cardiothoracics','Colorectal','Emergency Surgery','Endocrine','ENT',
                                    'General Surgery','Gynaecology','HPB','Hernia','Laparoscopic Surgery','Maxillofacial','Neurosurgery',
                                    'Oesophagogastric','Orthopaedics','Paediatrics','Plastics','Transplant','Trauma','Urology','Vascular',]
                                          )
            min_yrs, max_yrs = st.slider("3rd) Choose time window:", 1700, 2030, [1735, 2021])
            new_jrnls1 = df2.loc[df2['specialty'].str.contains('|'.join(journal_spec)) == True]
            new_jrnls1T = new_jrnls1.loc[(new_jrnls1['year'] >= min_yrs) & (new_jrnls1['year'] <= max_yrs)]
            new_jrnls2T = new_jrnls1T.sort_values(by=['eponym'],ascending=True)
            new_jrnls2T["JOURNALS"] = "JOURNALS"
            if not journal_spec == None:
                figJDLT = px.sunburst(new_jrnls2T,path=['JOURNALS','journal_short','year','eponym'],
                      #values='Log10 Google hits',
                                      color='Log2 Google hits',hover_data=['eponym'],
                      color_continuous_scale='rdbu', #inferno,thermal,Magma,Cividis,deep,Viridis,icefire,ylgnbu,'portland','agsunset'
                              )
                figJDLT.update_layout(margin=dict(l=0, r=0, t=0, b=0),
                                      width=680,height=500)
                figJDLT.update_traces(hovertemplate=None, hoverinfo='skip')
                st.write(figJDLT)



       #     df["JOURNALS"] = "JOURNALS"
       #     dfX = dfY.head(1)
       #     new_jrnls4 = pd.concat([dfX,new_jrnls2]).reset_index(drop=True)
       #     dfZ2 = new_jrnls4.sort_values(by=['journal'],ascending=True)
       #     dfZ3 = dfZ2['journal'].dropna()
       #     stringZ = dfZ3.str.cat(sep=',')
       #     splitsZ = stringZ.split(",")
       #     SZ = set(splitsZ)
       #     TZ = np.array(list(SZ)).astype(object)
       #     UZ = np.sort(TZ)

       #     jrnlz = st.multiselect('Select journals:',options=list(UZ), format_func=lambda x: ' ' if x == '1' else x)
       #     new_jrnlz1 = dfZ2.loc[dfZ2['journal'].str.contains('|'.join(jrnlz)) == True]
       #     new_jrnlz2 = new_jrnlz1.sort_values(by=['eponym'],ascending=True)
       #     if not jrnlz == None:
       #         J_options = st.selectbox('Eponyms in journals:',
       #                           new_jrnlz2['eponym'].unique(), format_func=lambda x: ' ' if x == '1' else x)
        #        df_ep_info2 = new_jrnlz1[new_jrnlz1['eponym'].str.match(J_options)]
        #        journal = df_ep_info2['journal_name'].to_string(index=False)
        #        if not df_ep_info2['journal_name'].isnull().all():
        #            st.write(journal, unsafe_allow_html=True)
        #        if not df_ep_info2['year_str'].isnull().all():
        #           st.write('_When_:',df_ep_info2['year_str'].to_string(index=False))
        #        if not df_ep_info2['Who'].isnull().all():
        #            st.write('_Authors_:',df_ep_info2['Who'].to_string(index=False))


#----------------------------------------------------------------------------------------------#
#                                                                                              #
#  People (6)                                                                                  #
# ::: Handles                                                                                  #                                                                                              #
#                                                                                              #
#----------------------------------------------------------------------------------------------#
def exp_people():

    #Data read and arrange
    url = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/Eponyms4python_Lite.csv'
    df = pd.read_csv(url, dtype={'PMID':str,'Year':int})
    dfY1 = df.sort_values(by=['Surname'],ascending=True)
    who = st.selectbox('Selected person:', dfY1['Who'].unique(),
                           format_func=lambda x: ' ' if x == '1' else x) #use '1's for first row in CSV file to create empty row

    if not who == None:
        df_who_info = dfY1[dfY1['Who'].str.match(who)]

        if not df_who_info['Who_B'].isnull().all():
            st.write('_Name_:',df_who_info['Who_B'].to_string(index=False))
        
        if not df_who_info['Where'].isnull().all():
            st.write('_Where_:',df_who_info['Where'].to_string(index=False))

    df1 = pd.read_csv(url, dtype={'PMID':str,'Year':int})
    df2 = df1.sort_values(by=['Year'],ascending=True)
    mapbox_access_token = 'pk.eyJ1IjoiYWpoYXllczgzIiwiYSI6ImNrY2pqM2lvMDB4Z24ydG8zdDl0NTYwbTUifQ.2DKVfTAaE77XAXMpDeq_Pg'
    site_lat = df_who_info['Lat_A1']            #df3['Lat_A1']                
    site_lon = df_who_info['Long_A1']           #df3['Long_A1']
    text = df_who_info['Who'] + ', ' + df_who_info['CityOfEponym_A1'] + ', ' + df_who_info['Year'].astype(str)
    locations_name = df_who_info['Eponym_easy']
    figG3 = go.Figure()
    figG3.add_trace(go.Scattermapbox(
        lat=df_who_info['Lat_A1'],lon=df_who_info['Long_A1'],mode='markers',
                marker=go.scattermapbox.Marker(size=9,color='yellow',opacity=0.9),
                text=text,hoverinfo='text',))
    figG3.update_layout(
                autosize=True,hovermode='closest',showlegend=False,width=350,height=260,
                mapbox=dict(accesstoken=mapbox_access_token,
                            bearing=0,center=dict(lat=40.0,lon=0.0),
                            pitch=5,zoom=-0.45,style='dark'))
    figG3.update_layout(margin=dict(l=2, r=2, t=0, b=0))
    st.write(figG3)

#----------------------------------------------------------------------------------------------#
#                                                                                              #
#  Exam (8)                                                                                    #
# ::: Handles the                                                                              #                                                                                              #
#                                                                                              #
#----------------------------------------------------------------------------------------------#
def exp_exam():
    st.subheader("Often Encountered Eponyms in Surgical Exams") 
    url = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/Eponyms4python_Lite.csv'
    df = pd.read_csv(url, dtype={'PMID':str,'Year':int})
    df1 = df['ExamSpec'].dropna()
    string = df1.str.cat(sep=',')
    splits = string.split(",")
    S = set(splits)
    T = np.array(list(S)).astype(object)
    U = np.sort(T)
    exams = st.multiselect('Choose Specialties of Interest:',options=list(U),
                           format_func=lambda x: ' ' if x == '1' else x,
                           default=[#'All Specialties',
                                    'Academic','Anaesthetics','Bariatrics','Breast','Cardiothoracics',
                                    'Colorectal','Endocrine','ENT','General Surgery','Gynaecology',
                                    'HPB','Hernia','Maxillofacial',
                                    'Neurosurgery','Oesophagogastric','Orthopaedics',
                                    'Paediatrics','Plastics','Transplant',
                                    'Trauma','Urology','Vascular',
                                    ])
    new_exams1 = df.loc[df['ExamSpec'].str.contains('|'.join(exams)) == True]
    new_exams2 = new_exams1.sort_values(by=['Eponym'],ascending=True)

    if not exams == None:
        Ex_options = st.selectbox('Eponyms:',
                                  new_exams2['Eponym_easy'].unique(), format_func=lambda x: ' ' if x == '1' else x)

        df_ep_info2 = new_exams1[new_exams1['Eponym_easy'].str.match(Ex_options)]
            
        if not df_ep_info2['Year_str'].isnull().all():
            st.write('_When_:',df_ep_info2['Year_str'].to_string(index=False))

        if not df_ep_info2['Who_B'].isnull().all():
            st.write('_Who_:',df_ep_info2['Who_B'].to_string(index=False))

#----------------------------------------------------------------------------------------------#
#                                                                                              #
#  Speciality (9)                                                                              #
# ::: Handles the                                                                              #                                                                                              #
#                                                                                              #
#----------------------------------------------------------------------------------------------#
def exp_spec():
    st.subheader("Find Eponyms by Speciality")
    url = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/Eponyms4python_Lite.csv'
    df = pd.read_csv(url, dtype={'PMID':str,'Year':int})
    df1 = df['Topic'].dropna()
    string = df1.str.cat(sep=',')
    splits = string.split(",")
    S = set(splits)
    T = np.array(list(S)).astype(object)
    U = np.sort(T)
    special = st.multiselect('Speciality:',options=list(U),
                           format_func=lambda x: ' ' if x == '1' else x,
                           default=['Academic','Anaesthetics','Bariatrics',
                                    'Breast','Colorectal','Cardiothoracics',
                                    'Emergency Surgery','ENT','Endocrine','General Surgery','Gynaecology',
                                    'Hernia','HPB','Laparoscopic Surgery','Maxillofacial','Neurosurgery',
                                    'Oesophagogastric','Orthopaedics',
                                    'Paediatrics','Plastics','Transplant',
                                    'Trauma','Urology','Vascular',
                                    ])
    new_special1 = df.loc[df['Topic'].str.contains('|'.join(special)) == True]
    new_special2 = new_special1.sort_values(by=['Eponym'],ascending=True)

    if not special == None:
        Spec_options = st.selectbox('Related eponyms:',
                                  new_special2['Eponym_easy'].unique(), format_func=lambda x: ' ' if x == '1' else x)   #selectbox

        df_ep_info2 = new_special1[new_special1['Eponym_easy'].str.match(Spec_options)]
        ep_yr = df_ep_info2['Year'].to_string(index=False)

        if not df_ep_info2['Who_B'].isnull().all():
            st.write('_Who_:',df_ep_info2['Who_B'].to_string(index=False))

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

        if not df_ep_info2['Who_B'].isnull().all():
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
#  Disease (9)                                                                                 #
# ::: Handles the                                                                              #                                                                                              #
#                                                                                              #
#----------------------------------------------------------------------------------------------#
def exp_dis():

    url = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/Eponyms4python_Lite.csv'
    df = pd.read_csv(url, dtype={'PMID':str,'Year':int})
    df1 = df['Disease'].dropna()
    string = df1.str.cat(sep=',')
    splits = string.split(",")
    S = set(splits)
    T = np.array(list(S)).astype(object)
    U = np.sort(T)
    disease = st.multiselect('Choose disease:', options=list(U),
                             format_func=lambda x: ' ' if x == '1' else x,)
    new_dis1 = df.loc[df['Disease'].str.contains('|'.join(disease)) == True]
    new_dis2 = new_dis1.sort_values(by=['Eponym'],ascending=True)


    if not disease == None:
        Dis_options = st.selectbox('Related eponyms:',
                                   new_dis2['Eponym_easy'].unique(),
                               format_func=lambda x: ' ' if x == '1' else x)   #selectbox

        df_ep_info2 = new_dis1[new_dis1['Eponym_easy'].str.match(Dis_options)]
        ep_yr = df_ep_info2['Year'].to_string(index=False)

        if not df_ep_info2['Who_B'].isnull().all():
            st.write('_Who_:',df_ep_info2['Who_B'].to_string(index=False))

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

        if not df_ep_info2['Who_B'].isnull().all():
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
#  A to Z (10)                                                                                 #
# ::: Handles the                                                                              #                                                                                              #
#                                                                                              #
#----------------------------------------------------------------------------------------------#
def exp_A2Z():
    st.subheader("Surgical eponym database")
    types = st.radio('1st) Choose eponym types:',["All","Selected",])

    if types == 'All':
        url = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/Eponyms4python_Lite.csv'
        df1 = pd.read_csv(url, dtype={'PMID':str,'Year':int})
        df2 = df1.sort_values(by=['Eponym'],ascending=True)

        min_yrs, max_yrs = st.slider("2nd) Optional - Define a time window:", 1550, 2050, [1550, 2021])

        new_1T = df2.loc[(df2['Year'] >= min_yrs) & (df2['Year'] <= max_yrs)]
        new_2T = new_1T.sort_values(by=['Eponym'],ascending=True)
    
        options = st.selectbox('', new_2T['Eponym_easy'].unique()) #format_func=lambda x: ' ' if x == '1' else x)
        #df_ep_info = new_2T[new_2T['Eponym_easy'].str.match(options)]

        #if not df_ep_info['Who'].isnull().all():
        #    st.markdown("---")
        #    st.write('*_Who_*:', df_ep_info['Who_B'].to_string(index=False))

        #    ep_yr = df_ep_info['Year'].to_string(index=False)
        #    if not df_ep_info['Year'].isnull().all():
        #        st.write('*_When_*:', df_ep_info['Year_str'].to_string(index=False))

        #    if not df_ep_info['Where'].isnull().all():
        #       st.write('*_Where_*:', df_ep_info['Where'].to_string(index=False))

    if types == 'Selected':
        url = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/Eponyms4python_Lite.csv'
        df1 = pd.read_csv(url, dtype={'PMID':str,'Year':int})
        df2 = df1.sort_values(by=['Year'],ascending=True)
        spec_df = df2['Type'].dropna()
        string = spec_df.str.cat(sep=',')
        splits = string.split(",")
        S = set(splits)
        T = np.array(list(S)).astype(object)
        U = np.sort(T)
        journal_spec = st.multiselect("Eponym types:",options=list(U),
                           format_func=lambda x: ' ' if x == '1' else x,
                           default=['Anatomy','Incisions','Instruments','Operations','Pathology','Physiology',
                                    'Positions','Scores','Signs','Statistics','Surgical Maneuvers & Techniques',
                                    'Syndromes','Trials',])

        min_yrs, max_yrs = st.slider("2nd) Optional - Define a time window:", 1550, 2050, [1550, 2021])
        new_jrnls1 = df2.loc[df2['Type'].str.contains('|'.join(journal_spec)) == True]
        new_jrnls2 = new_jrnls1.sort_values(by=['Year'],ascending=True)
        new_jrnls2T = new_jrnls2.loc[(new_jrnls2['Year'] >= min_yrs) & (new_jrnls2['Year'] <= max_yrs)]
        new_jrnls3T = new_jrnls2T.sort_values(by=['Eponym'],ascending=True)
    
        options = st.selectbox('Begin typing here:', new_jrnls3T['Eponym_easy'].unique(), format_func=lambda x: ' ' if x == '1' else x)
        df_ep_info = new_jrnls3T[new_jrnls3T['Eponym_easy'].str.match(options)]

        if not df_ep_info['Who'].isnull().all():
            st.write('*_Who_*:', df_ep_info['Who_B'].to_string(index=False))

            ep_yr = df_ep_info['Year'].to_string(index=False)
            if not df_ep_info['Year'].isnull().all():
                st.write('*_When_*:', df_ep_info['Year_str'].to_string(index=False))

            if not df_ep_info['Where'].isnull().all():
                st.write('*_Where_*:', df_ep_info['Where'].to_string(index=False))



#-------------------------------------------------------------------------------------------#
if __name__ == "__main__":
    main()
