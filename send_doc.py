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


def send_doc():
    doc = str(sys.argv[1])
    caption = str(sys.argv[2])

    cmd = 'sendDocument'
    url = f"https://api.telegram.org/bot{token}/{cmd}"
    data = {"chat_id": cid, "caption": caption}

    with open(doc, "rb") as doc_file:
        ret = requests.post(url, data=data, files={"document": doc_file})



if __name__ == '__main__':
    send_doc()

