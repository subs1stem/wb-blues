#!/bin/bash
apt install gcc libffi-dev libssl-dev python3-dev python3-venv libbluetooth-dev

echo 'Creating service...'
cp -u -r service/wb-blues.service /etc/systemd/system/
systemctl daemon-reload
systemctl enable wb-blues.service

cp -u -r source /mnt/data/etc/wb-blues && cd /mnt/data/etc/wb-blues || exit

echo 'Installing venv...'
python3 -m venv venv
source venv/bin/activate

echo 'Installing requirements...'
pip install -r requirements.txt
deactivate

echo '--------------------------------------------------------------------'
echo 'Done. Edit the settings.py file at the path /mnt/data/etc/wb-blues.'
echo 'Use "systemctl start wb-blues.service" for running module.'
