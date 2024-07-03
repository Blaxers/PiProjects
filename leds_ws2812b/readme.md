# install on default Raspian desktop enviroment
1. upgrade enviroment
```
apt update && apt upgrade -y
```
2. install packages
```
sudo pip3 install rpi_ws281x adafruit-circuitpython-neopixel --break-system-packages
```
3. add execute to file 
```
chmod +x ./*
```
4. add service to run script on start os
```
sudo cp light_control.service /etc/systemd/system/ && sudo chmod 644 /etc/systemd/system/light_control.service && sudo systemctl daemon-reload && sudo systemctl enable light_control.service && sudo systemctl start light_control.service && sudo systemctl status light_control.service
```