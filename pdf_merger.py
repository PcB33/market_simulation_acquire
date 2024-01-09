# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 21:50:10 2022

@author: Phili
"""
from PyPDF2 import PdfMerger, PdfFileReader
import os
merger = PdfMerger()
# ausfüllen
path_to_empty_pdf = "C:/Users/Phili/OneDrive/Desktop/All_CVs merge/empty.pdf"
path_to_cvs = "C:/Users/Phili/OneDrive/Desktop/All_CVs merge/CV_folder"
path_to_result_pdf = "C:/Users/Phili/OneDrive/Desktop/All_CVs merge/result.pdf"
# algorithmus
for company in os.listdir(path_to_cvs):
    company_path = path_to_cvs + "/" + company
    if os.path.isdir(company_path):
        for pdf_file in os.listdir(company_path):
            pdf_path = company_path + "/" + pdf_file
            if pdf_path.endswith(".pdf"):
                merger.append(PdfFileReader(pdf_path, strict=False))
        merger.append(path_to_empty_pdf)
merger.write(path_to_result_pdf)
merger.close()