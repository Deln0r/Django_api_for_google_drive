from rest_framework import serializers

class UploadFileSerializer(serializers.Serializer):
    """
    Сериализатор для данных загрузки файла.

    Этот сериализатор используется для валидации и десериализации данных, 
    которые поступают в POST-запрос при загрузке файла.
    Он определяет два поля:

    - data (CharField): Содержимое файла в виде строки. Обязательное поле.
    - name (CharField): Имя файла. Обязательное поле.
    """

    data = serializers.CharField()  # Поле для содержимого файла (текст)
    name = serializers.CharField()  # Поле для имени файла