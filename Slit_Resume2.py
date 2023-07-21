#!/usr/bin/env python
# coding: utf-8

# In[39]:


# import nbformat
# from nbconvert import PythonExporter
# My_Loc = r'C:\Users\mahes\Streamlit_Resume'
# def convertNotebook(notebookPath, modulePath):

#     with open(notebookPath) as fh:
#         nb = nbformat.reads(fh.read(), nbformat.NO_CONVERT)
#     exporter = PythonExporter()
#     source, meta = exporter.from_notebook_node(nb)
#     with open(modulePath, 'w+') as fh:
#         fh.write(source)
        
# convertNotebook(f'{My_Loc}\Slit_Resume2.ipynb',f'{My_Loc}\Slit_Resume2.py')


# In[1]:


#!/usr/bin/env python
import streamlit as st ######
import emoji
from PIL import Image
import datetime
import sys as sys
import os
import glob


# In[23]:


so5_logo = Image.open(f"Resume_IC.png")
Profile_pic = (f"Profile_Pic.png")
Pdf_Resume = (f"Mahesh Resume.pdf")
#User Level Variables
First_Name = "Mahesh"
Last_Name = "Bathija"
Full_Name = First_Name+' '+Last_Name
Current_Designation = "Team Lead"
Current_Team = "Fraud Analytics"
Current_Organization = "Hudson's Bay Company"
Current_Org_from = "09/2020"
Email = "maheshmbathija81193@gmail.com"
Phone = "+91 8951861604"
Linkedin_URL = "https://www.linkedin.com/in/maheshm8"
Location = "Bangalore, India"
birthdate = "November 1993"


Skills = ['Python','SQL','Tableau','Excel','Streamlit','Statistics','Selenium']

Higest_Education = "MBA"
HE_University = "Jain University"
HE_Location = "Bangalore, India"
HE_From = "2016"
HE_To = "2019"

Profile = """With over 8 years of expertise in Fraud Analytics and Abuse Prevention, I possess a strong 
command of analytical tools like SQL and Python. I adeptly utilize advanced analytical 
techniques to actively and passively identify instances of Fraud and Abuse, while also 
deriving valuable insights from the data. I maintain regular communication with 
stakeholders to effectively mitigate these risks and implement proactive policies to prevent 
future occurrences. By leveraging my extensive experience and skill set, I continuously strive 
to enhance the detection and prevention of Fraud and Abuse, ensuring a secure and 
trustworthy environment for all.
"""

E_resume = """I have created this impressive "E-Resume" using Python and the Streamlit Framework. It serves as a platform to showcase my exceptional Python and Streamlit skillsets. The first tab elegantly presents my detailed resume, while the second tab showcases a collection of my accomplished projects, reflecting my proficiency and experience."""

Short_Headline = """Fraud Analytics Expert | Leveraging 8+ Years of Experience in Detecting Fraud and Non Fraud Risk | ex-Amazon | ex-Tesco"""

Awards = {
    "Prime Player Award" : {
        "Organization" : "Saks Off Fifth",
        "Year" : "2022",
        "Month" : "12"
    },
    "Investigator Of Month" : {
        "Organization" : "Amazon",
        "Year" : "2015",
        "Month" : "07"
    }
}

ORG1_Details = """About Fraud Analytics Team – Detecting fraud, boosting revenue through trend identification and mitigation
- Led a successful team of 2 analysts, collaborating on multiple projects and cutting false referrals by 35%."""
ORG2_Details = """About T&S Team – focuses on combating fraud for online marketplace and Logistics Fraud."""
ORG3_Details = """About Fraud Prevention Team – Fraud prevention for offline and online employees and customers"""
ORG4_Details = """About TRMS – Screen customer orders for fraud to prevent chargebacks and protect customers"""

Professional_Experience = {
    "ORG1" : {
        "Company Name" : "Hudson's Bay Company",
        "URL" : "",
        "Role Name" : "Team Lead, Fraud Analytics",
        "From" : "09/2020",
        "To" : "Present",
        "Job Location" : "Bangalore, India",
        "Role Details" : ORG1_Details,
        "Key Projects" : {"Project_1" : {
            "Project Name" : "Customer Risk Scorecard",
            "Details" : """To understand how risky/good a customer is; This tool provides a complete view of customers, including sales, returns, chargebacks, promos, fake returns, risk scores, demographics, and address history. It is an all-in-one tool for customer information, providing a single view of the customer across all channels and touchpoints.""",
            "Savings" : "approx. $3M and 200hrs Monthly",
            "Tools" : "Python | VBA | SQL | Streamlit | Tableau"
        },
                         "Project_2" : {
            "Project Name" : "Promo-Code Reduction Analysis",
            "Details" : """identifying revenue reducing promo-codes and tracking agents for corrective action. Detected and dismissed agent involved in collusion""",
            "Savings" : "$900k for 6 Months",
            "Tools" : "Python | Snowflake"
        },
                         "Project_3" : {
            "Project Name" : "Self Serve Dashboards",
            "Details" : """successfully developed self-serve dashboards that serve as comprehensive platforms to efficiently manage and assess risk across various customer and employee segments. These intuitive dashboards provide a centralized hub for monitoring high-risk individuals at different levels, including loyalty, returns, promo-codes, missing-package claims, gift card fraud, bulk buyers, and warehouse audits. By consolidating this information into a single interface, stakeholders can easily access and analyze critical data, enabling proactive risk mitigation strategies. These user-friendly dashboards enhance decision-making processes and empower teams to take swift actions, ensuring a robust risk management framework for the organization.""",
            "Savings" : "approx. 50hrs Monthly",
            "Tools" : "Snowflake | Tableau | Python"
        },
                         "Project_4" : {
            "Project Name" : "Daily/Weekly Report automation",
            "Details" : """automated daily fraud report generation using Selenium in Python, including sign-in, browsing, exporting, graph building, and emailing""",
            "Savings" : "approx. 20hrs Monthly",
            "Tools" : "Selenium | Python"
        }
                         }
    },
    "ORG2" : {
        "Company Name" : "Myntra",
        "URL" : "",
        "Role Name" : "Associate, Trust & Safety",
        "From" : "10/2019",
        "To" : "09/2020",
        "Job Location" : "Bangalore, India",
        "Role Details" : ORG2_Details,
        "Key Projects" : {"Project_1" : {
            "Project Name" : "Anomaly Detection Modules",
            "Details" : """Developed multiple anomaly detection modules that are executed daily by the operations team. These modules identify high-value risky orders in real-time, promptly alerting the risk team for immediate corrective action. Additionally, the modules detect customers who repeatedly purchase risky items in high quantity and customers with bank-declined orders, ensuring proactive risk mitigation and enhanced fraud prevention measures.""",
            "Savings" : "approx. 30L Monthly",
            "Tools" : "Python | SQL"
        },
                         "Project_2" : {
            "Project Name" : "Fake Returns Mitigation Report",
            "Details" : """Developed an advanced Fake Returns Model that analyzes customer, pickup/return point, and courier data to identify high-risk identities. By leveraging synergistic multiple datasets, the model generates actionable insights enabling the business to take proactive measures such as deactivating risky customers or stores, minimizing losses, and optimizing operational efficiency.""",
            "Savings" : "approx. 50L Monthly",
            "Tools" : "Python | SQL"
        }
                         }
    },
    "ORG3" : {
        "Company Name" : "Tesco",
        "URL" : "",
        "Role Name" : "Senior Analyst, Fraud Prevention",
        "From" : "08/2016",
        "To" : "10/2019",
        "Job Location" : "Bangalore, India",
        "Role Details" : ORG3_Details,
        "Key Projects" : {"Project_1" : {
            "Project Name" : "Transformed 3rd party risk detection monitors",
            "Details" : """converted Monitors into SQL queries, enabling greater customization andreducing reliance on external tools""",
            "Savings" : "approx. £50000 one time",
            "Tools" : "Python | SQL"
        },
                         "Project_2" : {
            "Project Name" : "Fraud rules Analysis",
            "Details" : """reduced false referrals by 70%, identifying critical and non-critical monitors and optimizing manual investigations""",
            "Savings" : "20hrs Monthly & £20000 Monthly",
            "Tools" : "Python | SQL"
        }
                         }
    },
    "ORG4" : {
        "Company Name" : "Amazon",
        "URL" : "",
        "Role Name" : "Risk Investigator, TRMS",
        "From" : "07/2014",
        "To" : "01/2014",
        "Job Location" : "Bangalore, India",
        "Role Details" : ORG4_Details,
        "Key Projects" : {"Project_1" : {
            "Project Name" : '',
            "Details" : '',
            "Savings" : '',
            "Tools" : ''
        }
                         }
    }
}


# In[21]:


# Other Variables
email_emoji = emoji.emojize(':envelope:')
phone_emoji = emoji.emojize(':telephone_receiver:')
Linkedin_URL_emoji = emoji.emojize(':arrow_upper_right:')
Linkedin_URL_emoji = "\U0001FE0F"
# \U000FE0F
Location_emoji = emoji.emojize(':house:')
birthday_emoji = emoji.emojize(':birthday_cake:')

Coding_emoji = emoji.emojize(':man_technologist:')
sheet_emoji = emoji.emojize(':page_facing_up:')
chart_emoji = emoji.emojize(':bar_chart:')
books_emoji = emoji.emojize(':books:')
savings_emoji = emoji.emojize(':moneybag:')
tools_emoji = emoji.emojize(':gear:')
details_emoji = emoji.emojize(':information_source:')
download_resume_emoji = emoji.emojize(':memo:')

profile_emoji = emoji.emojize(':male-detective:')
skills_emoji = emoji.emojize(':toolbox:')
workexp_emoji = emoji.emojize(':briefcase:')
education_emoji = emoji.emojize(':mortar_board:')
projects_emoji = emoji.emojize(':rocket:')

project_emoji = "\U0001F3AF"
resume_tab_emoji = "\U0001F5BA"
details_emoji_2 = "\U0001F6C8"
pen_emoji = emoji.emojize(':pen:')

right_point_emoji = emoji.emojize(':backhand_index_pointing_right:')


# In[30]:


st.set_page_config(page_title=First_Name+' Resume', page_icon=so5_logo,layout="wide")
css_file =  (r"styles/main.css")
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)


# In[8]:


#Streamlit top Markdows
# st.markdown(""" <style>
# #MainMenu {visibility: hidden;}
# footer {visibility: hidden;}
# </style> """, unsafe_allow_html=True)
# st.markdown("""
#         <style>
#                .css-18e3th9 {
#                     padding-top: 0rem;
#                     padding-bottom: 10rem;
#                     padding-left: 5rem;
#                     padding-right: 5rem;
#                 }
#                .css-1d391kg {
#                     padding-top: 0rem;
#                     padding-right: 1rem;
#                     padding-bottom: 3.5rem;
#                     padding-left: 1rem;
#                 }
#         </style>
#         """, unsafe_allow_html=True)

# st.markdown("""
#     <style>
#     [data-testid=column]:nth-of-type(1) [data-testid=stVerticalBlock]{
#         gap: 0rem;
#     }
#     </style>
#     """,unsafe_allow_html=True)

# hide_full_screen = '''
# <style>
# .element-container:nth-child(3) .overlayBtn {visibility: hidden;}
# .element-container:nth-child(12) .overlayBtn {visibility: hidden;}
# </style>
# '''

# st.markdown(hide_full_screen, unsafe_allow_html=True) 

# hide_img_fs = '''
# <style>
# button[title="View fullscreen"]{
#     visibility: hidden;}
# </style>
# '''

# st.markdown(hide_img_fs, unsafe_allow_html=True)

with open(Pdf_Resume,'rb') as pdf_file:
    Pdf_Resume_bn = pdf_file.read()

Profile_pic_i = Image.open(Profile_pic)

# password = open('Pwd.txt','r').read()


# In[38]:


# text_input_container = st.empty()
# t = text_input_container.text_input("Enter Password",type='password')


# if t==password:
#     pass
# else:
#     if len(t)>0:
#         st.caption('Incorrect Password entered')
#     else:
#         st.write('Enter Password ...')
#         st.stop()
#     sys.exit()

# if t != "":
#     text_input_container.empty()


# In[11]:


tab1, tab2 = st.tabs([resume_tab_emoji+" Resume", project_emoji+" Projects"])


# In[17]:


# Resume Front
with tab1:
    col1, col2 = st.columns([2,7])
    with col1:
        st.caption('#')
        st.image(Profile_pic_i, width=230)

    with col2:
        st.title(Full_Name)
        st.markdown(f'<p style="color:#ffffff;font-size:18px;margin-bottom:0;text-align:left;"><b> '+Current_Designation+' ,'+Current_Team+' </b></p>',unsafe_allow_html=True)
        st.write(Short_Headline)
        st.download_button(
            label=download_resume_emoji+" Download Resume",
            data=Pdf_Resume_bn,
            file_name=First_Name+' Resume.pdf',
            mime="application/octet-stream",
        )
        st.markdown(f'<p style="color:#ffffff;font-size:16px;margin-bottom:0;text-align:left;">'+email_emoji+' '+Email+' | '+phone_emoji+' '+Phone+'</p>',unsafe_allow_html=True)
        st.markdown(f'<p style="color:#ffffff;font-size:16px;margin-bottom:0;text-align:left;">'+Linkedin_URL_emoji+' '+Linkedin_URL+' | '+Location_emoji+' '+Location+'</p>',unsafe_allow_html=True)
        st.markdown(f'<p style="color:#ffffff;font-size:16px;margin-bottom:0;text-align:left;">'+birthday_emoji+' '+birthdate+'</p>',unsafe_allow_html=True)
#         st.write(email_emoji, Email,'|',phone_emoji,Phone)
#         st.write(Linkedin_URL_emoji, Linkedin_URL,'|',Location_emoji,Location)
    
    # About Streamlit Resume
    st.subheader(details_emoji_2+"  E-Resume Information")
    st.write(E_resume)
    
    # Profile
    st.subheader(profile_emoji+" Profile")
    st.write(Profile)

    # Skills
    st.subheader(skills_emoji+" Skills")
    st.write("""
    - """+Coding_emoji+""" SQL : Azure, Redshift, Snowflake, Hadoop | ★★★★✬
    - """+Coding_emoji+""" Python : Pandas, Selenium, Streamlit, Numpy, Plotly | ★★★★
    - """+chart_emoji+""" Excel | ★★★★✬
    - """+chart_emoji+""" Tableau | ★★★★
    - """+chart_emoji+""" MicroStrategy | ★★★
    - """+books_emoji+""" Statistics : Hypothesis testing, AB Testing, Probabiltity | ★★★✬
    """)

    # Work Experience

    st.subheader(workexp_emoji+" Work Experience")
    st.write(right_point_emoji+" for Project details, visit next tab")
    for i in Professional_Experience.keys():
        l1=str((Professional_Experience[i]['Role Name'],'|',Professional_Experience[i]['Company Name']))
        l2=(Professional_Experience[i]['From'],'-',Professional_Experience[i]['To'],'|',Professional_Experience[i]['Job Location'])
        l3=(Professional_Experience[i]['Role Details'])
        st.markdown(f'<p style="color:#ffffff;font-size:18px;margin-bottom:0;text-align:left;"><b> '+Professional_Experience[i]['Role Name']+' | '+Professional_Experience[i]['Company Name']+' </b></p>',unsafe_allow_html=True)
        st.markdown(f'<p style="color:#ffffff;font-size:13px;margin-bottom:0;text-align:left;"><b> '+Professional_Experience[i]['From']+'-'+Professional_Experience[i]['To']+' | '+Professional_Experience[i]['Job Location']+' </b></p>',unsafe_allow_html=True)
        st.caption(Professional_Experience[i]['Role Details'])
        for j in Professional_Experience[i]['Key Projects']:
            if Professional_Experience[i]['Key Projects'][j]['Project Name'] != '':
                l4 = Professional_Experience[i]['Key Projects'][j]['Project Name']
#                 l5 = Professional_Experience[i]['Key Projects'][j]['Details']
#                 l6 = Professional_Experience[i]['Key Projects'][j]['Savings']
#                 l7 = Professional_Experience[i]['Key Projects'][j]['Tools']
                col3,col4 = st.columns([1,90])
                col4.write('- '+l4)
#                 with st.expander("See explanation"):
#                     st.caption(details_emoji+' : '+l5)
#                     st.caption(savings_emoji+' : '+l6)
#                     st.caption(tools_emoji+' : '+l7)
        st.caption('')

    # Education 

    st.subheader(education_emoji+" Education")
    st.markdown(f'<p style="color:#ffffff;font-size:18px;margin-bottom:0;text-align:left;"><b> '+Higest_Education+' ,'+HE_University+' </b></p>',unsafe_allow_html=True)
    st.markdown(f'<p style="color:#ffffff;font-size:13px;margin-bottom:0;text-align:left;"><b> '+HE_From+'-'+HE_To+' | '+HE_Location+' </b></p>',unsafe_allow_html=True)


# In[13]:


with tab2:
    st.subheader(projects_emoji+" Projects")
    for i in Professional_Experience.keys():
        if Professional_Experience[i]['Key Projects']['Project_1']['Project Name']!='':            
            l2_1=str(Professional_Experience[i]['Company Name'])
            st.markdown(f'<p style="color:#ffffff;font-size:18px;margin-bottom:0;text-align:left;"><b> '+Professional_Experience[i]['Company Name']+' </b></p>',unsafe_allow_html=True)
            for j in Professional_Experience[i]['Key Projects']:
                if Professional_Experience[i]['Key Projects'][j]['Project Name'] != '':
                    l4 = Professional_Experience[i]['Key Projects'][j]['Project Name']
                    l5 = Professional_Experience[i]['Key Projects'][j]['Details']
                    l6 = Professional_Experience[i]['Key Projects'][j]['Savings']
                    l7 = Professional_Experience[i]['Key Projects'][j]['Tools']
                    col3,col4 = st.columns([1,90])
                    col4.write('- '+l4)
                    with st.expander("See explanation"):
                        st.caption(details_emoji+' : '+l5)
                        st.caption(savings_emoji+' : '+l6)
                        st.caption(tools_emoji+' : '+l7)
            st.caption('')
            


# In[14]:


# tab = st.selectbox('Tab to shorten and make scrollable:', [1])
# css=f'''
# div.stTabs > div > div:nth-of-type({tab+1}) {{
#     color: red;
#     height: 10px;
#     overflow-y: scroll;
#     overflow-x: hidden;
# }}
# '''
# st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)


# In[26]:


# import nbformat
# from nbconvert import PythonExporter
# My_Loc = r'C:\Users\mahes\Streamlit_Resume'
# def convertNotebook(notebookPath, modulePath):

#     with open(notebookPath) as fh:
#         nb = nbformat.reads(fh.read(), nbformat.NO_CONVERT)
#     exporter = PythonExporter()
#     source, meta = exporter.from_notebook_node(nb)
#     with open(modulePath, 'w+') as fh:
#         fh.write(source)
        
# convertNotebook(f'{My_Loc}\Slit_Resume2.ipynb',f'{My_Loc}\Slit_Resume2.py')

