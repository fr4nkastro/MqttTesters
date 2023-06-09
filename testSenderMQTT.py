import paho.mqtt.client as mqtt

# Definir las funciones de callbacks de conexión y publicación
def on_connect(client, userdata, flags, rc):
    print("Conectado con resultado de código: "+str(rc))

def on_publish(client, userdata, mid):
    print("Mensaje publicado en el tópico 'test'")

# Crear una instancia de cliente MQTT
client = mqtt.Client()

# Asignar las funciones de callback de conexión y publicación
client.on_connect = on_connect
client.on_publish = on_publish

# Conectarse al broker de Mosquitto en localhost
client.connect("192.168.1.24", 1883, 60)

# Publicar un mensaje de prueba en el tópico 'test'
message = "Este es un mensaje de prueba"
client.publish("test", message)

# Mantener la conexión MQTT activa
client.loop_forever()
