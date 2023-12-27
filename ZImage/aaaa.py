        self.btn_register = tk.Button(self, text="Register", width=9, font=("Times New Roman", 20, "bold"), fg="white", bg="black", bd=1, command=self.register_button_action)
        self.btn_register.place(x=1305, y=740, height=40)


    def register_button_action(self):

        # Validation for name
        name = self.txt_name.get()
        if not name.replace(" ", "").isalnum():
            messagebox.showerror("Error", "Invalid Name.")
            return
        
        # Validation for address
        address = self.txt_address.get()
        if not address.replace(" ", "").isalnum():
            messagebox.showerror("Error", "Invalid Address.")
            return

        # Validation for phone 
        phone = self.txt_phone.get()
        if not phone.isdigit() or len(phone) != 10:
            messagebox.showerror("Error", "Invalid Phone Number")
            return
        
        # Validation for email
        email = self.txt_email.get()
        email_pattern = re.compile(r'^[a-zA-Z0-9]+(_[a-zA-Z0-9]+)?@[a-zA-Z0-9]+\.[a-zA-Z]{2,4}$')
        if not email_pattern.match(email):
            messagebox.showerror("Error", "Invalid Email Address. Please enter a valid email.")
            return
        
        # Validation for username
        username = self.txt_username.get()
        if not username.replace(" ", "").isalnum() or len(username) > 30:
            messagebox.showerror("Error", "Please use appropriate username.")
            return

        # Validation for password
        password = self.txt_password.get()
        if not password.replace(" ", "").isalnum() or len(password) > 30:
            messagebox.showerror("Error", "Please use appropriate password.")   
            return
        
        confirm_password = self.txt_confirmpw.get()
        if confirm_password != password:
            messagebox.showerror("Error", "Passwords do not match.")
            return
        
        payment_method = self.cmb_payment.get()
        if not payment_method:
            messagebox.showerror("Error", "Invalid Payment Method.") 
            return 
        
        
        