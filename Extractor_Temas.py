import csv
from telethon.sync import TelegramClient
from telethon.tl.types import User, Channel, Chat

api_id = '38334884'       
api_hash = '5abe39bf9f60546a49e338cc65dd3088'   
phone = '+593995234279'         
group_username = -1003414543219
limit_msgs = 5000 

client = TelegramClient('session_master', api_id, api_hash)
client.connect()

if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Código Telegram: '))


print(f"--- Analizando ID: {group_username} ---")
entity = client.get_entity(group_username)


es_foro = False
nombre_chat = "Desconocido"

if isinstance(entity, User):
    print(">>> TIPO DETECTADO: USUARIO (Persona o Bot)")
    nombre_chat = entity.first_name
    es_foro = False 
elif isinstance(entity, (Channel, Chat)):
    print(">>> TIPO DETECTADO: GRUPO / CANAL")
    nombre_chat = entity.title
   
    es_foro = getattr(entity, 'forum', False)

print(f"Nombre: {nombre_chat}")
print(f"¿Es un Foro/Topics?: {'SÍ' if es_foro else 'NO'}")


csv_filename = f'{group_username}_blindado.csv'
count = 0

with open(csv_filename, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Fecha', 'Sender_ID', 'Topic_ID', 'Mensaje'])

    
    if es_foro:
        print(">>> Modo FORO activado. Buscando temas...")
        try:
            topics = client.get_forum_topics(entity)
            if not topics.topics:
                 print("No se listaron temas, intentando barrido general...")
                 iterador = client.iter_messages(entity, limit=limit_msgs)
            else:
                print(f"Encontrados {len(topics.topics)} temas. Extrayendo...")
                all_messages = []
                for topic in topics.topics:
                    print(f"   -> Tema: {topic.title}")
                    msgs = client.get_messages(entity, limit=limit_msgs, reply_to=topic.id)
                    all_messages.extend(msgs)
                iterador = all_messages
        except Exception as e:
            print(f"Error accediendo a temas: {e}. Cambiando a modo normal.")
            iterador = client.iter_messages(entity, limit=limit_msgs)

    else:
        print(">>> Modo NORMAL (Chat directo o Grupo simple).")
        
        iterador = client.iter_messages(entity, limit=limit_msgs)

    
    print(">>> Guardando mensajes en CSV...")
    for message in iterador:
        if message and message.message: 
            
            
            topic_id = "General"
            if message.reply_to and hasattr(message.reply_to, 'reply_to_msg_id'):
                 topic_id = message.reply_to.reply_to_msg_id

            writer.writerow([
                message.date,
                message.sender_id,
                topic_id,
                message.message.replace('\n', ' ')
            ])
            count += 1
            if count % 100 == 0:
                print(f"Guardados {count} mensajes...")

print(f"\n--- ÉXITO: Se guardaron {count} mensajes en {csv_filename} ---")