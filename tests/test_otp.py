# tests/test_otp.py
import os
from ..script import generate_otp, create_otp_csv

def test_generate_otp_length():
    otp = generate_otp(4)
    assert len(str(otp)) == 4  # OTP should be 4 digits

def test_generate_otp_range():
    otp = generate_otp(4)
    assert 1000 <= otp <= 9999  # OTP should be a 4-digit number

def test_create_otp_csv():
    filename = "test_otp.csv"
    create_otp_csv(filename, 5)  # Create a small CSV with 5 rows
    assert os.path.exists(filename)  # Check file was created
    os.remove(filename)  # Clean up after test
