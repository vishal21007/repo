"""Generate 6 digit Random Secure OTP"""
import random
s=random.random()
print("The otp is : ",int(s*1000000))