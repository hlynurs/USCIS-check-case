from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys
import smtplib
from email.mime.text import MIMEText

url = sys.argv[1]
receipt = sys.argv[2]
email = sys.argv[3]
userid = sys.argv[4]
userpassword = sys.argv[5]

#print("Sending information to website")
var = 1
while (var == 1):
    driver = webdriver.Firefox()
    driver.get(url)
    elem = driver.find_element_by_id("receipt_number")
    elem.clear()
    elem.send_keys(receipt)
    elem.submit()
    time.sleep(10)
    text = driver.find_element_by_class_name("text-center").text
    driver.close()
    if (text.find('Biometrics') == -1):
        break
    # Wait 12 hours before checking again
    time.sleep(43200)

# Out of loop
# Send e-mail to recipient including the results
message = 'Subject: %s\n\n%s' % ("Case Update!", text)
print("Case has been updated, sending e-mail")
s = smtplib.SMTP('smtp.gmail.com:587')
s.starttls()
s.ehlo()
s.login(userid, userpassword)
s.sendmail('caseCheck@python.com', email, message)
print("E-mail sent!")
s.quit
