from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
class PDFGenerator:    
    @staticmethod
    def generate_pdf(sender_data, recipient_data):
        
        sender_name = sender_data["Last Name"]+" "+sender_data["First Name"]
        base_name = sender_name.replace(' ', '_')

        # Create folder to store labels if it doesn't exist.
        destination_folder = 'Shiping Labels'
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        # Assigns a name to each generated label
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        pdf_file = f"{destination_folder}/{base_name}_{timestamp}.pdf"
        file_path = os.path.join(pdf_file)

        # Check if the file already exists, and if so, increment by 1
        counter = 1
        while os.path.exists(file_path):  
            pdf_file = f"{destination_folder}/{base_name}_{timestamp}_{counter}.pdf"
            file_path = os.path.join(destination_folder, pdf_file)
            counter += 1
        
        # Label design
        c = canvas.Canvas(pdf_file, pagesize=letter)
        
        delivery_img = "IMG/delivery-img.png"
        c.drawImage(image=delivery_img, x=100, y=740, width=50, height=50, mask='auto')
        c.setFont("Helvetica-Bold", 14)
        c.drawString(100, 740, "SENDUrPack")
        c.drawString(50, 720, "____________________________________________________________________________")

        c.setFont("Helvetica",12)
        # Print sender data
        c.drawString(100, 680, "SENDER:")
        y = 660
        for field, value in sender_data.items():
            c.drawString(120, y, f"{field}: {value}")
            y -= 20
        
        scissor_img="IMG/scissor-img.png"
        c.drawImage(image=scissor_img, x=10, y=423, width=20, height=20, mask='auto')
        c.drawString(25, 430, "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - ")
        
        
        c.drawImage(image=delivery_img, x=100, y=370, width=50, height=50, mask='auto')
        c.setFont("Helvetica-Bold", 14)
        c.drawString(100, 370, "SENDUrPack")
        c.drawString(50, 350, "____________________________________________________________________________")
        
        c.setFont("Helvetica",12)       
        
        # Print recipient data
        c.drawString(100, 310, "RECIPIENT:")
        y = 290
        for field, value in recipient_data.items():
            c.drawString(120, y, f"{field}: {value}")
            y -= 20

        c.save()
        messagebox.showinfo("Success", "Shiping Label generated successfully")
        
        return file_path
