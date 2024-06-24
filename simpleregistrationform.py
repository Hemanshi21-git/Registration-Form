from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()
root.title("Registration form")
root.iconbitmap("C:/internship task/registration task/forms.ico")
root.configure(bg="#0B3954")

# Load the background image
background_image = Image.open("C:/internship task/registration task/background.jpg")
background_photo = ImageTk.PhotoImage(background_image)

# Create a canvas and place the background image
canvas = Canvas(root)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=background_photo, anchor="nw")

# Header frame for the title
header_frame = Frame(root, bg="#183652", bd=5)
header_frame.place(relx=0.5, rely=0.06, relwidth=0.3, relheight=0.1, anchor="n")
header_label = Label(header_frame, text="Registration", font=("Arial", 24), bg="#183652", fg="white")
header_label.place(relwidth=1, relheight=1)

def validate_phone_number(P):
    """Validate that the input is a digit and the length is not more than 10."""
    return P == "" or (P.isdigit() and len(P) <= 10)

def validate_age(P):
    """Validate that the input is a digit and between 1 and 150."""
    return P == "" or (P.isdigit() and 1 <= int(P) <= 150)

def login():
    """Function to handle the login button click."""
    # Retrieve all the entered details
    first_name = fname_entry.get().strip()
    last_name = lname_entry.get().strip()
    age = age_entry.get().strip()
    email = emailid_entry.get().strip()
    phone = phone_entry.get().strip()
    gender = gender_var.get().strip()
    State = State_entry.get().strip()
    district = district_entry.get().strip()
    pincode = pincode_entry.get().strip()
    username = username_entry.get().strip()
    address = address_entry.get("1.0", END).strip()

    # Check if any required field is empty
    if (not first_name or not last_name or not age or not email or not phone or
        not gender or not State or not district or not pincode or not username or not address):
        messagebox.showerror("Error", "Please fill all fields.")
        return
    
    # Display a message box with all the registration details
    messagebox.showinfo("Registration Details",
        f"Name: {first_name} {last_name}\n"
        f"Age: {age}\n"
        f"Email: {email}\n"
        f"Phone: {phone}\n"
        f"Gender: {gender}\n"
        f"Address:\n{address}, {State}, {district}, Pincode: {pincode}\n"
        f"Username: {username}")


def reset_fields():
    """Function to reset all entry fields."""
    fname_entry.delete(0, END)
    lname_entry.delete(0, END)
    age_entry.delete(0, END)
    age_entry.config(validate="key", validatecommand=vcmd_age)  # Reconfigure validation command
    emailid_entry.delete(0, END)
    phone_entry.delete(0, END)
    phone_entry.config(validate="key", validatecommand=vcmd_phone)  # Reconfigure validation command
    gender_var.set("Male")  # Reset gender to default
    address_entry.delete("1.0", END)
    State_entry.delete(0, END)
    district_entry.delete(0, END)
    pincode_entry.delete(0, END)
    pincode_entry.config(validate="key", validatecommand=vcmd_phone)  # Reconfigure validation command
    username_entry.delete(0, END)


frame = Frame(canvas, width=1800, height=1000, bg="#6BA5D9",bd=1,relief="solid",highlightthickness=2, highlightbackground="black")
frame.place(relx=0.5, rely=0.58, anchor=CENTER)

# Register validation functions
vcmd_phone = (root.register(validate_phone_number), '%P')
vcmd_age = (root.register(validate_age), '%P')

# Labels and Entries for additional fields
fname_label = Label(frame, text="First Name",bg="#6BA5D9",fg="#183652", font="helvetica")
fname_entry = Entry(frame, font="helvetica")
fname_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)
fname_entry.grid(row=0, column=1, padx=10, pady=10)

lname_label = Label(frame, text="Last Name",bg="#6BA5D9",fg="#183652", font="helvetica")
lname_entry = Entry(frame, font="helvetica")
lname_label.grid(row=1, column=0, padx=10, pady=10, sticky=W)
lname_entry.grid(row=1, column=1, padx=10, pady=10)

age_label = Label(frame, text="Age",bg="#6BA5D9",fg="#183652", font="helvetica")
age_entry = Entry(frame, font="helvetica", validate="key", validatecommand=vcmd_age)
age_label.grid(row=2, column=0, padx=10, pady=10, sticky=W)
age_entry.grid(row=2, column=1, padx=10, pady=10)

emailid_label = Label(frame, text="Email id" ,bg="#6BA5D9",fg="#183652", font="helvetica")
emailid_entry = Entry(frame, font="helvetica")
emailid_label.grid(row=3, column=0, padx=10, pady=10, sticky=W)
emailid_entry.grid(row=3, column=1, padx=10, pady=10)

phone_label = Label(frame, text="Phone Number",bg="#6BA5D9",fg="#183652", font="helvetica")
phone_entry = Entry(frame, font="helvetica", validate="key", validatecommand=vcmd_phone)
phone_label.grid(row=4, column=0, padx=10, pady=10, sticky=W)
phone_entry.grid(row=4, column=1, padx=10, pady=10)

gender_label = Label(frame, text="Gender",bg="#6BA5D9",fg="#183652", font="helvetica")
gender_label.grid(row=5, column=0, padx=10, pady=10, sticky=W)

# Dropdown menu for gender selection
gender_var = StringVar(value="Male")  # Default value set to "Male"
gender_options = ["Male", "Female", "Other"]
gender_dropdown = OptionMenu(frame, gender_var, *gender_options)
gender_dropdown.config(font=("helvetica", 12),bg="#183652",fg="#ffffff")
gender_dropdown.grid(row=5, column=1, padx=10, pady=10, sticky=W)

username_label = Label(frame, text="Username",bg="#6BA5D9",fg="#183652", font="helvetica")
username_entry = Entry(frame, font="helvetica")
username_label.grid(row=6, column=0, padx=10, pady=10, sticky=W)
username_entry.grid(row=6, column=1, padx=10, pady=10)

address_label = Label(frame, text="Address",bg="#6BA5D9",fg="#183652", font="helvetica")
address_label.grid(row=7, column=0, padx=10, pady=10, sticky=W)

# Multiline text entry for address
address_entry = Text(frame, width=25, height=2, font="helvetica")
address_entry.grid(row=7, column=1, columnspan=3, padx=10, pady=10, sticky=W)

State_label = Label(frame, text="State",bg="#6BA5D9",fg="#183652", font="helvetica")
State_entry = Entry(frame, font="helvetica")
State_label.grid(row=8, column=0, padx=10, pady=10, sticky=W)
State_entry.grid(row=8, column=1, padx=10, pady=10)

district_label = Label(frame, text="District",bg="#6BA5D9",fg="#183652", font="helvetica")
district_label.grid(row=9, column=0, padx=10, pady=10, sticky=W)
district_entry = Entry(frame, font="helvetica")
district_entry.grid(row=9, column=1, padx=10, pady=10)

pincode_label = Label(frame, text="Pincode",bg="#6BA5D9",fg="#183652", font="helvetica")
pincode_label.grid(row=10, column=0, padx=10, pady=10, sticky=W)
pincode_entry = Entry(frame, font="helvetica", validate="key", validatecommand=vcmd_phone)
pincode_entry.grid(row=10, column=1, padx=10, pady=10)  # Corrected placement of pincode_entry

# Login button
login_button = Button(frame, text="Login",bg="#183652",fg="#ffffff", font="helvetica", command=login)
login_button.grid(row=11, column=1, padx=10, pady=10)

# Reset button
reset_button = Button(frame, text="Reset",bg="#183652",fg="#ffffff", font="helvetica", command=reset_fields)
reset_button.grid(row=11, column=0, padx=10, pady=10)

root.mainloop()
          