import requests
from fastapi import FastAPI
from bs4 import BeautifulSoup

app = FastAPI()

url = "https://app.videas.fr/auth/signup/"
signup_url = "https://app.videas.fr/auth/signup/"

@app.get("/create-account/{index}")
def create_account(index: int):
    session = requests.Session()
    response = session.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    csrf_token = soup.find('input', {'name': 'csrfmiddlewaretoken'}).get('value')
    payload = {
        'csrfmiddlewaretoken': csrf_token,
        'email': f"mihai{index}.networkstudio@maildrop.cc",
        'password1': "NetworkStudio123.",
        'password2': "NetworkStudio123."
    }
    
    headers = {
        'Referer': url
    }
    
    post_response = session.post(signup_url, data=payload, headers=headers)
    if post_response.url == "https://app.videas.fr/auth/signup/":
        return {"message": f"Account {index} already exists"}
    return {"message": f"Account {index} created"}
