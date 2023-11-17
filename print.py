import streamlit as st
from io import BytesIO
from fpdf import FPDF 

# Function to generate PDF from the list of displayed doctors
def generate_pdf(doctors):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', size=16)  # Set font style and size for the title
    pdf.cell(200, 10, txt="Healthcare Provider Search Results", ln=True, align='C')  # Title
    pdf.set_font("Arial", size=12)
    
    # Write data to PDF
    for doctor in doctors:
        pdf.ln(10)  # Move to the next line for spacing
        pdf.cell(200, 10, txt=f"Name: {doctor['last_name']}, {doctor['first_name']}", ln=True)
        pdf.cell(200, 10, txt=f"Address: {doctor['address']}", ln=True)
        
    
    # Save the PDF in memory
    pdf_bytes = pdf.output(dest="S").encode("latin-1")
    return pdf_bytes