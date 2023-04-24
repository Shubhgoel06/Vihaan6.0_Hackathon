import datetime
import time
from plyer import notification

def get_user_input_time():
    while True:
        user_input = input("Enter the time you regurarly injected insulin in hh:mm format: ")
        try:
            reminder_time = datetime.datetime.strptime(user_input, "%H:%M")
            return reminder_time
        except ValueError:
            print("Invalid time format. Please enter the time in hh:mm format.")

def insulin(reminder_time):
    injection_notification_title = "⚠️ INJECT INSULIN ⚠"
    injection_notification_message = "Inject your Inslin Injection now!!"
    #injection_notification_icon = r"C:\Users\HP\OneDrive\Desktop\injection.png"  # replace with the path to your notification icon
    injection_notification_timeout = 10  # timeout in seconds

    while True:
        current_time = datetime.datetime.now().time()
        if current_time >= reminder_time.time():
            notification.notify(title=injection_notification_title,
                                message=injection_notification_message,
                                #app_icon=injection_notification_icon,
                                timeout=injection_notification_timeout)
            response = input("Have you Injected Insulin? (y/n) ")
            if response.lower() == "y":
                break
        time.sleep(15)  # wait for 20 minutes

    food_notification_title = "⚠ FOOD REMINDER ⚠"
    food_notification_message = "Please eat a healthy meal now!!"
    #food_notification_icon = "path/to/icon.png"  # replace with the path to your notification icon
    food_notification_timeout = 10  # timeout in seconds

    while True:
        notification.notify(title=food_notification_title,
                            message=food_notification_message,
                            #app_icon=food_notification_icon,
                            timeout=food_notification_timeout)
        time.sleep(20)  # wait for 20 minutes
        response = input("Have you eaten properly? (y/n) ")
        if response.lower() == "y":
            break
        

def main():
    reminder_time = get_user_input_time()
    insulin(reminder_time)

if __name__ == '__main__':
    main()
