#!/bin/bash
airmon-ng start wlan1
wait
ifconfig wlan1mon down
wait
macchanger -A wlan1mon
wait
ifconfig wlan1mon up
