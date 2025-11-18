# --------------------------------------------------------
# Name: Aman Rawat
# Roll No: 2501060006
# Course: BCA
# Semester: 1st
# Subject: Problem Solving with Python
# Assignment: Unit-1 Mini Project
# Title: Student Profile Console App
# Date: 17-11-2025
# --------------------------------------------------------


# Task 1: Welcome Section


print("\n" + "="*60)
print("🎓 Welcome to Student Profile System")
print("="*60)
print("This program collects your details and shows your profile card.")
print("It also demonstrates Python basics like:")
print("- Variables")
print("- Operators")
print("- String functions")
print("- Formatting\n")


# Task 2: Input & Variables


full_name = input("Enter your full name: ")
roll_no = input("Enter your roll number: ")
program = input("Enter your program (e.g., BCA): ")
university = input("Enter your university name: ")
city = input("Enter your city: ")
age = int(input("Enter your age: "))
hobby = input("Enter your hobby: ")

print("\n✔ Student data recorded successfully!\n")


# Task 3: Operators Demonstration


print("="*60)
print("🔢 Python Operators Demonstration")
print("="*60)

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# --- Arithmetic Operators ---
print("\n--- Arithmetic Operators ---")
print(f"{num1} +  {num2} = {num1 + num2}")
print(f"{num1} -  {num2} = {num1 - num2}")
print(f"{num1} *  {num2} = {num1 * num2}")
print(f"{num1} /  {num2} = {num1 / num2}")
print(f"{num1} %  {num2} = {num1 % num2}")
print(f"{num1} ** {num2} = {num1 ** num2}")
print(f"{num1} // {num2} = {num1 // num2}")

# --- Assignment Operator Example ---
a = num1
print("\n--- Assignment Operators Example ---")
a += 5
print(f"num1 += 5 → {a}")

# --- Comparison Operators ---
print("\n--- Comparison Operators ---")
print(f"{num1} > {num2} : {num1 > num2}")
print(f"{num1} == {num2} : {num1 == num2}")
print(f"{num1} != {num2} : {num1 != num2}")

# --- Logical Operators ---
print("\n--- Logical Operators ---")
print(f"({num1} > {num2}) and ({num1} != {num2}) → {(num1 > num2) and (num1 != num2)}")
print(f"({num1} > {num2}) or  ({num1} == {num2}) → {(num1 > num2) or (num1 == num2)}")
print(f"not({num1} == {num2}) → {not(num1 == num2)}")

# --- Identity Operators ---
print("\n--- Identity Operators ---")
print(f"num1 is num2 → {num1 is num2}")
print(f"num1 is not num2 → {num1 is not num2}")

# --- Membership Operators ---
print("\n--- Membership Operators ---")
sample = full_name.lower()
print(f"'a' in your name → {'a' in sample}")
print(f"'z' not in your name → {'z' not in sample}")


# Task 4: Strings & Formatting


print("\n" + "="*60)
print("🔤 String Operations & Formatting")
print("="*60)

print("Uppercase:", full_name.upper())
print("Lowercase:", full_name.lower())
print("Title Case:", full_name.title())
print("Trimmed Name:", full_name.strip())
print("Replace 'a' with '@':", full_name.replace("a", "@"))
print("Count of 'a' in name:", full_name.count("a"))

# Escape characters
print("\nEscape Characters Demo:")
print("Hello\nWorld")
print("Hello\tWorld")
print("Python says \"Welcome!\"")


# Task 5: Final Profile Output


print("\n" + "-"*60)
print("          STUDENT PROFILE SYSTEM")
print("-"*60)

print(f"Name:            {full_name}")
print(f"Roll No:         {roll_no}")
print(f"Course:          {program}")
print(f"University:      {university}")
print(f"City:            {city}")
print(f"Age:             {age}")
print(f"Hobby:           {hobby}")

print("-"*60)
print("Welcome to Python Programming! ✔")
print("-"*60)

# Task 6 (Bonus): Save Profile
save = input("\nDo you want to save your profile? (yes/no): ").lower()

if save == "yes":
    with open("student_profile.txt", "w") as f:
        f.write("STUDENT PROFILE\n")
        f.write("-"*50 + "\n")
        f.write(f"Name: {full_name}\n")
        f.write(f"Roll No: {roll_no}\n")
        f.write(f"Course: {program}\n")
        f.write(f"University: {university}\n")
        f.write(f"City: {city}\n")
        f.write(f"Age: {age}\n")
        f.write(f"Hobby: {hobby}\n")
        f.write("-"*50)

    print("\n✔ Profile saved to student_profile.txt")
else:
    print("\nProfile not saved.")


















