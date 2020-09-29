# legifrance-proxy
*Selenium proxy to bypass the anti-scrapping protection of Legifrance*

More precisely, given a request to legifrance, this script will launch an headless browser via Selenium
to do the request in a real browser and return the HTML

## Installation

```
pip install -r requirements.txt
sudo apt install chromium chromium-driver
```

## Usage

### Launching the server

```
python app.py
```

### Requesting a page

```
http://0.0.0.0:8080/<path>?<args>
ex: http://0.0.0.0:8080/liste/legislatures
```
