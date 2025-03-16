# script.py
import pandas as pd
from random import randint

def generate_otp(length):
    return int("".join([str(randint(0, 9)) for i in range(length)]))

def create_otp_csv(filename, num_rows):
    result = [generate_otp(4) for _ in range(num_rows)]
    pd.DataFrame(result, columns=["Dummy_OTP"]).to_csv(filename, index=False)

if __name__ == "__main__":
    create_otp_csv("Sample_OTP.csv", 500)
