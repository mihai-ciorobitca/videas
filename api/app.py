from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from fastapi import FastAPI

app = FastAPI()

url = "https://app.videas.fr/auth/signup/"
chrome_options = Options()
chrome_options.add_argument("--headless")

@app.get("/create-account/{index}")
def create_account(index: int):
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    email_input = driver.find_element(By.NAME, "email")
    email_input.send_keys(f"mihai{index}.networkstudio@maildrop.cc")
    password1_input = driver.find_element(By.NAME, "password1")
    password1_input.send_keys("NetworkStudio123.")
    password2_input = driver.find_element(By.NAME, "password2")
    password2_input.send_keys("NetworkStudio123.")
    signup_button = driver.find_element(By.CSS_SELECTOR, "#signup_form > button")
    signup_button.click()
    driver.quit()
    return {"message": f"Account {index} created successfully."}
