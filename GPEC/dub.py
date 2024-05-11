import requests, os, time
from dotenv import load_dotenv
import streamlit as st
def dubbing(url, lang):
    load_dotenv()

    BASE_URL = "https://client.camb.ai/apis"
    API_KEY = os.getenv("API_KEY")
    HEADERS = {"headers": {"x-api-key": API_KEY}}

    video_url = url
    payload = {
        'video_url': video_url,
        'source_language': 1, # English
        'target_language': lang, # Malayalam
    }
    res = requests.post(f"{BASE_URL}/end_to_end_dubbing", json=payload, **HEADERS)
    print(res.status_code)
    task_id = res.json()["task_id"]
    print(f"Task ID: {task_id}")

    while True:
        res = requests.get(f"{BASE_URL}/end_to_end_dubbing/{task_id}", **HEADERS)
        status = res.json()["status"]
        print(f"Polling: {status}")
        time.sleep(5)
        if status == "SUCCESS":
            run_id = res.json()["run_id"]
            break

    print(f"Run ID: {run_id}")
    res = requests.get(f"{BASE_URL}/dubbed_run_info/{run_id}", **HEADERS)
    link = res.json()["video_url"]
    return link