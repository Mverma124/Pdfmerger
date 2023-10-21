import PyPDF2
import tkinter as tk
from tkinter import filedialog
def select_pdf_files():
    file_paths = filedialog.askopenfilenames(filetypes=[("PDF Files", "*.pdf")])
    for file_path in file_paths:
        pdf_listbox.insert(tk.END, file_path)

def merge_pdfs():
    pdf_files = pdf_listbox.get(0, tk.END)
    if pdf_files:
        output_file = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
        if output_file:
            pdf_merger = PyPDF2.PdfFileMerger()
            for pdf_file in pdf_files:
                pdf_merger.append(pdf_file)
            pdf_merger.write(output_file)
            pdf_merger.close()
            result_label.config(text=f"Merged PDF saved as {output_file}")
        else:
            result_label.config(text="Merge canceled.")
    else:
        result_label.config(text="No PDF files selected.")

'''the main window'''
root = tk.Tk()
root.title("PDF Merger")

'''button to select PDF files'''
select_button = tk.Button(root, text="Select PDF Files", command=select_pdf_files)
select_button.pack(pady=10)

'''listbox to display selected PDF files'''
pdf_listbox = tk.Listbox(root, selectmode=tk.MULTIPLE, width=150, height=10)
pdf_listbox.pack()

'''Create a button to merge PDFs'''
merge_button = tk.Button(root, text="Merge PDFs", command=merge_pdfs)
merge_button.pack(pady=10)

'''Create a label to display the result'''
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
