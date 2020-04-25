#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup
import urllib


result = requests.get('https://python.org/downloads')
src = result.content
soup = BeautifulSoup(src, 'html.parser')
all_versions = soup.select('.list-row-container li')
for version in all_versions:
    for i in version.select(".release-date"):
        variablename = (i.get_text())
        if "April 6, 2013" in version.select(".release-date")[0].get_text():
            version_number = str(version.select(".release-number")[0].get_text()).split(" ")[1]
            if "2.7" in version_number:
                    urllib.urlretrieve("https://www.python.org/ftp/python/" + version_number + "/python-" + \
                        version_number + ".amd64.msi", 'briston_python_version_274.msi')