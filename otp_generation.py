#!/usr/bin/env python3
"""This module generates random 4-digit OTPs and saves them to a CSV file.
It provides functions to create OTPs and write them to a specified file.
Usage: Run the script directly to generate a sample CSV with 500 OTPs.
"""
from random import randint
import pandas as pd

def otp_generator():
    """The core function which generates the individual OTP"""
    return int("".join([str(randint(0,9)) for i in range(4)]))

def otp_collection(limit):
    """Function module which generates n OTP's depending
    upon the limit and store them in a CSV file"""
    result=[]
    for _ in range(limit):
        result.append(otp_generator())
    #Converting the collected sample OTP into a CSV file
    pd.DataFrame(data=result,columns=["Dummy_OTP's"]).to_csv("OTP_Collections.csv",index=False)

if __name__=="__main__":
    otp_collection(500)
