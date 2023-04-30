import subprocess
import requests
import time
import os
import logging

domoticz_url = os.environ.get('DOMOTICZ_URL')
domoticz_login = os.environ.get('DOMOTICZ_LOGIN')
domoticz_password = os.environ.get('DOMOTICZ_PASSWORD')
ups_name = os.environ.get('UPS_NAME')
ups_host = os.environ.get('UPS_HOST')
ups_port = os.environ.get('UPS_PORT')
ups_power = os.environ.get('UPS_POWER')

#Declaration of IDX in domoticz
idx_map = {
    'battery_voltage': '208',
    'input_frequency': '209',
    'input_voltage': '215',
    'output_voltage': '210',
    'ups_load': '214',
    'ups_load_power': '212',
    'ups_status': '216'
}

def get_ups_data(ups_name, host, port):
    output = subprocess.check_output(["upsc", f"{ups_name}@{host}:{port}"])
    output = output.decode("utf-8")
    lines = output.strip().split("\n")
    data = {}
    for line in lines:
        key, value = line.split(": ")
        field_name = key.replace(".", "_").lower()
        data[field_name] = value
    return data

def send_to_domoticz(url, login, password, idx, svalue, alert=False, alert_level=0, alert_text=''):
    if alert:
        payload = {'type': 'command', 'param': 'udevice', 'idx': idx, 'nvalue': alert_level, 'svalue': alert_text}
    else:
        payload = {'type': 'command', 'param': 'udevice', 'idx': idx, 'nvalue': '0', 'svalue': str(svalue)}
    response = requests.get(url + '/json.htm', auth=(login, password), params=payload)
    logging.info(f"Sending {svalue} to idx {idx} returned {response.status_code}")
    logging.info(f"Response text: {response.text}")
    return response.status_code



while True:
    ups_data = get_ups_data(ups_name, ups_host, ups_port)
    ups_data['ups_load_power'] = str(round(float(ups_power) * (float(ups_data['ups_load'])/100)))+';0'
    for key, value in ups_data.items():
        if key in idx_map:
            idx = idx_map[key]

            if key == "ups_status":
                if value == "OL":
                    alert_level="1"
                    alert_text="Praca normalna"
                elif value == "OB":
                    alert_level="4"
                    alert_text="Brak zasilania sieciowego"
                else:
                    alert_level="2"
                    alert_text="Błąd: "+value
                send_to_domoticz(domoticz_url, domoticz_login, domoticz_password, idx, value, True, alert_level, alert_text)
            else:
                send_to_domoticz(domoticz_url, domoticz_login, domoticz_password, idx, value)
    time.sleep(15)