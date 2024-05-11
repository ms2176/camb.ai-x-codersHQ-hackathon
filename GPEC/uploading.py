import requests
from dub import dubbing
from selenium import webdriver
import streamlit as st
def uploading_file(file_path):
    def upload_to_catbox(file_path, userhash=None):
        try:
            # Open the file in binary mode and read its contents
            with open(file_path, 'rb') as file:
                # Create a dictionary with the file to be uploaded
                files = {'fileToUpload': file}
                
                # Additional arguments for the request
                args = {'userhash': userhash, 'reqtype': 'fileupload'}
                
                # Make a POST request to Catbox API
                response = requests.post('https://catbox.moe/user/api.php', files=files, data=args)
                
                # Check if the request was successful
                if response.status_code == 200:
                    # Extract the link from the response text
                    link = response.text
                    return link.strip()  # Remove any leading or trailing whitespace
                else:
                    print("Failed to upload file. Status code:", response.status_code)
        except FileNotFoundError:
            print("File not found:", file_path)
        except Exception as e:
            print("An error occurred:", str(e))

    # Example usage
    file_path = file_path
    # Replace 'Your userhash here' with your actual userhash if you have one, otherwise, leave it as None
    userhash = None
    cloud_link = upload_to_catbox(file_path, userhash)
    if cloud_link:
        print("Cloud link:", cloud_link)
    st.write("Video has been uploaded successfully!")
    return cloud_link
