from flask import Flask, request
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from selenium.webdriver.chrome.options import Options
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def hello():
    value = request.json
    barcode = value["barcode"]
    chrome_options = Options()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options=chrome_options)
    driver.get("https://www.ilacprospektusu.com/ara/ilac/barkod/"+str(barcode))
    driver.find_element(By.XPATH, "/html/body/table/tbody/tr[2]/td/table/tbody/tr/td/div/div/ul/li[1]/a[2]").click()
    prospektus = driver.find_element(By.XPATH, "/html/body/table/tbody/tr[3]/td/table/tbody/tr/td[1]/div").text
    prospektus = prospektus.split("\n")
    fields={"head":prospektus[0],"Value":prospektus[1:]}

    return fields
if __name__ == "__main__":
   app.run(debug=True)