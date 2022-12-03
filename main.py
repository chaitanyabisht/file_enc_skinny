import streamlit as st
from stutils import encryptFile, decryptFile
import os

st.title('File Encryption Application')

uploaded_file = st.file_uploader("Choose a file")

# Choose encryption mode
mode = st.selectbox('Choose encryption mode', ('ECB', 'CBC', 'CTR'))
# Choose password
password = st.text_input('Enter password', value='', type='password')

# Encrypt
if st.button('Encrypt'):
    if uploaded_file is not None:
        # Write to file
        file = open(uploaded_file.name, 'wb')
        file.write(uploaded_file.getvalue())
        file.close()
        # Encrypt
        encryptFile(uploaded_file.name, password, mode)
        # Download file
        with open(uploaded_file.name + ".enc", 'rb') as f:
            bytes = f.read()
            st.download_button(label='Download', data=bytes, file_name=uploaded_file.name + ".enc", mime='application/octet-stream')
        # Delete original file
        os.remove(uploaded_file.name)
    else:
        st.error('Please upload a file')

elif st.button('Decrypt'):
    if uploaded_file is not None:
        # Write to file
        file = open(uploaded_file.name, 'wb')
        file.write(uploaded_file.getvalue())
        file.close()
        # Decrypt
        decryptFile(uploaded_file.name, password, mode)
        # Download file
        with open(uploaded_file.name[:-4] + ".dec", 'rb') as f:
            bytes = f.read()
            st.download_button(label='Download', data=bytes, file_name=uploaded_file.name[:-4] + ".dec", mime='application/octet-stream')
        # Delete original file
        os.remove(uploaded_file.name)
    else:
        st.error('Please upload a file')


