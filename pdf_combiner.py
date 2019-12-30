"""
create a list of selected pdfs
for each item in the list, iterate through and combine
then give an output path for the combined pdf to be stored as
"""

import os
import PyPDF2
import tkinter

from tkinter import filedialog
from tkinter import messagebox

root = tkinter.Tk()
root.withdraw()


def pdf_compiler():

    # initiate path list
    some_list_of_paths = []

    # initiate bool as True for while loop to run at least once
    additional_pdf_bool = True

    # while bool remains True, continue asking user for additional pdfs
    # after pdf selection happens, ask user if more pdfs are needed
    while additional_pdf_bool is True:
        pdf_selection = filedialog.askopenfilename(title="Select PDF", filetypes=[("PDFs", "*.pdf")])
        some_list_of_paths.append(pdf_selection)
        additional_pdf_bool = messagebox.askyesno("Question", "Are more PDFs needed?")

    # create the merger object
    # strict=False allows the merger to ignore white space in the pdfs being read in
    pdf_merger = PyPDF2.PdfFileMerger(strict=False)

    # iterate through list of paths provided by the user and append them to the merger object
    for path in some_list_of_paths:
        pdf_merger.append(path)

    # ask user where to store the pdf
    # give the compiled pdf a name and path
    # verify final_destination does not exist
    # if final_destination does exist, append " (i)" to the file name
    output_path = filedialog.askdirectory(title="Select pdf output destination")
    final_destination = f'{output_path}/Compiled PDF.pdf'

    i = 1
    while os.path.exists(final_destination):
        final_destination = f'{output_path}/Compiled PDF ({i}).pdf'
        i += 1

    # open the output_path as a writeable binary (necessary due to pdfs being images instead of plain text files)
    # then write the merger object to the output path
    with open(final_destination, 'wb') as fileobj:
        pdf_merger.write(fileobj)


if __name__ == '__main__':
    pdf_compiler()
