import vk_api
import api_settings
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType



def main():

    token, group_id = api_settings.load_token_and_id()

    if(token == None or group_id == None):
        return

    vk_session = vk_api.VkApi(token=token)
    longpoll = VkBotLongPoll(vk_session, group_id)

    print('Бот запущен. Ожидание сообщений...')

    for event in longpoll.listen():

        if event.type == VkBotEventType.MESSAGE_NEW:

            message = event.obj.message

            user_id = message.get('from_id')
            text = message.get('text', '')

            print(f'Новое сообщение от {user_id}: {text}')


if __name__ == '__main__':
    main()