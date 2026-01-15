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
import datetime
import requests
import pandas as pd
import plotly.express as px
import base64
from datetime import timedelta
import plotly.figure_factory as ff


# # In[23]:
bot_token = '7470750444:AAEVSp9woUIREXs7RiBmgRgaQF9S4NGMNj4'
# chat_id = 123
# def telegram_send_message(message,bot_token=bot_token,chat_id = group_chat_id):
#     """
#     Sends a message via Telegram bot API.

#     Args:
#     - bot_token (str): The API token of your Telegram bot.
#     - chat_id (int or str): The chat ID where the message should be sent. 
#                             Use negative values for group chat IDs.
#     - message (str): The message to be sent.
    
#     Returns:
#     - dict: JSON response from the Telegram API.
#     """
#     url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
#     params = {
#         'chat_id': chat_id,
#         'text': message
#     }
#     response = requests.get(url, params=params)
#     return response.json()

# response = requests.get('https://ipinfo.io')
# data = response.json()
# # Extract relevant data
# ip_address = data['ip']
# city = data['city']
# region = data['region']
# country = data['country']
# isp = data.get('org', 'Unknown')
# timezone = data.get('timezone', 'Unknown')
# hostname = data.get('hostname', 'Unknown')
# organization = data.get('org', 'Unknown')
# visit_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
# txt_file_path = 'visitor_data.txt'
# line = f"DR,{ip_address},{city},{region},{country},{isp},{timezone},{hostname},{visit_time}\n"
# st.write(line)
# telegram_send_message(message=line)
# telegram_send_message(message='url opened',chat_id=704541819)

so5_logo = Image.open(f"Resume_IC.png")
Profile_pic = (f"Profile_Pic.png")
Pdf_Resume = (f"Mahesh Resume.pdf")
#User Level Variables
First_Name = "Mahesh M"
Last_Name = "Bathija"
Full_Name = First_Name+' '+Last_Name
Current_Designation = "Manager"
Current_Team = "Business Intelligence"
Current_Organization = "Saks Global"
Current_Org_from = "12/2024"
Email = "maheshmbathija81193@gmail.com"
Phone = "+91 8951861604"
Linkedin_URL = "https://www.linkedin.com/in/maheshm8"
Location = "Bangalore, India"
birthdate = "November 1993"
Experience_yrs = 10


Skills = ['Python','SQL','Tableau','Excel','Streamlit','Statistics','Selenium','Team Management','Leadership','Data Analytics','Quant Analytics']

Higest_Education = "MBA"
HE_University = "Jain University"
HE_Location = "Bangalore, India"
HE_From = "2016"
HE_To = "2019"
Edu_Specialization = "Supply Chain & Logistics"

Profile = f"""BI Manager with {str(Experience_yrs)} +years of experience across global retail analytics, fraud & risk, and data-driven operations. 
Currently leading a 9-member Business Intelligence team delivering standardized, scalable BI solutions across Planning, Supply Chain, Digital Operations, and 
Finance. Strong in SQL, Python, and modern BI platforms, with a track record of driving reporting standardization, automation, and self-service analytics. 
Known for building high-performing teams and leading changes that improve decision quality, efficiency, and business impact."""

E_resume = """I have created this impressive "E-Resume" using Python and the Streamlit Framework. It serves as a platform to showcase my exceptional Python and Streamlit skillsets. The first tab elegantly presents my detailed resume, while the second tab showcases a collection of my accomplished projects, reflecting my proficiency and experience. I recommend viewing this E-Resume on a desktop for the best experience, as the interactive features and visualizations are optimized for larger screens, ensuring a smoother and more detailed presentation of my skills and projects."""

Short_Headline = f"""BI Manager with {Experience_yrs}+ years across global retail analytics, fraud & risk, and data-driven operations. Currently leading a global BI team delivering scalable analytics and automation for core retail decision-making."""

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


ORG5_Details = """BI Manager owning enterprise analytics and reporting strategy while leading a global team supporting core retail decision-making functions."""
ORG0_Details = """My Role - Lead and collaborate with the team to build,backtest, and deploy live algorithmic trading strategies\nfor stocks."""
ORG1_Details = """About Fraud Analytics Team – Detecting fraud, boosting revenue through trend identification and mitigation\n
Led a successful team of 2 analysts, collaborating on multiple projects and cutting false referrals by 35%."""
ORG2_Details = """About T&S Team – focuses on combating fraud for online marketplace and Logistics Fraud."""
ORG3_Details = """About Fraud Prevention Team – Fraud prevention for offline and online employees and customers"""
ORG4_Details = """About TRMS – Screen customer orders for fraud to prevent chargebacks and protect customers"""

Professional_Experience = {
"ORG5": {
    "Company Name": "Saks Global",
    "URL": "https://www.saksglobal.com/",
    "URL_Logo":"Saks_Global_logo.png",
    "Role Name": "Manager, BI Reporting",
    "From": "12/2024",
    "To": "Present",
    "Job Location": "Bangalore, India",
    "Role Details": ORG5_Details,
    "Key Projects": {
        "Project_1": {
            "Project Name": "Enterprise BI Standardization & Self-Service Enablement",
            "Details": """Led a multi-domain BI transformation to consolidate fragmented reporting into standardized, governed dashboards across Planning, Supply Chain, Digital Operations, and Finance. Defined common KPIs, redesigned semantic layers, and established self-service analytics, reducing dependency on BI for ad-hoc reporting and improving leadership trust in data.""",
            "Savings": "Improved decision efficiency; reduced recurring reporting effort by hundreds of hours annually",
            "Tools": "SQL | Python | Looker | Excel | DBT"
        },
        "Project_2": {
            "Project Name": "AI-Driven Image & Pose Analytics Program",
            "Details": """Led a cross-functional team to design and deliver an AI-based image and pose analytics solution to assess product imagery quality and alignment with catalog standards. Owned problem definition, delivery roadmap, stakeholder alignment, and integration into existing analytics workflows, enabling scalable adoption beyond traditional BI use cases.""",
            "Savings": "Reduced manual image review effort and improved catalog quality consistency at scale, 91% Accuracy",
            "Tools": "Python | Computer Vision | MediaPipe | SQL | BI Dashboards"
        }
    }
},
"ORG0": {
    "Company Name": "Stock Vertex Ventures",
    "URL": "https://www.indiratrade.com/",
    "URL_Logo":"indira.jpg",
    "Role Name": "Team Lead, Quant Analytics",
    "From": "02/2024",
    "To": "Present",
    "Job Location": "Bangalore, India",
    "Role Details": ORG0_Details,
    "Key Projects": {
        "Project_1": {
            "Project Name": "Alpha Derivatives Trading Strategy",
            "Details": """The strategy focused on developing an algorithm to automate buying and exiting derivative trades, leveraging advanced indicators. Additionally, it involved building comprehensive reporting tools using Streamlit for real-time analysis and insights""",
            "Savings": "ROI of 120%",
            "Tools": "Python | SQL | Streamlit"
        },
        "Project_2": {
            "Project Name": "Built entire SQL Database with Indices OHLC Data",
            "Details": """By building a custom SQL database for indices data, we significantly improved the reliability and efficiency of our backtesting process, reduced reliance on AWS servers, and gained greater control over data quality checks.""",
            "Savings": "approx 40hrs per Week",
            "Tools": "Python | SQLite"
        }
    }
},
    "ORG1" : {
        "Company Name" : "Hudson's Bay Company",
        "URL" : "https://www.hbc.com/",
        "URL_Logo":"HBC.png",
        "Role Name" : "Team Lead, Fraud Analytics",
        "From" : "09/2020",
        "To" : "12/2023",
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
            "Project Name" : "Carrier Data Integration",
            "Details" : """Successfully implemented a data ingestion system for scan events across 8 carrier partners. This initiative enabled the company to accurately monitor on-time delivery rates and significantly enhance delivery performance.""",
            "Savings" : "approx. 30hrs Monthly",
            "Tools" : "Snowflake | SQL | Python"
        },
                         "Project_5" : {
            "Project Name" : "Sizing Optimization Project",
            "Details" : """I led a project to enhance sizing charts on our website, focusing on key catalogue categories with high return rates due to sizing issues. Using SQL and Python for data extraction and analysis, I identified SKUs with the most returns where products were often reported as too large or too small. I refined the sizing charts for these specific categories, leveraging Tableau for data visualization to present insights and track improvements. This resulted in more accurate sizing guides, reduced returns, and improved customer satisfaction.""",
            "Savings" : "$2M",
            "Tools" : "SQL | Python"
        },
                         "Project_6" : {
            "Project Name" : "Daily/Weekly Report automation",
            "Details" : """automated daily fraud report generation using Selenium in Python, including sign-in, browsing, exporting, graph building, and emailing""",
            "Savings" : "approx. 20hrs Monthly",
            "Tools" : "Selenium | Python"
        }
                         }
    },
    "ORG2" : {
        "Company Name" : "Myntra",
        "URL" : "https://www.myntra.com/",
        "URL_Logo":"myntra.png",
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
        "URL" : "https://www.tesco.com/",
        "URL_Logo":"tesco.png",
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
        "URL" : "https://www.amazon.com/",
        "URL_Logo":"amazon.png",
        "Role Name" : "Risk Investigator, TRMS",
        "From" : "07/2014",
        "To" : "02/2016",
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
Linkedin_URL_emoji = emoji.emojize(':link:')
# Linkedin_URL_emoji = "\U0002197"
# \U000FE0F
Location_emoji = emoji.emojize(':house:')
birthday_emoji = emoji.emojize(':birthday_cake:')
office_emoji = emoji.emojize(':office_building:')

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
skills_emoji = emoji.emojize(':puzzle_piece:')
workexp_emoji = emoji.emojize(':briefcase:')
education_emoji = emoji.emojize(':mortar_board:')
projects_emoji = emoji.emojize(':rocket:')
chart_inc = emoji.emojize(':chart_increasing:')
necktie = emoji.emojize(':necktie:')
robot = emoji.emojize(':robot:')
bulb = emoji.emojize(':light_bulb:')
building_construction = emoji.emojize(':building_construction:')

project_emoji = "\U0001F3AF"
resume_tab_emoji = "\U0001F5BA"
details_emoji_2 = "\U0001F6C8"
pen_emoji = emoji.emojize(':pen:')

right_point_emoji = emoji.emojize(':backhand_index_pointing_right:')
left_point_emoji = emoji.emojize(':backhand_index_pointing_left:')

# 🤖 ⓘ📝 💡
# U+1F916
# U+24D8
# U+1F4DD
# https://emojidb.org/email-emojis?utm_source=user_search

# emoji.demojize('\U0001F916')
# emoji.demojize('\U0001F4A1')


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
# r = [9, 8, 8, 8, 8, 8, 7, 7, 6, 6,7.5,7.5,9]
# theta = ['Data Analytics',
#  'SQL',
#  'Excel',
#  'Streamlit',
#  'Python',
#  'Tableau',
#  'Statistics',
#  'Selenium',
#  'MicroStrategy',
#  'Quant Analytics',
# 'Leadership',
# 'REST API',
# 'Automation']

# Create a DataFrame and sort by Proficiency descending
# data = {'Skills': theta, 'Proficiency': r}
# df = pd.DataFrame(data).sort_values(by='Proficiency', ascending=False)

# Create the bar chart with a custom color scale
# fig = px.bar(df, x="Skills", y="Proficiency", color="Proficiency",
#             color_continuous_scale=[
#                 "rgb(173, 255, 47)",
#                 "rgb(0, 100, 0)"
#             ],
#             title="Skills Matrix")

# # Add black borders to bars and bold labels on x-axis
# fig.update_traces(marker=dict(line=dict(color='black', width=1)))
# fig.update_xaxes(tickfont=dict(size=10, family='Arial Black'))
# fig.update_layout(showlegend=False, coloraxis_showscale=False,
#                  title_font=dict(size=16, family='Arial Black'))  # Hide the color scale
# fig.update_layout(title_x=0.4,showlegend=False)
# fig.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)','paper_bgcolor': 'rgba(0, 0, 0, 0)',})
# fig.update_layout(height=270, width=700,showlegend=False,margin=dict(l=0, r=0, t=28, b=0))
# fig.update_layout(xaxis_showgrid=False, yaxis_showgrid=False)
# fig.update_layout(
#                   xaxis_title="<b>Skills</b>",  # Set x-axis title
#                   yaxis_title="<b>Proficiency</b>",
#                   xaxis_title_standoff=10,  # Adjust standoff for better spacing
#                   xaxis_tickfont=dict(size=10, family='Arial Black'))  # Bold x-axis labels
skills_data = {
    "Category": [
        "BI & Analytics Leadership","BI & Analytics Leadership","BI & Analytics Leadership",
        "Data & Analytics","Data & Analytics","Data & Analytics","Data & Analytics",
        "BI Platforms","BI Platforms","BI Platforms",
        "Automation & Engineering","Automation & Engineering",
        "Domain Expertise","Domain Expertise","Domain Expertise","Domain Expertise"
    ],
    "Skill": [
        "People Management","Stakeholder Management","BI Governance & KPI Standardization",
        "SQL","Python","Statistics","Excel",
        "Tableau","MicroStrategy","Streamlit",
        "Automation","REST API",
        "Fraud & Risk Analytics","Retail Analytics","BI","Quant Analytics"
    ],
    # Equal value → no ranking implied
    "Value": [1] * 16
}
df_skills = pd.DataFrame(skills_data)
fig = px.treemap(
    df_skills,
    path=["Category", "Skill"],
    values="Value",
    title="Core Competencies"
)

# ---- Styling to match your resume theme ----
fig.update_traces(
    textinfo="label",
    hovertemplate="<b>%{label}</b><extra></extra>",
    marker=dict(line=dict(color="black", width=1))
)

fig.update_layout(
    title_font=dict(size=16, family="Arial Black"),
    title_x=0.4,
    margin=dict(l=0, r=0, t=30, b=0),
    height=400,
    width=1400,
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)"
)

data = []
for i in Professional_Experience.keys():
    l1 = ' '.join([Professional_Experience[i]['Role Name'], '|', Professional_Experience[i]['Company Name']])
    l2s = ' '.join([Professional_Experience[i]['From']])
    l2c = ' '.join([Professional_Experience[i]['To']])
    l3 = Professional_Experience[i]['Role Details']
    data.append([l1, l2s,l2c, l3])
df = pd.DataFrame(data, columns=['Task', 'Start','Finish', 'Role Details'])
df['Start'] = pd.to_datetime('01/' + df['Start'], format='%d/%m/%Y')
df['Finish'] = df['Finish'].apply(lambda x: (datetime.datetime.today() + timedelta(days=60)) if x == 'Present' else pd.to_datetime('01/' + x, format='%d/%m/%Y'))
df['Finish'] = pd.to_datetime(df['Finish'].astype(str).str[:10],format='%Y-%m-%d')
df['Start'] = df['Start'].astype('str')
df['Finish'] = df['Finish'].astype('str')
df_dict_list = df.to_dict(orient='records')
# edu_rec = {"Task":Higest_Education+' | '+HE_University,
#           "Start":HE_From+"-01-01",
#           "Finish":HE_To+"-01-01",
#           "Role Details":Edu_Specialization}
# df_dict_list.append(edu_rec)
for record in df_dict_list:
    record['Start'] = pd.to_datetime(record['Start'])
df_dict_list_sorted = sorted(df_dict_list, key=lambda x: x['Start'])
for record in df_dict_list_sorted:
    record['Start'] = record['Start'].strftime('%Y-%m-%d')
fig2 = ff.create_gantt(df_dict_list_sorted) 
fig2.update_layout(
    title="Professional Experience Timeline",
    showlegend=False,
    xaxis_tickformat="%Y %b")
fig2.update_traces(marker=dict(line=dict(color='black', width=1)))
fig2.update_xaxes(tickfont=dict(size=10, family='Arial Black'))
fig2.update_layout(showlegend=False, coloraxis_showscale=False,
                 title_font=dict(size=16, family='Arial Black'))  # Hide the color scale
fig2.update_layout(title_x=0.3,showlegend=False)
fig2.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)','paper_bgcolor': 'rgba(0, 0, 0, 0)',})
fig2.update_layout(height=270, width=700,showlegend=False,margin=dict(l=0, r=0, t=28, b=0))
fig2.update_layout(xaxis_showgrid=False, yaxis_showgrid=False)
fig2.update_layout(xaxis={'rangeselector':{'visible':False}})
fig2.update_layout(
                  xaxis_title="<b>Year Month</b>",  # Set x-axis title
                  yaxis_title="<b>Role, Company</b>",
                  xaxis_title_standoff=10,  # Adjust standoff for better spacing
                  xaxis_tickfont=dict(size=10, family='Arial Black'))  # Bold x-axis labels
fig2.update_traces(
    hovertemplate="<b>%{y}</b><br>" +  # Display Role Name | Company Name
                  "Year Month: %{x:%Y %b}<br>")

tab1, tab2 = st.tabs([resume_tab_emoji+" Resume", building_construction+" Projects"])


# In[17]:
# hostname=socket.gethostname()
# IPAddr=socket.gethostbyname(hostname)
# uuid_str = uuid.uuid1()
# time_str = datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
# ano_data = ['HN: ',hostname,'IP: ',IPAddr,'UUID: ',uuid_str,'Time: ',time_str]

# with open(r'Data_Ref.txt', 'a') as fp:
#     fp.write("\n"+str(ano_data))
#     fp.close()

# Resume Front
with tab1:
    col1, col2 = st.columns([2,7])
    with col1:
        st.caption('#')
        st.image(Profile_pic_i, width=230)

    with col2:
        st.title(Full_Name)
        st.markdown(f'<p style="color:#ffffff;font-size:18px;margin-bottom:0;text-align:left;"><b> '+Current_Designation+', '+Current_Team+' </b></p>',unsafe_allow_html=True)
        st.write(Short_Headline)
        st.download_button(
            label=download_resume_emoji+" Download Resume",
            data=Pdf_Resume_bn,
            file_name=First_Name+' Resume.pdf',
            mime="application/octet-stream",
        )
        st.markdown(f'<p style="color:#ffffff;font-size:16px;margin-bottom:0;text-align:left;">'+email_emoji+' '+Email+' | '+phone_emoji+' '+Phone+'</p>',unsafe_allow_html=True)
        st.markdown(f'<p style="color:#ffffff;font-size:16px;margin-bottom:0;text-align:left;">{Linkedin_URL_emoji} <a href="{Linkedin_URL}" style="color:#ffffff;text-decoration:none;">{Linkedin_URL}</a> | {Location_emoji} {Location}</p>', unsafe_allow_html=True)
        st.markdown(f'<p style="color:#ffffff;font-size:16px;margin-bottom:0;text-align:left;">'+birthday_emoji+' '+birthdate+'</p>',unsafe_allow_html=True)
#         st.write(email_emoji, Email,'|',phone_emoji,Phone)
#         st.write(Linkedin_URL_emoji, Linkedin_URL,'|',Location_emoji,Location)
    st.write("#")    
    st.divider()
    # About Streamlit Resume
    st.subheader(bulb+"  E-Resume Information")
    st.write(E_resume)
    
    # Profile
    st.subheader(profile_emoji+" Profile")
    st.write(Profile)

        

    # Skills✬
    st.subheader(skills_emoji+" Skills")
    # colsk1,colsk2 = st.columns([1,1])
    # colsk1.write("""
    # - """+Coding_emoji+""" SQL : Azure, Redshift, Snowflake, Hadoop | ★★★★✬
    # - """+Coding_emoji+""" Python : Pandas, Selenium, Streamlit, Numpy, Plotly | ★★★★
    # - """+chart_emoji+""" Excel | ★★★★✬
    # - """+chart_emoji+""" Tableau | ★★★★
    # - """+chart_emoji+""" MicroStrategy | ★★★
    # - """+books_emoji+""" Statistics : Hypothesis testing, AB Testing, Probabiltity | ★★★✬
    # - """+chart_inc+""" Data Analytics | ★★★★
    # - """+chart_inc+""" Quant Analytics | ★★★
    # - """+necktie+""" Leadership | ★★★★
    # - """+robot+""" REST API | ★★★★
    # """)
    st.plotly_chart(fig)
    st.plotly_chart(fig2) 

    # Work Experience

    st.subheader(workexp_emoji+" Work Experience")
    st.write(right_point_emoji+right_point_emoji+" for Project details, visit next tab"+left_point_emoji+left_point_emoji)
    for i in Professional_Experience.keys():
        l1=str((Professional_Experience[i]['Role Name'],'|',Professional_Experience[i]['Company Name']))
        l2=(Professional_Experience[i]['From'],'-',Professional_Experience[i]['To'],'|',Professional_Experience[i]['Job Location'])
        l3=(Professional_Experience[i]['Role Details'])
        st.markdown(f'<p style="color:#ffffff;font-size:18px;margin-bottom:0;text-align:left;"><b> '+office_emoji+' '+Professional_Experience[i]['Role Name']+' | '+Professional_Experience[i]['Company Name']+'    </b>'+'<a href='+'"'+ Professional_Experience[i]['URL']+'"'+'><img src="data:image/png;base64,{}" style="margin-left:20px;" width="50" height="40"></a></p>'.format(base64.b64encode(open(Professional_Experience[i]['URL_Logo'], "rb").read()).decode()),unsafe_allow_html=True)
        # st.markdown(f'<p style="color:#ffffff;font-size:18px;margin-bottom:0;text-align:left;"><b> '+office_emoji+' '+Professional_Experience[i]['Role Name']+' | '+Professional_Experience[i]['Company Name']+' </b></p>',unsafe_allow_html=True)
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
    st.write(right_point_emoji+right_point_emoji+" for Project details, visit next tab"+left_point_emoji+left_point_emoji)
    # Education 
    st.subheader(education_emoji+" Education")
    st.markdown(f'<p style="color:#ffffff;font-size:18px;margin-bottom:0;text-align:left;"><b> '+Higest_Education+', '+HE_University+' </b></p>',unsafe_allow_html=True)
    st.markdown(f'<p style="color:#ffffff;font-size:13px;margin-bottom:0;text-align:left;"><b> '+HE_From+'-'+HE_To+' | '+HE_Location+' </b></p>',unsafe_allow_html=True)
    st.caption('Specialization : '+Edu_Specialization)


# In[13]:


with tab2:
    st.subheader(building_construction+" Projects")
    for i in Professional_Experience.keys():
        if Professional_Experience[i]['Key Projects']['Project_1']['Project Name']!='':            
            l2_1=str(Professional_Experience[i]['Company Name'])
            st.markdown(f'<p style="color:#ffffff;font-size:22px;margin-bottom:0;text-align:left;"><b> '+office_emoji+' '+Professional_Experience[i]['Company Name']+' </b></p>',unsafe_allow_html=True)
            for j in Professional_Experience[i]['Key Projects']:
                if Professional_Experience[i]['Key Projects'][j]['Project Name'] != '':
                    l4 = Professional_Experience[i]['Key Projects'][j]['Project Name']
                    l5 = Professional_Experience[i]['Key Projects'][j]['Details']
                    l6 = Professional_Experience[i]['Key Projects'][j]['Savings']
                    l7 = Professional_Experience[i]['Key Projects'][j]['Tools']
                    col3,col4 = st.columns([1,90])
                    st.markdown(f'<p style="color:#ffffff;font-size:16px;margin-bottom:0;text-align:left;"> '+'- '+l4+' </p>',unsafe_allow_html=True)    
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















