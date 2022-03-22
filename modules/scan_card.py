import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
reader = SimpleMFRC522()


def scan_card():
    print("Card scanner initiated")
    
    try:
        card_id = reader.read()[0]
    except:
        print("Failed to scan")
    finally:
        print("Card scanned with ID: ", card_id)
        return card_id
    
    