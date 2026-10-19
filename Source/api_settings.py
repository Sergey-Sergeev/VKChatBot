import os

FILE_API_SETTINGS_NAME = 'api_settings.txt'

def load_token_and_id():
    """return token and id from api settings file."""

    try:
        with open(os.getcwd() + '\\' + FILE_API_SETTINGS_NAME, 'r', encoding='utf-8') as f:
            token = f.readline().rstrip('\n')
            group_id = f.readline().rstrip('\n')

        if token == '' or group_id == '':
            print(f'Ошибка: в файле "{FILE_API_SETTINGS_NAME}" не прописаны токен и id в первых двух строках.')
            return None, None

        return token, group_id

    except FileNotFoundError:
        print(f'Ошибка: файл "{FILE_API_SETTINGS_NAME}" не найден.')
        return None, None
    except Exception as e:
        print(f'Ошибка при чтении файла: {e}')
        return None, None