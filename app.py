import urllib.parse
import os

from flask import Flask, request as flask_request, redirect

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

app = Flask('__main__')
SITE_NAME = 'https://www.legifrance.gouv.fr/'

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def proxy(path):
    # when testing in browser: avoid downloading fonts and requests overloading
    if path.endswith('.ttf') or path.endswith('.js') or path.endswith('.css') or path.endswith('.png') or path.endswith('.ico'):
        return ''

    url = f'{SITE_NAME}{path}?' + urllib.parse.urlencode(flask_request.args)
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    # when blocked, changing user agent unblock it
    chrome_options.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:74.0) Gecko/20100101 Firefox/74.0")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    html = driver.page_source

    # if blocked, a refresh can solve it
    if 'src="/_Incapsula_Resource' in html:
        driver.get(url)
        html = driver.page_source

    if driver.current_url != url:
        return redirect(driver.current_url.replace(SITE_NAME, '/'))

    driver.quit()
    return html

app.run(host='0.0.0.0', port=8081)