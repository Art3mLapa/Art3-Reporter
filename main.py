from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import json
import time
import os

print("\033[31m █████  ██████  ████████ ██████      ██████  ███████ ██████   ██████  ██████  ████████ ███████  ██████\033[0m")
print("\033[31m██   ██ ██   ██    ██         ██     ██   ██ ██      ██   ██ ██    ██ ██   ██    ██    ██      ██   ██\033[0m")
print("\033[31m███████ ██████     ██     █████      ██████  █████   ██████  ██    ██ ██████     ██    █████   ██████\033[0m")
print("\033[31m██   ██ ██   ██    ██         ██     ██   ██ ██      ██      ██    ██ ██   ██    ██    ██      ██   ██\033[0m")
print("\033[31m██   ██ ██   ██    ██    ██████      ██   ██ ███████ ██       ██████  ██   ██    ██    ███████ ██   ██\033[0m")
print("\033[31mv1.0 by art3mlapa\033[0m")

print("\033[33m[1] Asset(Audio,Decal,Place,Item)")
print("[2] Group")
print("[3] Profile\033[0m")

link_choice = int(input("\033[31mWhat you need mass-report? (1/2/3): "))
links = [
    "https://www.roblox.com/abusereport/asset?id=",
    "https://www.roblox.com/abuseReport/group?id=",
    "https://www.roblox.com/abusereport/userprofile?id="
]

# Проверьте, что введенное значение в диапазоне 1-3
selected_link = links[link_choice - 1] if 1 <= link_choice <= 3 else None

print("\033[33m[1] Inappropriate Language - Profanity & Adult Content")
print("[2] Asking for or Giving Private Information")
print("[3] Bullying, Harassment, Discrimination")
print("[4] Dating")
print("[5] Exploiting, Cheating, Scamming")
print("[6] Account Theft - Phishing, Hacking, Trading")
print("[7] Inappropriate Content - Place, Image, Model")
print("[8] Real Life Threats & Suicide Threats\033[0m")

reason_choice = input("\033[31m[?] Choice reason for report(1/.../8): ")

victim_id = input("\033[31m[?] Enter the victim's user/asset id: ")

script_directory = os.path.dirname(os.path.abspath(__file__))

chrome_driver_path = os.path.join(script_directory, 'chromedriver.exe')

chrome_service = ChromeService(chrome_driver_path)

options = webdriver.ChromeOptions()
options.add_argument("--disable-extensions")
options.add_argument("--disable-notifications")
#options.add_argument("--headless")
#options.add_argument("--log-level=3")

browser = webdriver.Chrome(service=chrome_service, options=options)

browser.get(f"{selected_link}{victim_id}")
with open("cookies.json", "r") as cookies_file:
    cookies_data = json.load(cookies_file)
    for cookie in cookies_data:
        if "sameSite" in cookie:
            supported_values = ["Strict", "Lax", "None"]
            if cookie["sameSite"] in supported_values:
                browser.add_cookie(cookie)
            else:
                del cookie["sameSite"]
                browser.add_cookie(cookie)
        else:
            browser.add_cookie(cookie)
            
browser.refresh()
while True:
    time.sleep(2)

    try:
        report_category_element = browser.find_element(By.ID, "ReportCategory")
        select = Select(report_category_element)
        select.select_by_value(reason_choice)
        report_abuse_element = browser.find_element(By.ID, "report-abuse")
        report_abuse_element.click()

        time.sleep(2)
        browser.back()

        print("\033[32m[^] Report successfully sent!\033[0m")
    except Exception as e:
        print(f"\033[31m[X] Error: {e}\033[0m")