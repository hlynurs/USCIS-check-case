from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys
import smtplib
from email.mime.text import MIMEText
from twilio import TwilioRestException
from twilio.rest import TwilioRestClient

url = sys.argv[1]
receipt = sys.argv[2]
email = sys.argv[3]
userid = sys.argv[4]
userpassword = sys.argv[5]
twilio_account_sid = sys.argv[6]
twilio_auth_token = sys.argv[7]
phone_to = sys.argv[8]
phone_from = sys.argv[9]
search_term = sys.argv[10]
counter = 1

twilio_client = TwilioRestClient(twilio_account_sid, twilio_auth_token)

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
    if (text.find(search_term) == -1):
        break
    print("Check number %d." % counter)
    # Wait 12 hours before checking again
    time.sleep(43200)
    counter = counter + 1

# Out of loop
# Send e-mail to recipient including the results
message = 'Subject: %s\n\n%s' % ("Case Update!", text)
print("Case has been updated, sending e-mail")
s = smtplib.SMTP('smtp.gmail.com:587')
s.starttls()
s.ehlo()
s.login(userid, userpassword)
#s.sendmail('caseCheck@python.com', email, message)
print("E-mail sent!")
s.quit

#Send SMS to phone with updated message
try:
    twilio_message = twilio_client.messages.create(body=text, to=phone_to, from_=phone_from)
    print("SMS sent!")
except TwilioRestException as e:
    print(e)
