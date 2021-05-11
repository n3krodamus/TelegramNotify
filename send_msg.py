#!/usr/bin/python

import configparser as cfg
import requests
import sys


config = cfg.ConfigParser()
config.read('conf/prod.ini')

## Config
token = config['TELEGRAM']['token']
cid = config['TELEGRAM']['cid']
log_dir = config['LOGS']['log_dir']



def send_msg():
    msg = str(sys.argv[1])
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {"chat_id": cid, "text": msg }
    ret = requests.post(url, data=data)





if __name__ == '__main__':
   send_msg() 
