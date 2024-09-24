# importing libraries
import pandas as pd
import mysql.connector
import streamlit as slt

from streamlit_option_menu import option_menu
import plotly.express as px
import time
import pymysql

# kerala bus routes
lists_K=[]
df_K=pd.read_csv(r"D:\Redbus\df_ker.csv")
for i,r in df_K.iterrows():
    lists_K.append(r["Route_name"])

#Andhra bus routes
lists_A=[]
df_A=pd.read_csv("df_A.csv")
for i,r in df_A.iterrows():
    lists_A.append(r["Route_name"])

#Telangana bus routes
lists_T=[]
df_T=pd.read_csv("df_T.csv")
for i,r in df_T.iterrows():
    lists_T.append(r["Route_name"])

#Goa bus routes
lists_G=[]
df_G=pd.read_csv("df_G.csv")
for i,r in df_G.iterrows():
    lists_G.append(r["Route_name"])

#Rajasthan bus routes
lists_R=[]
df_R=pd.read_csv("df_R.csv")
for i,r in df_R.iterrows():
    lists_R.append(r["Route_name"])

# Bihar bus routes
lists_B=[]
df_B=pd.read_csv("df_b.csv")
for i,r in df_B.iterrows():
    lists_B.append(r["Route_name"])

# Punjab bus routes
lists_P=[]
df_P=pd.read_csv("df_P.csv")
for i,r in df_P.iterrows():
    lists_P.append(r["Route_name"])

#Assam bus routes
lists_AS=[]
df_AS=pd.read_csv("df_AS.csv")
for i,r in df_AS.iterrows():
    lists_AS.append(r["Route_name"])

# Uttar Pradesh bus routes
lists_UP=[]
df_UP=pd.read_csv("df_UP.csv")
for i,r in df_UP.iterrows():
    lists_UP.append(r["Route_name"])

# West bengal bus
lists_WB=[]
df_WB=pd.read_csv("df_WB.csv")
for i,r in df_WB.iterrows():
    lists_WB.append(r["Route_name"])

#setting up streamlit page
slt.set_page_config(layout="wide")

web=option_menu(menu_title="      🆁🅴🅳 🅱🆄🆂 🅾🅽🅻🅸🅽🅴 🅱🅾🅾🅺🅸🅽🅶 🅰🅿🅿 ",
                options=["Home","🌍🌍States and Routes"],
                
                orientation="horizontal"
                )
# Home page setting
if web=="Home":
    slt.image("redbus_img.jfif",width=200)
       
    slt.title("𝑹𝒆𝒅𝒃𝒖𝒔 𝑫𝒂𝒕𝒂 𝑺𝒄𝒓𝒂𝒑𝒊𝒏𝒈 𝒘𝒊𝒕𝒉 𝑺𝒆𝒍𝒆𝒏𝒊𝒖𝒎 & 𝑫𝒚𝒏𝒂𝒎𝒊𝒄 𝑭𝒊𝒍𝒕𝒆𝒓𝒊𝒏𝒈 𝒖𝒔𝒊𝒏𝒈 𝑺𝒕𝒓𝒆𝒂𝒎𝒍𝒊𝒕")
        
    slt.subheader(":red[Domain:]  Transportation")
    
    slt.subheader(":red[Problem Statement :] ")
    slt.markdown("The 'Redbus Data Scraping and Filtering with Streamlit Application' aims to revolutionize the transportation industry by providing a comprehensive solution for collecting, analyzing, and visualizing bus travel data. By utilizing Selenium for web scraping, this project automates the extraction of detailed information from Redbus, including bus routes, schedules, prices, and seat availability. By streamlining data collection and providing powerful tools for data-driven decision-making, this project can significantly improve operational efficiency and strategic planning in the transportation industry.")
    
    slt.subheader(":red[Business Use Cases :] ")
    slt.markdown("Travel Aggregators, Market Analysis ,Customer Service, Competitor Analysis ")
    
    slt.subheader(":red[Skills take away :]")
    slt.markdown("Web Scraping using Selenium, Python, Streamlit , MySQL")

    slt.subheader(":red[Softwares Used:]") 
    
    slt.markdown("Selenium: Selenium is an open-source, automated testing tool commonly used for web scraping...Selenium is designed to mimic human interaction, replicating actions like clicking buttons and typing text.")
    slt.markdown('''Python Pandas :  Pandas is a Python library used for working with data sets and used for analyzing, cleaning and preprocessing the data.''')
    slt.markdown("Python Streamlit : Streamlit is a free, open-source framework that lets data scientists and AI/ML engineers quickly build and share interactive web apps from Python scripts.")
    slt.markdown('''MySQL : MySQL is a relational database management system that uses SQL. SQL is primarily used to query and manipulate database tables for storage and retrieval.''')

    slt.subheader(":red[Project Done by :]  VINITH CHRISTON")
    

# States and Routes page setting

if web == "🌍🌍States and Routes":

    S = slt.selectbox("𝗦𝗧𝗔𝗧𝗘𝗦", sorted(["ANDHRA PRADESH","ASSAM","BIHAR","KERALA",  "TELANGANA", "GOA", "RAJASTHAN", 
                                           "PUNJAB",  "UTTAR PRADESH", "WEST BENGAL"]))
    
    col1,col2=slt.columns(2)
    with col1:
       
       select_type = slt.radio("𝐁𝐔𝐒 𝐓𝐘𝐏𝐄𝐒", ("sleeper", "semi-sleeper","seater","others"))
    with col2:
        
        select_fare = slt.radio("𝗕𝗨𝗦 𝗙𝗔𝗥𝗘 𝗥𝗔𝗡𝗚𝗘 ", ("0-500", "500-1000", "1000 and above"))
    TIME=slt.time_input("𝗗𝗘𝗣𝗔𝗥𝗧𝗨𝗥𝗘 𝗧𝗜𝗠𝗘")

    # Kerala bus fare filtering
    if S == "KERALA":
        K = slt.selectbox("𝗔𝗩𝗔𝗜𝗟𝗔𝗕𝗟𝗘 𝗥𝗢𝗨𝗧𝗘𝗦",lists_K)

        def type_and_fare(bus_type, fare_range):
            conn = pymysql.connect(host="localhost", user="root", password="Vinith@97", database="redbus")
            my_cursor = conn.cursor()
            # Define fare range based on selection

            if fare_range == "0-500":
                fare_min, fare_max = 0, 500
            elif fare_range == "500-1000":
                fare_min, fare_max = 500, 1000
            else:
                fare_min, fare_max = 1000, 100000  # assuming a high max value for "1000 and above"


            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "seater":
                bus_type_condition = "Bus_type LIKE '%Seater %'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%' AND Bus_type NOT LIKE '%Seater%'"

            query = f'''
                SELECT * FROM bus_details3 
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{K}"
                AND {bus_type_condition} AND Start_time>='{TIME}'
                ORDER BY Price and Start_time DESC
            '''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            conn.close()

            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df

        df_result = type_and_fare(select_type, select_fare)
        slt.dataframe(df_result)

    # Andhra Pradesh bus fare filtering
    if S=="ANDHRA PRADESH":
        A=slt.selectbox("𝗔𝗩𝗔𝗜𝗟𝗔𝗕𝗟𝗘 𝗥𝗢𝗨𝗧𝗘𝗦",lists_A)

        def type_and_fare_A(bus_type, fare_range):
            conn = pymysql.connect(host="localhost", user="root", password="Vinith@97", database="redbus")
            my_cursor = conn.cursor()

            # Define fare range based on selection
            if fare_range == "0-500":
                fare_min, fare_max = 0, 500
            elif fare_range == "500-1000":
                fare_min, fare_max = 500, 1000
            else:
                fare_min, fare_max = 1000, 100000  # assuming a high max value for "1000 and above"



            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "seater":
                bus_type_condition = "Bus_type LIKE '%Seater %'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%' AND Bus_type NOT LIKE '%Seater%'"
            
            
            query = f'''
                SELECT * FROM bus_details3 
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{A}"
                AND {bus_type_condition} AND Start_time>='{TIME}'
                ORDER BY Price and Start_time DESC
            '''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            conn.close()

            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df

        df_result = type_and_fare_A(select_type, select_fare)
        slt.dataframe(df_result)
          

    # Telangana bus fare filtering
    if S=="TELANGANA":
        T=slt.selectbox("𝗔𝗩𝗔𝗜𝗟𝗔𝗕𝗟𝗘 𝗥𝗢𝗨𝗧𝗘𝗦",lists_T)

        def type_and_fare_T(bus_type, fare_range):
            conn = pymysql.connect(host="localhost", user="root", password="Vinith@97", database="redbus")
            my_cursor = conn.cursor()

            # Define fare range based on selection
            if fare_range == "0-500":
                fare_min, fare_max = 0, 500
            elif fare_range == "500-1000":
                fare_min, fare_max = 500, 1000
            else:
                fare_min, fare_max = 1000, 100000  # assuming a high max value for "1000 and above"


            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "seater":
                bus_type_condition = "Bus_type LIKE '%Seater %'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%' AND Bus_type NOT LIKE '%Seater%'"

            query = f'''
                SELECT * FROM bus_details3 
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{T}"
                AND {bus_type_condition} AND Start_time>='{TIME}'
                ORDER BY Price and Start_time DESC
            '''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            conn.close()

            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df

        df_result = type_and_fare_T(select_type, select_fare)
        slt.dataframe(df_result)

    # Goa bus fare filtering
    if S=="GOA":
        G=slt.selectbox("𝗔𝗩𝗔𝗜𝗟𝗔𝗕𝗟𝗘 𝗥𝗢𝗨𝗧𝗘𝗦",lists_G)

        def type_and_fare_G(bus_type, fare_range):
            conn = pymysql.connect(host="localhost", user="root", password="Vinith@97", database="redbus")
            my_cursor = conn.cursor()
            # Define fare range based on selection
            if fare_range == "0-500":
                fare_min, fare_max = 0, 500
            elif fare_range == "500-1000":
                fare_min, fare_max = 500, 1000
            else:
                fare_min, fare_max = 1000, 100000  # assuming a high max value for "1000 and above"

  # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "seater":
                bus_type_condition = "Bus_type LIKE '%Seater %'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%' AND Bus_type NOT LIKE '%Seater%'"



            query = f'''
                SELECT * FROM bus_details3 
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{G}"
                AND {bus_type_condition} AND Start_time>='{TIME}'
                ORDER BY Price and Start_time DESC
            '''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            conn.close()

            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df

        df_result = type_and_fare_G(select_type, select_fare)
        slt.dataframe(df_result)

    # Rajasthan bus fare filtering
    if S=="RAJASTHAN":
        R=slt.selectbox("𝗔𝗩𝗔𝗜𝗟𝗔𝗕𝗟𝗘 𝗥𝗢𝗨𝗧𝗘𝗦",lists_R)

        def type_and_fare_R(bus_type, fare_range):
            conn = pymysql.connect(host="localhost", user="root", password="Vinith@97", database="redbus")
            my_cursor = conn.cursor()
            # Define fare range based on selection
            if fare_range == "0-500":
                fare_min, fare_max = 0, 500
            elif fare_range == "500-1000":
                fare_min, fare_max = 500, 1000
            else:
                fare_min, fare_max = 1000, 100000  # assuming a high max value for "1000 and above"


            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "seater":
                bus_type_condition = "Bus_type LIKE '%Seater %'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%' AND Bus_type NOT LIKE '%Seater%'"


            query = f'''
                SELECT * FROM bus_details3 
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{R}"
                AND {bus_type_condition} AND Start_time>='{TIME}'
                ORDER BY Price and Start_time DESC
            '''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            conn.close()

            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df

        df_result = type_and_fare_R(select_type, select_fare)
        slt.dataframe(df_result)
          

    # Punjab bus fare filtering       
    if S=="PUNJAB":
        P=slt.selectbox("𝗔𝗩𝗔𝗜𝗟𝗔𝗕𝗟𝗘 𝗥𝗢𝗨𝗧𝗘𝗦",lists_P)

        def type_and_fare_P(bus_type, fare_range):
            conn = pymysql.connect(host="localhost", user="root", password="Vinith@97", database="redbus")
            my_cursor = conn.cursor()
            # Define fare range based on selection
            if fare_range == "0-500":
                fare_min, fare_max = 0, 500
            elif fare_range == "500-1000":
                fare_min, fare_max = 500, 1000
            else:
                fare_min, fare_max = 1000, 100000  # assuming a high max value for "1000 and above"


            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "seater":
                bus_type_condition = "Bus_type LIKE '%Seater %'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%' AND Bus_type NOT LIKE '%Seater%'"



            query = f'''
                SELECT * FROM bus_details3 
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{P}"
                AND {bus_type_condition} AND Start_time>='{TIME}'
                ORDER BY Price and Start_time DESC
            '''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            conn.close()

            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df

        df_result = type_and_fare_P(select_type, select_fare)
        slt.dataframe(df_result)
    
    # Bihar bus fare filtering
    if S=="BIHAR":
        B=slt.selectbox("𝗔𝗩𝗔𝗜𝗟𝗔𝗕𝗟𝗘 𝗥𝗢𝗨𝗧𝗘𝗦",lists_B)

        def type_and_fare_B(bus_type, fare_range):
            conn = pymysql.connect(host="localhost", user="root", password="Vinith@97", database="redbus")
            my_cursor = conn.cursor()
            # Define fare range based on selection
            if fare_range == "0-500":
                fare_min, fare_max = 0, 500
            elif fare_range == "500-1000":
                fare_min, fare_max = 500, 1000
            else:
                fare_min, fare_max = 1000, 100000  # assuming a high max value for "1000 and above"


            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "seater":
                bus_type_condition = "Bus_type LIKE '%Seater %'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%' AND Bus_type NOT LIKE '%Seater%'"



            query = f'''
                SELECT * FROM bus_details3 
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{B}"
                AND {bus_type_condition} AND Start_time>='{TIME}'
                ORDER BY Price and Start_time DESC
            '''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            conn.close()

            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df

        df_result = type_and_fare_B(select_type, select_fare)
        slt.dataframe(df_result)


    # Assam bus fare filtering
    if S=="ASSAM":
        AS=slt.selectbox("𝗔𝗩𝗔𝗜𝗟𝗔𝗕𝗟𝗘 𝗥𝗢𝗨𝗧𝗘𝗦",lists_AS)

        def type_and_fare_AS(bus_type, fare_range):
            conn = pymysql.connect(host="localhost", user="root", password="Vinith@97", database="redbus")
            my_cursor = conn.cursor()
            # Define fare range based on selection
            if fare_range == "0-500":
                fare_min, fare_max = 0, 500
            elif fare_range == "500-1000":
                fare_min, fare_max = 500, 1000
            else:
                fare_min, fare_max = 1000, 100000  # assuming a high max value for "1000 and above"


            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "seater":
                bus_type_condition = "Bus_type LIKE '%Seater %'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%' AND Bus_type NOT LIKE '%Seater%'"



            query = f'''
                SELECT * FROM bus_details3 
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{AS}"
                AND {bus_type_condition} AND Start_time>='{TIME}'
                ORDER BY Price and Start_time DESC
            '''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            conn.close()

            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df

        df_result = type_and_fare_AS(select_type, select_fare)
        slt.dataframe(df_result)

    # Uttar Pradesh bus fare filtering
    if S=="UTTAR PRADESH":
        UP=slt.selectbox("AVAILABLE ROUTES",lists_UP)

        def type_and_fare_UP(bus_type, fare_range):
            conn = pymysql.connect(host="localhost", user="root", password="Vinith@97", database="redbus")
            my_cursor = conn.cursor()
            # Define fare range based on selection
            if fare_range == "0-500":
                fare_min, fare_max = 0, 500
            elif fare_range == "500-1000":
                fare_min, fare_max = 500, 1000
            else:
                fare_min, fare_max = 1000, 100000  # assuming a high max value for "1000 and above"



            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "seater":
                bus_type_condition = "Bus_type LIKE '%Seater %'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%' AND Bus_type NOT LIKE '%Seater%'"



            query = f'''
                SELECT * FROM bus_details3 
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{UP}"
                AND {bus_type_condition} AND Start_time>='{TIME}'
                ORDER BY Price and Start_time DESC
            '''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            conn.close()

            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df

        df_result = type_and_fare_UP(select_type, select_fare)
        slt.dataframe(df_result)

    # West Bengal bus fare filtering
    if S=="WEST BENGAL":
        WB=slt.selectbox("𝗔𝗩𝗔𝗜𝗟𝗔𝗕𝗟𝗘 𝗥𝗢𝗨𝗧𝗘𝗦",lists_WB)

        def type_and_fare_WB(bus_type, fare_range):
            conn = pymysql.connec
            (host=="localhost", user=="root", password=="Vinith@97", database=="redbus")
            my_cursor = conn.cursor()
            # Define fare range based on selection
            if fare_range == "0-500":
                fare_min, fare_max = 0, 500
            elif fare_range == "500-1000":
                fare_min, fare_max = 500, 1000
            else:
                fare_min, fare_max = 1000, 100000  # assuming a high max value for "1000 and above"

            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "seater":
                bus_type_condition = "Bus_type LIKE '%Seater %'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%' AND Bus_type NOT LIKE '%Seater%'"



            query = f'''
                SELECT * FROM bus_details3 
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{WB}"
                AND {bus_type_condition} AND Start_time>='{TIME}'
                ORDER BY Price and Start_time  DESC
            '''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            conn.close()

            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df

        df_result = type_and_fare_WB(select_type, select_fare)
        slt.dataframe(df_result)


