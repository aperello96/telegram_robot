# telegram_robot
## En este proyecto se incluye algunas de las funciones basicas para implementar un servicio de mensajeria automática con telegram

### Pasos previos a usar el código:

Para poder usar la api de telegram, necesitaremos un token y un chatid para poder identificar la conversación.

1. Registrarse a telegram y iniciar el cliente con el siguiente proceso:
```
Abrir una conversación con @BotFather
```

2. Iniciar el programa pulsando el boton "start"

3. Inserta el siguiente comando para crear un nuevo bot: 
```
/newbot
```
4. El asistente le preguntará que nombre queiere ponerle. Este es el nombre que van a ver los usuarios y no hace falta que sea único:
```
nombre_robot
```

5. El asistente le preguntará un nombre de usuario único. Este tiene que terminar con "_bot", por ejemplo:
```
nombre_robot_test_bot
```

6. Finalmente el robot le proporcionará un token único para poder usarlo.
```
Done! Congratulations on your new bot. You will find it at t.me/nombre_robot_test_bot
. You can now add a description, about section and profile picture for your bot, see /help for a list of commands. By the way, when you've finished creating your cool bot, ping our Bot Support if you want a better username for it. Just make sure the bot is fully operational before you do this.

Use this token to access the HTTP API:
1334584610:AAEPmjlh84N62Lv3jAWEgOftlxfLfMhB1gy
Keep your token secure and store it safely, it can be used by anyone to control your bot.

For a description of the Bot API, see this page: https://core.telegram.org/bots/api
```

7. Obtenemos el chatID:
Iniciamos una conversación al nuevo bot que hemos generado abriéndolo directamente desde el link que nos ha dado el @BotFather o buscando en el buscador por el nombre único creado.
Enviamos en el chat:
```
/start Holaa
```

8. En un mismo navegador usamos la siguiente url cambiando el <token> por nuestro token generado
```
https://api.telegram.org/bot<TOKEN>/getUpdates
```

Este nos devolvera un codigo como el siguiente donde obtendremos el chatID

```
// 20230629126375
// https://api.telegram.org/bot1334584610:AAEPmjlh84N62Lv3jAWEgOftlxfLfMhB1gy/getUpdates

{
  "ok": true,
  "result": [
    {
      "update_id": 971238617,
      "message": {
        "message_id": 3,
        "from": {
          "id": 5941080371,
          "is_bot": false,
          "first_name": "tu_nombre",
          "last_name": "tu_apellido",
          "username": "nombre_de_usuario",
          "language_code": "en"
        },
        "chat": {
          "id": 5941080371,
          "first_name": "tu_nombre",
          "last_name": "tu_apellido",
          "username": "nombre_de_usuario",
          "type": "private"
        },
        "date": 1688027465,
        "text": "Holaa"
      }
    }
  ]
}
```

9. Creamos un archivo .env con el token y el chatID:
```
API_TOKEN = '1334584610:AAEPmjlh84N62Lv3jAWEgOftlxfLfMhB1gy'
CHAT_ID = '5941080371'
```
### Instalación de dependencias:
Para usar el código es necesario la instalación de las siguientes librerias:
```
pip install python-dotenv
```

```
pip install requests
```

### Ejecuta test_robot.py para recibir un mensaje:
Ejecuta el test_robot.py para recibir en tu chat de telegram "Hola desde python" y una imagen de test

### Para mas información aqui se encuentra la url de como empezar y la lista de los métodos disponibles en la api:
[Api telegram](https://core.telegram.org/bots/api#available-methods)