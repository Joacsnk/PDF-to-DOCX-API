from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from pdf2docx import Converter # Converção
import tempfile
import os




# Página
def convert_page(request):
    return render(request, 'convert/convert.html')


# API
@csrf_exempt
def convert_pdf_to_docx_api(request):
    
    if request.method != 'POST':
        return HttpResponse("Método não permitido", status=405) # Caso tenha sido outro método

    arquivo = request.FILES.get('arquivo')

    if not arquivo:
        return HttpResponse("Arquivo não enviado", status=400) # Caso sem arquivo

    if not arquivo.name.endswith('.pdf'):
        return HttpResponse("Apenas PDF permitido", status=400) # Caso não seja PDF

    with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as temp_pdf: # Salva temporáriamente o arquivo
        for chunk in arquivo.chunks():
            temp_pdf.write(chunk)
        temp_pdf_path = temp_pdf.name

    temp_docx_path = temp_pdf_path.replace('.pdf', '.docx') # Troca o nome do arquivo

    cv = Converter(temp_pdf_path) # Conversão
    cv.convert(temp_docx_path)
    cv.close()

    with open(temp_docx_path, 'rb') as f:
        response = HttpResponse(
            f.read(),
            content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
        )
        response['Content-Disposition'] = 'attachment; filename="convertido.docx"'

    os.remove(temp_pdf_path) # Apaga os arquivos temporários
    os.remove(temp_docx_path)

    return response