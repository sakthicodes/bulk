# bulk_messaging.py
import pywhatkit  # Importing pywhatkit for sending WhatsApp messages  # Importing Selenium for sending SMS
import time
import smtplib
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd



def send_whatsapp_message(phone_numbers, message):
    for phone_number in phone_numbers:
          pywhatkit.sendwhatmsg_instantly(phone_number, message)
          time.sleep(25)
def send_email(receiver_emails, message):
    # Set up Gmail SMTP connection
    sender_email = "jeyadharsan7@gmail.com"
    password = "rqapkzvbfelpodui"  # Replace with your Gmail password
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)
                    
    for receiver_email in receiver_emails:
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender_email, password)
            # Send email
            server.sendmail(sender_email, receiver_email, message)
            print(f"Email sent successfully to {receiver_email}")
            
            # Close connection
            server.quit()
        except Exception as e:
            print(f"Failed to send email to {receiver_email}: {e}")

def send_sms1(phone_number, message):
    # Configure WebDriver for Firefox
    driver = webdriver.Firefox()

    try:
        # Open Google Messages
        driver.get("https://messages.google.com/web")
        
        # Wait for user to log in manually
        
        # Wait for page to load
        time.sleep(25)
        
        # Find search input field
        driver.find_element(By.XPATH,"/html/body/mw-app/mw-bootstrap/div/main/mw-main-container/div/mw-main-nav/div/mw-fab-link/a").click()
        time.sleep(25)

        if len(phone_number)<=1:
            driver.find_element(By.XPATH,'/html/body/mw-app/mw-bootstrap/div/main/mw-main-container/div/mw-new-conversation-container/mw-new-conversation-sub-header/div/div[2]/mw-contact-chips-input/div/div/input').send_keys(phone_number)
        # Type phone number
            time.sleep(5)
            driver.find_element(By.XPATH,"/html/body/mw-app/mw-bootstrap/div/main/mw-main-container/div/mw-new-conversation-container/div/mw-contact-selector-button/button").click()
            time.sleep(10)
        else:
            driver.find_element(By.XPATH,"/html/body/mw-app/mw-bootstrap/div/main/mw-main-container/div/mw-new-conversation-container/div/mw-new-conversation-start-group-button/button").click()
            time.sleep(5)
            for number in phone_number:
                driver.find_element(By.XPATH,'/html/body/mw-app/mw-bootstrap/div/main/mw-main-container/div/mw-new-conversation-container/mw-new-conversation-sub-header/div/div[2]/mw-contact-chips-input/div/div/input').send_keys(number)
        # Type phone number
                time.sleep(5)
                driver.find_element(By.XPATH,"/html/body/mw-app/mw-bootstrap/div/main/mw-main-container/div/mw-new-conversation-container/div/mw-contact-selector-button/button").click()
                time.sleep(5)
            driver.find_element(By.XPATH,"/html/body/mw-app/mw-bootstrap/div/main/mw-main-container/div/mw-new-conversation-container/mw-new-conversation-sub-header/div/div[2]/mw-contact-chips-input/button").click()
            time.sleep(10)

        driver.find_element(By.XPATH,"/html/body/mw-app/mw-bootstrap/div/main/mw-main-container/div/mw-conversation-container/div/div[1]/div/mws-message-compose/div/div[2]/div/div/mws-autosize-textarea/textarea").send_keys(message)
        
        time.sleep(10)
        ActionChains(driver).move_to_element(driver.find_element(By.XPATH,'/html/body/mw-app/mw-bootstrap/div/main/mw-main-container/div/mw-conversation-container/div/div[1]/div/mws-message-compose/div/div[2]/div/div/mws-message-send-button/div/mw-message-send-button/button'))
        driver.find_element(By.XPATH,'/html/body/mw-app/mw-bootstrap/div/main/mw-main-container/div/mw-conversation-container/div/div[1]/div/mws-message-compose/div/mws-message-send-button/div/mw-message-send-button/button').click()
        time.sleep(10)
        print("Message sent successfully!")
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    
    finally:
        # Close the browser
        driver.quit()






