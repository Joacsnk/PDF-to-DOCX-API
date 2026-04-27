# 📄 PDF to DOCX API em Django
---

Conversão de arquivos PDF para DOCX utilizando Django no backend e JavaScript (Fetch API) no frontend. O sistema permite upload de arquivos e retorna automaticamente o documento convertido para download.

# 🧠 Sobre o Projeto
---

Este projeto demonstra:

- Upload de arquivos via formulário HTML
- Envio assíncrono com JavaScript (fetch)
- Processamento de arquivos no backend (Django)
- Conversão de PDF para DOCX com **pdf2docx**
- Retorno de arquivos binários para download

O foco é didático. Entender como funciona o fluxo completo de:
 **upload → processamento → download em aplicações web.**

# ⚙️ Como o Sistema Funciona
---
## 📥 Upload do Arquivo

O usuário seleciona um PDF e envia através do formulário:

~~~
<form method="POST" enctype="multipart/form-data">
~~~

O atributo:
~~~
enctype="multipart/form-data"
~~~
é essencial para permitir envio de arquivos.

## 🔄 Envio Assíncrono (Frontend)
---

O envio é interceptado com JavaScript:

~~~
const formData = new FormData(e.target);
~~~

E enviado para a API:

~~~
fetch('/convert/api/', {
    method: 'POST',
    body: formData
});
~~~

Isso evita recarregar a página.

## 📦 Recebimento no Backend
---

No Django, o arquivo chega em:

~~~
arquivo = request.FILES.get('arquivo')
~~~~~~

Ele é tratado como um objeto de upload.

## 📁 Armazenamento Temporário
---

O arquivo é salvo temporariamente:

~~~
with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as temp_pdf:
~~~

Isso permite que a biblioteca de conversão acesse o arquivo no sistema.

## 🔁 Conversão PDF → DOCX
---

A conversão é feita com:

~~~
cv = Converter(temp_pdf_path)
cv.convert(temp_docx_path)
cv.close()
~~~
## 📤 Retorno do Arquivo
---

O arquivo convertido é retornado como resposta HTTP:

~~~
HttpResponse(
    f.read(),
    content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
)
~~~

Com header:
~~~
Content-Disposition: attachment
~~~

Isso força o download no navegador.

## 🧹 Limpeza
---

Após a conversão:

~~~
os.remove(temp_pdf_path)
os.remove(temp_docx_path)
~~~ 

Evita acúmulo de arquivos no servidor.

## 🔄 Fluxo Completo
---

**1. Usuário → Upload PDF**
       ↓
**2. Frontend (fetch)**
       ↓
**3. Django recebe arquivo**
       ↓
**4. Salva temporariamente**
       ↓
**5. Converte com pdf2docx**
       ↓
**6. Retorna DOCX**
       ↓
**7. Download automático**

# 🧠 Conceitos Envolvidos
---

* Upload de arquivos (multipart/form-data)
* Requisições assíncronas (AJAX / Fetch API)
* Manipulação de arquivos no backend
* Processamento de dados binários
* HTTP Response com download
* Segurança básica (CSRF, validações)

# 🛡️ Considerações de Segurança
---

O projeto inclui práticas importantes:

* Validação de tipo de arquivo (PDF)
* Limite de tamanho de upload
* Proteção contra múltiplas requisições (rate limit)
* Controle de concorrência (evita sobrecarga)
