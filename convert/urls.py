from django.urls import path
from .views import convert_page, convert_pdf_to_docx_api

urlpatterns = [
    path('', convert_page, name='convert_page'),   # /convert/
    path('api/', convert_pdf_to_docx_api, name='convert_api'),  # /convert/api/
]