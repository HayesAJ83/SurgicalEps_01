#Copyright [2021] [EXCISION LIMITED]
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

#-------------------------------------------------------------------------------------------------#
#                                                                                                 #
#  Main                                                                                           #
# ::: Handles the navigation / routing and data loading / caching                                 #                                                                                              #
#                                                                                                 #
#-------------------------------------------------------------------------------------------------#

def main():
    #components.iframe("https://en.wikipedia.org/wiki/Crohn%27s_disease", scrolling=True)
    st.sidebar.write('''_Click **X** in top right to hide sidebar_''')
    st.sidebar.subheader('Navigator')
    page = st.sidebar.radio('Go to:',
                            ["Surgical Names App",
                             "Design Team",])

    if page ==   "Surgical Names App":   show_explore()
    elif page == "Design Team":        show_the_app_team()

#-------------------------------------------------------------------------------------------------#
#                                                                                                 #
#  About the team                                                                                 #
# :::                                                                                             #
#                                                                                                 #
#-------------------------------------------------------------------------------------------------#
def show_the_app_team():
    st.write('''_To show sidebar, click **>** in top left_''')
    st.title("App Design Team")
    st.markdown('''The team consists of a group of General Surgeons based in Edinburgh who are
                motivated to develop software to improve surgical **data systems**,
                **research** and **education**.''')
    st.markdown('''To meet these aims, a company called **Excision** was founded in 2020, and
                **Surgical Names** web app was the first major project.''',unsafe_allow_html=True)

    st.sidebar.markdown("---")
    st.sidebar.markdown('''**Contact details**''')
    st.sidebar.info('''Comments, queries and suggestions welcome: surgicalnames@gmail.com''')
    
    st.subheader("Project Lead & App Developer")
    with st.beta_expander('Alastair Hayes'):
        col1, col2, col3 = st.beta_columns(3)
        image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Alastair_Hayes.png'
        col1.image(image, width=100);
        col2.write('''Alastair is a General Surgery Specialty Training Registrar in Edinburgh with
                    interests in Upper GI & Endocrine. His qualifications include FRCSEd(Gen) & PhD.''')
        col3.write('''His main coding language is Python & is working to develop software solutions for clinical
                    data system problems, research & education in surgical practice.''')

    st.subheader("Associate Project Lead")
    with st.beta_expander('Anne Ewing'):
        st.markdown('''Anne is a General Surgery Specialty Training Registrar in Edinburgh with interests in Upper
                    GI & Hernias. She is passionate about surgical teaching and outside work Anne is a competitive athlete.''')   

    st.markdown("---")
    st.subheader("Acknowledgements")
    with st.beta_expander('Websites'):
        st.markdown('''
                    [Google](https://www.google.com/search/howsearchworks/?fg=1),
                    [Mapbox](https://www.mapbox.com),
                    [Pandas](https://pandas.pydata.org),
                    [Plotly](https://plotly.com/python/),
                    [PubMed&reg;](http://www.ncbi.nlm.nih.gov/pubmed),
                    [Streamlit](https://www.streamlit.io)''')

    with st.beta_expander('People'):
        st.markdown('''Gillian  - Educational Lead Theatres, Royal Infirmary of Edinburgh [Instrument Pics]''') 
        st.markdown('''Andrew De Beaux - Consultant General Surgeon, Royal Infirmary of Edinburgh [Hernia Info]''') 

#-------------------------------------------------------------------------------------------------#
#                                                                                                 #
#  Explorer                                                                                       #
# ::: Handles the navigation                                                                      #                                                                                              #
#                                                                                                 #
#-------------------------------------------------------------------------------------------------#
def show_explore():
    st.sidebar.subheader('Surgical Names App')
    exp = st.sidebar.radio('Explore:',
                                ["Home",
                                 "A to Z - by Specialty",
                                 "By Disease or Symptom",
                                 "By Journal",
                                 "By Operation",
                                 "By World Maps",
                                 "Categories",
                                 "Exam Favourites",
                                 "Teaching Tool",
                                 ])
    if   exp == "Home":                     exp_about()         #1
    elif exp == "A to Z - by Specialty":    exp_A2Z()           #2
    elif exp == "By Disease or Symptom":    exp_dis()           #3
    elif exp == "By Journal":               exp_journals()      #4
    elif exp == "By Operation":             exp_operation()     #5
    elif exp == "By World Maps":            exp_geo()           #6         
    elif exp == "Exam Favourites":          exp_exam()          #7
    elif exp == "Categories":               exp_cats()          #8
    elif exp == "Teaching Tool":            exp_teach()         #9
    
#-------------------------------------------------------------------------------------------------#
#                                                                                                 #
#  About (1)                                                                                      #
# ::: Handles                                                                                     #                                                                                              
#                                                                                                 #
#-------------------------------------------------------------------------------------------------#
def exp_about():

    st.write('''_To show sidebar, click **>** in top left_''')
    st.markdown('''# www.SurgicalNames.com''')
    st.markdown('''_An Educational Web App from Excision Ltd_''')
    st.markdown("---")
    with st.beta_expander('Introduction'):
        st.write('''An '_eponymous_' term is one which is derived from
                    somebody's name. Famous examples used in surgical practice include _Graves disease_,
                    _McBurney's point_, & _Strasberg's critical view of safety_. When used correctly, eponymous
                    terms can enhance communication, shared understanding & can help with decision-making.''')

        st.write('''Until now, to better understand these useful terms, we have been limited dictionaries and
                    encylopedias which index items alphabetically. But because of the rich meaning and
                    historical background of each term, we imagined a better resource to catalogue & learn
                    these fascinating terms.''')

        st.write('''With the development of Machine Learning tools, and in particular the excellent format
                    by [Streamlit](https://www.streamlit.io), we have **multi-indexed surgical eponymous terms
                    in intuitive & interactive ways**.''')

        st.write('''The functions built into surgicalnames.com are aimed at simulating how we think of terminology
                    (eg. by disease or operation), to help busy people quickly master a deep understanding
                    of terms related to their work.''')

        st.write('''You will find several **interactive visualizations** which we hope you will find enjoyable
                    & help you retain information for longer. Where possible, you will find **links to
                    original papers & related webpages**.''')

        st.write('''This project, surgicalnames.com, is under continuous development with a growing database of terms
                    & evolving functionality as we develop the software.''')
        st.markdown("---")
        
    with st.beta_expander('Quick Start'):
        st.write('''Navigate with the sidebar on the left. If sidebar is not shown, **click > in top left** to display.
                    Then explore using sidebar options:''')
           
        st.markdown('''<span style="font-size:12pt;color:black;font-weight:bold;">A to Z:</span>
                   <span style="font-size:12pt;color:black;">Search by name and filter by specialty.</span>''',
                   unsafe_allow_html=True)
        st.markdown('''<span style="font-size:12pt;color:black;font-weight:bold;">By Disease or Symptom:</span>
                   <span style="font-size:12pt;color:black;"> Here you can find eponyms related
                   to conditions of interest.</span>''',unsafe_allow_html=True)
        st.markdown('''<span style="font-size:12pt;color:black;font-weight:bold;">By Journal:</span>
                   <span style="font-size:12pt;color:black;"> In this section, journals can be
                   selected to find which eponyms can be traced to their of publication archives.
                   Explore through time using the time travel function.</span>''',
                   unsafe_allow_html=True)
        st.markdown('''<span style="font-size:12pt;color:black;font-weight:bold;">By Operation:</span>
                   <span style="font-size:12pt;color:black;"> Here you can choose an operation type
                   (eg. Oesophagectomy), and then access all the common eponyms related to that
                   procedure.</span>''',unsafe_allow_html=True)
        st.markdown('''<span style="font-size:12pt;color:black;font-weight:bold;">By World Maps:</span>
                   <span style="font-size:12pt;color:black;"> Choose a region of the world to find
                   local eponyms. Select a continent, country or city.</span>''',
                   unsafe_allow_html=True)
        st.markdown('''<span style="font-size:12pt;color:black;font-weight:bold;">Categories:</span>
                   <span style="font-size:12pt;color:black;">Choose from anatomy,
                   incisions, surgical instruments, operations, pathology, physiology, patient
                   positioning, eponymous fluids, clinical scores or signs, statistical tests, surgical
                   maneuvers & techniques, syndromes, doctrines & rules or research trials.
                   </span>''',unsafe_allow_html=True)
        st.markdown('''<span style="font-size:12pt;color:black;font-weight:bold;">Exam Favourites:
                   </span><span style="font-size:12pt;color:black;"> Select from those often found
                   in exams & filter by speciality.</span>''',unsafe_allow_html=True)
        st.markdown('''<span style="font-size:12pt;color:black;font-weight:bold;">Teaching Tool:</span>
                   <span style="font-size:12pt;color:black;">Choose from Bedside, Classroom or
                   Operating Room modes.</span>''',unsafe_allow_html=True)
        st.markdown("---")

    with st.beta_expander('Audience'):
        st.write('''We build this app with the aim of helping people from a variety of backgrounds who would
                    encounter these eponymous terms, including doctors, nurses, secretaries, operating room staff,
                    physician assistants, allied health professionals & students.''')
        st.markdown("---")

    with st.beta_expander('Disclaimer'):
        st.write('''The information you find on this surgicalnames.com site is limited to educational purposes only.
                    Although many of these eponymous terms are used in daily practice, we do not comment on their
                    accuracy or value, as this is beyond the scope of this app.''')
        st.markdown("---")

    st.markdown("---")
    st.write('''Copyright © 2021 Excision Ltd. All rights reserved.''')
    st.sidebar.markdown("---")
    st.sidebar.markdown('''**Latest News**''')
    st.sidebar.info("App will be launched April 2021")

#-------------------------------------------------------------------------------------------------#
#                                                                                                 #
#  A to Z (2)                                                                                     #
# ::: Handles the                                                                                 #                                                                                              #
#                                                                                                 #
#-------------------------------------------------------------------------------------------------#

import streamlit.components.v1 as components
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
import time


def exp_A2Z():

    st.write('''_To show sidebar, click **>** in top left_''')
    st.title('Search the full database')
    types = st.radio('Step 1) Choose specialties:',["All","Selected",])

    if types == "All":
        @st.cache(suppress_st_warning=True)
        def load_surgepsdata(url):
            time.sleep(0.1)
            return pd.read_csv(url)

        url = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/Eponyms4python_Lite.csv'
        df1 = pd.read_csv(url, dtype={'PMID':str,'Year':int})
        DF1 = load_surgepsdata(url)
        df2 = DF1.sort_values(by=['Eponym'],ascending=True)
        st.markdown("---")
        min_yrs, max_yrs = st.slider('Step 2) Define a time window (years):', 100, 2050, [150, 2021])
        st.markdown("---")
        new_1T = df2.loc[(df2['Year'] >= min_yrs) & (df2['Year'] <= max_yrs)]
        blank_row = {'Alphabet':'','Eponym':'1','Eponym_easy':'1','Eponym_easy_yr':'',}
        new_2T = new_1T.append(blank_row, ignore_index=True)
        new_3T = new_2T.sort_values(by=['Eponym'],ascending=True)
        options = st.selectbox('Step 3) Search:',
                        new_3T['Eponym_easy'].unique(), format_func=lambda x: ' ' if x == '1' else x)
        df_ep_info = new_3T[new_3T['Eponym_easy'].str.match(options)]


#        @st.cache(suppress_st_warning=True)
#        def load_pic(url):
#            time.sleep(1)
#            return image

        if options == "Aaron sign":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Aaron.png'
            st.image(image, width=160)
        if options == "Allis forceps":
            image_human = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Allis.png'
            image_forceps = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Allis_Forceps.png'
            col1, col2, col3, col4, col5 = st.beta_columns(5)
            col1.image(image_human, width=121);col2.image(image_forceps, width=291)
            col3.write(''); col4.write('')

        if options == "Allison lung retractor":
            image_human = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Allison.png'
            image_retractor = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Allison_Retractor.png'
            col1, col2, col3, col4,col5, col6, col7 = st.beta_columns(7)
            col1.image(image_human, width=140); col3.image(image_retractor, width=141);
            col2.write(''); col4.write('')

        if options == "Allison repair":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Allison.png'
            st.image(image, width=160)
        if options == "Altemeier procedure":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Altemeier.png'
            st.image(image, width=160)
        if options == "Ambrosetti classification":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Ambrosetti.png'
            st.image(image, width=160)
        if options == "Amyand hernia":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Amyand.png'
            st.image(image, width=160)
        if options == "Artery of Adamkiewicz":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Adamkiewicz.png'
            st.image(image, width=160)
            
        if options == "Babcock forceps":
            image_human = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Babcock.png'
            image_forceps = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Babcock_Forceps2.png'
            col1, col2, col3, col4 = st.beta_columns(4)
            col1.image(image_human, width=160); col2.image(image_forceps, width=297);
            col3.write(''); col4.write('')
        if options == "Barrett's oesophagus":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Barrett.png'
            st.image(image, width=160)
        if options == "Bassini hernia repair":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Bassini.png'
            st.image(image, width=160)
        if options == "Battle's incision":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Battle.png'
            st.image(image, width=160)
        if options == "Battle's sign":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Battle.png'
            st.image(image, width=160)
        if options == "Beger procedure":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Beger.png'
            st.image(image, width=160)
        if options == "Belsey Mark IV operation":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Belsey.png'
            st.image(image, width=160)
        if options == "Berry's ligament":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Berry.png'
            st.image(image, width=160)
        if options == "Billroth I procedure":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Billroth.png'
            st.image(image, width=160)
        if options == "Billroth II procedure":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Billroth.png'
            st.image(image, width=160)
        if options == "Bochdalek hernia":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Bochdalek.png'
            st.image(image, width=160)
        if options == "Boerhaave syndrome":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Boerhaave.png'
            st.image(image, width=160)
        if options == "Bouveret syndrome":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Bouveret.png'
            st.image(image, width=160)
        if options == "Brown-Séquard syndrome":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Brown-Sequard.png'
            st.image(image, width=160)
        if options == "Brooke ileostomy":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Brooke.png'
            st.image(image, width=160)
        if options == "Buerger disease":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Buerger.png'
            st.image(image, width=160)
        if options == "Calot's triangle":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Calot2.png'
            st.image(image, width=500)
        if options == "Interstitial cells of Cajal":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Cajal.png'
            st.image(image, width=160)
        if options == "Crigler-Najjar syndrome":
            image_human_C = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Crigler.png'
            image_human_N = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Najjar.png'
            col1, col2, col3 = st.beta_columns(3)
            col1.image(image_human_C, width=160);
            col2.image(image_human_N, width=170); col3.write('')
        if options == "Crohn's disease":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Crohn.png'
            st.image(image, width=160)
        if options == "Cushing's ulcer":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Cushing.png'
            st.image(image, width=160)
        if options == "DeBakey forceps":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_DeBakey_Forceps.png'
            st.image(image, width=300)
        if options == "De Garengeot's hernia":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_De_Garengeot.png'
            st.image(image, width=160)
        if options == "Delorme's procedure":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Delorme.png'
            st.image(image, width=160)
        if options == "DeMeester score":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_DeMeester.png'
            st.image(image, width=160)
        if options == "Doyen retractor":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Doyen.png'
            st.image(image, width=160)
#            image_human = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Doyen.png'
#            image_retractor = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Doyen_Retractor.png'
#            col1, col2, col3, col4 = st.beta_columns(4)
#            col1.image(image_human, width=160); col2.image(image_forceps, width=297);
#            col3.write(''); col4.write('')
        if options == "Fallopian tube":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Falloppio.png'
            st.image(image, width=160)
        if options == "Fanelli catheter":
            image_human = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Fanelli.png'
            image_catheter = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Fanelli_Catheter.png'
            col1, col2, col3 = st.beta_columns(3)
            col1.image(image_human, width=160); col2.image(image_catheter, width=214); col3.write('')
        if options == "Foley catheter":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Foley.png'
            st.image(image, width=160)
#        if options == "Foley catheter":
#            image_human = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Foley.png'
#            image_catheter = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Foley_Catheter.png'
#            col1, col2, col3, col4 = st.beta_columns(4)
#            col1.image(image_human, width=160); col2.image(image_catheter, width=297);
#            col3.write(''); col4.write('')
        if options == "Finochietto retractor":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Finochietto.png'
            st.image(image, width=160)
        if options == "Fisher's exact test":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Fisher.png'
            st.image(image, width=160)
        if options == "Frantz tumour":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Frantz.png'
            st.image(image, width=160)
        if options == "Graham patch":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Graham.png'
            st.image(image, width=160)
        if options == "Ghillebert probability estimate":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Ghillebert.png'
            st.image(image, width=160)
        if options == "Graves disease":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Graves.png'
            st.image(image, width=160)
        if options == "Gleason score":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Gleason.png'
            st.image(image, width=160)
        if options == "Hartmann's operation":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Henri_Hartmann.png'
            st.image(image, width=160)
        if options == "Hartmann's pouch":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Henri_Hartmann.png'
            st.image(image, width=160)
        if options == "Hashimoto's thyroiditis":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Hashimoto.png'
            st.image(image, width=160)
        if options == "Hasson technique":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Hasson.png'
            st.image(image, width=160)
        if options == "Spiral valves of Heister":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Heister.png'
            st.image(image, width=160)
        if options == "Ivor Lewis oesophagectomy":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Ivor_Lewis.png'
            st.image(image, width=160)
        if options == "Joll's retractor":
            image_human = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Joll.png'
            image_retractor = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Jolls_Retractor.png'
            col1, col2, col3 = st.beta_columns(3)
            col1.image(image_human, width=160);col2.image(image_retractor, width=220);col3.write('')
        if options == "Joll's triangle":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Joll.png'
            st.image(image, width=160)
        if options == "Kasai procedure":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Kasai.png'
            st.image(image, width=160)
        if options == "Killian's triangle":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Killian.png'
            st.image(image, width=160)
        if options == "Klatskin's tumour":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Klatskin.png'
            st.image(image, width=160)
        if options == "Kocher's incision of the abdomen":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Kocher.png'
            st.image(image, width=160)
        if options == "Kocher maneuver":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Kocher.png'
            st.image(image, width=160)
        if options == "Lugol's iodine":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Lugol.png'
            st.image(image, width=160)
        if options == "Masson's tumor":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Masson.png'
            st.image(image, width=160)
        if options == "Meckel's diverticulum":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Meckel.png'
            st.image(image, width=160)
        if options == "Merendino jejunal interposition":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Merendino.png'
            st.image(image, width=160)
        if options == "Morrison's pouch":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Morrison.png'
            st.image(image, width=160)
        if options == "Murphy's sign":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Murphy.png'
            st.image(image, width=160)
        if options == "Nodules of Aranzio":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Aranzi.png'
            st.image(image, width=160)
        if options == "Skipworth's sign":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Skip.png'
            st.image(image, width=160)
        if options == "Sphincter of Oddi":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Oddi.png'
            st.image(image, width=160)
        if options == "Mirizzi's syndrome":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Pablo_Mirizzi.png'
            st.image(image, width=160)
        if options == "Arc of Riolan":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Jean_Riolan.png'
            st.image(image, width=160)
        if options == "Rouviere's sulcus":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Rouviere.png'
            st.image(image, width=160)
        if options == "Shouldice hernia repair":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Shouldice.png'
            st.image(image, width=160)
        if options == "Strasberg's critical view of safety":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Strasberg.png'
            st.image(image, width=160)
        if options == "Takayasu's arteritis":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Takayasu.jpg'
            st.image(image, width=160)

        if options == "Tapia syndrome":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Tapia.spng'
            st.image(image, width=160)
        if options == "Ligament of Treitz":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Treitz.png'
            st.image(image, width=160)

        if options == "Valsalva maneuver":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Valsalva.png'
            st.image(image, width=160)
        if options == "Whipple's operation":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Whipple.png'
            st.image(image, width=160)
        if options == "Foramen of Winslow":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Winslow.png'
            st.image(image, width=160)
        if options == "Yankauer suction tip":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Yankauer.png'
            st.image(image, width=160)

        else:pass
        if df_ep_info['Who'].any(): st.write('*_Who_*:', df_ep_info['Who_B'].to_string(index=False))
        else: pass
        if df_ep_info['Year'].any(): st.write('*_When_*:', df_ep_info['Year_str'].to_string(index=False))
        else:pass
        if df_ep_info['Where'].any(): st.write('*_Where_*:', df_ep_info['Where'].to_string(index=False))
        else:pass

        if df_ep_info['Description'].any():
            st.markdown("---")
        description = df_ep_info['Description'].to_string(index=False)
        if df_ep_info['Description'].any():
            st.markdown(description, unsafe_allow_html=True)
        else:pass
        if df_ep_info['Ref'].any():
            st.markdown("---")
            st.write('<u>References</u>', unsafe_allow_html=True)
            st.write(df_ep_info['Ref'].to_string(index=False), unsafe_allow_html=True)
        else: pass
        if df_ep_info['Pubmed'].any() or df_ep_info['Ref_site'].any() or df_ep_info['Wiki_link'].any() or df_ep_info['WNI_link'].any():
            st.markdown("---")
            st.write('<u>External Links</u>', unsafe_allow_html=True)
        ref_site = df_ep_info['Ref_site'].to_string(index=False)
        if df_ep_info['Ref_site'].any(): st.markdown(f"* **Primary Paper** [webpage]({ref_site})")
        else:pass
        pub_link = df_ep_info['Pubmed'].to_string(index=False)
        if df_ep_info['Pubmed'].any(): st.markdown(f"* **Pubmed** [webpage]({pub_link})")
        else:pass
        wiki_link = df_ep_info['Wiki_link'].to_string(index=False)
        if df_ep_info['Wiki_link'].any(): st.markdown(f"* **Wikipedia** [webpage]({wiki_link})")
        else:pass
        wni_link = df_ep_info['WNI_link'].to_string(index=False)
        if df_ep_info['WNI_link'].any(): st.markdown(f"* **Whonamedit** [webpage]({wni_link})")
        else:pass

        
    if types == "Selected":
        url = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/Eponyms4python_Lite.csv'
        df1 = pd.read_csv(url, dtype={'PMID':str,'Year':int})
        df2 = df1.sort_values(by=['Eponym'],ascending=True)
        spec_df = df2['Topic'].dropna()
        string = spec_df.str.cat(sep=',')
        splits = string.split(",")
        S = set(splits)
        T = np.array(list(S)).astype(object)
        U = np.sort(T)
        specs = st.multiselect('Specilaties of interest - pick and choose',options=list(U),
                           format_func=lambda x: ' ' if x == '1' else x,
                           default=['Academic','Anaesthetics','Bariatrics','Breast','Cardiothoracics',
                                    'Colorectal','Emergency Surgery','Endocrine','ENT',
                                    'General Surgery','Gynaecology','HPB','Hernia',
                                    'Laparoscopic Surgery','Maxillofacial','Neurosurgery','Obstetrics',
                                    'Oesophagogastric','Ophthalmology','Orthopaedics','Paediatrics','Plastics',
                                    'Radiology','Transplant','Trauma','Urology','Vascular',]
                                          )

        min_yrs, max_yrs = st.slider("Step 2) Define a time window:", 100, 2050, [150, 2021])
        st.markdown("---")
        new_1T = df2.loc[(df2['Year'] >= min_yrs) & (df2['Year'] <= max_yrs)]
        new_2T = new_1T.loc[new_1T['Topic'].str.contains('|'.join(specs)) == True]
        new_3T = new_2T.sort_values(by=['Eponym'],ascending=True)
        options = st.selectbox('Search:',new_3T['Eponym_easy'].unique(), format_func=lambda x: ' ' if x == '1' else x)
        df_ep_info = new_2T[new_2T['Eponym_easy'].str.match(options)]

        if options == "Aaron sign":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Aaron.png'
            st.image(image, width=160)
        if options == "Allis forceps":
            image_human = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Allis.png'
            image_forceps = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Allis_Forceps.png'
            col1, col2, col3, col4 = st.beta_columns(4)
            col1.image(image_human, width=160);col2.image(image_forceps, width=386)
            col3.write(''); col4.write('')
        if options == "Allison lung retractor":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Allison.png'
            st.image(image, width=160)
        if options == "Allison repair":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Allison.png'
            st.image(image, width=160)
        if options == "Altemeier procedure":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Altemeier.png'
            st.image(image, width=160)
        if options == "Ambrosetti classification":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Ambrosetti.png'
            st.image(image, width=160)
        if options == "Amyand hernia":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Amyand.png'
            st.image(image, width=160)
        if options == "Babcock forceps":
            image_human = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Babcock.png'
            image_forceps = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Babcock_Forceps2.png'
            col1, col2, col3, col4 = st.beta_columns(4)
            col1.image(image_human, width=160); col2.image(image_forceps, width=297);
            col3.write(''); col4.write('')
        if options == "Barrett's oesophagus":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Barrett.png'
            st.image(image, width=160)
        if options == "Bassini hernia repair":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Bassini.png'
            st.image(image, width=160)
        if options == "Battle's incision":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Battle.png'
            st.image(image, width=160)
        if options == "Battle's sign":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Battle.png'
            st.image(image, width=160)
        if options == "Beger procedure":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Beger.png'
            st.image(image, width=160)
        if options == "Belsey Mark IV operation":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Belsey.png'
            st.image(image, width=160)
        if options == "Berry's ligament":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Berry.png'
            st.image(image, width=160)
        if options == "Billroth I procedure":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Billroth.png'
            st.image(image, width=160)
        if options == "Billroth II procedure":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Billroth.png'
            st.image(image, width=160)
        if options == "Bochdalek hernia":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Bochdalek.png'
            st.image(image, width=160)
        if options == "Boerhaave syndrome":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Boerhaave.png'
            st.image(image, width=160)
        if options == "Bouveret syndrome":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Bouveret.png'
            st.image(image, width=160)
        if options == "Brown-Séquard syndrome":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Brown-Sequard.png'
            st.image(image, width=160)
        if options == "Brooke ileostomy":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Brooke.png'
            st.image(image, width=160)
        if options == "Buerger disease":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Buerger.png'
            st.image(image, width=160)
        if options == "Calot's triangle":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Calot2.png'
            st.image(image, width=500)
        if options == "Interstitial cells of Cajal":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Cajal.png'
            st.image(image, width=160)
        if options == "Crigler-Najjar syndrome":
            image_human_C = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Crigler.png'
            image_human_N = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Najjar.png'
            col1, col2, col3 = st.beta_columns(3)
            col1.image(image_human_C, width=160);
            col2.image(image_human_N, width=170); col3.write('')
        if options == "Crohn's disease":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Crohn.png'
            st.image(image, width=160)
        if options == "Cushing's ulcer":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Cushing.png'
            st.image(image, width=160)
        if options == "DeBakey forceps":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_DeBakey_Forceps.png'
            st.image(image, width=300)
        if options == "De Garengeot's hernia":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_De_Garengeot.png'
            st.image(image, width=160)
        if options == "Delorme's procedure":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Delorme.png'
            st.image(image, width=160)
        if options == "DeMeester score":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_DeMeester.png'
            st.image(image, width=160)
        if options == "Doyen retractor":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Doyen.png'
            st.image(image, width=160)
#            image_human = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Doyen.png'
#            image_retractor = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Doyen_Retractor.png'
#            col1, col2, col3, col4 = st.beta_columns(4)
#            col1.image(image_human, width=160); col2.image(image_forceps, width=297);
#            col3.write(''); col4.write('')
        if options == "Fallopian tube":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Falloppio.png'
            st.image(image, width=160)
        if options == "Fanelli catheter":
            image_human = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Fanelli.png'
            image_catheter = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Fanelli_Catheter.png'
            col1, col2, col3 = st.beta_columns(3)
            col1.image(image_human, width=160); col2.image(image_catheter, width=214); col3.write('')
        if options == "Foley catheter":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Foley.png'
            st.image(image, width=160)
#        if options == "Foley catheter":
#            image_human = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Foley.png'
#            image_catheter = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Foley_Catheter.png'
#            col1, col2, col3, col4 = st.beta_columns(4)
#            col1.image(image_human, width=160); col2.image(image_catheter, width=297);
#            col3.write(''); col4.write('')
        if options == "Finochietto retractor":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Finochietto.png'
            st.image(image, width=160)
        if options == "Fisher's exact test":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Fisher.png'
            st.image(image, width=160)
        if options == "Frantz tumour":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Frantz.png'
            st.image(image, width=160)
        if options == "Graham patch":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Graham.png'
            st.image(image, width=160)
        if options == "Graves disease":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Graves.png'
            st.image(image, width=160)
        if options == "Gleason score":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Gleason.png'
            st.image(image, width=160)
        if options == "Hartmann's operation":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Henri_Hartmann.png'
            st.image(image, width=160)
        if options == "Hartmann's pouch":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Henri_Hartmann.png'
            st.image(image, width=160)
        if options == "Hashimoto's thyroiditis":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Hashimoto.png'
            st.image(image, width=160)
        if options == "Hasson technique":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Hasson.png'
            st.image(image, width=160)
        if options == "Spiral valves of Heister":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Heister.png'
            st.image(image, width=160)
        if options == "Ivor Lewis oesophagectomy":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Ivor_Lewis.png'
            st.image(image, width=160)
        if options == "Joll's retractor":
            image_human = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Joll.png'
            image_retractor = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Jolls_Retractor.png'
            col1, col2, col3 = st.beta_columns(3)
            col1.image(image_human, width=160);col2.image(image_retractor, width=220);col3.write('')
        if options == "Joll's triangle":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Joll.png'
            st.image(image, width=160)
        if options == "Killian's triangle":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Killian.png'
            st.image(image, width=160)
        if options == "Klatskin's tumour":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Klatskin.png'
            st.image(image, width=160)
        if options == "Kocher's incision of the abdomen":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Kocher.png'
            st.image(image, width=160)
        if options == "Kocher maneuver":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Kocher.png'
            st.image(image, width=160)
        if options == "Lugol's iodine":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Lugol.png'
            st.image(image, width=160)
        if options == "Masson's tumor":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Masson.png'
            st.image(image, width=160)
        if options == "Meckel's diverticulum":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Meckel.png'
            st.image(image, width=160)
        if options == "Merendino jejunal interposition":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Merendino.png'
            st.image(image, width=160)
        if options == "Morrison's pouch":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Morrison.png'
            st.image(image, width=160)
        if options == "Murphy's sign":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Murphy.png'
            st.image(image, width=160)
        if options == "Nodules of Aranzio":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Aranzi.png'
            st.image(image, width=160)
        if options == "Skipworth's sign":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Skip.png'
            st.image(image, width=160)
        if options == "Sphincter of Oddi":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Oddi.png'
            st.image(image, width=160)
        if options == "Mirizzi's syndrome":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Pablo_Mirizzi.png'
            st.image(image, width=160)
        if options == "Rouviere's sulcus":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Rouviere.png'
            st.image(image, width=160)
        if options == "Shouldice hernia repair":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Shouldice.png'
            st.image(image, width=160)
        if options == "Strasberg's critical view of safety":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Strasberg.png'
            st.image(image, width=160)
        if options == "Takayasu's arteritis":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Takayasu.jpg'
            st.image(image, width=160)
        if options == "Ligament of Treitz":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Treitz.png'
            st.image(image, width=160)
        if options == "Whipple's operation":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Whipple.png'
            st.image(image, width=160)
        if options == "Foramen of Winslow":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Winslow.png'
            st.image(image, width=160)
        if options == "Yankauer suction tip":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Yankauer.png'
            st.image(image, width=160)


        else:pass
        if df_ep_info['Who'].any(): st.write('*_Who_*:', df_ep_info['Who_B'].to_string(index=False))
        else: pass
        if df_ep_info['Year'].any(): st.write('*_When_*:', df_ep_info['Year_str'].to_string(index=False))
        else:pass
        if df_ep_info['Where'].any(): st.write('*_Where_*:', df_ep_info['Where'].to_string(index=False))
        else:pass

        if df_ep_info['Description'].any():
            st.markdown("---")
        description = df_ep_info['Description'].to_string(index=False)
        if df_ep_info['Description'].any():
            st.markdown(description, unsafe_allow_html=True)
        else:pass
        if df_ep_info['Ref'].any():
            st.markdown("---")
            st.write('<u>References</u>', unsafe_allow_html=True)
            st.write(df_ep_info['Ref'].to_string(index=False), unsafe_allow_html=True)
        else: pass

        if df_ep_info['Pubmed'].any() or df_ep_info['Ref_site'].any() or df_ep_info['Wiki_link'].any() or df_ep_info['WNI_link'].any():
            st.markdown("---")
            st.write('<u>External Links</u>', unsafe_allow_html=True)
        ref_site = df_ep_info['Ref_site'].to_string(index=False)
        if df_ep_info['Ref_site'].any(): st.markdown(f"* **Primary Paper** [webpage]({ref_site})")
        else:pass
        pub_link = df_ep_info['Pubmed'].to_string(index=False)
        if df_ep_info['Pubmed'].any(): st.markdown(f"* **Pubmed** [webpage]({pub_link})")
        else:pass
        wiki_link = df_ep_info['Wiki_link'].to_string(index=False)
        if df_ep_info['Wiki_link'].any(): st.markdown(f"* **Wikipedia** [webpage]({wiki_link})")
        else:pass
        wni_link = df_ep_info['WNI_link'].to_string(index=False)
        if df_ep_info['WNI_link'].any(): st.markdown(f"* **Whonamedit** [webpage]({wni_link})")
        else:pass


#-------------------------------------------------------------------------------------------------#
#                                                                                                 #
#  Disease (3)                                                                                    #
# ::: Handles the                                                                                 #                                                                                              #
#                                                                                                 #
#-------------------------------------------------------------------------------------------------#
def exp_dis():
    st.write('''_To show sidebar, click **>** in top left_''')
    st.title("Search by disease, sign or symptom") 
    url = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/Eponyms4python_Lite.csv'
    df = pd.read_csv(url, dtype={'PMID':str,'Year':int})
    df1 = df['Disease'].dropna()
    string = df1.str.cat(sep=',')
    splits = string.split(",")
    S = set(splits)
    T = np.array(list(S)).astype(object)
    U = np.sort(T)
    disease = st.multiselect('Step 1) Choose a disease, sign or symptom:', options=list(U),)
    st.markdown("---")
    new_dis1 = df.loc[df['Disease'].str.contains('|'.join(disease)) == True]
    new_dis2 = new_dis1.sort_values(by=['Eponym'],ascending=True)
    if disease:
        options = st.selectbox('Step 2) Search list of related terms:',
                                   new_dis2['Eponym_easy'].unique(),
                               format_func=lambda x: ' ' if x == '1' else x)

        df_ep_info = new_dis1[new_dis1['Eponym_easy'].str.match(options)]
        ep_yr = df_ep_info['Year'].to_string(index=False)

        if options == "Aaron sign":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Aaron.png'
            st.image(image, width=160)
        if options == "Allis forceps":
            image_human = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Allis.png'
            image_forceps = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Allis_Forceps.png'
            col1, col2, col3, col4 = st.beta_columns(4)
            col1.image(image_human, width=160);col2.image(image_forceps, width=386)
            col3.write(''); col4.write('')
        if options == "Allison lung retractor":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Allison.png'
            st.image(image, width=160)
        if options == "Allison repair":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Allison.png'
            st.image(image, width=160)
        if options == "Altemeier procedure":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Altemeier.png'
            st.image(image, width=160)
        if options == "Ambrosetti classification":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Ambrosetti.png'
            st.image(image, width=160)
        if options == "Amyand hernia":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Amyand.png'
            st.image(image, width=160)
        if options == "Babcock forceps":
            image_human = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Babcock.png'
            image_forceps = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Babcock_Forceps2.png'
            col1, col2, col3, col4 = st.beta_columns(4)
            col1.image(image_human, width=160); col2.image(image_forceps, width=297);
            col3.write(''); col4.write('')
        if options == "Barrett's oesophagus":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Barrett.png'
            st.image(image, width=160)
        if options == "Bassini hernia repair":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Bassini.png'
            st.image(image, width=160)
        if options == "Battle's incision":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Battle.png'
            st.image(image, width=160)
        if options == "Battle's sign":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Battle.png'
            st.image(image, width=160)
        if options == "Beger procedure":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Beger.png'
            st.image(image, width=160)
        if options == "Belsey Mark IV operation":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Belsey.png'
            st.image(image, width=160)
        if options == "Berry's ligament":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Berry.png'
            st.image(image, width=160)
        if options == "Billroth I procedure":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Billroth.png'
            st.image(image, width=160)
        if options == "Billroth II procedure":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Billroth.png'
            st.image(image, width=160)
        if options == "Bochdalek hernia":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Bochdalek.png'
            st.image(image, width=160)
        if options == "Boerhaave syndrome":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Boerhaave.png'
            st.image(image, width=160)
        if options == "Bouveret syndrome":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Bouveret.png'
            st.image(image, width=160)
        if options == "Brown-Séquard syndrome":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Brown-Sequard.png'
            st.image(image, width=160)
        if options == "Brooke ileostomy":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Brooke.png'
            st.image(image, width=160)
        if options == "Buerger disease":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Buerger.png'
            st.image(image, width=160)
        if options == "Calot's triangle":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Calot2.png'
            st.image(image, width=500)
        if options == "Interstitial cells of Cajal":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Cajal.png'
            st.image(image, width=160)
        if options == "Crigler-Najjar syndrome":
            image_human_C = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Crigler.png'
            image_human_N = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Najjar.png'
            col1, col2, col3 = st.beta_columns(3)
            col1.image(image_human_C, width=160);
            col2.image(image_human_N, width=170); col3.write('')
        if options == "Crohn's disease":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Crohn.png'
            st.image(image, width=160)
        if options == "Cushing's ulcer":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Cushing.png'
            st.image(image, width=160)
        if options == "DeBakey forceps":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_DeBakey_Forceps.png'
            st.image(image, width=300)
        if options == "De Garengeot's hernia":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_De_Garengeot.png'
            st.image(image, width=160)
        if options == "Delorme's procedure":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Delorme.png'
            st.image(image, width=160)
        if options == "DeMeester score":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_DeMeester.png'
            st.image(image, width=160)
        if options == "Doyen retractor":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Doyen.png'
            st.image(image, width=160)
#            image_human = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Doyen.png'
#            image_retractor = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Doyen_Retractor.png'
#            col1, col2, col3, col4 = st.beta_columns(4)
#            col1.image(image_human, width=160); col2.image(image_forceps, width=297);
#            col3.write(''); col4.write('')
        if options == "Fallopian tube":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Falloppio.png'
            st.image(image, width=160)
        if options == "Fanelli catheter":
            image_human = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Fanelli.png'
            image_catheter = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Fanelli_Catheter.png'
            col1, col2, col3 = st.beta_columns(3)
            col1.image(image_human, width=160); col2.image(image_catheter, width=214); col3.write('')
        if options == "Foley catheter":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Foley.png'
            st.image(image, width=160)
#        if options == "Foley catheter":
#            image_human = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Foley.png'
#            image_catheter = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Foley_Catheter.png'
#            col1, col2, col3, col4 = st.beta_columns(4)
#            col1.image(image_human, width=160); col2.image(image_catheter, width=297);
#            col3.write(''); col4.write('')
        if options == "Finochietto retractor":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Finochietto.png'
            st.image(image, width=160)
        if options == "Fisher's exact test":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Fisher.png'
            st.image(image, width=160)
        if options == "Frantz tumour":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Frantz.png'
            st.image(image, width=160)
        if options == "Graham patch":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Graham.png'
            st.image(image, width=160)
        if options == "Graves disease":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Graves.png'
            st.image(image, width=160)
        if options == "Gleason score":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Gleason.png'
            st.image(image, width=160)
        if options == "Hartmann's operation":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Henri_Hartmann.png'
            st.image(image, width=160)
        if options == "Hartmann's pouch":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Henri_Hartmann.png'
            st.image(image, width=160)
        if options == "Hashimoto's thyroiditis":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Hashimoto.png'
            st.image(image, width=160)
        if options == "Hasson technique":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Hasson.png'
            st.image(image, width=160)
        if options == "Ivor Lewis oesophagectomy":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Ivor_Lewis.png'
            st.image(image, width=160)
        if options == "Joll's retractor":
            image_human = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Joll.png'
            image_retractor = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Jolls_Retractor.png'
            col1, col2, col3 = st.beta_columns(3)
            col1.image(image_human, width=160);col2.image(image_retractor, width=220);col3.write('')
        if options == "Joll's triangle":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Joll.png'
            st.image(image, width=160)
        if options == "Killian's triangle":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Killian.png'
            st.image(image, width=160)
        if options == "Klatskin's tumour":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Klatskin.png'
            st.image(image, width=160)
        if options == "Kocher's incision of the abdomen":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Kocher.png'
            st.image(image, width=160)
        if options == "Kocher maneuver":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Kocher.png'
            st.image(image, width=160)
        if options == "Lugol's iodine":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Lugol.png'
            st.image(image, width=160)
        if options == "Masson's tumor":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Masson.png'
            st.image(image, width=160)
        if options == "Meckel's diverticulum":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Meckel.png'
            st.image(image, width=160)
        if options == "Merendino jejunal interposition":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Merendino.png'
            st.image(image, width=160)
        if options == "Morrison's pouch":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Morrison.png'
            st.image(image, width=160)
        if options == "Murphy's sign":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Murphy.png'
            st.image(image, width=160)
        if options == "Nodules of Aranzio":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Aranzi.png'
            st.image(image, width=160)
        if options == "Skipworth's sign":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Skip.png'
            st.image(image, width=160)
        if options == "Sphincter of Oddi":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Oddi.png'
            st.image(image, width=160)
        if options == "Mirizzi's syndrome":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Pablo_Mirizzi.png'
            st.image(image, width=160)
        if options == "Rouviere's sulcus":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Rouviere.png'
            st.image(image, width=160)
        if options == "Shouldice hernia repair":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Shouldice.png'
            st.image(image, width=160)
        if options == "Strasberg's critical view of safety":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Strasberg.png'
            st.image(image, width=160)
        if options == "Takayasu's arteritis":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Takayasu.jpg'
            st.image(image, width=160)
        if options == "Ligament of Treitz":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Treitz.png'
            st.image(image, width=160)
        if options == "Whipple's operation":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Whipple.png'
            st.image(image, width=160)
        if options == "Foramen of Winslow":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Winslow.png'
            st.image(image, width=160)
        if options == "Yankauer suction tip":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Yankauer.png'
            st.image(image, width=160)
            
        else:pass
        if df_ep_info['Who'].any(): st.write('*_Who_*:', df_ep_info['Who_B'].to_string(index=False))
        else: pass
        if df_ep_info['Year'].any(): st.write('*_When_*:', df_ep_info['Year_str'].to_string(index=False))
        else:pass
        if df_ep_info['Where'].any(): st.write('*_Where_*:', df_ep_info['Where'].to_string(index=False))
        else:pass

        if df_ep_info['Description'].any():
            st.markdown("---")
        description = df_ep_info['Description'].to_string(index=False)
        if df_ep_info['Description'].any():
            st.markdown(description, unsafe_allow_html=True)
        else:pass

        if df_ep_info['Ref'].any():
            st.markdown("---")
            st.write('<u>References</u>', unsafe_allow_html=True)
            st.write(df_ep_info['Ref'].to_string(index=False), unsafe_allow_html=True)
        else: pass

        if df_ep_info['Pubmed'].any() or df_ep_info['Ref_site'].any() or df_ep_info['Wiki_link'].any() or df_ep_info['WNI_link'].any():
            st.markdown("---")
            st.write('<u>External Links</u>', unsafe_allow_html=True)

        ref_site = df_ep_info['Ref_site'].to_string(index=False)
        if df_ep_info['Ref_site'].any(): st.markdown(f"* **Primary Paper** [webpage]({ref_site})")
        else:pass
        pub_link = df_ep_info['Pubmed'].to_string(index=False)
        if df_ep_info['Pubmed'].any(): st.markdown(f"* **Pubmed** [webpage]({pub_link})")
        else:pass
        wiki_link = df_ep_info['Wiki_link'].to_string(index=False)
        if df_ep_info['Wiki_link'].any(): st.markdown(f"* **Wikipedia** [webpage]({wiki_link})")
        else:pass
        wni_link = df_ep_info['WNI_link'].to_string(index=False)
        if df_ep_info['WNI_link'].any(): st.markdown(f"* **Whonamedit** [webpage]({wni_link})")
        else:pass



#-------------------------------------------------------------------------------------------------#
#                                                                                                 #
#  Journals (4)                                                                                   #
# ::: Handles                                                                                     #                                                                                              #
#                                                                                                 #
#-------------------------------------------------------------------------------------------------#
def exp_journals():
    st.write('''_To show sidebar, click **>** in top left_''')
    st.title("Find which eponyms originate from particular journals") 
    ScreenSize = st.radio('Step 1) Select screen size:',
                          options=['Smartphone',
                                   'Desktop / Laptop / Tablet'],index=0)

    if ScreenSize == "Smartphone":
        types = st.radio('Step 2) Choose specialties:',["All","Selected",])
        if types == 'All':
            min_yrs, max_yrs = st.slider("3rd) Choose time window:", 1700, 2030, [1715, 2021])
            url_J = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/Eponyms4python_Lite4Journals.csv'
            dfY = pd.read_csv(url_J) #,dtype={'year':int}) 
            dfY1 = dfY.dropna()
            dfY1["Journals"] = "Journals"
            dfT = dfY1.sort_values(by=['year'],ascending=True)
            time_df = dfT.loc[(dfT['year'] >= min_yrs) & (dfT['year'] <= max_yrs)]
            time_spec_df = time_df['specialty'].dropna()
            string = time_spec_df.str.cat(sep=',')
            splits = string.split(",")
            S = set(splits)
            T = np.array(list(S)).astype(object)
            U = np.sort(T)
            st.markdown("---")
            st.markdown('''<span style="font-size:10pt;color:black;">**Click on journal name to zoom in**,
                       and in the center to pan out.</span>''', unsafe_allow_html=True)
            figJDLT = px.sunburst(time_df,path=['Journals','journal_short','year','eponym'],
                                  color='Log2 Google hits',hover_data=['eponym'],color_continuous_scale='RdBu',)
            figJDLT.update_layout(margin=dict(l=0, r=0, t=0, b=0),width=400,height=300)
            figJDLT.update_traces(hovertemplate='<b>%{label}</b>')
            st.write(figJDLT)
            st.markdown("---")
            time_jrnl = time_df.sort_values(by=['journal'],ascending=True)
            time_jrnl1 = time_jrnl['journal'].dropna()
            string1 = time_jrnl1.str.cat(sep=',')
            splits1 = string1.split(",")
            S1 = set(splits1)
            T1 = np.array(list(S1)).astype(object)
            U1 = np.sort(T1)
            jrnls = st.multiselect('4th) Select journals:',options=list(U1),
                              format_func=lambda x: ' ' if x == '1' else x)
            new_jrnls1 = time_df.loc[time_df['journal'].str.contains('|'.join(jrnls)) == True]
            new_jrnls2 = new_jrnls1.sort_values(by=['eponym_yr'],ascending=True)
            if jrnls:
                options = st.selectbox('5th) Eponyms in selected journals:',
                                  new_jrnls2['eponym_yr'].unique(), format_func=lambda x: ' ' if x == '1' else x)
                df_ep_info = new_jrnls1[new_jrnls1['eponym_yr'].str.match(options)]
                journal = df_ep_info['journal_name'].to_string(index=False)

                if options == "Aaron sign":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Aaron.png'
                    st.image(image, width=160)
                if options == "Allis forceps":
                    image_human = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Allis.png'
                    image_forceps = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Allis_Forceps.png'
                    col1, col2, col3, col4 = st.beta_columns(4)
                    col1.image(image_human, width=160);col2.image(image_forceps, width=386)
                    col3.write(''); col4.write('')
                if options == "Allison lung retractor":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Allison.png'
                    st.image(image, width=160)
                if options == "Allison repair":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Allison.png'
                    st.image(image, width=160)
                if options == "Altemeier procedure":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Altemeier.png'
                    st.image(image, width=160)
                if options == "Ambrosetti classification":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Ambrosetti.png'
                    st.image(image, width=160)
                if options == "Amyand hernia":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Amyand.png'
                    st.image(image, width=160)
                if options == "Babcock forceps":
                    image_human = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Babcock.png'
                    image_forceps = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Babcock_Forceps2.png'
                    col1, col2, col3, col4 = st.beta_columns(4)
                    col1.image(image_human, width=160); col2.image(image_forceps, width=297);
                    col3.write(''); col4.write('')
                if options == "Barrett's oesophagus":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Barrett.png'
                    st.image(image, width=160)
                if options == "Bassini hernia repair":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Bassini.png'
                    st.image(image, width=160)
                if options == "Battle's sign":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Battle.png'
                    st.image(image, width=160)
                if options == "Beger procedure":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Beger.png'
                    st.image(image, width=160)
                if options == "Berry's ligament":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Berry.png'
                    st.image(image, width=160)
                if options == "Brown-Séquard syndrome":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Brown-Sequard.png'
                    st.image(image, width=160)
                if options == "Brooke ileostomy":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Brooke.png'
                    st.image(image, width=160)
                if options == "Calot's triangle":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Calot2.png'
                    st.image(image, width=500)
                if options == "Cushing's ulcer":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Cushing.png'
                    st.image(image, width=160)
                if options == "DeBakey forceps":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_DeBakey_Forceps.png'
                    st.image(image, width=300)
                if options == "De Garengeot's hernia":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_De_Garengeot.png'
                    st.image(image, width=160)
                if options == "Delorme's procedure":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Delorme.png'
                    st.image(image, width=160)
                if options == "Fanelli catheter":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Fanelli.png'
                    st.image(image, width=160)
                if options == "Foley catheter":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Foley.png'
                    st.image(image, width=160)
                if options == "Graves disease":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Graves.png'
                    st.image(image, width=160)
                if options == "Hartmann's operation":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Henri_Hartmann.png'
                    st.image(image, width=160)
                if options == "Hartmann's pouch":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Henri_Hartmann.png'
                    st.image(image, width=160)
                if options == "Hashimoto's thyroiditis":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Hashimoto.png'
                    st.image(image, width=160)
                if options == "Ivor Lewis oesophagectomy":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Ivor_Lewis.png'
                    st.image(image, width=160)
                if options == "Joll's retractor":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Joll.png'
                    st.image(image, width=160)
                if options == "Joll's triangle":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Joll.png'
                    st.image(image, width=160)
                if options == "Killian's triangle":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Killian.png'
                    st.image(image, width=160)
                if options == "Kocher's incision of the abdomen":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Kocher.png'
                    st.image(image, width=160)
                if options == "Kocher maneuver":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Kocher.png'
                    st.image(image, width=160)
                if options == "Meckel's diverticulum":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Meckel.png'
                    st.image(image, width=160)
                if options == "Merendino jejunal interposition":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Merendino.png'
                    st.image(image, width=160)
                if options == "Morrison's pouch":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Morrison.png'
                    st.image(image, width=160)
                if options == "Nodules of Aranzio":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Aranzi.png'
                    st.image(image, width=160)
                if options == "Sphincter of Oddi":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Oddi.png'
                    st.image(image, width=160)
                if options == "Mirizzi's syndrome":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Pablo_Mirizzi.png'
                    st.image(image, width=160)
                if options == "Rouviere's sulcus":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Rouviere.png'
                    st.image(image, width=160)
                if options == "Shouldice hernia repair":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Shouldice.png'
                    st.image(image, width=160)
                if options == "Strasberg's critical view of safety":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Strasberg.png'
                    st.image(image, width=160)
                if options == "Takayasu's arteritis":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Takayasu.jpg'
                    st.image(image, width=160)
                if options == "Ligament of Treitz":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Treitz.png'
                    st.image(image, width=160)
                if options == "Whipple's operation":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Whipple.png'
                    st.image(image, width=160)
                if options == "Foramen of Winslow":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Winslow.png'
                    st.image(image, width=160)


                if df_ep_info['journal_name'].any(): st.write(journal, unsafe_allow_html=True)
                else: pass
                if df_ep_info['year_str'].any():st.write('_When_:',df_ep_info['year_str'].to_string(index=False))
                else: pass
                if df_ep_info['Who'].any():st.write('_Who_:',df_ep_info['Who'].to_string(index=False))

                if df_ep_info['Ref'].any():
                    st.markdown("---")
                    st.write('<u>References</u>', unsafe_allow_html=True)
                    st.write(df_ep_info['Ref'].to_string(index=False), unsafe_allow_html=True)
                else: pass

                
                #if df_ep_info2['Description'].any():
                #    st.markdown(description, unsafe_allow_html=True)
                #if df_ep_info2['History'].any():
                #    st.write('**_History_**:', history)
                #st.markdown("---")


        if types == 'Selected':
            url_J = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/Eponyms4python_Lite4Journals.csv'
            dfY = pd.read_csv(url_J) #,dtype={'year':int})
            dfY1 = dfY.dropna()
            dfY1["Journals"] = "Journals"
            df2 = dfY1.sort_values(by=['year'],ascending=True)
            spec_df = df2['specialty'].dropna()
            string = spec_df.str.cat(sep=',')
            splits = string.split(",")
            S = set(splits)
            T = np.array(list(S)).astype(object)
            U = np.sort(T)
            journal_spec = st.multiselect('Specilaties of interest - pick and choose',options=list(U),
                           format_func=lambda x: ' ' if x == '1' else x,
                           default=['Academic','Anaesthetics','Bariatrics','Breast','Cardiothoracics',
                                    'Colorectal','Emergency Surgery','Endocrine','ENT',
                                    'General Surgery','Gynaecology','HPB','Hernia',
                                    'Laparoscopic Surgery','Maxillofacial','Neurosurgery','Obstetrics',
                                    'Oesophagogastric','Orthopaedics','Paediatrics','Plastics','Radiology',
                                    'Transplant','Trauma','Urology','Vascular',]
                                          )
            min_yrs, max_yrs = st.slider("3rd) Choose time window:", 1700, 2030, [1715, 2021])
            st.markdown("---")
            st.markdown('''<span style="font-size:10pt;color:black;">**Click on journal name to zoom in**,
                       and in the center to pan out.</span>''', unsafe_allow_html=True)
            new_jrnls1 = df2.loc[df2['specialty'].str.contains('|'.join(journal_spec)) == True]
            new_jrnls1T = new_jrnls1.loc[(new_jrnls1['year'] >= min_yrs) & (new_jrnls1['year'] <= max_yrs)]
            new_jrnls2T = new_jrnls1T.sort_values(by=['eponym'],ascending=True)
            new_jrnls2T["Journals"] = "Journals"
            if not journal_spec == None:
                figJDLT = px.sunburst(new_jrnls2T,path=['Journals','journal_short','year','eponym'],#values='Log10 Google hits',
                                      color='Log2 Google hits',hover_data=['eponym'], color_continuous_scale='RdBu',)
                      #inferno,thermal,Magma,Cividis,deep,Viridis,icefire,ylgnbu,'portland','agsunset'
                figJDLT.update_layout(margin=dict(l=0, r=0, t=0, b=0),width=400,height=300)
                figJDLT.update_traces(hovertemplate='<b>%{label}</b>')
                st.write(figJDLT)

            time_jrnl = new_jrnls1T.sort_values(by=['journal'],ascending=True)
            time_jrnl1 = time_jrnl['journal'].dropna()
            string1 = time_jrnl1.str.cat(sep=',')
            splits1 = string1.split(",")
            S1 = set(splits1)
            T1 = np.array(list(S1)).astype(object)
            U1 = np.sort(T1)
            st.markdown("---")
            
            jrnls = st.multiselect('4th) Select journals:',options=list(U1),
                                   format_func=lambda x: ' ' if x == '1' else x)
            new_jrnls1 = new_jrnls2T.loc[new_jrnls2T['journal'].str.contains('|'.join(jrnls)) == True]
            new_jrnls2 = new_jrnls1.sort_values(by=['eponym_yr'],ascending=True)

            if jrnls:
                options = st.selectbox('5th) Eponyms in selected journals:',
                                  new_jrnls2['eponym_yr'].unique(), format_func=lambda x: ' ' if x == '1' else x)
                df_ep_info = new_jrnls1[new_jrnls1['eponym_yr'].str.match(options)]
                journal = df_ep_info['journal_name'].to_string(index=False)

                if options == "Aaron sign":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Aaron.png'
                    st.image(image, width=160)
                if options == "Allis forceps":
                    image_human = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Allis.png'
                    image_forceps = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Allis_Forceps.png'
                    col1, col2, col3, col4 = st.beta_columns(4)
                    col1.image(image_human, width=160);col2.image(image_forceps, width=386)
                    col3.write(''); col4.write('')
                if options == "Allison lung retractor":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Allison.png'
                    st.image(image, width=160)
                if options == "Allison repair":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Allison.png'
                    st.image(image, width=160)
                if options == "Altemeier procedure":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Altemeier.png'
                    st.image(image, width=160)
                if options == "Ambrosetti classification":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Ambrosetti.png'
                    st.image(image, width=160)
                if options == "Amyand hernia":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Amyand.png'
                    st.image(image, width=160)
                if options == "Babcock forceps":
                    image_human = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Babcock.png'
                    image_forceps = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Babcock_Forceps2.png'
                    col1, col2, col3, col4 = st.beta_columns(4)
                    col1.image(image_human, width=160); col2.image(image_forceps, width=297);
                    col3.write(''); col4.write('')
                if options == "Barrett's oesophagus":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Barrett.png'
                    st.image(image, width=160)
                if options == "Bassini hernia repair":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Bassini.png'
                    st.image(image, width=160)
                if options == "Battle's sign":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Battle.png'
                    st.image(image, width=160)
                if options == "Beger procedure":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Beger.png'
                    st.image(image, width=160)
                if options == "Berry's ligament":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Berry.png'
                    st.image(image, width=160)
                if options == "Brown-Séquard syndrome":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Brown-Sequard.png'
                    st.image(image, width=160)
                if options == "Brooke ileostomy":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Brooke.png'
                    st.image(image, width=160)
                if options == "Calot's triangle":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Calot2.png'
                    st.image(image, width=500)
                if options == "Cushing's ulcer":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Cushing.png'
                    st.image(image, width=160)
                if options == "DeBakey forceps":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_DeBakey_Forceps.png'
                    st.image(image, width=300)
                if options == "De Garengeot's hernia":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_De_Garengeot.png'
                    st.image(image, width=160)
                if options == "Delorme's procedure":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Delorme.png'
                    st.image(image, width=160)
                if options == "Fanelli catheter":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Fanelli.png'
                    st.image(image, width=160)
                if options == "Foley catheter":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Foley.png'
                    st.image(image, width=160)
                if options == "Graves disease":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Graves.png'
                    st.image(image, width=160)
                if options == "Hartmann's operation":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Henri_Hartmann.png'
                    st.image(image, width=160)
                if options == "Hartmann's pouch":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Henri_Hartmann.png'
                    st.image(image, width=160)
                if options == "Hashimoto's thyroiditis":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Hashimoto.png'
                    st.image(image, width=160)
                if options == "Ivor Lewis oesophagectomy":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Ivor_Lewis.png'
                    st.image(image, width=160)
                if options == "Joll's retractor":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Joll.png'
                    st.image(image, width=160)
                if options == "Joll's triangle":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Joll.png'
                    st.image(image, width=160)
                if options == "Killian's triangle":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Killian.png'
                    st.image(image, width=160)
                if options == "Kocher's incision of the abdomen":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Kocher.png'
                    st.image(image, width=160)
                if options == "Kocher maneuver":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Kocher.png'
                    st.image(image, width=160)
                if options == "Meckel's diverticulum":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Meckel.png'
                    st.image(image, width=160)
                if options == "Merendino jejunal interposition":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Merendino.png'
                    st.image(image, width=160)
                if options == "Morrison's pouch":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Morrison.png'
                    st.image(image, width=160)
                if options == "Nodules of Aranzio":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Aranzi.png'
                    st.image(image, width=160)
                if options == "Sphincter of Oddi":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Oddi.png'
                    st.image(image, width=160)
                if options == "Mirizzi's syndrome":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Pablo_Mirizzi.png'
                    st.image(image, width=160)
                if options == "Rouviere's sulcus":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Rouviere.png'
                    st.image(image, width=160)
                if options == "Shouldice hernia repair":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Shouldice.png'
                    st.image(image, width=160)
                if options == "Strasberg's critical view of safety":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Strasberg.png'
                    st.image(image, width=160)
                if options == "Takayasu's arteritis":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Takayasu.jpg'
                    st.image(image, width=160)
                if options == "Ligament of Treitz":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Treitz.png'
                    st.image(image, width=160)
                if options == "Whipple's operation":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Whipple.png'
                    st.image(image, width=160)
                if options == "Foramen of Winslow":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Winslow.png'
                    st.image(image, width=160)

                if df_ep_info['journal_name'].any(): st.write(journal, unsafe_allow_html=True)
                else: pass
                if df_ep_info['year_str'].any():st.write('_When_:',df_ep_info['year_str'].to_string(index=False))
                else: pass
                if df_ep_info['Who'].any():st.write('_Who_:',df_ep_info['Who'].to_string(index=False))
                else: pass

                if df_ep_info['Ref'].any():
                    st.markdown("---")
                    st.write('<u>References</u>', unsafe_allow_html=True)
                    st.write(df_ep_info['Ref'].to_string(index=False), unsafe_allow_html=True)
                else: pass
                
                #if df_ep_info2['Description'].any():
                #    st.markdown(description, unsafe_allow_html=True)
                #if df_ep_info2['History'].any():
                #    st.write('**_History_**:', history)



    if ScreenSize == "Desktop / Laptop / Tablet":
        types = st.radio('2nd) Choose specialties:',["All","Selected",])
        if types == 'All':
            min_yrs, max_yrs = st.slider("3rd) Choose time window:", 1700, 2030, [1715, 2021])
            st.markdown("---")
            url_J = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/Eponyms4python_Lite4Journals.csv'
            dfY = pd.read_csv(url_J) #, dtype={'year':int})
            dfY1 = dfY.dropna()
            dfY1["Journals"] = "Journals"
            dfT = dfY1.sort_values(by=['year'],ascending=True)
            time_df = dfT.loc[(dfT['year'] >= min_yrs) & (dfT['year'] <= max_yrs)]
            time_spec_df = time_df['specialty'].dropna()
            string = time_spec_df.str.cat(sep=',')
            splits = string.split(",")
            S = set(splits)
            T = np.array(list(S)).astype(object)
            U = np.sort(T)
            st.markdown('''<span style="font-size:12pt;color:black;">**Click on journal name to zoom in**,
                       and click in the center to pan out.</span>''', unsafe_allow_html=True)
            figJDLT = px.sunburst(time_df,path=['Journals','journal_short','year','eponym'],
                            color='Log2 Google hits',hover_data=['eponym'],#values='Log10 Google hits',
                            color_continuous_scale='rdbu',
                                  ) #'RdBu'
            figJDLT.update_layout(margin=dict(l=0, r=0, t=0, b=10),width=700,height=550)
            figJDLT.update_traces(hovertemplate='<b>%{label}</b>')
            st.write(figJDLT)
            st.markdown("---")
            time_jrnl = time_df.sort_values(by=['journal'],ascending=True)
            time_jrnl1 = time_jrnl['journal'].dropna()
            string1 = time_jrnl1.str.cat(sep=',')
            splits1 = string1.split(",")
            S1 = set(splits1)
            T1 = np.array(list(S1)).astype(object)
            U1 = np.sort(T1)
            jrnls = st.multiselect('4th) Select journals:',options=list(U1),
                              format_func=lambda x: ' ' if x == '1' else x)
            new_jrnls1 = time_df.loc[time_df['journal'].str.contains('|'.join(jrnls)) == True]
            new_jrnls2 = new_jrnls1.sort_values(by=['eponym_yr'],ascending=True)
            if jrnls:
                options = st.selectbox('5th) Eponyms in selected journals:',
                                  new_jrnls2['eponym_yr'].unique(), format_func=lambda x: ' ' if x == '1' else x)
                df_ep_info = new_jrnls1[new_jrnls1['eponym_yr'].str.match(options)]
                journal = df_ep_info['journal_name'].to_string(index=False)

                if options == "Aaron sign":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Aaron.png'
                    st.image(image, width=160)
                if options == "Allison lung retractor":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Allison.png'
                    st.image(image, width=160)
                if options == "Allison repair":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Allison.png'
                    st.image(image, width=160)
                if options == "Altemeier procedure":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Altemeier.png'
                    st.image(image, width=160)
                if options == "Ambrosetti classification":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Ambrosetti.png'
                    st.image(image, width=160)
                if options == "Amyand hernia":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Amyand.png'
                    st.image(image, width=160)
                if options == "Barrett's oesophagus":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Barrett.png'
                    st.image(image, width=160)
                if options == "Bassini hernia repair":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Bassini.png'
                    st.image(image, width=160)
                if options == "Battle's sign":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Battle.png'
                    st.image(image, width=160)
                if options == "Beger procedure":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Beger.png'
                    st.image(image, width=160)
                if options == "Berry's ligament":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Berry.png'
                    st.image(image, width=160)
                if options == "Brown-Séquard syndrome":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Brown-Sequard.png'
                    st.image(image, width=160)
                if options == "Brooke ileostomy":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Brooke.png'
                    st.image(image, width=160)
                if options == "Calot's triangle":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Calot2.png'
                    st.image(image, width=500)
                if options == "Cushing's ulcer":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Cushing.png'
                    st.image(image, width=160)
                if options == "DeBakey forceps":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_DeBakey_Forceps.png'
                    st.image(image, width=300)
                if options == "De Garengeot's hernia":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_De_Garengeot.png'
                    st.image(image, width=160)
                if options == "Delorme's procedure":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Delorme.png'
                    st.image(image, width=160)
                if options == "Fanelli catheter":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Fanelli.png'
                    st.image(image, width=160)
                if options == "Foley catheter":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Foley.png'
                    st.image(image, width=160)
                if options == "Graves disease":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Graves.png'
                    st.image(image, width=160)
                if options == "Hartmann's operation":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Henri_Hartmann.png'
                    st.image(image, width=160)
                if options == "Hartmann's pouch":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Henri_Hartmann.png'
                    st.image(image, width=160)
                if options == "Hashimoto's thyroiditis":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Hashimoto.png'
                    st.image(image, width=160)
                if options == "Ivor Lewis oesophagectomy":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Ivor_Lewis.png'
                    st.image(image, width=160)
                if options == "Joll's retractor":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Joll.png'
                    st.image(image, width=160)
                if options == "Joll's triangle":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Joll.png'
                    st.image(image, width=160)
                if options == "Killian's triangle":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Killian.png'
                    st.image(image, width=160)
                if options == "Kocher's incision of the abdomen":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Kocher.png'
                    st.image(image, width=160)
                if options == "Kocher maneuver":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Kocher.png'
                    st.image(image, width=160)
                if options == "Meckel's diverticulum":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Meckel.png'
                    st.image(image, width=160)
                if options == "Merendino jejunal interposition":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Merendino.png'
                    st.image(image, width=160)
                if options == "Morrison's pouch":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Morrison.png'
                    st.image(image, width=160)
                if options == "Nodules of Aranzio":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Aranzi.png'
                    st.image(image, width=160)
                if options == "Sphincter of Oddi":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Oddi.png'
                    st.image(image, width=160)
                if options == "Mirizzi's syndrome":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Pablo_Mirizzi.png'
                    st.image(image, width=160)
                if options == "Rouviere's sulcus":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Rouviere.png'
                    st.image(image, width=160)
                if options == "Shouldice hernia repair":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Shouldice.png'
                    st.image(image, width=160)
                if options == "Strasberg's critical view of safety":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Strasberg.png'
                    st.image(image, width=160)
                if options == "Takayasu's arteritis":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Takayasu.jpg'
                    st.image(image, width=160)
                if options == "Ligament of Treitz":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Treitz.png'
                    st.image(image, width=160)
                if options == "Whipple's operation":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Whipple.png'
                    st.image(image, width=160)
                if options == "Foramen of Winslow":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Winslow.png'
                    st.image(image, width=160)


                if df_ep_info['journal_name'].any(): st.write(journal, unsafe_allow_html=True)
                else: pass
                if df_ep_info['year_str'].any():st.write('_When_:',df_ep_info['year_str'].to_string(index=False))
                else: pass
                if df_ep_info['Who'].any():st.write('_Who_:',df_ep_info['Who'].to_string(index=False))
                else: pass

                if df_ep_info['Ref'].any():
                    st.markdown("---")
                    st.write('<u>References</u>', unsafe_allow_html=True)
                    st.write(df_ep_info['Ref'].to_string(index=False), unsafe_allow_html=True)
                else: pass

                #if df_ep_info2['Description'].any():
                #    st.markdown(description, unsafe_allow_html=True)
                #if df_ep_info2['History'].any():
                #    st.write('**_History_**:', history)
                

        if types == 'Selected':
            url_J = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/Eponyms4python_Lite4Journals.csv'
            dfY = pd.read_csv(url_J)
            dfY1 = dfY.dropna()
            dfY1["Journals"] = "Journals"
            df2 = dfY1.sort_values(by=['year'],ascending=True)
            spec_df = df2['specialty'].dropna()
            string = spec_df.str.cat(sep=',')
            splits = string.split(",")
            S = set(splits)
            T = np.array(list(S)).astype(object)
            U = np.sort(T)
            journal_spec = st.multiselect('Specilaties of interest - pick and choose',options=list(U),
                           format_func=lambda x: ' ' if x == '1' else x,
                           default=['Academic','Anaesthetics','Bariatrics','Breast','Cardiothoracics',
                                    'Colorectal','Emergency Surgery','Endocrine','ENT',
                                    'General Surgery','Gynaecology','HPB','Hernia',
                                    'Laparoscopic Surgery','Maxillofacial','Neurosurgery','Obstetrics',
                                    'Oesophagogastric','Orthopaedics','Paediatrics','Plastics','Radiology',
                                    'Transplant','Trauma','Urology','Vascular',])
            min_yrs, max_yrs = st.slider("3rd) Choose time window:", 1700, 2030, [1715, 2021])
            st.markdown("---")
            st.markdown('''<span style="font-size:12pt;color:black;">**Click on journal name to zoom in**,
                       and click in the center to pan out.</span>''', unsafe_allow_html=True)
            new_jrnls1 = df2.loc[df2['specialty'].str.contains('|'.join(journal_spec)) == True]
            new_jrnls1T = new_jrnls1.loc[(new_jrnls1['year'] >= min_yrs) & (new_jrnls1['year'] <= max_yrs)]
            new_jrnls2T = new_jrnls1T.sort_values(by=['eponym'],ascending=True)
            new_jrnls2T["Journals"] = "Journals"
            if not journal_spec == None:
                figJDLT = px.sunburst(new_jrnls2T,path=['Journals','journal_short','year','eponym'],
                                      color='Log2 Google hits',hover_data=['eponym'], color_continuous_scale='rdbu')
                figJDLT.update_layout(margin=dict(l=0, r=0, t=0, b=0),width=700,height=550)
                figJDLT.update_traces(hovertemplate='<b>%{label}</b>')
                st.write(figJDLT)
            st.markdown("---")
            time_jrnl = new_jrnls1T.sort_values(by=['journal'],ascending=True)
            time_jrnl1 = time_jrnl['journal'].dropna()
            string1 = time_jrnl1.str.cat(sep=',')
            splits1 = string1.split(",")
            S1 = set(splits1)
            T1 = np.array(list(S1)).astype(object)
            U1 = np.sort(T1)
        
            jrnls = st.multiselect('4th) Select journals:',options=list(U1),
                              format_func=lambda x: ' ' if x == '1' else x)
            new_jrnls1 = new_jrnls2T.loc[new_jrnls2T['journal'].str.contains('|'.join(jrnls)) == True]
            new_jrnls2 = new_jrnls1.sort_values(by=['eponym_yr'],ascending=True)

            if jrnls:
                options = st.selectbox('5th) Eponyms in selected journals:',
                                  new_jrnls2['eponym_yr'].unique(), format_func=lambda x: ' ' if x == '1' else x)
                df_ep_info = new_jrnls1[new_jrnls1['eponym_yr'].str.match(options)]
                journal = df_ep_info['journal_name'].to_string(index=False)

                if options == "Aaron sign":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Aaron.png'
                    st.image(image, width=160)
                if options == "Allison lung retractor":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Allison.png'
                    st.image(image, width=160)
                if options == "Allison repair":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Allison.png'
                    st.image(image, width=160)
                if options == "Altemeier procedure":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Altemeier.png'
                    st.image(image, width=160)
                if options == "Ambrosetti classification":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Ambrosetti.png'
                    st.image(image, width=160)
                if options == "Amyand hernia":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Amyand.png'
                    st.image(image, width=160)
                if options == "Barrett's oesophagus":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Barrett.png'
                    st.image(image, width=160)
                if options == "Bassini hernia repair":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Bassini.png'
                    st.image(image, width=160)
                if options == "Battle's sign":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Battle.png'
                    st.image(image, width=160)
                if options == "Beger procedure":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Beger.png'
                    st.image(image, width=160)
                if options == "Berry's ligament":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Berry.png'
                    st.image(image, width=160)
                if options == "Brown-Séquard syndrome":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Brown-Sequard.png'
                    st.image(image, width=160)
                if options == "Brooke ileostomy":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Brooke.png'
                    st.image(image, width=160)
                if options == "Calot's triangle":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Calot2.png'
                    st.image(image, width=500)
                if options == "Cushing's ulcer":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Cushing.png'
                    st.image(image, width=160)
                if options == "DeBakey forceps":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_DeBakey_Forceps.png'
                    st.image(image, width=300)
                if options == "De Garengeot's hernia":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_De_Garengeot.png'
                    st.image(image, width=160)
                if options == "Delorme's procedure":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Delorme.png'
                    st.image(image, width=160)
                if options == "Fanelli catheter":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Fanelli.png'
                    st.image(image, width=160)
                if options == "Foley catheter":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Foley.png'
                    st.image(image, width=160)
                if options == "Graves disease":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Graves.png'
                    st.image(image, width=160)
                if options == "Hartmann's operation":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Henri_Hartmann.png'
                    st.image(image, width=160)
                if options == "Hartmann's pouch":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Henri_Hartmann.png'
                    st.image(image, width=160)
                if options == "Hashimoto's thyroiditis":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Hashimoto.png'
                    st.image(image, width=160)
                if options == "Ivor Lewis oesophagectomy":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Ivor_Lewis.png'
                    st.image(image, width=160)
                if options == "Joll's retractor":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Joll.png'
                    st.image(image, width=160)
                if options == "Joll's triangle":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Joll.png'
                    st.image(image, width=160)
                if options == "Killian's triangle":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Killian.png'
                    st.image(image, width=160)
                if options == "Kocher's incision of the abdomen":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Kocher.png'
                    st.image(image, width=160)
                if options == "Kocher maneuver":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Kocher.png'
                    st.image(image, width=160)
                if options == "Meckel's diverticulum":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Meckel.png'
                    st.image(image, width=160)
                if options == "Merendino jejunal interposition":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Merendino.png'
                    st.image(image, width=160)
                if options == "Morrison's pouch":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Morrison.png'
                    st.image(image, width=160)
                if options == "Nodules of Aranzio":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Aranzi.png'
                    st.image(image, width=160)
                if options == "Sphincter of Oddi":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Oddi.png'
                    st.image(image, width=160)
                if options == "Mirizzi's syndrome":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Pablo_Mirizzi.png'
                    st.image(image, width=160)
                if options == "Rouviere's sulcus":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Rouviere.png'
                    st.image(image, width=160)
                if options == "Shouldice hernia repair":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Shouldice.png'
                    st.image(image, width=160)
                if options == "Strasberg's critical view of safety":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Strasberg.png'
                    st.image(image, width=160)
                if options == "Takayasu's arteritis":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Takayasu.jpg'
                    st.image(image, width=160)
                if options == "Ligament of Treitz":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Treitz.png'
                    st.image(image, width=160)
                if options == "Whipple's operation":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Whipple.png'
                    st.image(image, width=160)
                if options == "Foramen of Winslow":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Winslow.png'
                    st.image(image, width=160)

                if df_ep_info['journal_name'].any(): st.write(journal, unsafe_allow_html=True)
                else: pass
                if df_ep_info['year_str'].any():st.write('_When_:',df_ep_info['year_str'].to_string(index=False))
                else: pass
                if df_ep_info['Who'].any():st.write('_Who_:',df_ep_info['Who'].to_string(index=False))
                else: pass
                if df_ep_info['Ref'].any():
                    st.markdown("---")
                    st.write('<u>References</u>', unsafe_allow_html=True)
                    st.write(df_ep_info['Ref'].to_string(index=False), unsafe_allow_html=True)
                else: pass
                
                #if df_ep_info2['Description'].any():
                #    st.markdown(description, unsafe_allow_html=True)
                #if df_ep_info2['History'].any():
                #    st.write('**_History_**:', history)


#-------------------------------------------------------------------------------------------------#
#                                                                                                 #
#  Surgical Operations (5)                                                                        #
# ::: Handles                                                                                     #                                                                                              #
#                                                                                                 #
#-------------------------------------------------------------------------------------------------#
def exp_operation():
    st.write('''_To show sidebar, click **>** in top left_''')
    st.markdown(
        """<style type="text/css" media="screen">.hovertext text {font-size: 20px !important;}
        </style>""",unsafe_allow_html=True,)

    st.title("Find eponyms relevant to your operation") 
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
    eponymByOp = st.multiselect('Step 1) Select from operations:',options=list(U),
                                format_func=lambda x: ' ' if x == '1' else x)
    new_df = df1.loc[df1['Operation'].str.contains('|'.join(eponymByOp)) == True]
    new_df2 = new_df.sort_values(by=['Eponym'],ascending=True)
 
    if eponymByOp:
        options = st.selectbox('Step 2) Search list:', new_df2['Eponym_easy'].unique(),
                                  format_func=lambda x: ' ' if x == '1' else x)
        df_ep_info = new_df[new_df['Eponym_easy'].str.match(options)]
        ep_yr = df_ep_info['Year'].to_string(index=False)

        if options == "Aaron sign":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Aaron.png'
            st.image(image, width=160)
        if options == "Allis forceps":
            image_human = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Allis.png'
            image_forceps = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Allis_Forceps.png'
            col1, col2, col3, col4 = st.beta_columns(4)
            col1.image(image_human, width=160);col2.image(image_forceps, width=386)
            col3.write(''); col4.write('')
        if options == "Allison lung retractor":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Allison.png'
            st.image(image, width=160)
        if options == "Allison repair":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Allison.png'
            st.image(image, width=160)
        if options == "Altemeier procedure":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Altemeier.png'
            st.image(image, width=160)
        if options == "Ambrosetti classification":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Ambrosetti.png'
            st.image(image, width=160)
        if options == "Amyand hernia":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Amyand.png'
            st.image(image, width=160)
        if options == "Babcock forceps":
            image_human = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Babcock.png'
            image_forceps = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Babcock_Forceps2.png'
            col1, col2, col3, col4 = st.beta_columns(4)
            col1.image(image_human, width=160); col2.image(image_forceps, width=297);
            col3.write(''); col4.write('')
        if options == "Barrett's oesophagus":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Barrett.png'
            st.image(image, width=160)
        if options == "Bassini hernia repair":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Bassini.png'
            st.image(image, width=160)
        if options == "Battle's sign":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Battle.png'
            st.image(image, width=160)
        if options == "Beger procedure":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Beger.png'
            st.image(image, width=160)
        if options == "Berry's ligament":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Berry.png'
            st.image(image, width=160)
        if options == "Brown-Séquard syndrome":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Brown-Sequard.png'
            st.image(image, width=160)
        if options == "Brooke ileostomy":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Brooke.png'
            st.image(image, width=160)
        if options == "Calot's triangle":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Calot2.png'
            st.image(image, width=500)
        if options == "Cushing's ulcer":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Cushing.png'
            st.image(image, width=160)
        if options == "DeBakey forceps":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_DeBakey_Forceps.png'
            st.image(image, width=300)
        if options == "De Garengeot's hernia":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_De_Garengeot.png'
            st.image(image, width=160)
        if options == "Delorme's procedure":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Delorme.png'
            st.image(image, width=160)
        if options == "Fanelli catheter":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Fanelli.png'
            st.image(image, width=160)
        if options == "Foley catheter":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Foley.png'
            st.image(image, width=160)
        if options == "Graves disease":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Graves.png'
            st.image(image, width=160)
        if options == "Hartmann's operation":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Henri_Hartmann.png'
            st.image(image, width=160)
        if options == "Hartmann's pouch":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Henri_Hartmann.png'
            st.image(image, width=160)
        if options == "Hashimoto's thyroiditis":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Hashimoto.png'
            st.image(image, width=160)
        if options == "Ivor Lewis oesophagectomy":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Ivor_Lewis.png'
            st.image(image, width=160)
        if options == "Joll's retractor":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Joll.png'
            st.image(image, width=160)
        if options == "Joll's triangle":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Joll.png'
            st.image(image, width=160)
        if options == "Killian's triangle":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Killian.png'
            st.image(image, width=160)
        if options == "Kocher's incision of the abdomen":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Kocher.png'
            st.image(image, width=160)
        if options == "Kocher maneuver":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Kocher.png'
            st.image(image, width=160)
        if options == "Meckel's diverticulum":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Meckel.png'
            st.image(image, width=160)
        if options == "Merendino jejunal interposition":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Merendino.png'
            st.image(image, width=160)
        if options == "Morrison's pouch":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Morrison.png'
            st.image(image, width=160)
        if options == "Nodules of Aranzio":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Aranzi.png'
            st.image(image, width=160)
        if options == "Sphincter of Oddi":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Oddi.png'
            st.image(image, width=160)
        if options == "Mirizzi's syndrome":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Pablo_Mirizzi.png'
            st.image(image, width=160)
        if options == "Rouviere's sulcus":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Rouviere.png'
            st.image(image, width=160)
        if options == "Shouldice hernia repair":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Shouldice.png'
            st.image(image, width=160)
        if options == "Strasberg's critical view of safety":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Strasberg.png'
            st.image(image, width=160)
        if options == "Takayasu's arteritis":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Takayasu.jpg'
            st.image(image, width=160)
        if options == "Ligament of Treitz":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Treitz.png'
            st.image(image, width=160)
        if options == "Whipple's operation":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Whipple.png'
            st.image(image, width=160)
        if options == "Foramen of Winslow":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Winslow.png'
            st.image(image, width=160)

        else:pass
        if df_ep_info['Who'].any(): st.write('*_Who_*:', df_ep_info['Who_B'].to_string(index=False))
        else: pass
        if df_ep_info['Year'].any(): st.write('*_When_*:', df_ep_info['Year_str'].to_string(index=False))
        else:pass
        if df_ep_info['Where'].any(): st.write('*_Where_*:', df_ep_info['Where'].to_string(index=False))
        else:pass

        if df_ep_info['Description'].any():
            st.markdown("---")

        description = df_ep_info['Description'].to_string(index=False)

        if df_ep_info['Description'].any():
            st.markdown(description, unsafe_allow_html=True)
        else:pass

        if df_ep_info['Ref'].any():
            st.markdown("---")
            st.write('<u>References</u>', unsafe_allow_html=True)
            st.write(df_ep_info['Ref'].to_string(index=False), unsafe_allow_html=True)
        else: pass

        if df_ep_info['Pubmed'].any() or df_ep_info['Ref_site'].any() or df_ep_info['Wiki_link'].any() or df_ep_info['WNI_link'].any():
            st.markdown("---")
            st.write('<u>External Links</u>', unsafe_allow_html=True)

        ref_site = df_ep_info['Ref_site'].to_string(index=False)
        if df_ep_info['Ref_site'].any(): st.markdown(f"* **Primary Paper** [webpage]({ref_site})")
        else:pass
        pub_link = df_ep_info['Pubmed'].to_string(index=False)
        if df_ep_info['Pubmed'].any(): st.markdown(f"* **Pubmed** [webpage]({pub_link})")
        else:pass
        wiki_link = df_ep_info['Wiki_link'].to_string(index=False)
        if df_ep_info['Wiki_link'].any(): st.markdown(f"* **Wikipedia** [webpage]({wiki_link})")
        else:pass
        wni_link = df_ep_info['WNI_link'].to_string(index=False)
        if df_ep_info['WNI_link'].any(): st.markdown(f"* **Whonamedit** [webpage]({wni_link})")
        else:pass



#-------------------------------------------------------------------------------------------------#
#                                                                                                 #
#  Geographical Origins (6)                                                                       #
# ::: Handles the                                                                                 #                                                                                              #
#                                                                                                 #
#-------------------------------------------------------------------------------------------------#
def exp_geo():
    st.write('''_To show sidebar, click **>** in top left_''')
    st.title("Geographical origins of eponyms") 
    ScreenSize = st.radio('Step 1) Select screen size:',
                     options=['Smartphone',
                              'Desktop / Laptop / Tablet',],index=0)

    if ScreenSize == "Smartphone":
        st.markdown("""<style type="text/css" media="screen">div[role="listbox"] ul {height:100px}</style>""",unsafe_allow_html=True,)
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
        journal_spec = st.multiselect("Step 2) Select specific specialties:",
             options=list(U), format_func=lambda x: ' ' if x == '1' else x,)
        min_yrs, max_yrs = st.slider("3rd) Optional - define a time window:", 100, 2050, [150, 2021])
        new_geo1 = df2.loc[df2['Topic'].str.contains('|'.join(journal_spec)) == True]
        new_geo2 = new_geo1.sort_values(by=['Year'],ascending=True)
        new_geo2T = new_geo2.loc[(new_geo2['Year'] >= min_yrs) & (new_geo2['Year'] <= max_yrs)]
        site_lat = new_geo2T['Lat_A1']                          
        site_lon = new_geo2T['Long_A1']           
        text = new_geo2T['Eponym_easy'] + ', ' + new_geo2T['CityOfEponym_A1'] + ', ' + new_geo2T['Year'].astype(str)
        locations_name = new_geo2T['Eponym_easy']
        st.markdown("---")
        st.markdown('''<span style="font-size:10pt;color:black;">**Click on a place name to zoom in**,
                       and in the center to pan out.</span>''', unsafe_allow_html=True)

        new_geo2T["World"] = "World"
        figJDLT = px.sunburst(new_geo2T,path=['World',
            'Continent_A1','CountryOfEponym_A1','RegionOfEponym_A1','Eponym_easy'],
                              color='Log10_GxP',hover_data=['Eponym'],color_continuous_scale='viridis',)
        figJDLT.update_layout(margin=dict(l=0, r=0, t=0, b=10),width=380,height=350)
        figJDLT.update_traces(hovertemplate='<b>%{label}</b>') 
        st.write(figJDLT)
        st.markdown('''<span style="font-size:10pt;color:black;">**Zoom** into the map **using touchscreen**.</span>''', unsafe_allow_html=True)
        figG3 = go.Figure()
        figG3.add_trace(go.Scattermapbox(lat=site_lat,lon=site_lon,mode='markers',
                marker=go.scattermapbox.Marker(size=5.6,color='yellow',opacity=0.6),
                text=text,hoverinfo='text',))
        figG3.update_layout(
                autosize=True,hovermode='closest',showlegend=False,width=340,height=240,
                mapbox=dict(accesstoken=mapbox_access_token,bearing=0,center=dict(lat=38,lon=0),
                pitch=5,zoom=-0.47,style='dark'))
        figG3.update_layout(margin=dict(l=2, r=2, t=0, b=0))
        st.write(figG3)
        st.markdown("---")
        blank_row = {'Alphabet':'','Eponym':'1','Eponym_easy':'1','Eponym_easy_yr':'','Topic':'','Disease':'',
                     'Where':'','Operation':'1','Author_1':'1','Year':'','Year_str':'',}  #'Author_1_Role':'1','RegionOfEponym_A1':'',
        new_geo3T = new_geo2T.append(blank_row, ignore_index=True)
        new_geo4T = new_geo3T.sort_values(by=['Eponym'],ascending=True)
        options = st.selectbox('Type here to look up an eponym of interest:',
                    new_geo4T['Eponym_easy'].unique(), format_func=lambda x: ' ' if x == '1' else x)
        df_ep_info = new_geo4T[new_geo4T['Eponym_easy'].str.match(options)]

        if options == "Aaron sign":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Aaron.png'
            st.image(image, width=160)
        if options == "Allis forceps":
            image_human = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Allis.png'
            image_forceps = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Allis_Forceps.png'
            col1, col2, col3, col4 = st.beta_columns(4)
            col1.image(image_human, width=160);col2.image(image_forceps, width=386)
            col3.write(''); col4.write('')
        if options == "Allison lung retractor":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Allison.png'
            st.image(image, width=160)
        if options == "Allison repair":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Allison.png'
            st.image(image, width=160)
        if options == "Altemeier procedure":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Altemeier.png'
            st.image(image, width=160)
        if options == "Ambrosetti classification":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Ambrosetti.png'
            st.image(image, width=160)
        if options == "Amyand hernia":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Amyand.png'
            st.image(image, width=160)
        if options == "Babcock forceps":
            image_human = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Babcock.png'
            image_forceps = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Babcock_Forceps2.png'
            col1, col2, col3, col4 = st.beta_columns(4)
            col1.image(image_human, width=160); col2.image(image_forceps, width=297);
            col3.write(''); col4.write('')
        if options == "Barrett's oesophagus":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Barrett.png'
            st.image(image, width=160)
        if options == "Bassini hernia repair":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Bassini.png'
            st.image(image, width=160)
        if options == "Battle's sign":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Battle.png'
            st.image(image, width=160)
        if options == "Beger procedure":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Beger.png'
            st.image(image, width=160)
        if options == "Berry's ligament":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Berry.png'
            st.image(image, width=160)
        if options == "Brown-Séquard syndrome":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Brown-Sequard.png'
            st.image(image, width=160)
        if options == "Brooke ileostomy":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Brooke.png'
            st.image(image, width=160)
        if options == "Calot's triangle":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Calot2.png'
            st.image(image, width=500)
        if options == "Cushing's ulcer":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Cushing.png'
            st.image(image, width=160)
        if options == "DeBakey forceps":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_DeBakey_Forceps.png'
            st.image(image, width=300)
        if options == "De Garengeot's hernia":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_De_Garengeot.png'
            st.image(image, width=160)
        if options == "Delorme's procedure":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Delorme.png'
            st.image(image, width=160)
        if options == "Fanelli catheter":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Fanelli.png'
            st.image(image, width=160)
        if options == "Foley catheter":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Foley.png'
            st.image(image, width=160)
        if options == "Graves disease":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Graves.png'
            st.image(image, width=160)
        if options == "Hartmann's operation":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Henri_Hartmann.png'
            st.image(image, width=160)
        if options == "Hartmann's pouch":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Henri_Hartmann.png'
            st.image(image, width=160)
        if options == "Hashimoto's thyroiditis":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Hashimoto.png'
            st.image(image, width=160)
        if options == "Ivor Lewis oesophagectomy":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Ivor_Lewis.png'
            st.image(image, width=160)
        if options == "Joll's retractor":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Joll.png'
            st.image(image, width=160)
        if options == "Joll's triangle":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Joll.png'
            st.image(image, width=160)
        if options == "Killian's triangle":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Killian.png'
            st.image(image, width=160)
        if options == "Kocher's incision of the abdomen":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Kocher.png'
            st.image(image, width=160)
        if options == "Kocher maneuver":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Kocher.png'
            st.image(image, width=160)
        if options == "Meckel's diverticulum":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Meckel.png'
            st.image(image, width=160)
        if options == "Merendino jejunal interposition":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Merendino.png'
            st.image(image, width=160)
        if options == "Morrison's pouch":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Morrison.png'
            st.image(image, width=160)
        if options == "Nodules of Aranzio":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Aranzi.png'
            st.image(image, width=160)
        if options == "Sphincter of Oddi":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Oddi.png'
            st.image(image, width=160)
        if options == "Mirizzi's syndrome":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Pablo_Mirizzi.png'
            st.image(image, width=160)
        if options == "Rouviere's sulcus":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Rouviere.png'
            st.image(image, width=160)
        if options == "Shouldice hernia repair":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Shouldice.png'
            st.image(image, width=160)
        if options == "Strasberg's critical view of safety":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Strasberg.png'
            st.image(image, width=160)
        if options == "Takayasu's arteritis":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Takayasu.jpg'
            st.image(image, width=160)
        if options == "Ligament of Treitz":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Treitz.png'
            st.image(image, width=160)
        if options == "Whipple's operation":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Whipple.png'
            st.image(image, width=160)
        if options == "Foramen of Winslow":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Winslow.png'
            st.image(image, width=160)
        
        else:pass
        if df_ep_info['Who'].any(): st.write('*_Who_*:', df_ep_info['Who_B'].to_string(index=False))
        else: pass
        if df_ep_info['Year'].any(): st.write('*_When_*:', df_ep_info['Year_str'].to_string(index=False))
        else:pass
        if df_ep_info['Where'].any(): st.write('*_Where_*:', df_ep_info['Where'].to_string(index=False))
        else:pass

        if df_ep_info['Description'].any():
            st.markdown("---")

        description = df_ep_info['Description'].to_string(index=False)

        if df_ep_info['Description'].any():
            st.markdown(description, unsafe_allow_html=True)
        else:pass

        if df_ep_info['Ref'].any():
            st.markdown("---")
            st.write('<u>References</u>', unsafe_allow_html=True)
            st.write(df_ep_info['Ref'].to_string(index=False), unsafe_allow_html=True)
        else: pass

        if df_ep_info['Pubmed'].any() or df_ep_info['Ref_site'].any() or df_ep_info['Wiki_link'].any() or df_ep_info['WNI_link'].any():
            st.markdown("---")
            st.write('<u>External Links</u>', unsafe_allow_html=True)

        ref_site = df_ep_info['Ref_site'].to_string(index=False)
        if df_ep_info['Ref_site'].any(): st.markdown(f"* **Primary Paper** [webpage]({ref_site})")
        else:pass
        pub_link = df_ep_info['Pubmed'].to_string(index=False)
        if df_ep_info['Pubmed'].any(): st.markdown(f"* **Pubmed** [webpage]({pub_link})")
        else:pass
        wiki_link = df_ep_info['Wiki_link'].to_string(index=False)
        if df_ep_info['Wiki_link'].any(): st.markdown(f"* **Wikipedia** [webpage]({wiki_link})")
        else:pass
        wni_link = df_ep_info['WNI_link'].to_string(index=False)
        if df_ep_info['WNI_link'].any(): st.markdown(f"* **Whonamedit** [webpage]({wni_link})")
        else:pass



    if ScreenSize == "Desktop / Laptop / Tablet":
        types = st.radio('Step 2) Choose specialties:',["All","Selected",])

        if types == 'All':
            min_yrs, max_yrs = st.slider("Step 3) Choose time window:", 100, 2030, [150, 2021])
            st.markdown("---")
            st.markdown("""<style type="text/css" media="screen">div[role="listbox"] ul {height:100px}</style>""",unsafe_allow_html=True,)
            mapbox_access_token = 'pk.eyJ1IjoiYWpoYXllczgzIiwiYSI6ImNrY2pqM2lvMDB4Z24ydG8zdDl0NTYwbTUifQ.2DKVfTAaE77XAXMpDeq_Pg'
            url = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/Eponyms4python_Lite.csv'
            df1 = pd.read_csv(url, dtype={'PMID':str,'Year':int})
            dfT = df1.sort_values(by=['Year'],ascending=True)
            time_df = dfT.loc[(dfT['Year'] >= min_yrs) & (dfT['Year'] <= max_yrs)]
            time_spec_df = time_df['Topic'].dropna()
            string = time_spec_df.str.cat(sep=',')
            splits = string.split(",")
            S = set(splits)
            T = np.array(list(S)).astype(object)
            U = np.sort(T)
            site_lat = time_df['Lat_A1']                            
            site_lon = time_df['Long_A1']           
            text = time_df['Eponym_easy'] + ', ' + time_df['CityOfEponym_A1'] + ', ' + time_df['Year'].astype(str)
            locations_name = time_df['Eponym_easy'] 
            st.markdown('''<span style="font-size:12pt;color:black;">**Click on a place name to zoom in**,
                       and then click in the center to pan out.</span>''', unsafe_allow_html=True)
            time_df["World"] = "World"
            figJDLT = px.sunburst(time_df,path=['World',
                'Continent_A1','CountryOfEponym_A1','RegionOfEponym_A1','Eponym_easy'],
                              color='Log10_GxP',hover_data=['Eponym'],
                              color_continuous_scale='viridis',)#'RdBu'
            figJDLT.update_layout(margin=dict(l=0, r=0, t=0, b=10),width=700,height=550)
            figJDLT.update_traces(hovertemplate='<b>%{label}</b>') 
            st.write(figJDLT)
            options3 = st.selectbox("4th) Type continent, country or city to geolocate. Type over previous, don't try to delete. ",
                                [" ",
                                 "Argentina","Austria","Brazil","Canada",
                                 "Denmark","Edinburgh","England","Europe",
                                 "France","Germany","Hawaii",'India',
                                 "Ireland","Italy","Japan","London",
                                 "Netherlands","New York City","North America",
                                 "Paris","Poland",
                                 "South America","Sweden","Switzerland",
                                 "UK","United Kingdom","USA","Vienna",
                                 "World",])

            if   options3 == " ":              lat_3 = 38.00; lon_3 =  11.0; zoom_country = 0.38; markersize = 7; Screen_width =  700; Screen_height = 430
            if   options3 == "Argentina":      lat_3 =-39.00; lon_3 = -65.0; zoom_country = 2.30; markersize =10; Screen_width =  700; Screen_height = 430
            if   options3 == "Austria":        lat_3 = 47.20; lon_3 =  13.4; zoom_country = 5.80; markersize =11; Screen_width =  700; Screen_height = 430
            if   options3 == "Brazil":         lat_3 =-10.00; lon_3 = -55.0; zoom_country = 2.50; markersize =11; Screen_width =  700; Screen_height = 430
            if   options3 == "Canada":         lat_3 = 61.00; lon_3 = -94.0; zoom_country = 1.90; markersize =10; Screen_width =  700; Screen_height = 430
            if   options3 == "Denmark":        lat_3 = 56.00; lon_3 =  9.70; zoom_country = 5.00; markersize =10; Screen_width =  700; Screen_height = 430
            if   options3 == "Edinburgh":      lat_3 = 55.92; lon_3 =  -3.2; zoom_country = 9.20; markersize =12; Screen_width =  700; Screen_height = 430
            if   options3 == "England":        lat_3 = 52.80; lon_3 =  -3.0; zoom_country = 5.05; markersize =11; Screen_width =  700; Screen_height = 430
            if   options3 == "Europe":         lat_3 = 54.40; lon_3 =  10.0; zoom_country = 2.50; markersize=8.5; Screen_width =  700; Screen_height = 430
            if   options3 == "France":         lat_3 = 47.00; lon_3 =   3.0; zoom_country = 4.50; markersize =10; Screen_width =  700; Screen_height = 430
            if   options3 == "Germany":        lat_3 = 51.30; lon_3 =  10.2; zoom_country = 4.50; markersize =10; Screen_width =  700; Screen_height = 430
            if   options3 == "Hawaii":         lat_3 = 20.50; lon_3 =-157.3; zoom_country = 5.50; markersize = 9; Screen_width =  700; Screen_height = 430
            if   options3 == "India":          lat_3 = 22.00; lon_3 =  80.0; zoom_country = 3.00; markersize = 9; Screen_width =  700; Screen_height = 430
            if   options3 == "Ireland":        lat_3 = 53.50; lon_3 =  -6.2; zoom_country = 5.00; markersize = 9; Screen_width =  700; Screen_height = 430
            if   options3 == "Italy":          lat_3 = 41.80; lon_3 =  14.0; zoom_country = 4.50; markersize =11; Screen_width =  700; Screen_height = 430
            if   options3 == "Japan":          lat_3 = 37.70; lon_3 = 135.5; zoom_country = 3.45; markersize =11; Screen_width =  700; Screen_height = 430
            if   options3 == "London":         lat_3 = 51.54; lon_3 =  -0.1; zoom_country = 8.96; markersize =12; Screen_width =  700; Screen_height = 430
            if   options3 == "Netherlands":    lat_3 = 52.20; lon_3 =   5.0; zoom_country = 6.00; markersize =11; Screen_width =  700; Screen_height = 430
            if   options3 == "New York City":  lat_3 = 40.78; lon_3 = -73.9; zoom_country = 9.00; markersize =11; Screen_width =  700; Screen_height = 430
            if   options3 == "North America":  lat_3 = 51.00; lon_3 =  -103; zoom_country = 1.75; markersize = 9; Screen_width =  700; Screen_height = 430
            if   options3 == "Paris":          lat_3 = 48.86; lon_3 =  2.35; zoom_country = 10.2; markersize =12; Screen_width =  700; Screen_height = 430
            if   options3 == "Poland":         lat_3 = 52.50; lon_3 =  19.0; zoom_country =  5.0; markersize =12; Screen_width =  700; Screen_height = 430
            if   options3 == "South America":  lat_3 =-21.80; lon_3 = -65.0; zoom_country = 1.72; markersize =10; Screen_width =  700; Screen_height = 430
            if   options3 == "Sweden":         lat_3 = 62.85; lon_3 =  18.5; zoom_country = 3.12; markersize =11; Screen_width =  700; Screen_height = 430
            if   options3 == "Switzerland":    lat_3 = 47.00; lon_3 =   8.0; zoom_country =  6.0; markersize =11; Screen_width =  700; Screen_height = 430
            if   options3 == "UK":             lat_3 = 54.45; lon_3 =  -3.2; zoom_country = 4.00; markersize =10; Screen_width =  700; Screen_height = 430
            if   options3 == "United Kingdom": lat_3 = 54.45; lon_3 =  -3.2; zoom_country = 4.00; markersize = 9; Screen_width =  700; Screen_height = 430
            if   options3 == "USA":            lat_3 = 39.00; lon_3 =-105.0; zoom_country = 2.00; markersize =10; Screen_width =  700; Screen_height = 430
            if   options3 == "Vienna":         lat_3 = 48.22; lon_3 = 16.37; zoom_country = 10.0; markersize =11; Screen_width =  700; Screen_height = 430
            if   options3 == "World":          lat_3 = 38.00; lon_3 =  11.0; zoom_country = 0.38; markersize = 7; Screen_width =  700; Screen_height = 430
               
            figG3 = go.Figure()
            figG3.add_trace(go.Scattermapbox(
                    lat=site_lat,lon=site_lon,mode='markers',
                    marker=go.scattermapbox.Marker(
                    size=markersize,color='yellow',opacity=0.7),
                    text=text,hoverinfo='text',))
            figG3.update_layout(
                    autosize=True,hovermode='closest',showlegend=False,
                    width=Screen_width,height=Screen_height,
                    mapbox=dict(accesstoken=mapbox_access_token,bearing=0,center=dict(lat=lat_3,lon=lon_3),
                    pitch=5,zoom=zoom_country,style='dark'))#dark satellite-streets
            figG3.update_layout(margin=dict(l=2, r=2, t=0, b=0))
            st.write(figG3)
            st.markdown('''<span style="font-size:10pt;color:black;">Tip: If map does not locate correctly, press 'Zoom in' on the top right corner.</span>''',
                    unsafe_allow_html=True)
            st.markdown("---")
            blank_row = {'Alphabet':'','Eponym':'1','Eponym_easy':'1','Eponym_easy_yr':'','Topic':'','Disease':'',
                         'Eponym_strip':'','Who':'','Who_B':'','Surname':'','Region_A1':'','RegionOfEponym_A1':'',
                         'Where':'','Author_1_Role':'1','Operation':'1','Author_1':'1','Year':'',
                         'Year_str':'','Sex_A1':'1'}
            time_df = dfT.loc[(dfT['Year'] >= min_yrs) & (dfT['Year'] <= max_yrs)]
            time_df2 = time_df.append(blank_row, ignore_index=True)
            time_df3 = time_df2.sort_values(by=['Eponym'],ascending=True)
            options = st.selectbox('Type here to look up an eponym of interest:',
                        time_df3['Eponym_easy'].unique(), format_func=lambda x: ' ' if x == '1' else x)
            df_ep_info = time_df3[time_df3['Eponym_easy'].str.match(options)]


            if options == "Aaron sign":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Aaron.png'
                st.image(image, width=160)
            if options == "Allis forceps":
                image_human = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Allis.png'
                image_forceps = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Allis_Forceps.png'
                col1, col2, col3, col4 = st.beta_columns(4)
                col1.image(image_human, width=160);col2.image(image_forceps, width=386)
                col3.write(''); col4.write('')
            if options == "Allison lung retractor":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Allison.png'
                st.image(image, width=160)
            if options == "Allison repair":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Allison.png'
                st.image(image, width=160)
            if options == "Altemeier procedure":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Altemeier.png'
                st.image(image, width=160)
            if options == "Ambrosetti classification":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Ambrosetti.png'
                st.image(image, width=160)
            if options == "Amyand hernia":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Amyand.png'
                st.image(image, width=160)
            if options == "Babcock forceps":
                image_human = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Babcock.png'
                image_forceps = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Babcock_Forceps2.png'
                col1, col2, col3, col4 = st.beta_columns(4)
                col1.image(image_human, width=160); col2.image(image_forceps, width=297);
                col3.write(''); col4.write('')
            if options == "Barrett's oesophagus":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Barrett.png'
                st.image(image, width=160)
            if options == "Bassini hernia repair":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Bassini.png'
                st.image(image, width=160)
            if options == "Battle's incision":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Battle.png'
                st.image(image, width=160)
            if options == "Battle's sign":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Battle.png'
                st.image(image, width=160)
            if options == "Beger procedure":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Beger.png'
                st.image(image, width=160)
            if options == "Berry's ligament":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Berry.png'
                st.image(image, width=160)
            if options == "Brown-Séquard syndrome":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Brown-Sequard.png'
                st.image(image, width=160)
            if options == "Brooke ileostomy":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Brooke.png'
                st.image(image, width=160)
            if options == "Calot's triangle":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Calot2.png'
                st.image(image, width=500)
            if options == "Cushing's ulcer":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Cushing.png'
                st.image(image, width=160)
            if options == "DeBakey forceps":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_DeBakey_Forceps.png'
                st.image(image, width=300)
            if options == "De Garengeot's hernia":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_De_Garengeot.png'
                st.image(image, width=160)
            if options == "Delorme's procedure":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Delorme.png'
                st.image(image, width=160)
            if options == "Fanelli catheter":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Fanelli.png'
                st.image(image, width=160)
            if options == "Foley catheter":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Foley.png'
                st.image(image, width=160)
            if options == "Graves disease":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Graves.png'
                st.image(image, width=160)
            if options == "Hartmann's operation":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Henri_Hartmann.png'
                st.image(image, width=160)
            if options == "Hartmann's pouch":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Henri_Hartmann.png'
                st.image(image, width=160)
            if options == "Hashimoto's thyroiditis":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Hashimoto.png'
                st.image(image, width=160)
            if options == "Ivor Lewis oesophagectomy":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Ivor_Lewis.png'
                st.image(image, width=160)
            if options == "Joll's retractor":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Joll.png'
                st.image(image, width=160)
            if options == "Joll's triangle":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Joll.png'
                st.image(image, width=160)
            if options == "Killian's triangle":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Killian.png'
                st.image(image, width=160)
            if options == "Kocher's incision of the abdomen":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Kocher.png'
                st.image(image, width=160)
            if options == "Kocher maneuver":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Kocher.png'
                st.image(image, width=160)
            if options == "Meckel's diverticulum":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Meckel.png'
                st.image(image, width=160)
            if options == "Merendino jejunal interposition":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Merendino.png'
                st.image(image, width=160)
            if options == "Morrison's pouch":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Morrison.png'
                st.image(image, width=160)
            if options == "Nodules of Aranzio":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Aranzi.png'
                st.image(image, width=160)
            if options == "Sphincter of Oddi":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Oddi.png'
                st.image(image, width=160)
            if options == "Mirizzi's syndrome":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Pablo_Mirizzi.png'
                st.image(image, width=160)
            if options == "Rouviere's sulcus":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Rouviere.png'
                st.image(image, width=160)
            if options == "Shouldice hernia repair":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Shouldice.png'
                st.image(image, width=160)
            if options == "Strasberg's critical view of safety":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Strasberg.png'
                st.image(image, width=160)
            if options == "Takayasu's arteritis":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Takayasu.jpg'
                st.image(image, width=160)
            if options == "Ligament of Treitz":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Treitz.png'
                st.image(image, width=160)
            if options == "Whipple's operation":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Whipple.png'
                st.image(image, width=160)
            if options == "Foramen of Winslow":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Winslow.png'
                st.image(image, width=160)

            else:pass
            if df_ep_info['Who'].any(): st.write('*_Who_*:', df_ep_info['Who_B'].to_string(index=False))
            else: pass
            if df_ep_info['Year'].any(): st.write('*_When_*:', df_ep_info['Year_str'].to_string(index=False))
            else:pass
            if df_ep_info['Where'].any(): st.write('*_Where_*:', df_ep_info['Where'].to_string(index=False))
            else:pass

            if df_ep_info['Description'].any():
                description = df_ep_info['Description'].to_string(index=False)
                st.markdown("---")
                st.markdown(description, unsafe_allow_html=True)
            else:pass

            if df_ep_info['Ref'].any():
                st.markdown("---")
                st.write('<u>References</u>', unsafe_allow_html=True)
                st.write(df_ep_info['Ref'].to_string(index=False), unsafe_allow_html=True)
            else: pass

            if df_ep_info['Pubmed'].any() or df_ep_info['Ref_site'].any() or df_ep_info['Wiki_link'].any() or df_ep_info['WNI_link'].any():
                st.markdown("---")
                st.write('<u>External Links</u>', unsafe_allow_html=True)

            ref_site = df_ep_info['Ref_site'].to_string(index=False)
            if df_ep_info['Ref_site'].any(): st.markdown(f"* **Primary Paper** [webpage]({ref_site})")
            else:pass
            pub_link = df_ep_info['Pubmed'].to_string(index=False)
            if df_ep_info['Pubmed'].any(): st.markdown(f"* **Pubmed** [webpage]({pub_link})")
            else:pass
            wiki_link = df_ep_info['Wiki_link'].to_string(index=False)
            if df_ep_info['Wiki_link'].any(): st.markdown(f"* **Wikipedia** [webpage]({wiki_link})")
            else:pass
            wni_link = df_ep_info['WNI_link'].to_string(index=False)
            if df_ep_info['WNI_link'].any(): st.markdown(f"* **Whonamedit** [webpage]({wni_link})")
            else:pass


        if types == 'Selected':
            st.markdown("""<style type="text/css" media="screen">div[role="listbox"] ul {height:100px}</style>""",unsafe_allow_html=True,)
            mapbox_access_token = 'pk.eyJ1IjoiYWpoYXllczgzIiwiYSI6ImNrY2pqM2lvMDB4Z24ydG8zdDl0NTYwbTUifQ.2DKVfTAaE77XAXMpDeq_Pg'
            url = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/Eponyms4python_Lite.csv'
            df1 = pd.read_csv(url, dtype={'PMID':str,'Year':int})
            df1["World"] = "World"
            df2 = df1.sort_values(by=['Year'],ascending=True)
            spec_df = df2['Topic'].dropna()
            string = spec_df.str.cat(sep=',')
            splits = string.split(",")
            S = set(splits)
            T = np.array(list(S)).astype(object)
            U = np.sort(T)
            specs = st.multiselect('Specilaties of interest - pick and choose',options=list(U),
                           format_func=lambda x: ' ' if x == '1' else x,
                           default=['Academic','Anaesthetics','Bariatrics','Breast','Cardiothoracics',
                                    'Colorectal','Emergency Surgery','Endocrine','ENT',
                                    'General Surgery','Gynaecology','HPB','Hernia',
                                    'Laparoscopic Surgery','Maxillofacial','Neurosurgery','Obstetrics',
                                    'Oesophagogastric','Ophthalmology','Orthopaedics','Paediatrics','Plastics',
                                    'Radiology','Transplant','Trauma','Urology','Vascular',]
                                          )
            min_yrs, max_yrs = st.slider("Step 3) Define a time window:", 100, 2050, [150, 2021])
            st.markdown("---")
            st.markdown('''<span style="font-size:12pt;color:black;">**Click on a place name to zoom in**,
                       and then click in the center to pan out.</span>''', unsafe_allow_html=True)
            new_geo1 = df2.loc[df2['Topic'].str.contains('|'.join(specs)) == True]
            new_geo2 = new_geo1.sort_values(by=['Year'],ascending=True)
            new_geo2T = new_geo2.loc[(new_geo2['Year'] >= min_yrs) & (new_geo2['Year'] <= max_yrs)]
            new_geo3T = new_geo2T.sort_values(by=['Eponym'],ascending=True)
            new_geo3T["World"] = "World"

            if not specs == None:
                figJDLT = px.sunburst(new_geo3T,path=['World','Continent_A1','CountryOfEponym_A1','RegionOfEponym_A1','Eponym_easy'],
                              color='Log10_GxP',hover_data=['Eponym'], color_continuous_scale='viridis',)#'RdBu'

                      #inferno,thermal,Magma,Cividis,deep,Viridis,icefire,ylgnbu,'portland','agsunset'
                figJDLT.update_layout(margin=dict(l=0, r=0, t=0, b=10),width=700,height=550)
                figJDLT.update_traces(hovertemplate='<b>%{label}</b>') 
                st.write(figJDLT)

            site_lat = new_geo3T['Lat_A1']                          
            site_lon = new_geo3T['Long_A1']           
            text = new_geo3T['Eponym_easy'] + ', ' + new_geo3T['CityOfEponym_A1'] + ', ' + new_geo3T['Year'].astype(str)
            locations_name = new_geo3T['Eponym_easy']

            options3 = st.selectbox("Step 4) Type continent, country or city to geolocate. Type over previous, don't try to delete. ",
                                [" ",
                                 "Argentina","Austria","Brazil","Canada",
                                 "Denmark","Edinburgh","England","Europe",
                                 "France","Germany","Hawaii",'India',
                                 "Ireland","Italy","Japan","London",
                                 "Netherlands","New York City","North America",
                                 "Paris","Poland",
                                 "South America","Sweden","Switzerland",
                                 "UK","United Kingdom","USA","Vienna",
                                 "World",])

            if   options3 == " ":              lat_3 = 38.00; lon_3 =  11.0; zoom_country = 0.38; markersize = 7; Screen_width =  700; Screen_height = 430
            if   options3 == "Argentina":      lat_3 =-39.00; lon_3 = -65.0; zoom_country = 2.30; markersize =10; Screen_width =  700; Screen_height = 430
            if   options3 == "Austria":        lat_3 = 47.20; lon_3 =  13.4; zoom_country = 5.80; markersize =11; Screen_width =  700; Screen_height = 430
            if   options3 == "Brazil":         lat_3 =-10.00; lon_3 = -55.0; zoom_country = 2.50; markersize =11; Screen_width =  700; Screen_height = 430
            if   options3 == "Canada":         lat_3 = 61.00; lon_3 = -94.0; zoom_country = 1.90; markersize =10; Screen_width =  700; Screen_height = 430
            if   options3 == "Denmark":        lat_3 = 56.00; lon_3 =  9.70; zoom_country = 5.00; markersize =10; Screen_width =  700; Screen_height = 430
            if   options3 == "Edinburgh":      lat_3 = 55.92; lon_3 =  -3.2; zoom_country = 9.20; markersize =12; Screen_width =  700; Screen_height = 430
            if   options3 == "England":        lat_3 = 52.80; lon_3 =  -3.0; zoom_country = 5.05; markersize =11; Screen_width =  700; Screen_height = 430
            if   options3 == "Europe":         lat_3 = 54.40; lon_3 =  10.0; zoom_country = 2.50; markersize=8.5; Screen_width =  700; Screen_height = 430
            if   options3 == "France":         lat_3 = 47.00; lon_3 =   3.0; zoom_country = 4.50; markersize =10; Screen_width =  700; Screen_height = 430
            if   options3 == "Germany":        lat_3 = 51.30; lon_3 =  10.2; zoom_country = 4.50; markersize =10; Screen_width =  700; Screen_height = 430
            if   options3 == "Hawaii":         lat_3 = 20.50; lon_3 =-157.3; zoom_country = 5.50; markersize = 9; Screen_width =  700; Screen_height = 430
            if   options3 == "India":          lat_3 = 22.00; lon_3 =  80.0; zoom_country = 3.00; markersize = 9; Screen_width =  700; Screen_height = 430
            if   options3 == "Ireland":        lat_3 = 53.50; lon_3 =  -6.2; zoom_country = 5.00; markersize = 9; Screen_width =  700; Screen_height = 430
            if   options3 == "Italy":          lat_3 = 41.80; lon_3 =  14.0; zoom_country = 4.50; markersize =11; Screen_width =  700; Screen_height = 430
            if   options3 == "Japan":          lat_3 = 37.70; lon_3 = 135.5; zoom_country = 3.45; markersize =11; Screen_width =  700; Screen_height = 430
            if   options3 == "London":         lat_3 = 51.54; lon_3 =  -0.1; zoom_country = 8.96; markersize =12; Screen_width =  700; Screen_height = 430
            if   options3 == "Netherlands":    lat_3 = 52.20; lon_3 =   5.0; zoom_country = 6.00; markersize =11; Screen_width =  700; Screen_height = 430
            if   options3 == "New York City":  lat_3 = 40.78; lon_3 = -73.9; zoom_country = 9.00; markersize =11; Screen_width =  700; Screen_height = 430
            if   options3 == "North America":  lat_3 = 51.00; lon_3 =  -103; zoom_country = 1.75; markersize = 9; Screen_width =  700; Screen_height = 430
            if   options3 == "Paris":          lat_3 = 48.86; lon_3 =  2.35; zoom_country = 10.2; markersize =12; Screen_width =  700; Screen_height = 430
            if   options3 == "Poland":         lat_3 = 52.50; lon_3 =  19.0; zoom_country =  5.0; markersize =12; Screen_width =  700; Screen_height = 430
            if   options3 == "South America":  lat_3 =-21.80; lon_3 = -65.0; zoom_country = 1.72; markersize =10; Screen_width =  700; Screen_height = 430
            if   options3 == "Sweden":         lat_3 = 62.85; lon_3 =  18.5; zoom_country = 3.12; markersize =11; Screen_width =  700; Screen_height = 430
            if   options3 == "Switzerland":    lat_3 = 47.00; lon_3 =   8.0; zoom_country =  6.0; markersize =11; Screen_width =  700; Screen_height = 430
            if   options3 == "UK":             lat_3 = 54.45; lon_3 =  -3.2; zoom_country = 4.00; markersize =10; Screen_width =  700; Screen_height = 430
            if   options3 == "United Kingdom": lat_3 = 54.45; lon_3 =  -3.2; zoom_country = 4.00; markersize = 9; Screen_width =  700; Screen_height = 430
            if   options3 == "USA":            lat_3 = 39.00; lon_3 =-105.0; zoom_country = 2.00; markersize =10; Screen_width =  700; Screen_height = 430
            if   options3 == "Vienna":         lat_3 = 48.22; lon_3 = 16.37; zoom_country = 10.0; markersize =11; Screen_width =  700; Screen_height = 430
            if   options3 == "World":          lat_3 = 38.00; lon_3 =  11.0; zoom_country = 0.38; markersize = 7; Screen_width =  700; Screen_height = 430
                
            figG3 = go.Figure()
            figG3.add_trace(go.Scattermapbox(
                    lat=site_lat,lon=site_lon,mode='markers',
                    marker=go.scattermapbox.Marker(
                    size=markersize,color='yellow',opacity=0.7),
                    text=text,hoverinfo='text',))
            figG3.update_layout(
                    autosize=True,hovermode='closest',showlegend=False,
                    width=Screen_width,height=Screen_height,
                    mapbox=dict(accesstoken=mapbox_access_token,bearing=0,center=dict(lat=lat_3,lon=lon_3),
                    pitch=5,zoom=zoom_country,style='dark'))#dark satellite-streets
            figG3.update_layout(margin=dict(l=2, r=2, t=0, b=0))
            st.write(figG3)
            
            st.markdown('''<span style="font-size:10pt;color:black;">Tip: If map does not locate correctly, press 'Zoom in' on the top right corner.</span>''',
                    unsafe_allow_html=True)
            st.markdown("---")
            blank_row = {'Alphabet':'','Eponym':'1','Eponym_easy':'1','Eponym_easy_yr':'','Year_str':'','Sex_A1':'1'}
            time_df2 = new_geo2T.append(blank_row, ignore_index=True)
            time_df3 = time_df2.sort_values(by=['Eponym'],ascending=True)
            options = st.selectbox('Type here to look up an eponym of interest:',
                        time_df3['Eponym_easy'].unique(), format_func=lambda x: ' ' if x == '1' else x)
            df_ep_info = time_df3[time_df3['Eponym_easy'].str.match(options)]

            if options == "Aaron sign":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Aaron.png'
                st.image(image, width=160)
            if options == "Allis forceps":
                image_human = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Allis.png'
                image_forceps = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Allis_Forceps.png'
                col1, col2, col3, col4 = st.beta_columns(4)
                col1.image(image_human, width=160);col2.image(image_forceps, width=386)
                col3.write(''); col4.write('')
            if options == "Allison lung retractor":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Allison.png'
                st.image(image, width=160)
            if options == "Allison repair":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Allison.png'
                st.image(image, width=160)
            if options == "Altemeier procedure":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Altemeier.png'
                st.image(image, width=160)
            if options == "Ambrosetti classification":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Ambrosetti.png'
                st.image(image, width=160)
            if options == "Amyand hernia":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Amyand.png'
                st.image(image, width=160)
            if options == "Babcock forceps":
                image_human = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Babcock.png'
                image_forceps = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Babcock_Forceps2.png'
                col1, col2, col3, col4 = st.beta_columns(4)
                col1.image(image_human, width=160); col2.image(image_forceps, width=297);
                col3.write(''); col4.write('')
            if options == "Barrett's oesophagus":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Barrett.png'
                st.image(image, width=160)
            if options == "Bassini hernia repair":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Bassini.png'
                st.image(image, width=160)
            if options == "Battle's incision":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Battle.png'
                st.image(image, width=160)
            if options == "Battle's sign":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Battle.png'
                st.image(image, width=160)
            if options == "Beger procedure":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Beger.png'
                st.image(image, width=160)
            if options == "Berry's ligament":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Berry.png'
                st.image(image, width=160)
            if options == "Brown-Séquard syndrome":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Brown-Sequard.png'
                st.image(image, width=160)
            if options == "Brooke ileostomy":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Brooke.png'
                st.image(image, width=160)
            if options == "Calot's triangle":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Calot2.png'
                st.image(image, width=500)
            if options == "Cushing's ulcer":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Cushing.png'
                st.image(image, width=160)
            if options == "DeBakey forceps":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_DeBakey_Forceps.png'
                st.image(image, width=300)
            if options == "De Garengeot's hernia":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_De_Garengeot.png'
                st.image(image, width=160)
            if options == "Delorme's procedure":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Delorme.png'
                st.image(image, width=160)
            if options == "Fanelli catheter":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Fanelli.png'
                st.image(image, width=160)
            if options == "Foley catheter":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Foley.png'
                st.image(image, width=160)
            if options == "Graves disease":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Graves.png'
                st.image(image, width=160)
            if options == "Hartmann's operation":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Henri_Hartmann.png'
                st.image(image, width=160)
            if options == "Hartmann's pouch":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Henri_Hartmann.png'
                st.image(image, width=160)
            if options == "Hashimoto's thyroiditis":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Hashimoto.png'
                st.image(image, width=160)
            if options == "Ivor Lewis oesophagectomy":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Ivor_Lewis.png'
                st.image(image, width=160)
            if options == "Joll's retractor":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Joll.png'
                st.image(image, width=160)
            if options == "Joll's triangle":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Joll.png'
                st.image(image, width=160)
            if options == "Killian's triangle":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Killian.png'
                st.image(image, width=160)
            if options == "Kocher's incision of the abdomen":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Kocher.png'
                st.image(image, width=160)
            if options == "Kocher maneuver":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Kocher.png'
                st.image(image, width=160)
            if options == "Meckel's diverticulum":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Meckel.png'
                st.image(image, width=160)
            if options == "Merendino jejunal interposition":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Merendino.png'
                st.image(image, width=160)
            if options == "Morrison's pouch":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Morrison.png'
                st.image(image, width=160)
            if options == "Nodules of Aranzio":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Aranzi.png'
                st.image(image, width=160)
            if options == "Sphincter of Oddi":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Oddi.png'
                st.image(image, width=160)
            if options == "Mirizzi's syndrome":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Pablo_Mirizzi.png'
                st.image(image, width=160)
            if options == "Rouviere's sulcus":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Rouviere.png'
                st.image(image, width=160)
            if options == "Shouldice hernia repair":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Shouldice.png'
                st.image(image, width=160)
            if options == "Strasberg's critical view of safety":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Strasberg.png'
                st.image(image, width=160)
            if options == "Takayasu's arteritis":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Takayasu.jpg'
                st.image(image, width=160)
            if options == "Ligament of Treitz":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Treitz.png'
                st.image(image, width=160)
            if options == "Whipple's operation":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Whipple.png'
                st.image(image, width=160)
            if options == "Foramen of Winslow":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Winslow.png'
                st.image(image, width=160)

            else:pass
            if df_ep_info['Who'].any(): st.write('*_Who_*:', df_ep_info['Who_B'].to_string(index=False))
            else: pass
            if df_ep_info['Year'].any(): st.write('*_When_*:', df_ep_info['Year_str'].to_string(index=False))
            else:pass
            if df_ep_info['Where'].any(): st.write('*_Where_*:', df_ep_info['Where'].to_string(index=False))
            else:pass

            if df_ep_info['Description'].any():
                description = df_ep_info['Description'].to_string(index=False)
                st.markdown("---")
                st.markdown(description, unsafe_allow_html=True)
            else:pass

            if df_ep_info['Pubmed'].any() or df_ep_info['Wiki_link'].any() or df_ep_info['WNI_link'].any() or df_ep_info['ICD11_link'].any():
                st.markdown("---")
                st.write('**External Links**')
        
            ref_link = df_ep_info['Pubmed'].to_string(index=False)
            if df_ep_info['Pubmed'].any(): st.markdown(f"[PubMed.gov]({ref_link})")
            else:pass
            wiki_link = df_ep_info['Wiki_link'].to_string(index=False)
            if df_ep_info['Wiki_link'].any():st.markdown(f"[Wikipedia.org]({wiki_link})")
            else:pass
            wni_link = df_ep_info['WNI_link'].to_string(index=False)
            if df_ep_info['WNI_link'].any():st.markdown(f"[Whonamedit.com]({wni_link})")
            else:pass

#-------------------------------------------------------------------------------------------------#
#                                                                                                 #
#  Categories (7)                                                                                 #
# ::: Handles the                                                                                 #                                                                                              #
#                                                                                                 #
#-------------------------------------------------------------------------------------------------#
def exp_cats():
    st.write('''_To show sidebar, click **>** in top left_''')
    st.title('Search by category type')
    ScreenSize = st.radio('Step 1) Select screen size:',
                     options=['Smartphone',
                              'Desktop / Laptop / Tablet',],index=0)

    if ScreenSize == "Smartphone":
        types = st.radio('Step 2) Choose specialties:',["All","Selected",])
        if types == "All":
            url = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/Eponyms4python_Lite.csv'
            df1 = pd.read_csv(url, dtype={'PMID':str,'Year':int})
            df2 = df1.sort_values(by=['Year'],ascending=True)
            spec_df = df2['Type'].dropna()
            string = spec_df.str.cat(sep=',')
            splits = string.split(",")
            S = set(splits)
            T = np.array(list(S)).astype(object)
            U = np.sort(T)
            min_yrs, max_yrs = st.slider("Step 3) Define a time window:", 100, 2050, [150, 2021])
            st.markdown("---")
            new_geo2 = df2.sort_values(by=['Year'],ascending=True)
            new_geo2T = new_geo2.loc[(new_geo2['Year'] >= min_yrs) & (new_geo2['Year'] <= max_yrs)]
            st.markdown('''<span style="font-size:10pt;color:black;">**Click on a category type to zoom in**,
                           and click in the center to pan out.</span>''', unsafe_allow_html=True)
            new_geo2T["Categories"] = "Categories"
            figJDLT = px.sunburst(new_geo2T,path=['Categories','Type_short','Eponym_easy'],
                              color='Log2_GxP',hover_data=['Eponym'],values='Year',
                              color_continuous_scale='Magma',)#'RdBu'viridis
            figJDLT.update_layout(margin=dict(l=0, r=0, t=0, b=10),width=350,height=350)
            figJDLT.update_traces(hovertemplate='<b>%{label}</b>') 
            st.write(figJDLT)
            blank_row = {'Alphabet':'','Eponym':'1','Eponym_easy':'1','Eponym_easy_yr':'','Topic':'','Where':'','Author_1_Role':'1',}
            time_df2 = new_geo2T.append(blank_row, ignore_index=True)
            time_df3 = time_df2.sort_values(by=['Eponym'],ascending=True)
            st.markdown("---")
            options = st.selectbox('Type here to look up an eponym of interest:',
                        time_df3['Eponym_easy'].unique(), format_func=lambda x: ' ' if x == '1' else x)
            df_ep_info = time_df3[time_df3['Eponym_easy'].str.match(options)]
            
            if options == "Aaron sign":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Aaron.png'
                st.image(image, width=160)
            if options == "Allis forceps":
                image_human = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Allis.png'
                image_forceps = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Allis_Forceps.png'
                col1, col2, col3, col4 = st.beta_columns(4)
                col1.image(image_human, width=160);col2.image(image_forceps, width=386)
                col3.write(''); col4.write('')
            if options == "Allison lung retractor":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Allison.png'
                st.image(image, width=160)
            if options == "Allison repair":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Allison.png'
                st.image(image, width=160)
            if options == "Altemeier procedure":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Altemeier.png'
                st.image(image, width=160)
            if options == "Ambrosetti classification":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Ambrosetti.png'
                st.image(image, width=160)
            if options == "Amyand hernia":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Amyand.png'
                st.image(image, width=160)
            if options == "Babcock forceps":
                image_human = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Babcock.png'
                image_forceps = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Babcock_Forceps2.png'
                col1, col2, col3, col4 = st.beta_columns(4)
                col1.image(image_human, width=160); col2.image(image_forceps, width=297);
                col3.write(''); col4.write('')
            if options == "Barrett's oesophagus":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Barrett.png'
                st.image(image, width=160)
            if options == "Bassini hernia repair":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Bassini.png'
                st.image(image, width=160)
            if options == "Battle's incision":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Battle.png'
                st.image(image, width=160)
            if options == "Battle's sign":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Battle.png'
                st.image(image, width=160)
            if options == "Beger procedure":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Beger.png'
                st.image(image, width=160)
            if options == "Berry's ligament":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Berry.png'
                st.image(image, width=160)
            if options == "Brown-Séquard syndrome":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Brown-Sequard.png'
                st.image(image, width=160)
            if options == "Brooke ileostomy":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Brooke.png'
                st.image(image, width=160)
            if options == "Calot's triangle":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Calot2.png'
                st.image(image, width=500)
            if options == "Cushing's ulcer":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Cushing.png'
                st.image(image, width=160)
            if options == "DeBakey forceps":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_DeBakey_Forceps.png'
                st.image(image, width=300)
            if options == "De Garengeot's hernia":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_De_Garengeot.png'
                st.image(image, width=160)
            if options == "Delorme's procedure":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Delorme.png'
                st.image(image, width=160)
            if options == "Fanelli catheter":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Fanelli.png'
                st.image(image, width=160)
            if options == "Foley catheter":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Foley.png'
                st.image(image, width=160)
            if options == "Graves disease":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Graves.png'
                st.image(image, width=160)
            if options == "Hartmann's operation":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Henri_Hartmann.png'
                st.image(image, width=160)
            if options == "Hartmann's pouch":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Henri_Hartmann.png'
                st.image(image, width=160)
            if options == "Hashimoto's thyroiditis":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Hashimoto.png'
                st.image(image, width=160)
            if options == "Ivor Lewis oesophagectomy":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Ivor_Lewis.png'
                st.image(image, width=160)
            if options == "Joll's retractor":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Joll.png'
                st.image(image, width=160)
            if options == "Joll's triangle":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Joll.png'
                st.image(image, width=160)
            if options == "Killian's triangle":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Killian.png'
                st.image(image, width=160)
            if options == "Kocher's incision of the abdomen":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Kocher.png'
                st.image(image, width=160)
            if options == "Kocher maneuver":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Kocher.png'
                st.image(image, width=160)
            if options == "Meckel's diverticulum":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Meckel.png'
                st.image(image, width=160)
            if options == "Merendino jejunal interposition":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Merendino.png'
                st.image(image, width=160)
            if options == "Morrison's pouch":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Morrison.png'
                st.image(image, width=160)
            if options == "Nodules of Aranzio":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Aranzi.png'
                st.image(image, width=160)
            if options == "Sphincter of Oddi":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Oddi.png'
                st.image(image, width=160)
            if options == "Mirizzi's syndrome":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Pablo_Mirizzi.png'
                st.image(image, width=160)
            if options == "Rouviere's sulcus":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Rouviere.png'
                st.image(image, width=160)
            if options == "Shouldice hernia repair":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Shouldice.png'
                st.image(image, width=160)
            if options == "Strasberg's critical view of safety":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Strasberg.png'
                st.image(image, width=160)
            if options == "Takayasu's arteritis":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Takayasu.jpg'
                st.image(image, width=160)
            if options == "Ligament of Treitz":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Treitz.png'
                st.image(image, width=160)
            if options == "Whipple's operation":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Whipple.png'
                st.image(image, width=160)
            if options == "Foramen of Winslow":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Winslow.png'
                st.image(image, width=160)
                
            else:pass
            if df_ep_info['Who'].any(): st.write('*_Who_*:', df_ep_info['Who_B'].to_string(index=False))
            else: pass
            if df_ep_info['Year'].any(): st.write('*_When_*:', df_ep_info['Year_str'].to_string(index=False))
            else:pass
            if df_ep_info['Where'].any(): st.write('*_Where_*:', df_ep_info['Where'].to_string(index=False))
            else:pass
            if df_ep_info['Description'].any() or df_ep_info['History'].any():
                st.markdown("---")
            description = df_ep_info['Description'].to_string(index=False)
            if df_ep_info['Description'].any():
                st.markdown(description, unsafe_allow_html=True)
            else:pass
            if df_ep_info['Ref'].any():
                st.markdown("---")
                st.write('<u>References</u>', unsafe_allow_html=True)
                st.write(df_ep_info['Ref'].to_string(index=False), unsafe_allow_html=True)
            else:pass
            if df_ep_info['Pubmed'].any() or df_ep_info['Ref_site'].any() or df_ep_info['Wiki_link'].any() or df_ep_info['WNI_link'].any() or df_ep_info['ICD11_link'].any():
                st.markdown("---")
                st.write('<u>External Links</u>', unsafe_allow_html=True)
            ref_site = df_ep_info['Ref_site'].to_string(index=False)
            if df_ep_info['Ref_site'].any(): st.markdown(f"* **Primary Paper** [webpage]({ref_site})")
            else:pass
            pub_link = df_ep_info['Pubmed'].to_string(index=False)
            if df_ep_info['Pubmed'].any(): st.markdown(f"* **Pubmed** [webpage]({pub_link})")
            else:pass
            wiki_link = df_ep_info['Wiki_link'].to_string(index=False)
            if df_ep_info['Wiki_link'].any(): st.markdown(f"* **Wikipedia** [webpage]({wiki_link})")
            else:pass
            wni_link = df_ep_info['WNI_link'].to_string(index=False)
            if df_ep_info['WNI_link'].any(): st.markdown(f"* **Whonamedit** [webpage]({wni_link})")
            else:pass

        if types == "Selected":
            url = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/Eponyms4python_Lite.csv'
            df1 = pd.read_csv(url, dtype={'PMID':str,'Year':int})
            df2 = df1.sort_values(by=['Eponym'],ascending=True)
            spec_df = df2['Topic'].dropna()
            string = spec_df.str.cat(sep=',')
            splits = string.split(",")
            S = set(splits)
            T = np.array(list(S)).astype(object)
            U = np.sort(T)
            specs = st.multiselect('Specilaties of interest - pick and choose',options=list(U),
                           format_func=lambda x: ' ' if x == '1' else x,
                           default=['Academic','Anaesthetics','Bariatrics','Breast','Cardiothoracics',
                                    'Colorectal','Emergency Surgery','Endocrine','ENT',
                                    'General Surgery','Gynaecology','HPB','Hernia',
                                    'Laparoscopic Surgery','Maxillofacial','Neurosurgery','Obstetrics',
                                    'Oesophagogastric','Ophthalmology','Orthopaedics','Paediatrics','Plastics',
                                    'Radiology','Transplant','Trauma','Urology','Vascular',]
                                          )
            min_yrs, max_yrs = st.slider("Step 3) Define a time window:", 100, 2050, [150, 2021])
            st.markdown("---")
            st.markdown('''<span style="font-size:10pt;color:black;">**Click on a category type to zoom in**,
                           and click in the center to pan out.</span>''', unsafe_allow_html=True)
            new_1T = df2.loc[(df2['Year'] >= min_yrs) & (df2['Year'] <= max_yrs)]
            new_2T = new_1T.loc[new_1T['Topic'].str.contains('|'.join(specs)) == True]
            new_3T = new_2T.sort_values(by=['Eponym'],ascending=True)
            new_3T["Categories"] = "Categories"
            figJDLT = px.sunburst(new_3T,path=['Categories','Type_short','Eponym_easy'],
                              color='Log2_GxP',hover_data=['Eponym'],values='Year',
                              color_continuous_scale='Magma',)#'RdBu'viridis
            figJDLT.update_layout(margin=dict(l=0, r=0, t=0, b=10),width=350,height=350)
            figJDLT.update_traces(hovertemplate='<b>%{label}</b>') 
            st.write(figJDLT)
            blank_row = {'Alphabet':'','Eponym':'1','Eponym_easy':'1','Eponym_easy_yr':'','Topic':'','Disease':'',}
            time_df2 = new_2T.append(blank_row, ignore_index=True)
            time_df3 = time_df2.sort_values(by=['Eponym'],ascending=True)
            st.markdown("---")
            options = st.selectbox('Type here to look up an eponym of interest:',
                        time_df3['Eponym_easy'].unique(), format_func=lambda x: ' ' if x == '1' else x)
            df_ep_info = time_df3[time_df3['Eponym_easy'].str.match(options)]

            if options == "Aaron sign":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Aaron.png'
                st.image(image, width=160)
            if options == "Allis forceps":
                image_human = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Allis.png'
                image_forceps = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Allis_Forceps.png'
                col1, col2, col3, col4 = st.beta_columns(4)
                col1.image(image_human, width=160);col2.image(image_forceps, width=386)
                col3.write(''); col4.write('')
            if options == "Allison lung retractor":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Allison.png'
                st.image(image, width=160)
            if options == "Allison repair":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Allison.png'
                st.image(image, width=160)
            if options == "Altemeier procedure":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Altemeier.png'
                st.image(image, width=160)
            if options == "Ambrosetti classification":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Ambrosetti.png'
                st.image(image, width=160)
            if options == "Amyand hernia":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Amyand.png'
                st.image(image, width=160)
            if options == "Babcock forceps":
                image_human = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Babcock.png'
                image_forceps = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Babcock_Forceps2.png'
                col1, col2, col3, col4 = st.beta_columns(4)
                col1.image(image_human, width=160); col2.image(image_forceps, width=297);
                col3.write(''); col4.write('')
            if options == "Barrett's oesophagus":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Barrett.png'
                st.image(image, width=160)
            if options == "Bassini hernia repair":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Bassini.png'
                st.image(image, width=160)
            if options == "Battle's incision":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Battle.png'
                st.image(image, width=160)
            if options == "Battle's sign":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Battle.png'
                st.image(image, width=160)
            if options == "Beger procedure":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Beger.png'
                st.image(image, width=160)
            if options == "Berry's ligament":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Berry.png'
                st.image(image, width=160)
            if options == "Brown-Séquard syndrome":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Brown-Sequard.png'
                st.image(image, width=160)
            if options == "Brooke ileostomy":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Brooke.png'
                st.image(image, width=160)
            if options == "Calot's triangle":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Calot2.png'
                st.image(image, width=500)
            if options == "Cushing's ulcer":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Cushing.png'
                st.image(image, width=160)
            if options == "DeBakey forceps":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_DeBakey_Forceps.png'
                st.image(image, width=300)
            if options == "De Garengeot's hernia":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_De_Garengeot.png'
                st.image(image, width=160)
            if options == "Delorme's procedure":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Delorme.png'
                st.image(image, width=160)
            if options == "Fanelli catheter":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Fanelli.png'
                st.image(image, width=160)
            if options == "Foley catheter":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Foley.png'
                st.image(image, width=160)
            if options == "Graves disease":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Graves.png'
                st.image(image, width=160)
            if options == "Hartmann's operation":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Henri_Hartmann.png'
                st.image(image, width=160)
            if options == "Hartmann's pouch":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Henri_Hartmann.png'
                st.image(image, width=160)
            if options == "Hashimoto's thyroiditis":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Hashimoto.png'
                st.image(image, width=160)
            if options == "Ivor Lewis oesophagectomy":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Ivor_Lewis.png'
                st.image(image, width=160)
            if options == "Joll's retractor":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Joll.png'
                st.image(image, width=160)
            if options == "Joll's triangle":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Joll.png'
                st.image(image, width=160)
            if options == "Killian's triangle":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Killian.png'
                st.image(image, width=160)
            if options == "Kocher's incision of the abdomen":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Kocher.png'
                st.image(image, width=160)
            if options == "Kocher maneuver":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Kocher.png'
                st.image(image, width=160)
            if options == "Meckel's diverticulum":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Meckel.png'
                st.image(image, width=160)
            if options == "Merendino jejunal interposition":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Merendino.png'
                st.image(image, width=160)
            if options == "Morrison's pouch":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Morrison.png'
                st.image(image, width=160)
            if options == "Nodules of Aranzio":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Aranzi.png'
                st.image(image, width=160)
            if options == "Sphincter of Oddi":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Oddi.png'
                st.image(image, width=160)
            if options == "Mirizzi's syndrome":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Pablo_Mirizzi.png'
                st.image(image, width=160)
            if options == "Rouviere's sulcus":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Rouviere.png'
                st.image(image, width=160)
            if options == "Shouldice hernia repair":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Shouldice.png'
                st.image(image, width=160)
            if options == "Strasberg's critical view of safety":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Strasberg.png'
                st.image(image, width=160)
            if options == "Takayasu's arteritis":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Takayasu.jpg'
                st.image(image, width=160)
            if options == "Ligament of Treitz":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Treitz.png'
                st.image(image, width=160)
            if options == "Whipple's operation":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Whipple.png'
                st.image(image, width=160)
            if options == "Foramen of Winslow":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Winslow.png'
                st.image(image, width=160)

            else:pass
            if df_ep_info['Who'].any(): st.write('*_Who_*:', df_ep_info['Who_B'].to_string(index=False))
            else: pass
            if df_ep_info['Year'].any(): st.write('*_When_*:', df_ep_info['Year_str'].to_string(index=False))
            else:pass
            if df_ep_info['Where'].any(): st.write('*_Where_*:', df_ep_info['Where'].to_string(index=False))
            else:pass
            if df_ep_info['Description'].any() or df_ep_info['History'].any():
                st.markdown("---")
            description = df_ep_info['Description'].to_string(index=False)
            if df_ep_info['Description'].any():
                st.markdown(description, unsafe_allow_html=True)
            else:pass
            if df_ep_info['Ref'].any():
                st.markdown("---")
                st.write('<u>References</u>', unsafe_allow_html=True)
                st.write(df_ep_info['Ref'].to_string(index=False), unsafe_allow_html=True)
            else:pass
            if df_ep_info['Pubmed'].any() or df_ep_info['Ref_site'].any() or df_ep_info['Wiki_link'].any() or df_ep_info['WNI_link'].any() or df_ep_info['ICD11_link'].any():
                st.markdown("---")
                st.write('<u>External Links</u>', unsafe_allow_html=True)
            ref_site = df_ep_info['Ref_site'].to_string(index=False)
            if df_ep_info['Ref_site'].any(): st.markdown(f"* **Primary Paper** [webpage]({ref_site})")
            else:pass
            pub_link = df_ep_info['Pubmed'].to_string(index=False)
            if df_ep_info['Pubmed'].any(): st.markdown(f"* **Pubmed** [webpage]({pub_link})")
            else:pass
            wiki_link = df_ep_info['Wiki_link'].to_string(index=False)
            if df_ep_info['Wiki_link'].any(): st.markdown(f"* **Wikipedia** [webpage]({wiki_link})")
            else:pass
            wni_link = df_ep_info['WNI_link'].to_string(index=False)
            if df_ep_info['WNI_link'].any(): st.markdown(f"* **Whonamedit** [webpage]({wni_link})")
            else:pass


    if ScreenSize == "Desktop / Laptop / Tablet":
        types = st.radio('2nd) Optional - choose specialties:',["All","Selected",])
        if types == "All":
            url = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/Eponyms4python_Lite.csv'
            df1 = pd.read_csv(url, dtype={'PMID':str,'Year':int})
            df2 = df1.sort_values(by=['Year'],ascending=True)
            spec_df = df2['Type'].dropna()
            string = spec_df.str.cat(sep=',')
            splits = string.split(",")
            S = set(splits)
            T = np.array(list(S)).astype(object)
            U = np.sort(T)
            min_yrs, max_yrs = st.slider("3rd) Optional - define a time window:", 100, 2050, [150, 2021])
            st.markdown("---")
            st.markdown('''<span style="font-size:12pt;color:black;">**Click on a category type to zoom in**,
                           and click in the center to pan out.</span>''', unsafe_allow_html=True)
            new_geo2 = df2.sort_values(by=['Year'],ascending=True)
            new_geo2T = new_geo2.loc[(new_geo2['Year'] >= min_yrs) & (new_geo2['Year'] <= max_yrs)]
            new_geo2T["Categories"] = "Categories"
            figJDLT = px.sunburst(new_geo2T,path=['Categories','Type_short','Eponym_easy'],
                              color='Log2_GxP',hover_data=['Eponym'],values='Year',
                              color_continuous_scale='Magma',)#'RdBu'viridis
            figJDLT.update_layout(margin=dict(l=0, r=0, t=0, b=10),width=700,height=550)
            figJDLT.update_traces(hovertemplate='<b>%{label}</b>') 
            st.write(figJDLT)
            blank_row = {'Alphabet':'','Eponym':'1','Eponym_easy':'1','Eponym_easy_yr':'','Topic':'','Disease':'',
                         'Eponym_strip':'','Who':'','Who_B':'','Surname':'','Region_A1':'','RegionOfEponym_A1':'',
                         'Where':'','Author_1_Role':'1','Operation':'1','Author_1':'1','Year':'','Year_str':'','Sex_A1':'1'}
            time_df2 = new_geo2T.append(blank_row, ignore_index=True)
            time_df3 = time_df2.sort_values(by=['Eponym'],ascending=True)
            st.markdown("---")
            options = st.selectbox('Type here to look up an eponym of interest:',
                        time_df3['Eponym_easy'].unique(), format_func=lambda x: ' ' if x == '1' else x)
            df_ep_info = time_df3[time_df3['Eponym_easy'].str.match(options)]

            if options == "Aaron sign":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Aaron.png'
                st.image(image, width=160)
            if options == "Allis forceps":
                image_human = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Allis.png'
                image_forceps = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Allis_Forceps.png'
                col1, col2, col3, col4 = st.beta_columns(4)
                col1.image(image_human, width=160);col2.image(image_forceps, width=386)
                col3.write(''); col4.write('')
            if options == "Allison lung retractor":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Allison.png'
                st.image(image, width=160)
            if options == "Allison repair":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Allison.png'
                st.image(image, width=160)
            if options == "Altemeier procedure":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Altemeier.png'
                st.image(image, width=160)
            if options == "Ambrosetti classification":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Ambrosetti.png'
                st.image(image, width=160)
            if options == "Amyand hernia":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Amyand.png'
                st.image(image, width=160)
            if options == "Babcock forceps":
                image_human = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Babcock.png'
                image_forceps = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Babcock_Forceps2.png'
                col1, col2, col3, col4 = st.beta_columns(4)
                col1.image(image_human, width=160); col2.image(image_forceps, width=297);
                col3.write(''); col4.write('')
            if options == "Barrett's oesophagus":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Barrett.png'
                st.image(image, width=160)
            if options == "Bassini hernia repair":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Bassini.png'
                st.image(image, width=160)
            if options == "Battle's incision":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Battle.png'
                st.image(image, width=160)
            if options == "Battle's sign":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Battle.png'
                st.image(image, width=160)
            if options == "Beger procedure":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Beger.png'
                st.image(image, width=160)
            if options == "Berry's ligament":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Berry.png'
                st.image(image, width=160)
            if options == "Brown-Séquard syndrome":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Brown-Sequard.png'
                st.image(image, width=160)
            if options == "Brooke ileostomy":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Brooke.png'
                st.image(image, width=160)
            if options == "Calot's triangle":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Calot2.png'
                st.image(image, width=500)
            if options == "Cushing's ulcer":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Cushing.png'
                st.image(image, width=160)
            if options == "DeBakey forceps":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_DeBakey_Forceps.png'
                st.image(image, width=300)
            if options == "De Garengeot's hernia":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_De_Garengeot.png'
                st.image(image, width=160)
            if options == "Delorme's procedure":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Delorme.png'
                st.image(image, width=160)
            if options == "Fanelli catheter":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Fanelli.png'
                st.image(image, width=160)
            if options == "Foley catheter":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Foley.png'
                st.image(image, width=160)
            if options == "Graves disease":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Graves.png'
                st.image(image, width=160)
            if options == "Hartmann's operation":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Henri_Hartmann.png'
                st.image(image, width=160)
            if options == "Hartmann's pouch":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Henri_Hartmann.png'
                st.image(image, width=160)
            if options == "Hashimoto's thyroiditis":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Hashimoto.png'
                st.image(image, width=160)
            if options == "Ivor Lewis oesophagectomy":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Ivor_Lewis.png'
                st.image(image, width=160)
            if options == "Joll's retractor":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Joll.png'
                st.image(image, width=160)
            if options == "Joll's triangle":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Joll.png'
                st.image(image, width=160)
            if options == "Killian's triangle":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Killian.png'
                st.image(image, width=160)
            if options == "Kocher's incision of the abdomen":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Kocher.png'
                st.image(image, width=160)
            if options == "Kocher maneuver":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Kocher.png'
                st.image(image, width=160)
            if options == "Meckel's diverticulum":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Meckel.png'
                st.image(image, width=160)
            if options == "Merendino jejunal interposition":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Merendino.png'
                st.image(image, width=160)
            if options == "Morrison's pouch":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Morrison.png'
                st.image(image, width=160)
            if options == "Nodules of Aranzio":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Aranzi.png'
                st.image(image, width=160)
            if options == "Sphincter of Oddi":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Oddi.png'
                st.image(image, width=160)
            if options == "Mirizzi's syndrome":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Pablo_Mirizzi.png'
                st.image(image, width=160)
            if options == "Rouviere's sulcus":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Rouviere.png'
                st.image(image, width=160)
            if options == "Shouldice hernia repair":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Shouldice.png'
                st.image(image, width=160)
            if options == "Strasberg's critical view of safety":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Strasberg.png'
                st.image(image, width=160)
            if options == "Takayasu's arteritis":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Takayasu.jpg'
                st.image(image, width=160)
            if options == "Ligament of Treitz":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Treitz.png'
                st.image(image, width=160)
            if options == "Whipple's operation":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Whipple.png'
                st.image(image, width=160)
            if options == "Foramen of Winslow":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Winslow.png'
                st.image(image, width=160)

            else:pass
            if df_ep_info['Who'].any(): st.write('*_Who_*:', df_ep_info['Who_B'].to_string(index=False))
            else: pass
            if df_ep_info['Year'].any(): st.write('*_When_*:', df_ep_info['Year_str'].to_string(index=False))
            else:pass
            if df_ep_info['Where'].any(): st.write('*_Where_*:', df_ep_info['Where'].to_string(index=False))
            else:pass
            if df_ep_info['Description'].any() or df_ep_info['History'].any():
                st.markdown("---")
            description = df_ep_info['Description'].to_string(index=False)
            if df_ep_info['Description'].any():
                st.markdown(description, unsafe_allow_html=True)
            else:pass
            if df_ep_info['Ref'].any():
                st.markdown("---")
                st.write('<u>References</u>', unsafe_allow_html=True)
                st.write(df_ep_info['Ref'].to_string(index=False), unsafe_allow_html=True)
            else:pass
            if df_ep_info['Pubmed'].any() or df_ep_info['Ref_site'].any() or df_ep_info['Wiki_link'].any() or df_ep_info['WNI_link'].any() or df_ep_info['ICD11_link'].any():
                st.markdown("---")
                st.write('<u>External Links</u>', unsafe_allow_html=True)
            ref_site = df_ep_info['Ref_site'].to_string(index=False)
            if df_ep_info['Ref_site'].any(): st.markdown(f"* **Primary Paper** [webpage]({ref_site})")
            else:pass
            pub_link = df_ep_info['Pubmed'].to_string(index=False)
            if df_ep_info['Pubmed'].any(): st.markdown(f"* **Pubmed** [webpage]({pub_link})")
            else:pass
            wiki_link = df_ep_info['Wiki_link'].to_string(index=False)
            if df_ep_info['Wiki_link'].any(): st.markdown(f"* **Wikipedia** [webpage]({wiki_link})")
            else:pass
            wni_link = df_ep_info['WNI_link'].to_string(index=False)
            if df_ep_info['WNI_link'].any(): st.markdown(f"* **Whonamedit** [webpage]({wni_link})")
            else:pass


        if types == "Selected":
            url = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/Eponyms4python_Lite.csv'
            df1 = pd.read_csv(url, dtype={'PMID':str,'Year':int})
            df2 = df1.sort_values(by=['Eponym'],ascending=True)
            spec_df = df2['Topic'].dropna()
            string = spec_df.str.cat(sep=',')
            splits = string.split(",")
            S = set(splits)
            T = np.array(list(S)).astype(object)
            U = np.sort(T)
            specs = st.multiselect('Specilaties of interest - pick and choose',options=list(U),
                           format_func=lambda x: ' ' if x == '1' else x,
                           default=['Academic','Anaesthetics','Bariatrics','Breast','Cardiothoracics',
                                    'Colorectal','Emergency Surgery','Endocrine','ENT',
                                    'General Surgery','Gynaecology','HPB','Hernia',
                                    'Laparoscopic Surgery','Maxillofacial','Neurosurgery','Obstetrics',
                                    'Oesophagogastric','Ophthalmology','Orthopaedics','Paediatrics','Plastics',
                                    'Radiology','Transplant','Trauma','Urology','Vascular',]
                                          )
            min_yrs, max_yrs = st.slider("Step 3) Define a time window:", 100, 2050, [150, 2021])
            st.markdown("---")
            st.markdown('''<span style="font-size:12pt;color:black;">**Click on a category type to zoom in**,
                           and click in the center to pan out.</span>''', unsafe_allow_html=True)
            new_1T = df2.loc[(df2['Year'] >= min_yrs) & (df2['Year'] <= max_yrs)]
            new_2T = new_1T.loc[new_1T['Topic'].str.contains('|'.join(specs)) == True]
            new_3T = new_2T.sort_values(by=['Eponym'],ascending=True)
            new_3T["Categories"] = "Categories"
            figJDLT = px.sunburst(new_3T,path=['Categories','Type_short','Eponym_easy'],
                              color='Log2_GxP',hover_data=['Eponym'],values='Year',
                              color_continuous_scale='Magma',)#'RdBu'viridis
            figJDLT.update_layout(margin=dict(l=0, r=0, t=0, b=10),width=700,height=550)
            figJDLT.update_traces(hovertemplate='<b>%{label}</b>') 
            st.write(figJDLT)

            blank_row = {'Alphabet':'','Eponym':'1','Eponym_easy':'1','Eponym_easy_yr':'','Year_str':'','Sex_A1':'1'}
            time_df2 = new_2T.append(blank_row, ignore_index=True)
            time_df3 = time_df2.sort_values(by=['Eponym'],ascending=True)
            st.markdown("---")
            options = st.selectbox('Type here to look up an eponym of interest:',
                        time_df3['Eponym_easy'].unique(), format_func=lambda x: ' ' if x == '1' else x)
            df_ep_info = time_df3[time_df3['Eponym_easy'].str.match(options)]

            if options == "Aaron sign":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Aaron.png'
                st.image(image, width=160)
            if options == "Allis forceps":
                image_human = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Allis.png'
                image_forceps = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Allis_Forceps.png'
                col1, col2, col3, col4 = st.beta_columns(4)
                col1.image(image_human, width=160);col2.image(image_forceps, width=386)
                col3.write(''); col4.write('')
            if options == "Allison lung retractor":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Allison.png'
                st.image(image, width=160)
            if options == "Allison repair":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Allison.png'
                st.image(image, width=160)
            if options == "Altemeier procedure":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Altemeier.png'
                st.image(image, width=160)
            if options == "Ambrosetti classification":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Ambrosetti.png'
                st.image(image, width=160)
            if options == "Amyand hernia":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Amyand.png'
                st.image(image, width=160)
            if options == "Babcock forceps":
                image_human = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Babcock.png'
                image_forceps = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Babcock_Forceps2.png'
                col1, col2, col3, col4 = st.beta_columns(4)
                col1.image(image_human, width=160); col2.image(image_forceps, width=297);
                col3.write(''); col4.write('')
            if options == "Barrett's oesophagus":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Barrett.png'
                st.image(image, width=160)
            if options == "Bassini hernia repair":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Bassini.png'
                st.image(image, width=160)
            if options == "Battle's incision":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Battle.png'
                st.image(image, width=160)
            if options == "Battle's sign":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Battle.png'
                st.image(image, width=160)
            if options == "Beger procedure":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Beger.png'
                st.image(image, width=160)
            if options == "Berry's ligament":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Berry.png'
                st.image(image, width=160)
            if options == "Brown-Séquard syndrome":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Brown-Sequard.png'
                st.image(image, width=160)
            if options == "Brooke ileostomy":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Brooke.png'
                st.image(image, width=160)
            if options == "Calot's triangle":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Calot2.png'
                st.image(image, width=500)
            if options == "Cushing's ulcer":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Cushing.png'
                st.image(image, width=160)
            if options == "DeBakey forceps":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_DeBakey_Forceps.png'
                st.image(image, width=300)
            if options == "De Garengeot's hernia":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_De_Garengeot.png'
                st.image(image, width=160)
            if options == "Delorme's procedure":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Delorme.png'
                st.image(image, width=160)
            if options == "Fanelli catheter":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Fanelli.png'
                st.image(image, width=160)
            if options == "Foley catheter":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Foley.png'
                st.image(image, width=160)
            if options == "Graves disease":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Graves.png'
                st.image(image, width=160)
            if options == "Hartmann's operation":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Henri_Hartmann.png'
                st.image(image, width=160)
            if options == "Hartmann's pouch":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Henri_Hartmann.png'
                st.image(image, width=160)
            if options == "Hashimoto's thyroiditis":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Hashimoto.png'
                st.image(image, width=160)
            if options == "Ivor Lewis oesophagectomy":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Ivor_Lewis.png'
                st.image(image, width=160)
            if options == "Joll's retractor":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Joll.png'
                st.image(image, width=160)
            if options == "Joll's triangle":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Joll.png'
                st.image(image, width=160)
            if options == "Killian's triangle":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Killian.png'
                st.image(image, width=160)
            if options == "Kocher's incision of the abdomen":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Kocher.png'
                st.image(image, width=160)
            if options == "Kocher maneuver":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Kocher.png'
                st.image(image, width=160)
            if options == "Meckel's diverticulum":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Meckel.png'
                st.image(image, width=160)
            if options == "Merendino jejunal interposition":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Merendino.png'
                st.image(image, width=160)
            if options == "Morrison's pouch":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Morrison.png'
                st.image(image, width=160)
            if options == "Nodules of Aranzio":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Aranzi.png'
                st.image(image, width=160)
            if options == "Sphincter of Oddi":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Oddi.png'
                st.image(image, width=160)
            if options == "Mirizzi's syndrome":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Pablo_Mirizzi.png'
                st.image(image, width=160)
            if options == "Rouviere's sulcus":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Rouviere.png'
                st.image(image, width=160)
            if options == "Shouldice hernia repair":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Shouldice.png'
                st.image(image, width=160)
            if options == "Strasberg's critical view of safety":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Strasberg.png'
                st.image(image, width=160)
            if options == "Takayasu's arteritis":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Takayasu.jpg'
                st.image(image, width=160)
            if options == "Ligament of Treitz":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Treitz.png'
                st.image(image, width=160)
            if options == "Whipple's operation":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Whipple.png'
                st.image(image, width=160)
            if options == "Foramen of Winslow":
                image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Winslow.png'
                st.image(image, width=160)

            else:pass
            if df_ep_info['Who'].any(): st.write('*_Who_*:', df_ep_info['Who_B'].to_string(index=False))
            else: pass
            if df_ep_info['Year'].any(): st.write('*_When_*:', df_ep_info['Year_str'].to_string(index=False))
            else:pass
            if df_ep_info['Where'].any(): st.write('*_Where_*:', df_ep_info['Where'].to_string(index=False))
            else:pass
            if df_ep_info['Description'].any() or df_ep_info['History'].any():
                st.markdown("---")
            description = df_ep_info['Description'].to_string(index=False)
            if df_ep_info['Description'].any():
                st.markdown(description, unsafe_allow_html=True)
            else:pass
            if df_ep_info['Ref'].any():
                st.markdown("---")
                st.write('<u>References</u>', unsafe_allow_html=True)
                st.write(df_ep_info['Ref'].to_string(index=False), unsafe_allow_html=True)
            else:pass
            if df_ep_info['Pubmed'].any() or df_ep_info['Ref_site'].any() or df_ep_info['Wiki_link'].any() or df_ep_info['WNI_link'].any() or df_ep_info['ICD11_link'].any():
                st.markdown("---")
                st.write('<u>External Links</u>', unsafe_allow_html=True)
            ref_site = df_ep_info['Ref_site'].to_string(index=False)
            if df_ep_info['Ref_site'].any(): st.markdown(f"* **Primary Paper** [webpage]({ref_site})")
            else:pass
            pub_link = df_ep_info['Pubmed'].to_string(index=False)
            if df_ep_info['Pubmed'].any(): st.markdown(f"* **Pubmed** [webpage]({pub_link})")
            else:pass
            wiki_link = df_ep_info['Wiki_link'].to_string(index=False)
            if df_ep_info['Wiki_link'].any(): st.markdown(f"* **Wikipedia** [webpage]({wiki_link})")
            else:pass
            wni_link = df_ep_info['WNI_link'].to_string(index=False)
            if df_ep_info['WNI_link'].any(): st.markdown(f"* **Whonamedit** [webpage]({wni_link})")
            else:pass
            
#-------------------------------------------------------------------------------------------------#
#                                                                                                 #
#  Exam (8)                                                                                       #
# ::: Handles the                                                                                 #                                                                                              #
#                                                                                                 #
#-------------------------------------------------------------------------------------------------#
def exp_exam():
    st.write('''_To show sidebar, click **>** in top left_''')
    st.title("Eponymous terms often found in exams") 
    url = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/Eponyms4python_Lite.csv'
    df = pd.read_csv(url, dtype={'PMID':str,'Year':int})
    df1 = df['ExamSpec'].dropna()
    string = df1.str.cat(sep=',')
    splits = string.split(",")
    S = set(splits)
    T = np.array(list(S)).astype(object)
    U = np.sort(T)
    exams = st.multiselect('Step 1) Choose specialties of interest:',options=list(U),
                           format_func=lambda x: ' ' if x == '1' else x,)
    new_exams1 = df.loc[df['ExamSpec'].str.contains('|'.join(exams)) == True]
    new_exams2 = new_exams1.sort_values(by=['Eponym'],ascending=True)

    if not exams == None:
        options = st.selectbox('Step 2) Search list relevant your specialty:',
                                  new_exams2['Eponym_easy'].unique(), format_func=lambda x: ' ' if x == '1' else x)
        df_ep_info = new_exams1[new_exams1['Eponym_easy'].str.match(options)]

        if options == "Aaron sign":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Aaron.png'
            st.image(image, width=160)
        if options == "Allis forceps":
            image_human = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Allis.png'
            image_forceps = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Allis_Forceps.png'
            col1, col2, col3, col4 = st.beta_columns(4)
            col1.image(image_human, width=160);col2.image(image_forceps, width=386)
            col3.write(''); col4.write('')

        if options == "Allison lung retractor":
            image_human = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Allison.png'
            image_retractor = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Allison_Retractor.png'
            col1, col2, col3, col4, col5 = st.beta_columns(5)
            col1.image(image_human, width=140); col2.image(image_retractor, width=141);
            col3.write(''); col4.write('')
    
        if options == "Allison repair":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Allison.png'
            st.image(image, width=160)
        if options == "Altemeier procedure":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Altemeier.png'
            st.image(image, width=160)
        if options == "Ambrosetti classification":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Ambrosetti.png'
            st.image(image, width=160)
        if options == "Amyand hernia":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Amyand.png'
            st.image(image, width=160)
        if options == "Babcock forceps":
            image_human = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Babcock.png'
            image_forceps = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Babcock_Forceps2.png'
            col1, col2, col3, col4 = st.beta_columns(4)
            col1.image(image_human, width=160); col2.image(image_forceps, width=297);
            col3.write(''); col4.write('')
        if options == "Barrett's oesophagus":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Barrett.png'
            st.image(image, width=160)
        if options == "Bassini hernia repair":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Bassini.png'
            st.image(image, width=160)
        if options == "Battle's incision":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Battle.png'
            st.image(image, width=160)
        if options == "Battle's sign":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Battle.png'
            st.image(image, width=160)
        if options == "Beger procedure":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Beger.png'
            st.image(image, width=160)
        if options == "Berry's ligament":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Berry.png'
            st.image(image, width=160)
        if options == "Brown-Séquard syndrome":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Brown-Sequard.png'
            st.image(image, width=160)
        if options == "Brooke ileostomy":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Brooke.png'
            st.image(image, width=160)
        if options == "Calot's triangle":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Calot2.png'
            st.image(image, width=500)
        if options == "Cushing's ulcer":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Cushing.png'
            st.image(image, width=160)
        if options == "DeBakey forceps":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_DeBakey_Forceps.png'
            st.image(image, width=300)
        if options == "De Garengeot's hernia":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_De_Garengeot.png'
            st.image(image, width=160)
        if options == "Delorme's procedure":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Delorme.png'
            st.image(image, width=160)
        if options == "Fanelli catheter":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Fanelli.png'
            st.image(image, width=160)
        if options == "Foley catheter":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Foley.png'
            st.image(image, width=160)
        if options == "Graves disease":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Graves.png'
            st.image(image, width=160)
        if options == "Hartmann's operation":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Henri_Hartmann.png'
            st.image(image, width=160)
        if options == "Hartmann's pouch":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Henri_Hartmann.png'
            st.image(image, width=160)
        if options == "Hashimoto's thyroiditis":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Hashimoto.png'
            st.image(image, width=160)
        if options == "Ivor Lewis oesophagectomy":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Ivor_Lewis.png'
            st.image(image, width=160)
        if options == "Joll's retractor":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Joll.png'
            st.image(image, width=160)
        if options == "Joll's triangle":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Joll.png'
            st.image(image, width=160)
        if options == "Killian's triangle":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Killian.png'
            st.image(image, width=160)
        if options == "Kocher's incision of the abdomen":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Kocher.png'
            st.image(image, width=160)
        if options == "Kocher maneuver":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Kocher.png'
            st.image(image, width=160)
        if options == "Meckel's diverticulum":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Meckel.png'
            st.image(image, width=160)
        if options == "Merendino jejunal interposition":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Merendino.png'
            st.image(image, width=160)
        if options == "Morrison's pouch":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Morrison.png'
            st.image(image, width=160)
        if options == "Nodules of Aranzio":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Aranzi.png'
            st.image(image, width=160)
        if options == "Sphincter of Oddi":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Oddi.png'
            st.image(image, width=160)
        if options == "Mirizzi's syndrome":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Pablo_Mirizzi.png'
            st.image(image, width=160)
        if options == "Rouviere's sulcus":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Rouviere.png'
            st.image(image, width=160)
        if options == "Shouldice hernia repair":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Shouldice.png'
            st.image(image, width=160)
        if options == "Strasberg's critical view of safety":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Strasberg.png'
            st.image(image, width=160)
        if options == "Takayasu's arteritis":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Takayasu.jpg'
            st.image(image, width=160)
        if options == "Ligament of Treitz":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Treitz.png'
            st.image(image, width=160)
        if options == "Whipple's operation":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Whipple.png'
            st.image(image, width=160)
        if options == "Foramen of Winslow":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Winslow.png'
            st.image(image, width=160)

        else:pass
        if df_ep_info['Who'].any(): st.write('*_Who_*:', df_ep_info['Who_B'].to_string(index=False))
        else: pass
        if df_ep_info['Year'].any(): st.write('*_When_*:', df_ep_info['Year_str'].to_string(index=False))
        else:pass
        if df_ep_info['Where'].any(): st.write('*_Where_*:', df_ep_info['Where'].to_string(index=False))
        else:pass

        if df_ep_info['Description'].any():
            description = df_ep_info['Description'].to_string(index=False)
            st.markdown("---")
            st.markdown(description, unsafe_allow_html=True)
        else:pass

        if df_ep_info['Ref'].any():
            st.markdown("---")
            st.write('<u>References</u>', unsafe_allow_html=True)
            st.write(df_ep_info['Ref'].to_string(index=False), unsafe_allow_html=True)
        else:pass

        if df_ep_info['Pubmed'].any() or df_ep_info['Ref_site'].any() or df_ep_info['Wiki_link'].any() or df_ep_info['WNI_link'].any() or df_ep_info['ICD11_link'].any():
            st.markdown("---")
            st.write('<u>External Links</u>', unsafe_allow_html=True)

        ref_site = df_ep_info['Ref_site'].to_string(index=False)
        if df_ep_info['Ref_site'].any(): st.markdown(f"* **Primary Paper** [webpage]({ref_site})")
        else:pass
        pub_link = df_ep_info['Pubmed'].to_string(index=False)
        if df_ep_info['Pubmed'].any(): st.markdown(f"* **Pubmed** [webpage]({pub_link})")
        else:pass
        wiki_link = df_ep_info['Wiki_link'].to_string(index=False)
        if df_ep_info['Wiki_link'].any(): st.markdown(f"* **Wikipedia** [webpage]({wiki_link})")
        else:pass
        wni_link = df_ep_info['WNI_link'].to_string(index=False)
        if df_ep_info['WNI_link'].any(): st.markdown(f"* **Whonamedit** [webpage]({wni_link})")
        else:pass
  

#-------------------------------------------------------------------------------------------------#
#                                                                                                 #
#  Teaching (9)                                                                                   #
# ::: Handles the                                                                                 #                                                                                              #
#                                                                                                 #
#-------------------------------------------------------------------------------------------------#
def exp_teach():
    st.write('''_To show sidebar, click **>** in top left_''')
    st.title("Teaching Tool")
    exp = st.radio('1st) Choose your setting:',
                                ['Bedside',        # - Scars, Signs, Diseases & Severity Scores",
                                 'Classroom',      # - History of Surgery',
                                 'Operating Room', # - Incisions, Instruments & Operations",
                                 ])

    if   exp == "Bedside":          teach_bed()       #T1 #- Scars, Signs, Severity Scores
    elif exp == 'Classroom':        teach_classrm()   #T2 #- History
    elif exp == "Operating Room":   teach_or()        #T3 #- Incisions, Instruments & Operations

def teach_bed():
    st.markdown("---")
    st.markdown('''### Clinial Features - What To Look For''')
    bed = st.radio('2nd) Bedside Teaching', ['Scars / Incisions', 'Clinical Signs',]) #'Disease Severity Scores' 

    if bed == "Scars / Incisions":
    #    color = st.select_slider('Select a region of the abdomen',
    #    options=['Upper Abdomen','RUQ', 'Epigastrium','Central', 'RIF', 'Suprapubic', 'LIF','Lower abdomen'])
    #    st.write('Scars and stomas in the', color)
    #    st.write('Insert image of abdomen')
        url = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/Eponyms4python_Lite.csv'
        df = pd.read_csv(url, dtype={'PMID':str,'Year':int})
        Cuts_df = df[(df['Type_bed_scar'].str.match('Incisions'))]
        if not Cuts_df['Type_bed_scar'].isnull().all():
            Table = ff.create_table(Cuts_df.drop(['Alphabet','CityOfEponym_A1','ISO_country_A1','Author_1_Role'],
                             axis=1).sort_values(by=['Eponym'],
                                                 ascending=True).reindex(columns=['Eponym']).reset_index(drop=True))
        options = st.selectbox('3rd) Choose from list of eponymous scars and stomas:', Cuts_df['Eponym'].unique())
        df_ep_info = Cuts_df[Cuts_df['Eponym'].str.match(options)]

        if options == "Battle's incision":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Battle.png'
            st.image(image, width=160)
        if options == "Brooke ileostomy":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Brooke.png'
            st.image(image, width=160)
        if options == "Hartmann's operation":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Henri_Hartmann.png'
            st.image(image, width=160)
        if options == "Kocher's incision of the abdomen":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Kocher.png'
            st.image(image, width=160)

        else:pass
        if df_ep_info['Who'].any(): st.write('*_Who_*:', df_ep_info['Who_B'].to_string(index=False))
        else: pass
        if df_ep_info['Year'].any(): st.write('*_When_*:', df_ep_info['Year_str'].to_string(index=False))
        else:pass
        if df_ep_info['Where'].any(): st.write('*_Where_*:', df_ep_info['Where'].to_string(index=False))
        else:pass

        if df_ep_info['Description'].any():
            st.markdown("---")
        description = df_ep_info['Description'].to_string(index=False)
        if df_ep_info['Description'].any():
            st.markdown(description, unsafe_allow_html=True)
        else:pass
        if df_ep_info['Ref'].any():
            st.markdown("---")
            st.write('<u>References</u>', unsafe_allow_html=True)
            st.write(df_ep_info['Ref'].to_string(index=False), unsafe_allow_html=True)
        else: pass
        if df_ep_info['Pubmed'].any() or df_ep_info['Ref_site'].any() or df_ep_info['Wiki_link'].any() or df_ep_info['WNI_link'].any():
            st.markdown("---")
            st.write('<u>External Links</u>', unsafe_allow_html=True)
        ref_site = df_ep_info['Ref_site'].to_string(index=False)
        if df_ep_info['Ref_site'].any(): st.markdown(f"* **Primary Paper** [webpage]({ref_site})")
        else:pass
        pub_link = df_ep_info['Pubmed'].to_string(index=False)
        if df_ep_info['Pubmed'].any(): st.markdown(f"* **Pubmed** [webpage]({pub_link})")
        else:pass
        wiki_link = df_ep_info['Wiki_link'].to_string(index=False)
        if df_ep_info['Wiki_link'].any(): st.markdown(f"* **Wikipedia** [webpage]({wiki_link})")
        else:pass
        wni_link = df_ep_info['WNI_link'].to_string(index=False)
        if df_ep_info['WNI_link'].any(): st.markdown(f"* **Whonamedit** [webpage]({wni_link})")
        else:pass



    if bed == "Clinical Signs":
        url = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/Eponyms4python_Lite.csv'
        df = pd.read_csv(url, dtype={'PMID':str,'Year':int})
        Sign_df = df[(df['Type'].str.match('Signs'))]
        if not Sign_df['Type'].isnull().all():
            Table = ff.create_table(Sign_df.drop(['Alphabet','CityOfEponym_A1','ISO_country_A1','Author_1_Role','WhoNamedIt',],
                             axis=1).sort_values(by=['Eponym'],
                                                 ascending=True).reindex(columns=['Eponym']).reset_index(drop=True))
        options = st.selectbox('3rd) Eponymous clinical features of disease:', Sign_df['Eponym'].unique())
        df_ep_info = Sign_df[Sign_df['Eponym'].str.match(options)]

        if options == "Aaron sign":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Aaron.png'
            st.image(image, width=160)
        if options == "Battle's sign":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Battle.png'
            st.image(image, width=160)
        if options == "Murphy's sign":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Murphy.png'
            st.image(image, width=160)
        if options == "Skipworth's sign":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Skip.png'
            st.image(image, width=160)

        else:pass
        if df_ep_info['Who'].any(): st.write('*_Who_*:', df_ep_info['Who_B'].to_string(index=False))
        else: pass
        if df_ep_info['Year'].any(): st.write('*_When_*:', df_ep_info['Year_str'].to_string(index=False))
        else:pass
        if df_ep_info['Where'].any(): st.write('*_Where_*:', df_ep_info['Where'].to_string(index=False))
        else:pass

        if df_ep_info['Description'].any():
            st.markdown("---")
        description = df_ep_info['Description'].to_string(index=False)
        if df_ep_info['Description'].any():
            st.markdown(description, unsafe_allow_html=True)
        else:pass
        if df_ep_info['Ref'].any():
            st.markdown("---")
            st.write('<u>References</u>', unsafe_allow_html=True)
            st.write(df_ep_info['Ref'].to_string(index=False), unsafe_allow_html=True)
        else: pass
        if df_ep_info['Pubmed'].any() or df_ep_info['Ref_site'].any() or df_ep_info['Wiki_link'].any() or df_ep_info['WNI_link'].any():
            st.markdown("---")
            st.write('<u>External Links</u>', unsafe_allow_html=True)
        ref_site = df_ep_info['Ref_site'].to_string(index=False)
        if df_ep_info['Ref_site'].any(): st.markdown(f"* **Primary Paper** [webpage]({ref_site})")
        else:pass
        pub_link = df_ep_info['Pubmed'].to_string(index=False)
        if df_ep_info['Pubmed'].any(): st.markdown(f"* **Pubmed** [webpage]({pub_link})")
        else:pass
        wiki_link = df_ep_info['Wiki_link'].to_string(index=False)
        if df_ep_info['Wiki_link'].any(): st.markdown(f"* **Wikipedia** [webpage]({wiki_link})")
        else:pass
        wni_link = df_ep_info['WNI_link'].to_string(index=False)
        if df_ep_info['WNI_link'].any(): st.markdown(f"* **Whonamedit** [webpage]({wni_link})")
        else:pass
    
def teach_classrm():
    st.markdown("---")
    st.markdown('''### History of Surgery through Eponyms''')

    classrm = st.radio('2nd) Select by disease or type of operation:',#'Select',
                                ['Disease',                           # - Scars, Signs, Diseases & Severity Scores",
                                 'Type of Operation',                 # - History of Surgery',
                                 ])

    if   classrm == "Disease":              classrm_dis()       #T1 #- Scars, Signs, Severity Scores
    elif classrm == 'Type of Operation':    classrm_op()        #T2 #- History
    
def classrm_dis():
    mapbox_access_token = 'pk.eyJ1IjoiYWpoYXllczgzIiwiYSI6ImNrY2pqM2lvMDB4Z24ydG8zdDl0NTYwbTUifQ.2DKVfTAaE77XAXMpDeq_Pg'
    url = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/Eponyms4python_Lite.csv'
    df = pd.read_csv(url, dtype={'PMID':str,'Year':int})
    df1 = df['Disease'].dropna()
    string = df1.str.cat(sep=',')
    splits = string.split(",")
    S = set(splits)
    T = np.array(list(S)).astype(object)
    U = np.sort(T)
    disease = st.multiselect('3rd) Choose a disease:', options=list(U),)
    new_dis1 = df.loc[df['Disease'].str.contains('|'.join(disease)) == True]
    new_dis2 = new_dis1.sort_values(by=['Year'],ascending=True)

    if disease:
        new_geo1 = new_dis2.loc[new_dis2['Disease'].str.contains('|'.join(disease)) == True]
        new_geo2 = new_geo1.sort_values(by=['Year'],ascending=True)
        options = st.selectbox('4th) Each related eponym:',
                                   new_dis2['Eponym_easy_yr'].unique(),
                               format_func=lambda x: ' ' if x == '1' else x)

        df_ep_info = new_geo2[new_geo2['Eponym_easy_yr'].str.match(options)]

        if options == "1913 - Aaron sign":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Aaron.png'
            st.image(image, width=160)
        if options == "1951 - Allison repair":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Allison.png'
            st.image(image, width=160)
        if options == "1952 - Altemeier procedure":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Altemeier.png'
            st.image(image, width=160)
        if options == "2002 - Ambrosetti classification":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Ambrosetti.png'
            st.image(image, width=160)
        if options == "1735 - Amyand hernia":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Amyand.png'
            st.image(image, width=160)
        if options == "1950 - Barrett's oesophagus":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Barrett.png'
            st.image(image, width=160)
        if options == "1887 - Bassini hernia repair":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Bassini.png'
            st.image(image, width=160)
        if options == "1895 - Battle's incision":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Battle.png'
            st.image(image, width=160)
        if options == "1890 - Battle's sign":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Battle.png'
            st.image(image, width=160)
        if options == "1972 - Beger procedure":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Beger.png'
            st.image(image, width=160)
        if options == "1967 - Belsey Mark IV operation":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Belsey.png'
            st.image(image, width=160)
        if options == "1901 - Berry's ligament":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Berry.png'
            st.image(image, width=160)
        if options == "1881 - Billroth I procedure":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Billroth.png'
            st.image(image, width=160)
        if options == "1885 - Billroth II procedure":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Billroth.png'
            st.image(image, width=160)
        if options == "1848 - Bochdalek hernia":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Bochdalek.png'
            st.image(image, width=160)
        if options == "1724 - Boerhaave syndrome":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Boerhaave.png'
            st.image(image, width=160)
        if options == "1896 - Bouveret syndrome":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Bouveret.png'
            st.image(image, width=160)
        if options == "1851 - Brown-Séquard syndrome":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Brown-Sequard.png'
            st.image(image, width=160)
        if options == "1952 - Brooke ileostomy":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Brooke.png'
            st.image(image, width=160)
        if options == "1908 - Buerger disease":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Buerger.png'
            st.image(image, width=160)
        if options == "1891 - Calot's triangle":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Calot2.png'
            st.image(image, width=500)
        if options == "1911 - Interstitial cells of Cajal":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Cajal.png'
            st.image(image, width=160)
        if options == "1952 - Crigler-Najjar syndrome":
            image_human_C = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Crigler.png'
            image_human_N = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Najjar.png'
            col1, col2, col3 = st.beta_columns(3)
            col1.image(image_human_C, width=160);
            col2.image(image_human_N, width=170); col3.write('')
        if options == "1932 - Crohn's disease":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Crohn.png'
            st.image(image, width=160)
        if options == "1932 - Cushing's ulcer":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Cushing.png'
            st.image(image, width=160)
        if options == "1960 - DeBakey forceps":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_DeBakey_Forceps.png'
            st.image(image, width=300)
        if options == "1731 - De Garengeot's hernia":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_De_Garengeot.png'
            st.image(image, width=160)
        if options == "1900 - Delorme's procedure":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Delorme.png'
            st.image(image, width=160)
        if options == "1974 - DeMeester score":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_DeMeester.png'
            st.image(image, width=160)
        if options == "1908 - Doyen retractor":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Doyen.png'
            st.image(image, width=160)
        if options == "1561 - Fallopian tube":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Falloppio.png'
            st.image(image, width=160)
        if options == "2012 - Fanelli catheter":
            image_human = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Fanelli.png'
            image_catheter = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Fanelli_Catheter.png'
            col1, col2, col3 = st.beta_columns(3)
            col1.image(image_human, width=160); col2.image(image_catheter, width=214); col3.write('')
        if options == "1936 - Finochietto retractor":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Finochietto.png'
            st.image(image, width=160)
        if options == "1934 - Fisher's exact test":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Fisher.png'
            st.image(image, width=160)
        if options == "1937 - Foley catheter":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Foley.png'
            st.image(image, width=160)
        if options == "1959 - Frantz tumour":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Frantz.png'
            st.image(image, width=160)
        if options == "1990 - Ghillebert probability estimate":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Ghillebert.png'
            st.image(image, width=160)
        if options == "1937 - Graham patch":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Graham.png'
            st.image(image, width=160)
        if options == "1835 - Graves disease":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Graves.png'
            st.image(image, width=160)
        if options == "1966 - Gleason score":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Gleason.png'
            st.image(image, width=160)
        if options == "1923 - Hartmann's operation":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Henri_Hartmann.png'
            st.image(image, width=160)
        if options == "1891 - Hartmann's pouch":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Henri_Hartmann.png'
            st.image(image, width=160)
        if options == "1912 - Hashimoto's thyroiditis":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Hashimoto.png'
            st.image(image, width=160)
        if options == "1970 - Hasson technique":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Hasson.png'
            st.image(image, width=160)
        if options == "1721 - Spiral valves of Heister":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Heister.png'
            st.image(image, width=160)
        if options == "1946 - Ivor Lewis oesophagectomy":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Ivor_Lewis.png'
            st.image(image, width=160)
        if options == "1935 - Joll's retractor":
            image_human = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Joll.png'
            image_retractor = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Jolls_Retractor.png'
            col1, col2, col3 = st.beta_columns(3)
            col1.image(image_human, width=160);col2.image(image_retractor, width=220);col3.write('')
        if options == "1938 - Joll's triangle":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Joll.png'
            st.image(image, width=160)
        if options == "1907 - Killian's triangle":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Killian.png'
            st.image(image, width=160)
        if options == "1965 - Klatskin's tumour":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Klatskin.png'
            st.image(image, width=160)
        if options == "1892 - Kocher's incision of the abdomen":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Kocher.png'
            st.image(image, width=160)
        if options == "1892 - Kocher maneuver":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Kocher.png'
            st.image(image, width=160)
        if options == "1829 - Lugol's iodine":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Lugol.png'
            st.image(image, width=160)
        if options == "1923 - Masson's tumor":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Masson.png'
            st.image(image, width=160)
        if options == "1809 - Meckel's diverticulum":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Meckel.png'
            st.image(image, width=160)
        if options == "1958 - Merendino jejunal interposition":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Merendino.png'
            st.image(image, width=160)
        if options == "1900 - Morrison's pouch":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Morrison.png'
            st.image(image, width=160)
        if options == "1912 - Murphy's sign":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Murphy.png'
            st.image(image, width=160)
        if options == "1579 - Nodules of Aranzio":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Aranzi.png'
            st.image(image, width=160)
        if options == "1951 - Kasai procedure":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Kasai.png'
            st.image(image, width=160)
        if options == "1649 - Arc of Riolan":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Jean_Riolan.png'
            st.image(image, width=160)
        if options == "2011 - Skipworth's sign":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Skip.png'
            st.image(image, width=160)
        if options == "1887 - Sphincter of Oddi":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Oddi.png'
            st.image(image, width=160)
        if options == "1948 - Mirizzi's syndrome":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Pablo_Mirizzi.png'
            st.image(image, width=160)
        if options == "1924 - Rouviere's sulcus":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Rouviere.png'
            st.image(image, width=160)
        if options == "1944 - Shouldice hernia repair":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Shouldice.png'
            st.image(image, width=160)
        if options == "1995 - Strasberg's critical view of safety":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Strasberg.png'
            st.image(image, width=160)
        if options == "Takayasu's arteritis":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Takayasu.jpg'
            st.image(image, width=160)
        if options == "1904 - Tapia syndrome":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Tapia.png'
            st.image(image, width=160)
        if options == "1853 - Ligament of Treitz":
            image = 'https://raw.gsithubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Treitz.png'
            st.image(image, width=160)
        if options == "1704 - Valsalva maneuver":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Valsalva.png'
            st.image(image, width=160)
        if options == "1934 - Whipple's operation":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Whipple.png'
            st.image(image, width=160)
        if options == "1715 - Foramen of Winslow":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Winslow.png'
            st.image(image, width=160)
        if options == "1907 - Yankauer suction tip":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Yankauer.png'
            st.image(image, width=160)



        else:pass
        if df_ep_info['Who'].any(): st.write('*_Who_*:', df_ep_info['Who_B'].to_string(index=False))
        else: pass
        if df_ep_info['Year'].any(): st.write('*_When_*:', df_ep_info['Year_str'].to_string(index=False))
        else:pass
        if df_ep_info['Where'].any(): st.write('*_Where_*:', df_ep_info['Where'].to_string(index=False))
        else:pass

        if df_ep_info['Description'].any():
            st.markdown("---")
        description = df_ep_info['Description'].to_string(index=False)
        if df_ep_info['Description'].any():
            st.markdown(description, unsafe_allow_html=True)
        else:pass
        if df_ep_info['Ref'].any():
            st.markdown("---")
            st.write('<u>References</u>', unsafe_allow_html=True)
            st.write(df_ep_info['Ref'].to_string(index=False), unsafe_allow_html=True)
        else: pass
        if df_ep_info['Pubmed'].any() or df_ep_info['Ref_site'].any() or df_ep_info['Wiki_link'].any() or df_ep_info['WNI_link'].any():
            st.markdown("---")
            st.write('<u>External Links</u>', unsafe_allow_html=True)
        ref_site = df_ep_info['Ref_site'].to_string(index=False)
        if df_ep_info['Ref_site'].any(): st.markdown(f"* **Primary Paper** [webpage]({ref_site})")
        else:pass
        pub_link = df_ep_info['Pubmed'].to_string(index=False)
        if df_ep_info['Pubmed'].any(): st.markdown(f"* **Pubmed** [webpage]({pub_link})")
        else:pass
        wiki_link = df_ep_info['Wiki_link'].to_string(index=False)
        if df_ep_info['Wiki_link'].any(): st.markdown(f"* **Wikipedia** [webpage]({wiki_link})")
        else:pass
        wni_link = df_ep_info['WNI_link'].to_string(index=False)
        if df_ep_info['WNI_link'].any(): st.markdown(f"* **Whonamedit** [webpage]({wni_link})")
        else:pass


def classrm_op():
    url = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/Eponyms4python_Lite.csv'
    df1 = pd.read_csv(url, dtype={'PMID':str,'Year':int,})
    df2 = df1.sort_values(by=['Year'],ascending=True)
    df3 = df2[(df2['Type'].str.match('Operations'))]
    df4 = df3[df3['Operation'].notna()]
    df5 = df4['Operation'].dropna()
    string = df5.str.cat(sep=',')
    splits = string.split(",")
    S = set(splits)
    T = np.array(list(S)).astype(object)
    U = np.sort(T)
    eponymByOp = st.multiselect('3rd) Types of operation:',options=list(U),
                                format_func=lambda x: ' ' if x == '1' else x)
    new_df = df4.loc[df4['Operation'].str.contains('|'.join(eponymByOp)) == True]
    new_df2 = new_df.sort_values(by=['Year'],ascending=True)
    if eponymByOp:
        Op_options = st.selectbox('4th) Search list of related eponyms:', new_df2['Eponym_easy_yr'].unique(),
                                  format_func=lambda x: ' ' if x == '1' else x)
        df_ep_info = new_df[new_df['Eponym_easy_yr'].str.match(Op_options)]
        ep_yr = df_ep_info['Year'].to_string(index=False)

        if Op_options == "Ivor Lewis oesophagectomy":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Ivor_Lewis.png'
            st.image(image, width=160)
        if Op_options == "Kocher maneuver":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Kocher.png'
            st.image(image, width=160)
        if Op_options == "Shouldice hernia repair":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Shouldice.png'
            st.image(image, width=160)

        else:pass
        if df_ep_info['Who'].any(): st.write('*_Who_*:', df_ep_info['Who_B'].to_string(index=False))
        else: pass
        if df_ep_info['Year'].any(): st.write('*_When_*:', df_ep_info['Year_str'].to_string(index=False))
        else:pass
        if df_ep_info['Where'].any(): st.write('*_Where_*:', df_ep_info['Where'].to_string(index=False))
        else:pass

        if df_ep_info['Description'].any():
            st.markdown("---")
        description = df_ep_info['Description'].to_string(index=False)
        if df_ep_info['Description'].any():
            st.markdown(description, unsafe_allow_html=True)
        else:pass
        if df_ep_info['Ref'].any():
            st.markdown("---")
            st.write('<u>References</u>', unsafe_allow_html=True)
            st.write(df_ep_info['Ref'].to_string(index=False), unsafe_allow_html=True)
        else: pass
        if df_ep_info['Pubmed'].any() or df_ep_info['Ref_site'].any() or df_ep_info['Wiki_link'].any() or df_ep_info['WNI_link'].any():
            st.markdown("---")
            st.write('<u>External Links</u>', unsafe_allow_html=True)
        ref_site = df_ep_info['Ref_site'].to_string(index=False)
        if df_ep_info['Ref_site'].any(): st.markdown(f"* **Primary Paper** [webpage]({ref_site})")
        else:pass
        pub_link = df_ep_info['Pubmed'].to_string(index=False)
        if df_ep_info['Pubmed'].any(): st.markdown(f"* **Pubmed** [webpage]({pub_link})")
        else:pass
        wiki_link = df_ep_info['Wiki_link'].to_string(index=False)
        if df_ep_info['Wiki_link'].any(): st.markdown(f"* **Wikipedia** [webpage]({wiki_link})")
        else:pass
        wni_link = df_ep_info['WNI_link'].to_string(index=False)
        if df_ep_info['WNI_link'].any(): st.markdown(f"* **Whonamedit** [webpage]({wni_link})")
        else:pass

def teach_or():
    st.markdown("---")
    st.markdown('''### Operative Eponyms''')
    OR = st.radio('2nd) In the operating theatre:', ["Who invented that operation?",
                                                     "Airways & anaesthesia",
                                                     "Who invented that incision or technique?",
                                                     "Who's instrument?",])

    if OR == "Who invented that operation?":
        url = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/Eponyms4python_Lite.csv'
        df = pd.read_csv(url, dtype={'PMID':str,'Year':int})
        Op_df = df[(df['Type'].str.match('Operation'))]
        if not Op_df['Type'].isnull().all():
            Table = ff.create_table(Op_df.drop(['Alphabet','CityOfEponym_A1'],axis=1).sort_values(by=['Eponym'],
                                                 ascending=True).reindex(columns=['Eponym']).reset_index(drop=True))
        options = st.selectbox('3rd) Choose from list of eponymous operations:', Op_df['Eponym'].unique())
        df_ep_info = Op_df[Op_df['Eponym'].str.match(options)]

        if options == "Hartmann's operation":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Henri_Hartmann.png'
            st.image(image, width=160)

        if options == "Ivor Lewis oesophagectomy":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Ivor_Lewis.png'
            st.image(image, width=160)

        else:pass
        if df_ep_info['Who'].any(): st.write('*_Who_*:', df_ep_info['Who_B'].to_string(index=False))
        else: pass
        if df_ep_info['Year'].any(): st.write('*_When_*:', df_ep_info['Year_str'].to_string(index=False))
        else:pass
        if df_ep_info['Where'].any(): st.write('*_Where_*:', df_ep_info['Where'].to_string(index=False))
        else:pass

        if df_ep_info['Description'].any():
            st.markdown("---")
        description = df_ep_info['Description'].to_string(index=False)
        if df_ep_info['Description'].any():
            st.markdown(description, unsafe_allow_html=True)
        else:pass
        if df_ep_info['Ref'].any():
            st.markdown("---")
            st.write('<u>References</u>', unsafe_allow_html=True)
            st.write(df_ep_info['Ref'].to_string(index=False), unsafe_allow_html=True)
        else: pass
        if df_ep_info['Pubmed'].any() or df_ep_info['Ref_site'].any() or df_ep_info['Wiki_link'].any() or df_ep_info['WNI_link'].any():
            st.markdown("---")
            st.write('<u>External Links</u>', unsafe_allow_html=True)
        ref_site = df_ep_info['Ref_site'].to_string(index=False)
        if df_ep_info['Ref_site'].any(): st.markdown(f"* **Primary Paper** [webpage]({ref_site})")
        else:pass
        pub_link = df_ep_info['Pubmed'].to_string(index=False)
        if df_ep_info['Pubmed'].any(): st.markdown(f"* **Pubmed** [webpage]({pub_link})")
        else:pass
        wiki_link = df_ep_info['Wiki_link'].to_string(index=False)
        if df_ep_info['Wiki_link'].any(): st.markdown(f"* **Wikipedia** [webpage]({wiki_link})")
        else:pass
        wni_link = df_ep_info['WNI_link'].to_string(index=False)
        if df_ep_info['WNI_link'].any(): st.markdown(f"* **Whonamedit** [webpage]({wni_link})")
        else:pass
    


    if OR == "Airways & anaesthesia":
        url = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/Eponyms4python_Lite.csv'
        df1 = pd.read_csv(url, dtype={'PMID':str,'Year':int,})
        df2 = df1.sort_values(by=['Eponym'],ascending=True)
        df3 = df2[(df2['Topic'].str.match('Anaesthetics'))]
        df4 = df3[df3['Eponym_easy'].notna()]

        Anaes_options2 = st.selectbox('3rd) Select eponyms related to airways and anaesthetics:',
                                     df4['Eponym_easy'].unique())
        df_ep_info = df2[df2['Eponym_easy'].str.match(Anaes_options2)]

        
        if df_ep_info['Who'].any(): st.write('*_Who_*:', df_ep_info['Who_B'].to_string(index=False))
        else: pass
        if df_ep_info['Year'].any(): st.write('*_When_*:', df_ep_info['Year_str'].to_string(index=False))
        else:pass
        if df_ep_info['Where'].any(): st.write('*_Where_*:', df_ep_info['Where'].to_string(index=False))
        else:pass

        if df_ep_info['Description'].any():
            st.markdown("---")
        description = df_ep_info['Description'].to_string(index=False)
        if df_ep_info['Description'].any():
            st.markdown(description, unsafe_allow_html=True)
        else:pass
        if df_ep_info['Ref'].any():
            st.markdown("---")
            st.write('<u>References</u>', unsafe_allow_html=True)
            st.write(df_ep_info['Ref'].to_string(index=False), unsafe_allow_html=True)
        else: pass
        if df_ep_info['Pubmed'].any() or df_ep_info['Ref_site'].any() or df_ep_info['Wiki_link'].any() or df_ep_info['WNI_link'].any():
            st.markdown("---")
            st.write('<u>External Links</u>', unsafe_allow_html=True)
        ref_site = df_ep_info['Ref_site'].to_string(index=False)
        if df_ep_info['Ref_site'].any(): st.markdown(f"* **Primary Paper** [webpage]({ref_site})")
        else:pass
        pub_link = df_ep_info['Pubmed'].to_string(index=False)
        if df_ep_info['Pubmed'].any(): st.markdown(f"* **Pubmed** [webpage]({pub_link})")
        else:pass
        wiki_link = df_ep_info['Wiki_link'].to_string(index=False)
        if df_ep_info['Wiki_link'].any(): st.markdown(f"* **Wikipedia** [webpage]({wiki_link})")
        else:pass
        wni_link = df_ep_info['WNI_link'].to_string(index=False)
        if df_ep_info['WNI_link'].any(): st.markdown(f"* **Whonamedit** [webpage]({wni_link})")
        else:pass



    if OR == "Who invented that incision or technique?":
        url = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/Eponyms4python_Lite.csv'
        df = pd.read_csv(url, dtype={'PMID':str,'Year':int})
        Cuts_df = df[(df['Type_op_cut'].str.match('Incisions'))]
        if not Cuts_df['Type_op_cut'].isnull().all():
            Table = ff.create_table(Cuts_df.drop(['Alphabet','CityOfEponym_A1','ISO_country_A1','Author_1_Role',],
                             axis=1).sort_values(by=['Eponym'],
                                                 ascending=True).reindex(columns=['Eponym']).reset_index(drop=True))
        Cuts_options2 = st.selectbox('''3rd) Choose from list of eponymous incisions and stomas:''', Cuts_df['Eponym_easy'].unique())
        df_ep_info = Cuts_df[Cuts_df['Eponym_easy'].str.match(Cuts_options2)]

        
        if df_ep_info['Who'].any(): st.write('*_Who_*:', df_ep_info['Who_B'].to_string(index=False))
        else: pass
        if df_ep_info['Year'].any(): st.write('*_When_*:', df_ep_info['Year_str'].to_string(index=False))
        else:pass
        if df_ep_info['Where'].any(): st.write('*_Where_*:', df_ep_info['Where'].to_string(index=False))
        else:pass

        if df_ep_info['Description'].any():
            st.markdown("---")
        description = df_ep_info['Description'].to_string(index=False)
        if df_ep_info['Description'].any():
            st.markdown(description, unsafe_allow_html=True)
        else:pass
        if df_ep_info['Ref'].any():
            st.markdown("---")
            st.write('<u>References</u>', unsafe_allow_html=True)
            st.write(df_ep_info['Ref'].to_string(index=False), unsafe_allow_html=True)
        else: pass
        if df_ep_info['Pubmed'].any() or df_ep_info['Ref_site'].any() or df_ep_info['Wiki_link'].any() or df_ep_info['WNI_link'].any():
            st.markdown("---")
            st.write('<u>External Links</u>', unsafe_allow_html=True)
        ref_site = df_ep_info['Ref_site'].to_string(index=False)
        if df_ep_info['Ref_site'].any(): st.markdown(f"* **Primary Paper** [webpage]({ref_site})")
        else:pass
        pub_link = df_ep_info['Pubmed'].to_string(index=False)
        if df_ep_info['Pubmed'].any(): st.markdown(f"* **Pubmed** [webpage]({pub_link})")
        else:pass
        wiki_link = df_ep_info['Wiki_link'].to_string(index=False)
        if df_ep_info['Wiki_link'].any(): st.markdown(f"* **Wikipedia** [webpage]({wiki_link})")
        else:pass
        wni_link = df_ep_info['WNI_link'].to_string(index=False)
        if df_ep_info['WNI_link'].any(): st.markdown(f"* **Whonamedit** [webpage]({wni_link})")
        else:pass


    if OR == "Who's instrument?":
        url = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/Eponyms4python_Lite.csv'
        df = pd.read_csv(url, dtype={'PMID':str,'Year':int})
        Instrum_df = df[(df['Type'].str.match('Instruments'))]
        if not Instrum_df['Type'].isnull().all():
            Table = ff.create_table(Instrum_df.drop(['Alphabet','CityOfEponym_A1'],axis=1).sort_values(by=['Eponym'],
                                                 ascending=True).reindex(columns=['Eponym']).reset_index(drop=True))
        Instrum_options2 = st.selectbox('3rd) Choose from list of surgical instruments:', Instrum_df['Eponym'].unique())
        df_ep_info = Instrum_df[Instrum_df['Eponym'].str.match(Instrum_options2)]

        if Instrum_options2 == "Allis forceps":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Allis_Forceps.png'
            st.image(image, width=300)
        if Instrum_options2 == "Allison lung retractor":
            image_human = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Allison.png'
            image_retractor = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Allison_Retractor.png'
            col1, col2, col3, col4, col5 = st.beta_columns(5)
            col1.image(image_human, width=140); col2.image(image_retractor, width=141);
            col3.write(''); col4.write('')
        if Instrum_options2 == "Babcock forceps":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Babcock_Forceps.png'
            st.image(image, width=400)
        if Instrum_options2 == "DeBakey forceps":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_DeBakey_Forceps.png'
            st.image(image, width=300)


        if df_ep_info['Who'].any(): st.write('*_Who_*:', df_ep_info['Who_B'].to_string(index=False))
        else: pass
        if df_ep_info['Year'].any(): st.write('*_When_*:', df_ep_info['Year_str'].to_string(index=False))
        else:pass
        if df_ep_info['Where'].any(): st.write('*_Where_*:', df_ep_info['Where'].to_string(index=False))
        else:pass

        if df_ep_info['Description'].any():
            st.markdown("---")
        description = df_ep_info['Description'].to_string(index=False)
        if df_ep_info['Description'].any():
            st.markdown(description, unsafe_allow_html=True)
        else:pass
        if df_ep_info['Ref'].any():
            st.markdown("---")
            st.write('<u>References</u>', unsafe_allow_html=True)
            st.write(df_ep_info['Ref'].to_string(index=False), unsafe_allow_html=True)
        else: pass
        if df_ep_info['Pubmed'].any() or df_ep_info['Ref_site'].any() or df_ep_info['Wiki_link'].any() or df_ep_info['WNI_link'].any():
            st.markdown("---")
            st.write('<u>External Links</u>', unsafe_allow_html=True)
        ref_site = df_ep_info['Ref_site'].to_string(index=False)
        if df_ep_info['Ref_site'].any(): st.markdown(f"* **Primary Paper** [webpage]({ref_site})")
        else:pass
        pub_link = df_ep_info['Pubmed'].to_string(index=False)
        if df_ep_info['Pubmed'].any(): st.markdown(f"* **Pubmed** [webpage]({pub_link})")
        else:pass
        wiki_link = df_ep_info['Wiki_link'].to_string(index=False)
        if df_ep_info['Wiki_link'].any(): st.markdown(f"* **Wikipedia** [webpage]({wiki_link})")
        else:pass
        wni_link = df_ep_info['WNI_link'].to_string(index=False)
        if df_ep_info['WNI_link'].any(): st.markdown(f"* **Whonamedit** [webpage]({wni_link})")
        else:pass



#@st.cache(suppress_st_warning=True)

def teach_spec():
    url = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/Eponyms4python_Lite.csv'
    df = pd.read_csv(url, dtype={'PMID':str,'Year':int})
    df1 = df['Topic'].dropna()
    string = df1.str.cat(sep=',')
    splits = string.split(",")
    S = set(splits)
    T = np.array(list(S)).astype(object)
    U = np.sort(T)
    special = st.multiselect('2nd) Select from specialies:',options=list(U),
                           format_func=lambda x: ' ' if x == '1' else x,)
    new_special1 = df.loc[df['Topic'].str.contains('|'.join(special)) == True]
    new_special2 = new_special1.sort_values(by=['Eponym'],ascending=True)


#-------------------------------------------------------------------------------------------#

main()

#if __name__ == "__main__":
#    main()
