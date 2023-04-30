# UPS VOLT to Domoticz

![Screenshot of the Domoticz home automation system's web interface, featuring a top bar with filter options and search functionality, a Lights/Switches section displaying the status of a light switch in the Server Room Basement, and a Utility Sensors section showing various sensors such as voltage, power consumption, and UPS load percentage. The interface is organized in a grid layout, with each device presented in a separate box.](domoticz_screenshot.png)

## Description

This script retrieves information about an uninterruptible power supply (UPS) connected via USB and sends it to a Domoticz home automation system. The script uses the Network UPS Tools (NUT) software to communicate with the UPS and retrieves information such as battery voltage, input and output voltage, input frequency, and UPS load. It also calculates the UPS load power based on a fixed UPS power value.

The script maps the retrieved data to specific Domoticz device indices and sends the data to Domoticz via its JSON API. The script also handles alert levels for the UPS status, setting appropriate alert levels and alert text depending on the UPS status. The script does not create new devices in Domoticz, so the necessary devices must be set up beforehand.

The script is intended to be run as a Docker container and accepts environment variables for the necessary configuration parameters such as the Domoticz URL, login credentials, UPS name, host, and port, and UPS power.

## Usage

To use the script, you will need to set the following environment variables:


- `DOMOTICZ_URL`: the URL of your Domoticz instance
- `DOMOTICZ_LOGIN`: your Domoticz login username
- `DOMOTICZ_PASSWORD`: your Domoticz login password
- `UPS_NAME`: the name of your UPS in NUT
- `UPS_HOST`: the IP address or hostname of the machine running NUT

You can then run the script using the following command: docker-compose up -d

## Setting up IDX mapping in Domoticz

The script maps the data retrieved from the UPS to specific Domoticz device indices using the idx_map dictionary (UPStoDomoticz.py file). The keys in this dictionary correspond to the data types retrieved from the UPS, and the values correspond to the device indices in Domoticz.

For example:
```
idx_map = {
    'battery_voltage': '208',
    'input_frequency': '209',
    'input_voltage': '215',
    'output_voltage': '210',
    'ups_load': '214',
    'ups_load_power': '212',
    'ups_status': '216'
}
```

In the above example, the battery voltage data retrieved from the UPS will be mapped to device index 208 in Domoticz, and so on for the other data types.

To set up the necessary devices in Domoticz, follow these steps:

1. Open the Domoticz web interface and go to the "Setup" tab.
2. Click on the "Hardware" button and select "Dummy".
3. Give the dummy hardware device a name, such as "UPS Data".
4. Click on the "Create Virtual Sensors" button and select "Custom Sensor".
5. Enter a name for the sensor (e.g., "Battery Voltage") and select the appropriate sensor type (e.g., "Voltage (V)").
6. Enter the device index number from the idx_map dictionary for the selected data type (e.g., 208 for battery voltage).
7. Repeat steps 4-6 for each data type in the idx_map dictionary.

Once you have set up the necessary devices in Domoticz, you can run the script to send the UPS data to Domoticz.


## Opis
Ten skrypt pobiera informacje o zasilaczu awaryjnym bezprzerwowej (UPS) podłączonym przez USB i wysyła je do systemu automatyki domowej Domoticz. Skrypt korzysta z oprogramowania Network UPS Tools (NUT) do komunikacji z UPS-em i pobierania informacji, takich jak napięcie baterii, napięcie wejściowe i wyjściowe, częstotliwość wejściowa oraz obciążenie UPS-a. Oblicza również moc obciążenia UPS na podstawie stałej wartości mocy UPS.

Skrypt mapuje pobrane dane na konkretne indeksy urządzeń Domoticz i wysyła dane do Domoticz za pomocą jego JSON API. Skrypt obsługuje również poziomy alarmowe dla statusu UPS, ustawiając odpowiednie poziomy alarmowe i tekst alarmowy w zależności od statusu UPS. Skrypt nie tworzy nowych urządzeń w Domoticz, więc konieczne jest wcześniejsze skonfigurowanie odpowiednich urządzeń.

Skrypt przeznaczony jest do uruchamiania jako kontener Docker i akceptuje zmienne środowiskowe dla niezbędnych parametrów konfiguracyjnych, takich jak adres URL Domoticz, dane uwierzytelniające, nazwa UPS, host i port oraz moc UPS.

## Użycie
Aby użyć skryptu, należy ustawić następujące zmienne środowiskowe:


- `DOMOTICZ_URL`: adres URL Twojej instancji Domoticz
- `DOMOTICZ_LOGIN`: nazwa użytkownika do logowania w Domoticz
- `DOMOTICZ_PASSWORD`: hasło do logowania w Domoticz
- `UPS_NAME`: nazwa Twojego UPS-a w NUT
- `UPS_HOST`: adres IP lub nazwa hosta maszyny, na której działa NUT

Następnie można uruchomić skrypt za pomocą polecenia: docker-compose up -d

## Konfiguracja mapowania IDX w Domoticz
Skrypt mapuje dane pobrane z UPS na konkretne indeksy urządzeń Domoticz za pomocą słownika idx_map (plik UPStoDomoticz.py). Klucze w tym słowniku odpowiadają typom danych pobranych z UPS, a wartości odpowiadają indeksom urządzeń w Domoticz.

Na przykład:
```
idx_map = {
    'battery_voltage': '208',
    'input_frequency': '209',
    'input_voltage': '215',
    'output_voltage': '210',
    'ups_load': '214',
    'ups_load_power': '212',
    'ups_status': '216'
}
```

W powyższym przykładzie dane dotyczące napięcia baterii pobrane z UPS zostaną zmapowane na indeks urządzenia 208 w Domoticz, i tak dalej dla innych typów danych.

Aby skonfigurować odpowiednie urządzenia w Domoticz, postępuj zgodnie z poniższymi krokami:

1. Otwórz interfejs sieciowy Domoticz i przejdź do zakładki "Konfiguracja".
2. Kliknij przycisk "Sprzęt" i wybierz "Wirtualny".
3. Nadaj wirtualnemu urządzeniu sprzętowemu nazwę, na przykład "Dane UPS".
4. Kliknij przycisk "Utwórz wirtualne czujniki" i wybierz "Niestandardowy czujnik".
5. Wpisz nazwę czujnika (np. "Napięcie baterii") i wybierz odpowiedni typ czujnika (np. "Napięcie (V)").
6. Wpisz numer indeksu urządzenia ze słownika idx_map dla wybranego typu danych (np. 208 dla napięcia baterii).
7. Powtórz kroki 4-6 dla każdego typu danych w słowniku idx_map.

Po skonfigurowaniu odpowiednich urządzeń w Domoticz można uruchomić skrypt, aby wysłać dane UPS do Domoticz.
