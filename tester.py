import paho.mqtt.subscribe as subscribe

def print_msg(client, userdata, message):
    print("%s : %s" % (message.topic, message.payload))

subscribe.callback(print_msg, "pfgs", hostname="mqtt.eclipse.org")