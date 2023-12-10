import tkinter as tk
import customtkinter as ctk
from tkinter import ttk, StringVar, messagebox
from datetime import datetime, date
import database


class TenantManagement:
    def __init__(self, master):
        self.master = master
        master.title("Tenant Management System")
        master.geometry("1020x420")
        master.resizable(False, False)

        # Sidebar
        self.sidebar_frame = ctk.CTkFrame(master)
        self.sidebar_frame.pack(side="left")
        self.sidebar_frame.pack_propagate(False)
        self.sidebar_frame.configure(width=100, height=420)

        # Mainframe
        self.main_frame = ctk.CTkFrame(master, border_width=2, border_color="#39A7FF")
        self.main_frame.pack(side="left")
        self.main_frame.pack_propagate(False)
        self.main_frame.configure(width=1020, height=520)

        # Buttons
        self.tenants_button = ctk.CTkButton(self.sidebar_frame, text="Tenants", fg_color="transparent",
                                            font=("Helvetica", 15, "bold"), text_color="#39A7FF",
                                            command=lambda: self.highlight(self.tenants_highlight, self.tenants_page))
        self.tenants_button.pack(side="top", pady=10)
        self.tenants_highlight = ctk.CTkLabel(self.sidebar_frame, text="", bg_color="transparent", width=5, height=40)
        self.tenants_highlight.place(x=5, y=5)

        self.rooms_button = ctk.CTkButton(self.sidebar_frame, text="Rooms", fg_color="transparent",
                                          font=("Helvetica", 15, "bold"), text_color="#39A7FF",
                                          command=lambda: self.highlight(self.rooms_highlight, self.rooms_page))
        self.rooms_button.pack(side="top", pady=10)
        self.rooms_highlight = ctk.CTkLabel(self.sidebar_frame, text="", bg_color="transparent", width=5, height=40)
        self.rooms_highlight.place(x=5, y=52)

        self.payments_button = ctk.CTkButton(self.sidebar_frame, text="Payments", fg_color="transparent",
                                             font=("Helvetica", 15, "bold"), text_color="#39A7FF",
                                             command=lambda: self.highlight(self.payments_highlight, self.payments_page))
        self.payments_button.pack(side="top", pady=10)
        self.payments_highlight = ctk.CTkLabel(self.sidebar_frame, text="", bg_color="transparent", width=5, height=40)
        self.payments_highlight.place(x=5, y=96)

        self.exit_button = ctk.CTkButton(self.sidebar_frame, text="Exit", fg_color="transparent",
                                         font=("Helvetica", 15, "bold"), text_color="#39A7FF", command=lambda: self.exit_ui())
        self.exit_button.pack(side="top", pady=10)

    def tenants_page(self):
        tenants_frame = ctk.CTkFrame(self.main_frame, width=920, height=420)
        tenants_frame.pack(side="left")
        #includes the tenants page
        tenant_page = TenantPage(tenants_frame)

    def rooms_page(self):
        rooms_frame = ctk.CTkFrame(self.main_frame, width=920, height=420)
        rooms_frame.pack(side="left")
        rooms_page = RoomsPage(rooms_frame)
        
    def payments_page(self):
        payments_frame = ctk.CTkFrame(self.main_frame, width=920, height=420)
        payments_frame.pack(side="left")
        payments_page = PaymentPage(payments_frame)
        
    def clear_page(self):
        for frame in self.main_frame.winfo_children():
            frame.destroy()

    def highlight(self, highlight_button, page):
        self.hide_highlight()
        highlight_button.configure(bg_color="#39A7FF")
        self.clear_page()
        page()

    def hide_highlight(self):
        self.tenants_highlight.configure(bg_color="transparent")
        self.rooms_highlight.configure(bg_color="transparent")

        self.payments_highlight.configure(bg_color="transparent")

    def exit_ui(self):
        self.master.destroy()
        
#Tenants page function        
class TenantPage:
    def __init__(self, master):
        self.master = master

        self.font1 = ("Helvetica", 15, "bold")
        self.font2 = ("Helvetica", 13)

        # Information Entry
        self.id_label = ctk.CTkLabel(self.master, font=self.font1, text='Tenant ID')
        self.id_label.place(x=15, y=20)
        self.id_entry = ctk.CTkEntry(self.master, font=self.font2, border_width=2,corner_radius=15)
        self.id_entry.place(x=100, y=20)

        self.name_label = ctk.CTkLabel(self.master, font=self.font1, text='Name')
        self.name_label.place(x=20, y=80)
        self.name_entry = ctk.CTkEntry(self.master, font=self.font2, border_width=2, corner_radius=15)
        self.name_entry.place(x=100, y=80)

        self.contact_label = ctk.CTkLabel(self.master, font=self.font1, text='Contact')
        self.contact_label.place(x=20, y=140)
        self.contact_entry = ctk.CTkEntry(self.master, font=self.font2, border_width=2,
                                          corner_radius=15)
        self.contact_entry.place(x=100, y=140)

        self.gender_label = ctk.CTkLabel(self.master, font=self.font1, text='Gender')
        self.gender_label.place(x=20, y=200)
        options1 = ['Male', 'Female']
        self.variable1 = StringVar()
        self.gender_option = ctk.CTkComboBox(self.master, font=self.font2, variable=self.variable1, values=options1,
                                              state='readonly', corner_radius=15,)
        self.gender_option.place(x=100, y=200)

        self.status_label = ctk.CTkLabel(self.master, font=self.font1, text='Status')
        self.status_label.place(x=20, y=260)
        options2 = ['Logged In', 'Logged Out', 'Away']
        self.variable2 = StringVar()
        self.status_option = ctk.CTkComboBox(self.master, font=self.font2, variable=self.variable2, values=options2,
                                              state='readonly', corner_radius=15)
        self.status_option.place(x=100, y=260)

 # Buttons
        self.clear_button = ctk.CTkButton(self.master, command=lambda: self.clear(True), font=self.font1,
                                          fg_color="#39A7FF", text="Clear", corner_radius=15, cursor="hand2",
                                          width=260)
        self.clear_button.place(x=20, y=320)
        
        self.add_button = ctk.CTkButton(self.master, command=self.add_tenant, font=self.font1, fg_color="#39A7FF",
                                        text="Add Tenant", corner_radius=15, cursor="hand2", width=260)
        self.add_button.place(x=20, y=365)

        self.update_button = ctk.CTkButton(self.master, command=self.update, font=self.font1, fg_color="#39A7FF",
                                           text="Update Tenant", corner_radius=15, cursor="hand2", width=260)
        self.update_button.place(x=305, y=365)

        self.delete_button = ctk.CTkButton(self.master, command=self.remove, font=self.font1, fg_color="#39A7FF",
                                           text="Delete Tenant", corner_radius=15, cursor="hand2", width=260)
        self.delete_button.place(x=590, y=365)


        #Treeview
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('Treeview', font=self.font2, foreground='#fff', background='#000', fieldbackground='#272829')
        style.map('Treeview', background=[('selected', '#1A8F2D')])

        self.tree = ttk.Treeview(self.master, height=15)
        self.tree['columns'] = ('ID', 'Name', 'Contact', 'Gender', 'Status')

        self.tree.column('#0', width=0, stretch=tk.NO)  # used to hide the first column so that there are no excess columns
        self.tree.column('ID', anchor=tk.CENTER, width=120)
        self.tree.column('Name', anchor=tk.CENTER, width=120)
        self.tree.column('Contact', anchor=tk.CENTER, width=120)
        self.tree.column('Gender', anchor=tk.CENTER, width=120)
        self.tree.column('Status', anchor=tk.CENTER, width=120)

        self.tree.heading('ID', text='Tenant ID')
        self.tree.heading('Name', text='Name')
        self.tree.heading('Contact', text='Contact')
        self.tree.heading('Gender', text='Gender')
        self.tree.heading('Status', text='Status')

        self.tree.place(x=300, y=15)

        self.tree.bind('<ButtonRelease>', self.display_data)

        self.add_to_treeview()
        
    # Function to connect to the database and update the Treeview
    def add_to_treeview(self):
        tenants = database.view_tenants()
        self.tree.delete(*self.tree.get_children())  # used to prevent inserting the same row multiple times
        for tenant in tenants:
            self.tree.insert('', tk.END, values=tenant)

    # Function to clear entry fields
    def clear(self, *clicked):
        if clicked:
            self.tree.selection_remove(self.tree.focus())
        self.id_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.contact_entry.delete(0, tk.END)
        self.variable1.set('')
        self.variable2.set('')

    # Function to display data in entry boxes when clicking on Treeview
    def display_data(self, event):
        selected_item = self.tree.focus()
        if selected_item:
            row = self.tree.item(selected_item)['values']
            self.clear()
            self.id_entry.insert(0, row[0])
            self.name_entry.insert(0, row[1])
            self.contact_entry.insert(0, row[2])
            self.variable1.set(row[3])
            self.variable2.set(row[4])

    # Function to remove a tenant
    def remove(self):
        selected_item = self.tree.focus()
        if not selected_item:
            messagebox.showerror("Error", "Please select a tenant to delete")
        else:
            id = self.tree.item(selected_item, 'values')[0]
            database.remove_tenant(id)
            self.add_to_treeview()
            self.clear()
            messagebox.showinfo("Success", "Data deleted successfully")

    # Function to update a tenant
    def update(self):
        selected_item = self.tree.focus()
        if not selected_item:
            messagebox.showerror("Error", "Please select a tenant to update")
        
        else:
            # Get the id from the selected item in the Treeview
            id = self.tree.item(selected_item, 'values')[0]
            name = self.name_entry.get()
            contact = self.contact_entry.get()
            gender = self.variable1.get()
            status = self.variable2.get()

            # Update the tenant using the retrieved id
        if not contact.isdigit():
            messagebox.showerror("Error", "Contact must be a valid integer")
        else:
            database.update_tenant(name, contact, gender, status, id)
            self.add_to_treeview()
            messagebox.showinfo("Success", "Data changed successfully")

    # Function to add a tenant
    def add_tenant(self):
        id = self.id_entry.get()
        name = self.name_entry.get()
        contact = self.contact_entry.get()
        gender = self.variable1.get()
        status = self.variable2.get()
        if not (id and name and contact and gender and status):
            messagebox.showerror("Error", "Please fill all the fields")
        elif not contact.isdigit():
            messagebox.showerror("Error", "Contact must be a valid integer")
        elif database.tenant_exists(id):
            messagebox.showerror("Error", "ID already exists")
        else:
            database.add_tenant(id, name, contact, gender, status)
            self.add_to_treeview()
            messagebox.showinfo("Success", "Data added successfully")
            

#CREATES ROOMS PAGE
class RoomsPage:
    def __init__(self, master):
        self.master = master

        self.font1 = ("Helvetica", 15, "bold")
        self.font2 = ("Helvetica", 13)
        
    # Information Entry
        self.room_id_label = ctk.CTkLabel(self.master, font=self.font1, text='Room ID')
        self.room_id_label.place(x=12, y=20)
        self.room_id_entry = ctk.CTkEntry(self.master, font=self.font2, border_width=2, corner_radius=15)
        self.room_id_entry.place(x=100, y=20)

        self.fees_label = ctk.CTkLabel(self.master, font=self.font1, text='Additional \nFees')
        self.fees_label.place(x=12, y=72)
        options1 = ['None', 'Electricity', 'Water', 'Electricity and Water']
        self.variable1 = StringVar()
        self.additional_fees_entry = ctk.CTkComboBox(self.master, font=self.font2, variable=self.variable1, values=options1, corner_radius=15, state='readonly')
        self.additional_fees_entry.place(x=100, y=80)

        self.rent_label = ctk.CTkLabel(self.master, font=self.font1, text='Monthly \nRent')
        self.rent_label.place(x=12, y=135)
        self.rent_entry = ctk.CTkEntry(self.master, font=self.font2, border_width=2,corner_radius=15)
        self.rent_entry.place(x=100, y=140)

        self.taken_slots_label = ctk.CTkLabel(self.master, font=self.font1, text='Taken Slots')
        self.taken_slots_label.place(x=8, y=200)
        self.taken_slots_entry = ctk.CTkEntry(self.master, font=self.font2, border_width=2, corner_radius=15)
        self.taken_slots_entry.place(x=100, y=200)

        self.total_slots_label = ctk.CTkLabel(self.master, font=self.font1, text='Total Slots')
        self.total_slots_label.place(x=8, y=260)
        self.total_slots_entry = ctk.CTkEntry(self.master, font=self.font2, border_width=2,corner_radius=15)
        self.total_slots_entry.place(x=100, y=260)
        
        
        # Buttons
        self.clear_button = ctk.CTkButton(self.master, command=lambda:self.clear(True), font=self.font1, fg_color="#39A7FF", text="Clear", corner_radius=15, cursor="hand2", width=260)
        self.clear_button.place(x=20, y=320)
        
        self.add_button = ctk.CTkButton(self.master, command=self.add_room,  font=self.font1, fg_color="#39A7FF", text="Add Room", corner_radius=15, cursor="hand2", width=260)
        self.add_button.place(x=20, y=365)

        self.update_button = ctk.CTkButton(self.master, command=self.update , font=self.font1, fg_color="#39A7FF", text="Update Room", corner_radius=15, cursor="hand2", width=260)
        self.update_button.place(x=305, y=365)

        self.delete_button = ctk.CTkButton(self.master, command=self.remove, font=self.font1, fg_color="#39A7FF", text="Delete Room", corner_radius=15, cursor="hand2", width=260)
        self.delete_button.place(x=590, y=365)
        
        #Treeview
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('Treeview', font=self.font2, foreground='#fff', background='#000', fieldbackground='#272829')
        style.map('Treeview', background=[('selected', '#1A8F2D')])

        self.tree = ttk.Treeview(self.master, height=15)
        self.tree['columns'] = ('room_id', 'additional_fees', 'monthly_rent', 'slots_taken', 'total_slots')

        self.tree.column('#0', width=0, stretch=tk.NO)  # used to hide the first column so that there are no excess columns
        self.tree.column('room_id', anchor=tk.CENTER, width=120)
        self.tree.column('additional_fees', anchor=tk.CENTER, width=120)
        self.tree.column('monthly_rent', anchor=tk.CENTER, width=120)
        self.tree.column('slots_taken', anchor=tk.CENTER, width=120)
        self.tree.column('total_slots', anchor=tk.CENTER, width=120)

        self.tree.heading('room_id', text='Room ID')
        self.tree.heading('additional_fees', text='Additional Fees')
        self.tree.heading('monthly_rent', text='Monthly Rent')
        self.tree.heading('slots_taken', text='Taken Slots')
        self.tree.heading('total_slots', text='Total Slots')

        self.tree.place(x=300, y=15)

        self.tree.bind('<ButtonRelease>', self.display_data)
        #responsible for showing treeview at startup
        self.add_to_treeview()
        
    # Function to connect to the database and update the Treeview
    def add_to_treeview(self):
        rooms = database.view_rooms()
        self.tree.delete(*self.tree.get_children())  # used to prevent inserting the same row multiple times
        for room in rooms:
            self.tree.insert('', tk.END, values=room)
            
    # Function to add a room
    def add_room(self):
        room_id = self.room_id_entry.get()
        additional_fees = self.additional_fees_entry.get()
        monthly_rent = self.rent_entry.get()
        taken_slots = self.taken_slots_entry.get()
        total_slots = self.total_slots_entry.get()
        
        if not (room_id and additional_fees and monthly_rent and taken_slots and total_slots):
                      messagebox.showerror("Error", "Please fill in all the fields")
        
        elif not(monthly_rent.isdigit()):
            messagebox.showerror("Error", "Monthly Rent must be a valid integer")
        
        elif not (taken_slots.isdigit() and total_slots.isdigit()):
                messagebox.showerror("Error", "Taken Slots and Total Slots must be valid integers")
          
        elif database.room_exists(room_id):
          messagebox.showerror("Error", "Room ID already exists")
          
        else:
          database.add_room(room_id, additional_fees, monthly_rent, taken_slots, total_slots)
          self.add_to_treeview()
          messagebox.showinfo("Success", "Room added successfully")
      
      # Function to clear entry fields
    def clear(self, *clicked):
        if clicked:
            self.tree.selection_remove(self.tree.focus())
        self.room_id_entry.delete(0, tk.END)
        self.additional_fees_entry.set('')
        self.rent_entry.delete(0, tk.END)
        self.taken_slots_entry.delete(0, tk.END)
        self.total_slots_entry.delete(0, tk.END)
        
    def display_data(self, a):
        selected_item = self.tree.focus()
        if selected_item:
            row = self.tree.item(selected_item)['values']
            self.clear()
            self.room_id_entry.insert(0, row[0])
            self.additional_fees_entry.set(row[1])
            self.rent_entry.insert(0, row[2])
            self.taken_slots_entry.insert(0, row[3])
            self.total_slots_entry.insert(0, row[4])
        else:
          pass
        
     # Function to remove a room
    def remove(self):
        selected_item = self.tree.focus()
        if not selected_item:
            messagebox.showerror("Error", "Please select a room to delete")
        else:
            room_id = self.tree.item(selected_item, 'values')[0]
            database.remove_room(room_id)
            self.add_to_treeview()
            self.clear()
            messagebox.showinfo("Success", "Data deleted successfully")
    
     # Function to update a room
    def update(self):
        selected_item = self.tree.focus()
        if not selected_item:
            messagebox.showerror("Error", "Please select a room to update")
        else:
            # Get the id from the selected item in the Treeview
            room_id = self.tree.item(selected_item, 'values')[0]
            additional_fees = self.additional_fees_entry.get()
            monthly_rent = self.rent_entry.get()
                
            taken_slots = self.taken_slots_entry.get()
            total_slots = self.total_slots_entry.get()
            
            
            if not (taken_slots.isdigit() and total_slots.isdigit()):
                messagebox.showerror("Error", "Taken Slots and Total Slots must be valid integers")
            elif not(monthly_rent.isdigit()):
                messagebox.showerror("Error", "Monthly Rent must be a valid integer")
            else:
                # Update the tenant using the retrieved id
                database.update_room(additional_fees, monthly_rent, taken_slots, total_slots, room_id)
                self.add_to_treeview()
                messagebox.showinfo("Success", "Data changed successfully")
                
                
#Tenants page function        
class PaymentPage:
    def __init__(self, master):
        self.master = master
        self.font1 = ("Helvetica", 15, "bold")
        self.font2 = ("Helvetica", 13)

        # Information Entry
        self.tenant_id_label = ctk.CTkLabel(self.master, font=self.font1, text='Tenant')
        self.tenant_id_label.place(x=15, y=20)
        #gets tenant ids from database
        self.tenant_data = database.get_tenant_ids_and_names(self)
        #creates a combobox for tenant ids
        self.variable1 = StringVar()
        self.tenant_id_option = ctk.CTkComboBox(self.master, font=self.font2, variable=self.variable1,
                                                values=[tenant["name"] for tenant in self.tenant_data],
                                                state='readonly', corner_radius=15,)
        self.tenant_id_option.place(x=100, y=20)

        self.tenant_room_id_label = ctk.CTkLabel(self.master, font=self.font1, text='Room ID')
        self.tenant_room_id_label.place(x=20, y=80)
        self.tenant_room_ids = database.get_room_ids()
        self.variable2 = StringVar()
        self.tenant_room_id_option = ctk.CTkComboBox(self.master, font=self.font2, variable=self.variable2, values=self.tenant_room_ids,
                                                    state='readonly', corner_radius=15,)
        self.tenant_room_id_option.place(x=100, y=80)

        self.payment_status_label = ctk.CTkLabel(self.master, font=self.font1, text='Payment \nStatus')
        self.payment_status_label.place(x=20, y=140)
        options1 = ['Paid', 'Overdue', 'Pending']
        self.variable3 = StringVar()
        self.payment_status_option = ctk.CTkComboBox(self.master, font=self.font2, variable=self.variable3, values=options1, corner_radius=15,
                                                     state='readonly')
        self.payment_status_option.place(x=100, y=140)

        self.last_payment_label = ctk.CTkLabel(self.master, font=self.font1, text='Last \nPayment')
        self.last_payment_label.place(x=20, y=200)
        self.last_payment_entry = ctk.CTkEntry(self.master, font=self.font2, border_width=2,corner_radius=15)
        self.last_payment_entry.place(x=100, y=200)

        self.payment_due_label = ctk.CTkLabel(self.master, font=self.font1, text='Payment \nDue')
        self.payment_due_label.place(x=20, y=260)
        self.payment_due_entry = ctk.CTkEntry(self.master, font=self.font2, border_width=2, corner_radius=15)
        self.payment_due_entry.place(x=100, y=260)
        
           # Buttons
        self.clear_button = ctk.CTkButton(self.master, command=lambda: self.clear(True), font=self.font1, 
                                          fg_color="#39A7FF", text="Clear", corner_radius=15, cursor="hand2",
                                          width=260)
        self.clear_button.place(x=20, y=320)
        
        self.add_button = ctk.CTkButton(self.master, command=self.add_payment, font=self.font1, fg_color="#39A7FF",
                                        text="Add Payment", corner_radius=15, cursor="hand2", width=260)
        self.add_button.place(x=20, y=365)

        self.update_button = ctk.CTkButton(self.master, command=self.update, font=self.font1, fg_color="#39A7FF",
                                           text="Update Payment", corner_radius=15, cursor="hand2", width=260)
        self.update_button.place(x=305, y=365)

        self.delete_button = ctk.CTkButton(self.master, command=self.remove, font=self.font1, fg_color="#39A7FF",
                                           text="Delete Payment", corner_radius=15, cursor="hand2", width=260)
        self.delete_button.place(x=590, y=365)
          
#Treeview
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('Treeview', font=self.font2, foreground='#fff', background='#000', fieldbackground='#272829')
        style.map('Treeview', background=[('selected', '#1A8F2D')])

        self.tree = ttk.Treeview(self.master, height=15)
        self.tree['columns'] = ('tenant_id', 'tenant_room_id', 'payment_status', 'last_payment', 'payment_due')
        
        self.tree.column('#0', width=0, stretch='no')
        self.tree.column('tenant_id', anchor=tk.CENTER, width=120)
        self.tree.column('tenant_room_id', anchor=tk.CENTER, width=120)
        self.tree.column('payment_status', anchor=tk.CENTER, width=120)
        self.tree.column('last_payment', anchor=tk.CENTER, width=120)
        self.tree.column('payment_due', anchor=tk.CENTER, width=120)
        
        self.tree.heading('tenant_id', text='Tenant Name')
        self.tree.heading('tenant_room_id', text='Room ID')
        self.tree.heading('payment_status', text='Payment Status')
        self.tree.heading('last_payment', text='Last Payment')
        self.tree.heading('payment_due', text='Payment Due')
        
        self.tree.place(x=300, y=15)
        
        self.tree.bind('<ButtonRelease>', self.display_data) #responsible for showing data in entry fields when clicked
         
        self.add_to_treeview()
        
    def add_to_treeview(self):
        payments = database.view_payments()
        self.tree.delete(*self.tree.get_children()) #Used to clear tree view before adding new data
        for payment in payments:
            self.tree.insert('', tk.END, values=payment)
            
    def add_payment(self):
        self.check_due_dates()
        tenant_id = self.variable1.get()
        tenant_room_id = self.variable2.get()
        payment_status = self.variable3.get()
        last_payment = self.last_payment_entry.get()
        payment_due = self.payment_due_entry.get()
        
        if not (tenant_id and tenant_room_id and payment_status and last_payment and payment_due):
            messagebox.showerror("Error", "Please fill all the fields")
        elif database.payment_exists(tenant_id):
            messagebox.showerror("Error", "Payment already exists")
        else:
            database.add_payment(tenant_id, tenant_room_id, payment_status, last_payment, payment_due)
            self.add_to_treeview()
            messagebox.showinfo("Success", "Data added successfully")
                
    # Function to clear selected entry fields
    def clear(self, *clicked):
        if clicked:
            self.tree.selection_remove(self.tree.focus())
        self.variable1.set('')
        self.variable2.set('')
        self.variable3.set('')
        self.last_payment_entry.delete(0, tk.END)
        self.payment_due_entry.delete(0, tk.END)
        
    def display_data(self, a):
        selected_item = self.tree.focus()
        if selected_item:
            row = self.tree.item(selected_item)['values']
            self.clear()
            self.variable1.set(row[0])
            self.variable2.set(row[1])
            self.variable3.set(row[2])
            self.last_payment_entry.insert(0, row[3])
            self.payment_due_entry.insert(0, row[4])
        else:
          pass
    
     # Function to remove a payment
    def remove(self):
        selected_item = self.tree.focus()
        if not selected_item:
            messagebox.showerror("Error", "Please select a data to delete")
        else:
            tenant_id = self.tree.item(selected_item, 'values')[0]
            database.remove_payment(tenant_id)
            self.add_to_treeview()
            self.clear()
            messagebox.showinfo("Success", "Data deleted successfully")
        
    # Function to update a payment
    def update(self):
        self.check_due_dates()
        selected_item = self.tree.focus()
        if not selected_item:
            messagebox.showerror("Error", "Please select a data to update")
        else:
            # Get the id from the selected item in the Treeview
            tenant_id = self.tree.item(selected_item, 'values')[0]
            new_tenant_room_id = self.variable2.get()
            new_payment_status = self.variable3.get()
            new_last_payment = self.last_payment_entry.get()
            new_payment_due = self.payment_due_entry.get()
        
            database.update_payment(new_tenant_room_id, new_payment_status, new_last_payment, new_payment_due, tenant_id)
            self.add_to_treeview()
            messagebox.showinfo("Success", "Data updated successfully")     
            
    # Function to check due dates
    def check_due_dates(self):
        today = date.today()

        # Iterate through payments and check due dates
        for item in self.tree.get_children():
            row = self.tree.item(item)['values']
            payment_due = datetime.strptime(row[4], "%m/%d/%y").date()
            payment_status = row[2]

             # If payment is due within tommorrow, show a message box
            if (payment_due - today).days and payment_status in ['Pending']:
                messagebox.showwarning("Payment Due", f"Payment for {row[0]} is due on {payment_due}")

root = ctk.CTk()
app = TenantManagement(root)
root.mainloop()
