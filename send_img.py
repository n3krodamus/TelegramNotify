#!/usr/bin/env python

import configparser as cfg
import requests
import sys


config = cfg.ConfigParser()
config.read('conf/prod.ini')

## Configuracion
token = config['TELEGRAM']['token']
cid = config['TELEGRAM']['cid']
log_dir = config['LOGS']['log_dir']
##


def send_img():
    img = str(sys.argv[1])
    caption = str(sys.argv[2])

    cmd = 'sendPhoto'
    url = f"https://api.telegram.org/bot{token}/{cmd}"
    data = {"chat_id": cid, "caption": caption}

    with open(img, "rb") as img_file:
        ret = requests.post(url, data=data, files={"photo": img_file})



if __name__ == '__main__':
    send_img()

