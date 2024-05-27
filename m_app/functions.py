import os

def handle_uploaded_file(file):
    upload_path = 'C:/Users/BRAISON/Desktop/django/myenv/m_project/m_app/static/css/uploads'
    os.makedirs(upload_path, exist_ok=True)
    with open(os.path.join(upload_path, file.name), 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
