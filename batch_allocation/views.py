from django.shortcuts import render
from .forms import BatchForm

# Create your views here.
def batch_allocation(request):
    form = BatchForm()
    if request.method == 'POST':
        form = BatchForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save()
            resume_path = instance.resume.path

            extracted_text = allocate_batch_from_pdf(resume_path)
            if extracted_text:
                return render(request, 'batch_allocation/batch_alloted.html', {'batch_data' : extracted_text})
        else:
            form = BatchForm()

    return render(request, 'batch_allocation/index.html', {'form': form})






#***************************** PDF ALLOCATION LOGIC *****************************#

import re
import PyPDF2

def allocate_batch_from_pdf(file_path):
    # Define keywords for each batch
    java_keywords = ['AWS certification', 'Java certification']
    dotnet_keywords = ['Azure certification', '.NET certification']
    data_eng_keywords = ['Python']

    # Read the PDF content
    content = ""
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            content += page.extract_text() or ""

    # Allocate batch based on content
    if any(re.search(r'\b' + keyword + r'\b', content, re.IGNORECASE) for keyword in java_keywords):
        return "Java Batch"
    elif any(re.search(r'\b' + keyword + r'\b', content, re.IGNORECASE) for keyword in dotnet_keywords):
        return ".NET Batch"
    elif any(re.search(r'\b' + keyword + r'\b', content, re.IGNORECASE) for keyword in data_eng_keywords):
        return "Data Engineering Batch"
    else:
        return "No Batch Found"