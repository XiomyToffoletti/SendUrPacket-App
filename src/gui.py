import tkinter as tk
from tkinter import ttk, messagebox
from pdf_generator import PDFGenerator
import os

#Base frame
class FormFrame(ttk.Frame):
    def __init__(self, parent, title, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        
        self.label_title = ttk.Label(self, text=title, font=("Arial", 12, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=2, pady=5)
        
        # Validation
        self.validate_text = self.register(self.only_letters)
        self.validate_number = self.register(self.only_numbers)

        self.create_fields()
        
    def only_letters(self, text):
        return all(c.isalpha() or c.isspace() for c in text)
    
    def only_numbers(self, text):
        return all(c.isdigit() for c in text)
    
    def create_fields(self):        
        required_labels = ["Last Name", "First Name", "ID", "Phone", "Street", "Number", "City", "State", "Postal Code"]
        optional_labels = ["Floor", "Door"]
        labels = required_labels + optional_labels
        self.entries = {}

        for i, label in enumerate(labels):
            label_text = f"{label}:" + (" *" if label in required_labels else "")
            
            ttk.Label(self, text=label_text).grid(row=i+1, column=0, padx=5, pady=5, sticky="e")
            entry = ttk.Entry(self, width=30)         
        
            # Validate entries
            validate_command = None
            if label in ["Last Name", "First Name", "Street", "City", "State"]:
                validate_command = (self.validate_text, "%P")
            elif label in ["ID", "Phone", "Number", "Postal Code", "Floor"]:
                validate_command = (self.validate_number, "%P")

            # Create entry with validation if applicable
            if validate_command:
                entry = ttk.Entry(self, width=30, validate="key", validatecommand=validate_command)
            else:
                entry = ttk.Entry(self, width=30)

            entry.grid(row=i+1, column=1, padx=5, pady=5)
            self.entries[label] = entry  # Field name as key
        
    # Generate dictionary with entered form data        
    def get_data(self):
        return {field: entry.get() for field, entry in self.entries.items()}

    # Verify that required fields are not empty
    def validate_fields(self):
        required_labels = ["Last Name", "First Name", "ID", "Phone", "Street", "Number", "City", "State", "Postal Code"]
        
        for label in required_labels:
            if not self.entries[label].get().strip():  
                messagebox.showerror("Error", "Fields marked with (*) are required.")
                return False  
        return True
    
    def clear_fields(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)  # Borra el contenido
            

    @staticmethod
    def generate_pdf(sender_frame, recipient_frame):
        """Generates the PDF if fields are valid."""
        if sender_frame.validate_fields() and recipient_frame.validate_fields():
            sender_data = {key: value.upper() for key, value in sender_frame.get_data().items()}  
            recipient_data = {key: value.upper() for key, value in recipient_frame.get_data().items()}  
        
            pdf_file = PDFGenerator.generate_pdf(sender_data, recipient_data)
            
            print(f"Generated PDF path: {pdf_file}")  # Debugging
            
            sender_frame.clear_fields()
            recipient_frame.clear_fields()
            
            if pdf_file and os.path.exists(pdf_file):
                print(f"PDF file found at: {pdf_file}, attempting to open...")  # Debugging
                try:
                    os.startfile(os.path.abspath(pdf_file))  # Convert to absolute path
                    print("PDF opened successfully.")  # Debugging
                except Exception as e:
                    print(f"Error while trying to open PDF: {e}")  # Debugging
                    messagebox.showerror("Error", f"Could not open the PDF file: {e}")

            else:
                print(f"Error: PDF file was not generated correctly. Expected path: {pdf_file}")  # Debugging
                messagebox.showerror("Error", f"Could not open the PDF file. Expected path: {pdf_file}")
            
        else:
            messagebox.showwarning("Warning", "Please complete all required fields (*).")


class SenderFrame(FormFrame): 
    """Form for the sender."""
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, "SENDER DATA", *args, **kwargs)

       
        

class RecipientFrame(FormFrame):
    """Form for the recipient."""
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, "RECIPIENT DATA", *args, **kwargs)


def start_interface():
    
    root = tk.Tk()
    root.title("SendUrPackapp")
    root.geometry("1000x600")
    root.iconbitmap("src/images/delivery_icon.ico")
    
    container_frame = ttk.Frame(root)
    container_frame.pack(pady=25, padx=20)

    sender_frame = SenderFrame(container_frame)
    sender_frame.pack(side="left", pady=30, padx=20)
    
    recipient_frame = RecipientFrame(container_frame)
    recipient_frame.pack(side="left", pady=30, padx=20)

    ttk.Button(
        root, 
        text="Generate Shiping Label", 
        command=lambda: FormFrame.generate_pdf(sender_frame, recipient_frame)
    ).pack(pady=20)

    root.mainloop()
