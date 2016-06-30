#!/usr/bin/env python

import sys, os

def main():
  if len(sys.argv) < 3:
    print "Usage: replay_requests [ap_mac] [host_mac]"
  else:
    ap_mac = sys.argv[1]
    host_mac = sys.argv[2]
    os.system("aireplay-ng -3 -b "+ap_mac+" -h "+host_mac+" wlan1mon")

if __name__ == "__main__":
  main()
