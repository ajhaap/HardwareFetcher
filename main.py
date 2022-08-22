from sqlite3 import connect
import openpyxl
import pyodbc
import pandas as pd
import os
import hwfFunctions

#find which driver is installed on the system
presentDriver = hwfFunctions.get_driver()

#create connection
connection = pyodbc.connect(
    driver = presentDriver,
    host = "localhost",
    database = "Surveillance",
    trusted_connection = "Yes"
    )

sqlQuery = "SELECT dbo.Hardware.Name, TRIM('htp:/' FROM URI) as URI, MacAddress, \
            SerialNumber, DetectedModel, dName FROM dbo.Hardware \
            INNER JOIN (SELECT dbo.Devices.IDHardware as dIDHardware, \
            dbo.Devices.Name AS dName, DeviceType, DeviceIndex FROM dbo.Devices) \
            AS paluu ON dbo.Hardware.IDHardware = paluu.dIDHardware WHERE DeviceType='Camera' \
            AND DeviceIndex='0'"

df = pd.read_sql(sql = sqlQuery, con = connection)

df.to_excel("c:\\tmp\\" + "databasetest.xlsx")

connection.close
