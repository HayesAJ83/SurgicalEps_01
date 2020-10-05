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
import plotly.express as px          
import plotly.graph_objects as go    
import plotly.figure_factory as ff
px.set_mapbox_access_token(open("/Users/alastairhayes/desktop/Eponyms/ajhayes83_1.mapbox_token").read())

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
                             "Surgical Eponym Explorer ©",
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
    st.markdown('''# SurgicalEps''')
    st.markdown('''_An Educational Web App from Excision_''')
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


if __name__ == "__main__":
    main()
