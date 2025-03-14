import os
import sys

from src.Customer_Churn_Prediction.logger import logging
from src.Customer_Churn_Prediction.exception import CustomException
import pandas as pd
import pymysql
from dotenv import load_dotenv

load_dotenv()

host = os.getenv("host")
user = os.getenv("user")
password = os.getenv("password")
db = os.getenv("db")

def read_sql_data():
    logging.info("Reading SQL database started")
    try:
        mydb = pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db
        )
        logging.info(f"Connection Established: {mydb}")

        df = pd.read_sql_query("SELECT * FROM raw_data", mydb)
        print(df.head())

        mydb.close()  # Close the connection after reading data

        return df

    except Exception as e:
        raise CustomException(e, sys)

