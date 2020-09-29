import urllib.parse
import os

from flask import Flask, request as flask_request

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

app = Flask('__main__')
SITE_NAME = 'https://www.legifrance.gouv.fr/'

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def proxy(path):
    url = f'{SITE_NAME}{path}?' + urllib.parse.urlencode(flask_request.args)
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    html = driver.page_source.encode("utf-8")
    driver.quit()
    os.system("rm -f *.crdownload")
    return html

app.run(host='0.0.0.0', port=8080)