import datetime

def take_attendance(roll_range):
    attendance = {}
  
    for roll_number in range(roll_range[0], roll_range[1] + 1):
        status = input(f"{roll_number} present? (1 for present, 0 for absent): ")
        attendance[roll_number] = "Present" if status == "1" else "Absent"

    return attendance

def view_absent_attendance(attendance_dict, batch, slot):
    absent_rolls = [roll for roll, status in attendance_dict.items() if status == "Absent"]
    current_date = datetime.date.today().strftime("%d/%m")
    if absent_rolls:
        message = f"BCA - {batch}\nDate - {current_date}\nSlot - {slot}\nAbsent:\n"
        for roll in absent_rolls:
            message += f"{roll}\n"
        return message
    else:
        return "No absent students."

def update_attendance(attendance_dict, roll_number, status):
    if roll_number in attendance_dict:
        attendance_dict[roll_number] = status
        print(f"Attendance updated for roll number {roll_number}")
    else:
        print(f"Roll number {roll_number} not found")

def delete_attendance(attendance_dict, roll_number):
    if roll_number in attendance_dict:
        del attendance_dict[roll_number]
        print(f"Attendance record for roll number {roll_number} deleted")
    else:
        print(f"Roll number {roll_number} not found")

attendance_list = {}
current_date = datetime.date.today().strftime("%d-%m")
slot = input("Enter the slot number: ")
batch = input("Enter the batch number: ")

while True:
    print("\nOptions:")
    print("1. Take Attendance")
    print("2. View Absent Attendance")
    print("3. Update Attendance")
    print("4. Delete Attendance")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        start_roll = int(input("Enter the starting roll number: "))
        end_roll = int(input("Enter the ending roll number: "))
        attendance_list = take_attendance((start_roll, end_roll))
    elif choice == "2":
        absent_message = view_absent_attendance(attendance_list, batch, slot)
        print(absent_message)
    elif choice == "3":
        roll_number = int(input("Enter the roll number to update: "))
        status = input("Is roll number present? (Enter '1' for present, else absent): ")
        update_attendance(attendance_list, roll_number, "Present" if status == "1" else "Absent")
    elif choice == "4":
        roll_number = int(input("Enter the roll number to delete: "))
        delete_attendance(attendance_list, roll_number)
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please enter a valid option.")
