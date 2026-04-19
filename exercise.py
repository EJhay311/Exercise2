# Exercise 2: File Handling

# Write to file
try:
    note = input("Enter a short note/message: ")
    with open("notes.txt", "w") as file:
        file.write(note + "\n")
    print("Saved successfully!")

except Exception as e:
    print("Error:", e)

# Read file
try:
    with open("notes.txt", "r") as file:
        print("\nFile content:")
        print(file.read())

except FileNotFoundError:
    print("File not found!")

# Append data
try:
    new_note = input("\nEnter another note: ")
    with open("notes.txt", "a") as file:
        file.write(new_note + "\n")

    with open("notes.txt", "r") as file:
        print("\nUpdated content:")
        print(file.read())

except Exception as e:
    print("Error:", e)

