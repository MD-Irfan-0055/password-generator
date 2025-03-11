import streamlit as st
import random
import string

def generate_password(length, use_digits, use_special_chars):
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits # add digits 0-9

    if use_special_chars:
        characters += string.punctuation

    return " ".join(random.choice(characters)for _ in range(length))

st.title("🔐 Password Generator")

length = st.slider("Password Length", min_value=8, max_value=16, value=14)

use_digits = st.checkbox("Include Digits")
use_special_chars = st.checkbox("Include Special Characters")

if st.button("Generate Password"):
    password = generate_password(length, use_digits, use_special_chars)
    st.write(f"Generated Password:", {password})

st.write("------")

st.write("Build with 🎉 by Muhammad Irfan (gihttps://github.com/MD-Irfan-0055)")