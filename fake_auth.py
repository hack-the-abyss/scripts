#!/usr/bin/env python

import sys, os

def main():
  if len(sys.argv) < 4:
    "Usage: fake_auth [essid] [ap_mac] [host_mac]"
  else:
    essid = sys.argv[1]
    ap_mac = sys.argv[2]
    host_mac = sys.argv[3]
    os.system("aireplay-ng -1 0 -e "+essid+" -a "+ap_mac+" -h "+host_mac+" wlan1mon")

if __name__ == "__main__":
  main()
