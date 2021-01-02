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
    st.sidebar.subheader('Navigator')
    page = st.sidebar.radio('',#'Go to',
                            ["SurgicalEps Explorer",
                             "App Design Team"])

    if page ==   "SurgicalEps Explorer":   show_explore()
    elif page == "App Design Team":        show_the_app_team()
    


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
    st.markdown('''To meet these aims, a company called **Excision** was founded in 2020, and **SurgicalEps** Web App was the first major project.''',unsafe_allow_html=True)

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
        st.markdown('''Anne is Specialty Training Registrar in Edinburgh with interests in Upper GI, Hernias and Emergency General Surgery.
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
    st.sidebar.subheader('SurgicalEps Explorer')
    exp = st.sidebar.radio('',#'Select',
                                ["About",
                                 "By Disease",
                                 "By Journal",
                                 "By Operation",
                                 "By World Maps",
                                 "Exam Favourites",
                                 "Full Database",
                                 ])
    if   exp == "About":           exp_about()             #1
    elif exp == "By Disease":      exp_dis()               #2
    elif exp == "By Journal":      exp_journals()          #3
    elif exp == "By Operation":    exp_operation()         #4
    elif exp == "By World Maps":   exp_geo()               #5         
    elif exp == "Exam Favourites": exp_exam()              #6
    elif exp == "Full Database":   exp_A2Z()               #7
    
#----------------------------------------------------------------------------------------------#
#                                                                                              #
#  About (1)                                                                                   #
# ::: Handles                                                                                  #                                                                                              
#                                                                                              #
#----------------------------------------------------------------------------------------------#

def exp_about():
    st.markdown(
        """<style type="text/css" media="screen">.hovertext text {font-size: 20px !important;}</style>""",unsafe_allow_html=True)
#Page
    st.write('''_UNDER CONSTRUCTION_''')
    st.markdown('''# SurgicalEps''')
    st.markdown('''_An Educational Web App from Excision Ltd_''')
    #st.markdown("---")
    st.subheader('Introduction')
    st.markdown(' ')
    #st.markdown('''<br><span style="font-size:14pt;font-weight:bold;color:black;text-decoration:underline;">Introduction</span>''', unsafe_allow_html=True)
    st.write('''There are a hundreds of eponyms used in daily surgical practice.
    We hope that you will find this App helpful in understanding what these terms mean, their history,
    and how they relate to one another. We include direct links to primary papers, as well as useful webpages in Wikipedia, Whonamedit?, ICD-11 and TeachMeSurgery.''')
    #st.markdown("---")
    st.subheader('Using This App')
    st.write(' ')
    st.markdown('''<span style="font-size:12pt;color:black;font-weight:bold;">By Disease:</span><span style="font-size:12pt;color:black;"> Here you can search eponyms related to a disease.</span>''',unsafe_allow_html=True)
    st.markdown('''<span style="font-size:12pt;color:black;font-weight:bold;">By Journal:</span><span style="font-size:12pt;color:black;"> In this section, journals can be selected tofind which eponyms can be traced to their of publication archives. Explorethrough time using the time travel function.</span>''',unsafe_allow_html=True)
    st.markdown('''<span style="font-size:12pt;color:black;font-weight:bold;">By Operation:</span><span style="font-size:12pt;color:black;"> Here you can choose an operation type (eg. Oesophagectomy), and then access all the common eponyms related to that procedure.</span>''',unsafe_allow_html=True)
    st.markdown('''<span style="font-size:12pt;color:black;font-weight:bold;">By World Maps:</span><span style="font-size:12pt;color:black;"> Choose a region of the world to find eponyms. Select a continent, country or famous city.</span>''',unsafe_allow_html=True)
    st.markdown('''<span style="font-size:12pt;color:black;font-weight:bold;">Exam Favourites:</span><span style="font-size:12pt;color:black;"> Select from those often found in exams.Explore by speciality.</span>''',unsafe_allow_html=True)
    st.markdown('''<span style="font-size:12pt;color:black;font-weight:bold;">Full Database:</span><span style="font-size:12pt;color:black;"> Choose from anatomical structures, incisions, surgical instruments, operations, pathology, physiology, patient positioning, clinical scores or signs, statistical tests, surgical maneuvers & techniques, syndromes, or research trials.</span>''',unsafe_allow_html=True)
    #st.markdown("---")
    st.subheader('Who Is This App For?')
    st.markdown(' ')
    st.write('''Doctors, nurses, secretaries, theatre staff, physician assistants, allied health professionals and students.''')
    #st.markdown("---")
    st.subheader('Disclaimer')
    st.markdown(' ')
    st.write('''Educational purposes.''')
    st.sidebar.markdown("---")
    st.sidebar.markdown('''**Latest News**''')
    st.sidebar.info("App will be launched Jan 2021")


#----------------------------------------------------------------------------------------------#
#                                                                                              #
#  Disease (2)                                                                                 #
# ::: Handles the                                                                              #                                                                                              #
#                                                                                              #
#----------------------------------------------------------------------------------------------#
def exp_dis():
    st.subheader("Find eponyms related to selected diseases") 
    url = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/Eponyms4python_Lite.csv'
    df = pd.read_csv(url, dtype={'PMID':str,'Year':int})
    df1 = df['Disease'].dropna()
    string = df1.str.cat(sep=',')
    splits = string.split(",")
    S = set(splits)
    T = np.array(list(S)).astype(object)
    U = np.sort(T)
    disease = st.multiselect('1st) Choose a disease:', options=list(U),
                             format_func=lambda x: ' ' if x == '1' else x,
                             )
    new_dis1 = df.loc[df['Disease'].str.contains('|'.join(disease)) == True]
    new_dis2 = new_dis1.sort_values(by=['Eponym'],ascending=True)


    if not disease == None:
        Dis_options = st.selectbox('2) Search list of related eponyms:',
                                   new_dis2['Eponym_easy'].unique(),
                               format_func=lambda x: ' ' if x == '1' else x
                                   )   #selectbox

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
#  Journals (3)                                                                                #
# ::: Handles                                                                                  #                                                                                              #
#                                                                                              #
#----------------------------------------------------------------------------------------------#

def exp_journals():
    #st.markdown('''[Advert space for Google AdSense4]''')
    st.subheader("Find eponyms that can be traced to journal archives") 
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
                              color_continuous_scale='rdbu',#'RdBu'
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
#  Surgical Operations (4)                                                                     #
# ::: Handles                                                                                  #                                                                                              #
#                                                                                              #
#----------------------------------------------------------------------------------------------#

def exp_operation():
    st.markdown(
        """<style type="text/css" media="screen">.hovertext text {font-size: 20px !important;}
        </style>""",unsafe_allow_html=True,)

    st.subheader("Find eponyms related to selected operations") 
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
    eponymByOp = st.multiselect('1st) Select from operations:',options=list(U), format_func=lambda x: ' ' if x == '1' else x)
    new_df = df1.loc[df1['Operation'].str.contains('|'.join(eponymByOp)) == True]
    new_df2 = new_df.sort_values(by=['Eponym'],ascending=True)
 
    if not eponymByOp == None:
        Op_options = st.selectbox('2) Search list of related eponyms:',
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
#  Geographical Origins (5)                                                                    #
# ::: Handles the                                                                              #                                                                                              #
#                                                                                              #
#----------------------------------------------------------------------------------------------#

def exp_geo():
    st.markdown(
        """<style type="text/css" media="screen">div[role="listbox"] ul {height:55px}
        </style>""",unsafe_allow_html=True,)
    st.subheader("Find eponyms related to their geographical origins") 
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


        st.subheader("Click on geographical locations to zoom in, and in the center to pan out.") 
        time_df["WORLD"] = "WORLD"
        figJDLT = px.sunburst(time_df,path=['WORLD',
            'Continent_A1','CountryOfEponym_A1','CityOfEponym_A1','Eponym_easy'],
                              #values='Log10_GxP',
                              color='Log10_GxP',
                              hover_data=['Eponym'],
                              color_continuous_scale='viridis',#'RdBu'
                                  )
        figJDLT.update_layout(margin=dict(l=0, r=0, t=0, b=0),width=360,height=350)
        figJDLT.update_traces(hovertemplate=None,hoverinfo='skip') 
        st.write(figJDLT)


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
        journal_spec = st.multiselect("2nd) Optional - enter specific specialties. Default 'Choose an option' shows all.",options=list(U),
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
        st.markdown('''<span style="font-size:10pt;color:black;">Tip: If map does not locate correctly, press 'Zoom in' on the top right corner.</span>''',
                unsafe_allow_html=True)
        #st.markdown("---")
        st.subheader("Click on geographical locations to zoom in, and in the center to pan out.") 
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

        st.markdown("---")
        new_geo3T = new_geo2T.sort_values(by=['Eponym'],ascending=True)
        options = st.selectbox('5th) Type here to get details of particular eponym:', new_geo3T['Eponym_easy'].unique(), format_func=lambda x: ' ' if x == '1' else x)
        df_ep_info = new_geo3T[new_geo3T['Eponym_easy'].str.match(options)]

        if not df_ep_info['Who'].isnull().all():
            st.write('*_Who_*:', df_ep_info['Who_B'].to_string(index=False))

            ep_yr = df_ep_info['Year'].to_string(index=False)
            if not df_ep_info['Year'].isnull().all():
                st.write('*_When_*:', df_ep_info['Year_str'].to_string(index=False))

            if not df_ep_info['Where'].isnull().all():
                st.write('*_Where_*:', df_ep_info['Where'].to_string(index=False))


#----------------------------------------------------------------------------------------------#
#                                                                                              #
#  Exam (6)                                                                                    #
# ::: Handles the                                                                              #                                                                                              #
#                                                                                              #
#----------------------------------------------------------------------------------------------#
def exp_exam():
    st.subheader("Eponyms often encountered in surgical exams") 
    url = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/Eponyms4python_Lite.csv'
    df = pd.read_csv(url, dtype={'PMID':str,'Year':int})
    df1 = df['ExamSpec'].dropna()
    string = df1.str.cat(sep=',')
    splits = string.split(",")
    S = set(splits)
    T = np.array(list(S)).astype(object)
    U = np.sort(T)
    exams = st.multiselect('1st) Choose specialties of interest:',options=list(U),
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
        Ex_options = st.selectbox('2) Search list of eponyms found in exams relevant to selected specialties:',
                                  new_exams2['Eponym_easy'].unique(), format_func=lambda x: ' ' if x == '1' else x)

        df_ep_info2 = new_exams1[new_exams1['Eponym_easy'].str.match(Ex_options)]
            
        if not df_ep_info2['Year_str'].isnull().all():
            st.write('_When_:',df_ep_info2['Year_str'].to_string(index=False))

        if not df_ep_info2['Who_B'].isnull().all():
            st.write('_Who_:',df_ep_info2['Who_B'].to_string(index=False))


#----------------------------------------------------------------------------------------------#
#                                                                                              #
#  A to Z (7)                                                                                 #
# ::: Handles the                                                                              #                                                                                              #
#                                                                                              #
#----------------------------------------------------------------------------------------------#
def exp_A2Z():
    st.subheader("Search the full SurgicalEps database and filter by eponym type")
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
