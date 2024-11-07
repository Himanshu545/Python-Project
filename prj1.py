from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

class CRM:
    def __init__(self, root):
        self.root = root
        self.root.title("Customer Relationship Management System")
        self.root.geometry("1080x600")

        # Load and set background image for main window
        self.bg_image = Image.open("D:/PYTHONN/im1.jpg")
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)
        self.bg_label = Label(self.root, image=self.bg_photo)
        self.bg_label.place(relwidth=1, relheight=1)

        # Title Labels
        lbltitle = Label(
            self.root, bd=20, relief=RIDGE,
            text="CUSTOMER RELATIONSHIP MANAGEMENT SYSTEM",
            fg="blue", bg="white", font=("Times New Roman", 30, "bold")
        )
        lbltitle.pack(side=TOP)

        lbltitle2 = Label(
            self.root, bd=20, relief=RIDGE,
            text="-------BY HT OFFICIALS", fg="blue", bg="white",
            font=("Times New Roman", 22, "bold")
        )
        lbltitle2.pack(side=TOP, fill=X)

        # Welcome Message
        welcome_label = Label(
            self.root, text="Welcome! Please click below to proceed.",
            font=("Times New Roman", 14, "bold"), bg="white"
        )
        welcome_label.pack(pady=20)

        # Main frame
        self.main_frame = Frame(self.root, bg="white")
        self.main_frame.pack(fill=BOTH, expand=True)

        # Button to open the dashboard
        self.open_dashboard_button = Button(
            self.main_frame, text="Proceed to CRM System",
            font=("Times New Roman", 15, "bold"), fg="#2d3e50", bg="white", bd=5,
            command=self.open_dashboard
        )
        self.open_dashboard_button.pack(pady=20)

        # Storage for customer details (This is just for demonstration; you might want to use a database in a real application)
        self.customers = {}

    def open_dashboard(self):
        # Create a new window for the dashboard
        dashboard_window = Toplevel(self.root)
        dashboard_window.title("CRM Dashboard")
        dashboard_window.geometry("800x600")

        # Load and set background image for the dashboard window
        dashboard_bg_image = Image.open("D:/PYTHONN/im3.jpg")
        dashboard_bg_image.putalpha(110)
        dashboard_bg_photo = ImageTk.PhotoImage(dashboard_bg_image)
        dashboard_bg_label = Label(dashboard_window, image=dashboard_bg_photo)
        dashboard_bg_label.image = dashboard_bg_photo
        dashboard_bg_label.place(relwidth=1, relheight=1)

        # Dashboard Label
        dashboard_label = Label(
            dashboard_window, text="Welcome to the CRM Dashboard!",
            font=("Times New Roman", 25, "bold"), fg="green", bg="white"
        )
        dashboard_label.pack(pady=40)

        # Button to open the Insert Customer form
        insert_button = Button(
            dashboard_window, text="Insert Customer", font=("Times New Roman", 15, "bold"),
            command=self.open_insert_form
        )
        insert_button.pack(pady=20)

        # Button to open Update Customer form
        update_button = Button(
            dashboard_window, text="Update Customer", font=("Times New Roman", 15, "bold"),
            command=self.open_update_form
        )
        update_button.pack(pady=20)

        # Button to open Delete Customer form
        delete_button = Button(
            dashboard_window, text="Delete Customer", font=("Times New Roman", 15, "bold"),
            command=self.open_delete_form
        )
        delete_button.pack(pady=20)

        # Button to open View Customer Details form
        view_button = Button(
            dashboard_window, text="View Customer Details", font=("Times New Roman", 15, "bold"),
            command=self.open_view_form
        )
        view_button.pack(pady=20)

        # Close Button
        close_button = Button(
            dashboard_window, text="Close Dashboard",
            command=dashboard_window.destroy, font=("Times New Roman", 15, "bold")
        )
        close_button.pack(pady=20)

    def open_insert_form(self):
        # Create a new window for the Insert Customer form
        insert_window = Toplevel(self.root)
        insert_window.title("Insert Customer")
        insert_window.geometry("600x800")

        # Form title
        form_title = Label(
            insert_window, text="Insert Customer Details", font=("Times New Roman", 18, "bold"), fg="blue"
        )
        form_title.pack(pady=20)

        # Enrolment ID entry
        enrolment_id_label = Label(insert_window, text="Enrolment ID", font=("Times New Roman", 14))
        enrolment_id_label.pack(anchor=W, padx=20, pady=5)
        self.enrolment_id_entry = Entry(insert_window, font=("Times New Roman", 14))
        self.enrolment_id_entry.pack(fill=X, padx=20, pady=5)

        # Name entry
        name_label = Label(insert_window, text="Name", font=("Times New Roman", 14))
        name_label.pack(anchor=W, padx=20, pady=5)
        self.name_entry = Entry(insert_window, font=("Times New Roman", 14))
        self.name_entry.pack(fill=X, padx=20, pady=5)

        # Contact entry
        contact_label = Label(insert_window, text="Contact", font=("Times New Roman", 14))
        contact_label.pack(anchor=W, padx=20, pady=5)
        self.contact_entry = Entry(insert_window, font=("Times New Roman", 14))
        self.contact_entry.pack(fill=X, padx=20, pady=5)

        # Age entry
        age_label = Label(insert_window, text="Age", font=("Times New Roman", 14))
        age_label.pack(anchor=W, padx=20, pady=5)
        self.age_entry = Entry(insert_window, font=("Times New Roman", 14))
        self.age_entry.pack(fill=X, padx=20, pady=5)

        # Gender dropdown
        gender_label = Label(insert_window, text="Gender", font=("Times New Roman", 14))
        gender_label.pack(anchor=W, padx=20, pady=5)
        self.gender_combobox = ttk.Combobox(insert_window, font=("Times New Roman", 14), state="readonly")
        self.gender_combobox['values'] = ("Male", "Female", "Other")
        self.gender_combobox.pack(fill=X, padx=20, pady=5)

        # Address entry
        address_label = Label(insert_window, text="Address", font=("Times New Roman", 14))
        address_label.pack(anchor=W, padx=20, pady=5)
        self.address_entry = Entry(insert_window, font=("Times New Roman", 14))
        self.address_entry.pack(fill=X, padx=20, pady=5)

        # Visa Type radio buttons
        visa_type_label = Label(insert_window, text="Visa Type", font=("Times New Roman", 14))
        visa_type_label.pack(anchor=W, padx=20, pady=5)
        self.visa_type = StringVar(value="Tourist")
        tourist_radio = Radiobutton(insert_window, text="Tourist", variable=self.visa_type, value="Tourist", font=("Times New Roman", 12))
        study_radio = Radiobutton(insert_window, text="Study", variable=self.visa_type, value="Study", font=("Times New Roman", 12))
        tourist_radio.pack(anchor=W, padx=20)
        study_radio.pack(anchor=W, padx=20)

        # Visa Country dropdown
        visa_country_label = Label(insert_window, text="Visa Country", font=("Times New Roman", 14))
        visa_country_label.pack(anchor=W, padx=20, pady=5)
        self.visa_country_combobox = ttk.Combobox(insert_window, font=("Times New Roman", 14), state="readonly")
        self.visa_country_combobox['values'] = ("Canada", "USA", "Australia", "South Korea", "UK", "Dubai", "Singapore")
        self.visa_country_combobox.pack(fill=X, padx=20, pady=5)

        # Submit button
        submit_button = Button(
            insert_window, text="Submit", font=("Times New Roman", 14, "bold"),
            command=self.submit_customer_details
        )
        submit_button.pack(pady=20)

    def submit_customer_details(self):
        # Get data from the form
        enrolment_id = self.enrolment_id_entry.get()
        name = self.name_entry.get()
        contact = self.contact_entry.get()
        age = self.age_entry.get()
        gender = self.gender_combobox.get()
        address = self.address_entry.get()
        visa_type = self.visa_type.get()
        visa_country = self.visa_country_combobox.get()

        # Store customer details
        if enrolment_id not in self.customers:
            self.customers[enrolment_id] = {
                'name': name,
                'contact': contact,
                'age': age,
                'gender': gender,
                'address': address,
                'visa_type': visa_type,
                'visa_country': visa_country
            }

            details = (
                f"Enrolment ID: {enrolment_id}\n"
                f"Name: {name}\n"
                f"Contact: {contact}\n"
                f"Age: {age}\n"
                f"Gender: {gender}\n"
                f"Address: {address}\n"
                f"Visa Type: {visa_type}\n"
                f"Visa Country: {visa_country}"
            )

            messagebox.showinfo("Customer Details Submitted", details)
            self.clear_insert_form()
        else:
            messagebox.showwarning("Customer Exists", "Customer with this Enrolment ID already exists.")

    def clear_insert_form(self):
        self.enrolment_id_entry.delete(0, END)
        self.name_entry.delete(0, END)
        self.contact_entry.delete(0, END)
        self.age_entry.delete(0, END)
        self.gender_combobox.set('')
        self.address_entry.delete(0, END)
        self.visa_type.set("Tourist")
        self.visa_country_combobox.set('')

    def open_update_form(self):
        update_window = Toplevel(self.root)
        update_window.title("Update Customer")
        update_window.geometry("650x1000")

        # Form title
        form_title = Label(
            update_window, text="Update Customer Details", font=("Times New Roman", 18, "bold"), fg="blue"
        )
        form_title.pack(pady=15)

        # Enrolment ID entry
        enrolment_id_label = Label(update_window, text="Enrolment ID", font=("Times New Roman", 14))
        enrolment_id_label.pack(anchor=W, padx=20, pady=5)
        self.update_enrolment_id_entry = Entry(update_window, font=("Times New Roman", 14))
        self.update_enrolment_id_entry.pack(fill=X, padx=15, pady=5)

        # Button to Load Customer Details
        load_button = Button(
            update_window, text="Load Customer Details", font=("Times New Roman", 14, "bold"),
            command=self.load_customer_details
        )
        load_button.pack(pady=15)

        # Customer details entries
        self.update_name_entry = self.create_entry(update_window, "Name")
        self.update_contact_entry = self.create_entry(update_window, "Contact")
        self.update_age_entry = self.create_entry(update_window, "Age")
        self.update_gender_combobox = self.create_combobox(update_window, "Gender", ["Male", "Female", "Other"])
        self.update_address_entry = self.create_entry(update_window, "Address")
        self.update_visa_type = StringVar(value="Tourist")
        self.create_radio_buttons(update_window, "Visa Type", ["Tourist", "Study"], self.update_visa_type)
        self.update_visa_country_combobox = self.create_combobox(update_window, "Visa Country",
                                                                  ["Canada", "USA", "Australia", "South Korea", "UK", "Dubai", "Singapore"])

        # Update button
        update_button = Button(
            update_window, text="Update", font=("Times New Roman", 14, "bold"),
            command=self.update_customer_details
        )
        update_button.pack(pady=15)

    def create_entry(self, parent, label_text):
        label = Label(parent, text=label_text, font=("Times New Roman", 14))
        label.pack(anchor=W, padx=20, pady=5)
        entry = Entry(parent, font=("Times New Roman", 14))
        entry.pack(fill=X, padx=20, pady=5)
        return entry

    def create_combobox(self, parent, label_text, values):
        label = Label(parent, text=label_text, font=("Times New Roman", 14))
        label.pack(anchor=W, padx=20, pady=5)
        combobox = ttk.Combobox(parent, font=("Times New Roman", 14), state="readonly")
        combobox['values'] = values
        combobox.pack(fill=X, padx=20, pady=5)
        return combobox

    def create_radio_buttons(self, parent, label_text, options, variable):
        label = Label(parent, text=label_text, font=("Times New Roman", 14))
        label.pack(anchor=W, padx=20, pady=5)
        for option in options:
            radio = Radiobutton(parent, text=option, variable=variable, value=option, font=("Times New Roman", 12))
            radio.pack(anchor=W, padx=20)

    def load_customer_details(self):
        enrolment_id = self.update_enrolment_id_entry.get()
        if enrolment_id in self.customers:
            customer = self.customers[enrolment_id]
            self.update_name_entry.delete(0, END)
            self.update_name_entry.insert(0, customer['name'])
            self.update_contact_entry.delete(0, END)
            self.update_contact_entry.insert(0, customer['contact'])
            self.update_age_entry.delete(0, END)
            self.update_age_entry.insert(0, customer['age'])
            self.update_gender_combobox.set(customer['gender'])
            self.update_address_entry.delete(0, END)
            self.update_address_entry.insert(0, customer['address'])
            self.update_visa_type.set(customer['visa_type'])
            self.update_visa_country_combobox.set(customer['visa_country'])
        else:
            messagebox.showwarning("Not Found", "Customer not found.")

    def update_customer_details(self):
        enrolment_id = self.update_enrolment_id_entry.get()
        if enrolment_id in self.customers:
            self.customers[enrolment_id]['name'] = self.update_name_entry.get()
            self.customers[enrolment_id]['contact'] = self.update_contact_entry.get()
            self.customers[enrolment_id]['age'] = self.update_age_entry.get()
            self.customers[enrolment_id]['gender'] = self.update_gender_combobox.get()
            self.customers[enrolment_id]['address'] = self.update_address_entry.get()
            self.customers[enrolment_id]['visa_type'] = self.update_visa_type.get()
            self.customers[enrolment_id]['visa_country'] = self.update_visa_country_combobox.get()

            messagebox.showinfo("Success", "Customer details updated successfully.")
            self.clear_update_form()
        else:
            messagebox.showwarning("Not Found", "Customer not found.")

    def clear_update_form(self):
        self.update_enrolment_id_entry.delete(0, END)
        self.update_name_entry.delete(0, END)
        self.update_contact_entry.delete(0, END)
        self.update_age_entry.delete(0, END)
        self.update_gender_combobox.set('')
        self.update_address_entry.delete(0, END)
        self.update_visa_type.set("Tourist")
        self.update_visa_country_combobox.set('')

    def open_delete_form(self):
        delete_window = Toplevel(self.root)
        delete_window.title("Delete Customer")
        delete_window.geometry("400x300")

        # Form title
        form_title = Label(
            delete_window, text="Delete Customer", font=("Times New Roman", 18, "bold"), fg="blue"
        )
        form_title.pack(pady=20)

        # Enrolment ID entry
        enrolment_id_label = Label(delete_window, text="Enrolment ID", font=("Times New Roman", 14))
        enrolment_id_label.pack(anchor=W, padx=20, pady=5)
        self.delete_enrolment_id_entry = Entry(delete_window, font=("Times New Roman", 14))
        self.delete_enrolment_id_entry.pack(fill=X, padx=20, pady=5)

        # Delete button
        delete_button = Button(
            delete_window, text="Delete", font=("Times New Roman", 14, "bold"),
            command=self.delete_customer
        )
        delete_button.pack(pady=20)

    def delete_customer(self):
        enrolment_id = self.delete_enrolment_id_entry.get()
        if enrolment_id in self.customers:
            del self.customers[enrolment_id]
            messagebox.showinfo("Success", "Customer deleted successfully.")
            self.delete_enrolment_id_entry.delete(0, END)
        else:
            messagebox.showwarning("Not Found", "Customer not found.")

    def open_view_form(self):
        view_window = Toplevel(self.root)
        view_window.title("View Customer Details")
        view_window.geometry("600x400")

        # Form title
        form_title = Label(
            view_window, text="View Customer Details", font=("Times New Roman", 18, "bold"), fg="blue"
        )
        form_title.pack(pady=20)

        # Enrolment ID entry
        enrolment_id_label = Label(view_window, text="Enrolment ID", font=("Times New Roman", 14))
        enrolment_id_label.pack(anchor=W, padx=20, pady=5)
        self.view_enrolment_id_entry = Entry(view_window, font=("Times New Roman", 14))
        self.view_enrolment_id_entry.pack(fill=X, padx=20, pady=5)

        # Button to View Customer Details
        view_button = Button(
            view_window, text="View Details", font=("Times New Roman", 14, "bold"),
            command=self.view_customer_details
        )
        view_button.pack(pady=20)

    def view_customer_details(self):
        enrolment_id = self.view_enrolment_id_entry.get()
        if enrolment_id in self.customers:
            customer = self.customers[enrolment_id]
            details = (
                f"Enrolment ID: {enrolment_id}\n"
                f"Name: {customer['name']}\n"
                f"Contact: {customer['contact']}\n"
                f"Age: {customer['age']}\n"
                f"Gender: {customer['gender']}\n"
                f"Address: {customer['address']}\n"
                f"Visa Type: {customer['visa_type']}\n"
                f"Visa Country: {customer['visa_country']}"
            )
            messagebox.showinfo("Customer Details", details)
        else:
            messagebox.showwarning("Not Found", "Customer not found.")

# Create the main window and start the CRM application
root = Tk()
ob = CRM(root)
root.mainloop() 
