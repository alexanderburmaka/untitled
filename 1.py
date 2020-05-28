import requests
import datetime


class BotHandler:

    def __init__(self, token):
        self.token = "651130819:AAHg2IGYRU48cbY-uqBLgFI8hwNy63Co-s8"
        self.api_url = "https://api.telegram.org/bot{}/".format(token)  # в url для api підставляємо значення token використовуючи .format

    def get_updates(self, timeout=30, offset=None):  # функція
        method = "getUpdates"  # задаємо назву методу
        params = {"timeout": timeout,
                  "offset": offset}  # timeout та offset встановлюються за значеннями вказаними в функції
        response = requests.get(self.api_url + method, params)  # за допомогою requests відправляємо get запит
        result_json = response.json()["result"]  # зберігаємо значення result в json 
        return result_json

    def send_message(self, text, chat_id):
        method = "sendMessege"  # задаємо назву методу
        params = {"chat_id": chat_id, "text": text}  # присвоюємо для params значення chat_id та text 
        response = requests.post(self.api_url + method, params)  # за допомогою requests відправляємо post запит  
        return response  # відправляємо повідомлення 

    def get_last_update(self):
        get_result = self.get_updates()

        if len(get_result) > 0:
            last_update = get_result[-1]
        else:
            last_update = get_result[len(get_result)]
        return last_update


greet_bot = BotHandler("651130819:AAHg2IGYRU48cbY-uqBLgFI8hwNy63Co-s8")
greetings = ("hello", "hi", "greetings", "sup")
now = datetime.datetime.now()


def main():
    new_offset = None
    today = now.day
    hour = now.hour


    while True:
        greet_bot.get_updates(new_offset)

        last_update = greet_bot.get_last_update()

        last_update_id = last_update['update_id']
        last_chat_text = last_update['message']['text']
        last_chat_id = last_update['message']['chat']['id']
        last_chat_name = last_update['message']['chat']['first_name']

        if last_chat_text.lower() in greetings and today == now.day and 6 <= hour < 12:
            greet_bot.send_message(last_chat_id, 'Good Morning  {}'.format(last_chat_name))
            today += 1

        elif last_chat_text.lower() in greetings and today == now.day and 12 <= hour < 17:
            greet_bot.send_message(last_chat_id, 'Good Afternoon {}'.format(last_chat_name))
            today += 1
        elif last_chat_text.lower() in greetings and today == now.day and 17 <= hour < 23:
            greet_bot.send_message(last_chat_id, 'Good Evening  {}'.format(last_chat_name))
            today += 1
        new_offset = last_update_id + 1
        if __name__ == '__main__':
            try:
                main()
            except KeyboardInterrupt:
                exit()
