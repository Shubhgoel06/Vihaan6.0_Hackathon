import csv

n = int(input("Enter number of patients: "))
# Prompt the user for input and store the values in variables
for i in range(n):
    patient_name = input("Enter your name: ")
    phone_number = int(input("Enter your phone number: "))
    delivery_address = input("Enter your address at which you want medicine is delivered: ")
    doctors_visit = input("Enter the date of your doctor's visit (YYYY-MM-DD): ")
    medicines_name = input("Enter name of medicines: ")
    prescribed_duration = int(input("For how many days is the medicine prescribed? "))
    time_taken = input("What time do you take this medicine?: ")
    last_purchase_date = input("Enter last date on which you purchased the medicine (YYYY-MM-DD): ")

# Open the CSV file in append mode and write the user's input to the file
with open('patient_info.csv', mode='a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([patient_name, phone_number, delivery_address, doctors_visit, medicines_name, prescribed_duration, time_taken, last_purchase_date])

# Print a message to confirm that the data has been saved
print("Patient information has been saved to patient_info.csv.")
