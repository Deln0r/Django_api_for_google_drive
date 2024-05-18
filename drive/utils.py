import os  # Для работы с файлами и путями
import json  # Для работы с JSON-файлами (например, с учетными данными)
import io  # Для работы с потоками ввода/вывода
from google.auth.transport.requests import Request  # Для обновления токена доступа
from google.oauth2.credentials import Credentials  # Для работы с учетными данными OAuth2
from google_auth_oauthlib.flow import InstalledAppFlow  # Для авторизации пользователя
from googleapiclient.discovery import build  # Для создания объекта сервиса Google Drive API
from googleapiclient.http import MediaIoBaseUpload  # Для загрузки файлов

# Области доступа, которые нужны приложению
SCOPES = ['https://www.googleapis.com/auth/drive.file'] 

def get_credentials():
    """
    Получает или обноляет учетные данные пользователя для доступа к Google Drive API.

    Если файл token.json существует, то загружаем учетные данные из него.
    Если учетные данные недействительны или истекли, пытаемся обновить их.
    Если обновление невозможно или файл token.json не существует, запускаем процесс авторизации пользователя.
    После получения или обновления учетных данных, сохраняем их в файл token.json.

    Returns:
        Credentials: Объект учетных данных пользователя.
    """
    creds = None  # Изначально нет учетных данных
    if os.path.exists('token.json'):  # Проверяем, есть ли сохраненный токен
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)  # Загружаем учетные данные из файла

    if not creds or not creds.valid:  # Проверяем, действительны ли учетные данные
        if creds and creds.expired and creds.refresh_token:  # Если токен истек, но есть токен обновления
            creds.refresh(Request())  # Пытаемся обновить токен
        else:  # Если токена нет или его нельзя обновить
            flow = InstalledAppFlow.from_client_secrets_file(  # Запускаем процесс авторизации
                'credentials.json', SCOPES)  # Используем файл с клиентским ID и секретом
            creds = flow.run_local_server(port=0)  # Открываем веб-браузер для авторизации

        with open('token.json', 'w') as token:  # Сохраняем полученные учетные данные
            token.write(creds.to_json())

    return creds  # Возвращаем учетные данные

def upload_file_to_drive(data, name):
    """
    Загружает файл в Google Drive.

    Args:
        data (str): Содержимое файла.
        name (str): Имя файла для сохранения в Google Drive.

    Returns:
        str: ID загруженного файла в Google Drive.
    """
    creds = get_credentials()  # Получаем учетные данные пользователя
    service = build('drive', 'v3', credentials=creds)  # Создаем объект сервиса Drive API

    file_metadata = {'name': name}  # Метаданные файла (только имя)
    media = MediaIoBaseUpload(io.BytesIO(data.encode()), mimetype='text/plain')  # Подготовка содержимого файла для загрузки
    
    # Загрузка файла на Google Drive
    file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()  

    return file.get('id')  # Возвращаем ID загруженного файла