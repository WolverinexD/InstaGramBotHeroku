import os

from dotenv import load_dotenv

# For Local Deploy
if os.path.exists(".env"):
    load_dotenv(".env")

# Necessary Vars
userpass = os.getenv("userpass")
usernaam = os.getenv("usernaam")

