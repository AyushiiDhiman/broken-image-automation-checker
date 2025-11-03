import pytest
import requests
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from jinja2 import Template
import time


def test_broken_images(pytestconfig):

    
    target_url = pytestconfig.getoption("url")

    # ✅ Default URL if none provided
    if not target_url:
        target_url = "https://practicetestautomation.com/"

    
    service = Service("drivers/chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    driver.get(target_url)
    driver.maximize_window()
    time.sleep(2)

   
    images = driver.find_elements(By.TAG_NAME, "img")
    results = []

    for img in images:
        img_url = img.get_attribute("src")

        if not img_url:
            results.append(["N/A", "BROKEN", "No src attribute"])
            continue

        try:
            response = requests.get(img_url, timeout=5)
            status = response.status_code

            if status >= 400:
                results.append([img_url, "BROKEN", status])
            else:
                results.append([img_url, "WORKING", status])

        except Exception as e:
            results.append([img_url, "BROKEN", str(e)])

    driver.quit()

    df = pd.DataFrame(results, columns=["Image URL", "Status", "Code"])
    df.to_csv("reports/broken_images_report.csv", index=False)

   
    html_template = """
    <html>
    <head>
        <title>Broken Image Report</title>
        <style>
            body {font-family: Arial; padding: 20px;}
            table {border-collapse: collapse; width: 100%;}
            th, td {border: 1px solid #ddd; padding: 8px;}
            th {background-color: #4CAF50; color: white;}
            .broken {background-color: #ffcccc;}
            .working {background-color: #ccffcc;}
        </style>
    </head>
    <body>
        <h2>Broken Image Report for {{ url }}</h2>

        <table>
            <tr>
                <th>Image URL</th>
                <th>Status</th>
                <th>Code</th>
            </tr>

            {% for row in data %}
            <tr class="{{ row[1]|lower }}">
                <td>{{ row[0] }}</td>
                <td>{{ row[1] }}</td>
                <td>{{ row[2] }}</td>
            </tr>
            {% endfor %}
        </table>
    </body>
    </html>
    """

    template = Template(html_template)
    html_output = template.render(url=target_url, data=results)

    with open("reports/broken_images_report.html", "w", encoding="utf-8") as f:
        f.write(html_output)

    print(" HTML report generated at: reports/broken_images_report.html")
    print(" CSV report generated at: reports/broken_images_report.csv")

    assert True






