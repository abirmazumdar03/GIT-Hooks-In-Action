"""This module is used for testing purpose"""
import os
import sys
sys.path.append("E:/Git_Practise/Git_Learning/GIT-Hooks-In-Action")
from otp_generation import otp_collection


def test_create_otp_collection():
    """A simple test script to test out the otp_generator script"""
    otp_collection(300)
    assert os.path.exists("OTP_Collections.csv")
    os.remove("OTP_Collections.csv")
