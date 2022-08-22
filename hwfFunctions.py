from ctypes import py_object
from json.encoder import py_encode_basestring
import pyodbc

#get the installed driver from the host system
def get_driver():

    drivers = pyodbc.drivers()

    #cycle through ODBC drivers from newest to oldest
    if 'ODBC Driver 18 for SQL Server' in drivers:
        presentDriver = '{ODBC Driver 18 for SQL Server}'
    elif 'ODBC Driver 17 for SQL Server' in drivers:
        presentDriver = '{ODBC Driver 17 for SQL Server}'
    elif 'ODBC Driver 13.1 for SQL Server' in drivers:
        presentDriver = '{ODBC Driver 13.1 for SQL Server}'
    elif 'ODBC Driver 13 for SQL Server' in drivers:
        presentDriver = '{ODBC Driver 13 for SQL Server}'
    elif 'ODBC Driver 11 for SQL Server' in drivers:
        presentDriver = 'ODBC Driver 11 for SQL Server'
    elif 'SQL Server Native Client 11.0' in drivers:
        presentDriver = '{SQL Server Native Client 11.0}'
    elif 'SQL Server Native Client 11.0' in drivers:
        presentDriver = '{SQL Server Native Client 11.0}'

    return presentDriver