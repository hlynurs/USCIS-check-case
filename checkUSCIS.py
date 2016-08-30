from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys
import smtplib
from email.mime.text import MIMEText

url = sys.argv[1]
receipt = sys.argv[2]
email = sys.argv[3]

#print("Sending information to website")
var = 1
while (var == 1):
    driver = webdriver.Firefox()
    driver.get(url)
    elem = driver.find_element_by_id("receipt_number")
    elem.clear()
    elem.send_keys(receipt)
    elem.submit()
    #elem.send_keys(Keys.RETURN)
    #print("Extracting text from results...")
    time.sleep(10)
    text = driver.find_element_by_class_name("text-center").text
    #print("Between finding element by class name and getting attribute")
    #print("Results: ")
    #print(text)
    driver.close()
    if (text.find('Biometricssd') == -1):
        break
    # Wait 12 hours before checking again
    time.sleep(43200)

# Out of loop
#print("Search term not found in text")
#print(text)

# Send e-mail to recipient including the results
msg = MIMEText(text)
msg['From'] = 'caseChecker@python.com'
msg['To'] = email
msg['Subject'] = "Case Update!"

s = smtplib.SMTP('Outgoing.verizon.net')
s.send_message(msg)
s.quit
