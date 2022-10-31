

# this file is coldstore python file and it is synchronous file,to run it, use the logger folder from python file
import paho.mqtt.client as mqtt
import pymongo
import json
from datetime import datetime
import time
from logger.log import get_logger


logger = get_logger()

try: 
    database='mongodb://localhost:27017'
    conn = pymongo.MongoClient(database)
    db = conn.TestingMqtt
    logger.info("Conection Successful to database :%s" % (database))
except Exception as e:
        logger.error("Exception caught While connection Database: %s" % e)


def on_message(client, userdata, message):
    try:
        print("Received message: ", str(message.payload.decode()))
        Temp = json.loads(message.payload.decode())['temp']
        Organization = json.loads(message.payload.decode())['org']
        Device_ID = json.loads(message.payload.decode())['d_id']
        Freeze_ID = json.loads(message.payload.decode())['f_id']
        print("Info", Temp, Organization, Device_ID, Freeze_ID)
        
        
        collections = db.list_collection_names()
        list = []
        if Organization not in collections:
            db.create_collection(Organization)

        list.append({
            "metadata": {"device_name": Device_ID, "freeze_id": Freeze_ID, "type": "temperature"},
            "timestamp": datetime.today().replace(microsecond=0),
            "temp": Temp,
        })
        db[Organization].insert_many(list)
    except Exception as e:
        logger.error("Exception caught While connection Database: %s" % e)

try:
    mqttbroker = "10.10.5.82"
    port = 1883
    client = mqtt.Client("P1")  
    client.connect(mqttbroker, port)
except Exception as e:
    logger.error("Exception caught While connection MqttBroker: %s" % e)

try:
    client.subscribe("apple/freeze-2/dev-2/temperature")
except Exception as e:
    logger.error("Exception caught While Subscribe ti Topic: %s" % e)

client.on_message = on_message
time.sleep(1)

client.loop_forever()




#log.config
# [loggers]
# keys=root

# [logger_root]
# level=DEBUG
# handlers=file_handler

# [formatters]
# keys=formatter

# [handlers]
# keys=file_handler

# [handler_file_handler]
# class=logging.handlers.TimedRotatingFileHandler
# level=INFO
# formatter=formatter
# args=('sdk.log', 'W5', 0, 4)

# [formatter_formatter]
# format={"date":"%(asctime)s","level":"%(levelname)s","file":"%(filename)s","lineno":"%(lineno)d", "msg": "%(message)s"}
# datefmt=%Y-%m-%d %H:%M:%S


#log

# import logging
# from logging import config
# from os import path


# def get_logger(name=None):
#     if name is None:
#         log_file_path = path.join(path.dirname(path.abspath(__file__)), 'log.config')
#         config.fileConfig(log_file_path)
#         logger = logging.getLogger()
#         return logger

#     else:
#         logger = logging.getLogger(name)
#         # Replace the previous handlers with the new FileHandler
#         for old_handler in logger.handlers:
#             logger.removeHandler(old_handler)

#         return logger

