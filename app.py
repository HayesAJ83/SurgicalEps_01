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
E4P = 'https://github.com/HayesAJ83/SurgicalEps_01/Eponyms4python_Lite.csv'
df1 = pd.read_csv(E4P, error_bad_lines=False)
df2 = df1.sort_values(by=['Year'],ascending=True)
df3 = df2.drop(['Lat_A1', 'Long_A1','Year','ISO_country_A1','CityOfEponym_A1',
               'Author_2','Pubmed_results','Type',
               'Societies','ICD11','PMID','Google_results','Class'], axis=1)
df3.rename(columns={'Author_1': 'Main Person'}, inplace=True)
df4 = df3.drop_duplicates(subset='Eponym', keep="first")

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
                             "App Team"])

    if page   == "Homepage":                   show_homepage()
    elif page == "Surgical Eponym Explorer":   show_explore()
    elif page == "App Team":                   show_the_app_team()



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
    st.markdown('''_An Educational Web App from Excision Ltd._''')
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
    st.title("Surgical App Development Team")
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
    E4P = 'https://github.com/HayesAJ83/SurgicalEps_01/Eponyms4python_Lite.csv'
    df1 = pd.read_csv(E4P, error_bad_lines=False)
    df2 = df1.sort_values(by=['Year'],ascending=True)
    df3 = df2.sort_values(by=['Operation'],ascending=True)  #Gives eponyms by operation alphabetically
    df4 = df3['Operation'].dropna()
    string = df4.str.cat(sep=',')
    splits = string.split(",")
    S = set(splits)
    T = np.array(list(S)).astype(object)
    U = np.sort(T)

    st.markdown('''[Advert space for Google AdSense1]''')
    st.subheader('''First, choose operation(s) of interest:''')
    eponymByOp = st.multiselect('',options=list(U), format_func=lambda x: ' ' if x == '1' else x)
    new_df = df1.loc[df1['Operation'].str.contains('|'.join(eponymByOp)) == True]
    new_df2 = new_df.sort_values(by=['Eponym'],ascending=True)
 
    if not eponymByOp == None:
        st.subheader('''Then, search this list of relevant eponyms:''')
        Op_options = st.selectbox('',
                                  new_df2['Eponym_easy'].unique(), format_func=lambda x: ' ' if x == '1' else x)   #selectbox


        df_ep_info2 = new_df[new_df['Eponym_easy'].str.match(Op_options)]
        ep_yr = df_ep_info2['Year'].to_string(index=False)

        if not df_ep_info2['Who'].isnull().all():
            st.write('*_Who_*:', df_ep_info2['Who'].to_string(index=False))

        if not df_ep_info2['Year_str'].isnull().all():
            st.write('*_When_*:', df_ep_info2['Year_str'].to_string(index=False))

        if not df_ep_info2['Where'].isnull().all():
            st.write('*_Where_*:', df_ep_info2['Where'].to_string(index=False))
    
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
           





if __name__ == "__main__":
    main()
