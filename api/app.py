from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse, RedirectResponse
import requests
from bs4 import BeautifulSoup

app = FastAPI()

url = "https://app.videas.fr/auth/signup/"
signup_url = "https://app.videas.fr/auth/signup/"

@app.get("/create-account/{index}")
def create_account(index: int):
    try:
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
        
        if post_response.url == url:
            message = f"Account {index} already exists"
        else:
            message = f"Account {index} created"
        
        return JSONResponse(content={"message": message})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        # Redirect to the next account creation
        return RedirectResponse(url=f"/create-account/{index + 1}")

