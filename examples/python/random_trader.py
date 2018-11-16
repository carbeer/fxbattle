#!/usr/bin/env python3

"""
  API-Key: 2F4524
  Endpoint: https://epfl.fxbattle.uk

  Example random trader

  usage random_trader.py --endpoint 'http://localhost:8080' --apikey 'api_key1' --timeout '1000'
"""
import argparse
from fxbattleclient import FxClient, FxClientError
from time import sleep
import time
import random
import tools
import numpy as np

parser = argparse.ArgumentParser(description='Example random trader')
parser.add_argument('--endpoint',
                    default='http://localhost:8080',
                    help='the api endpoint')
parser.add_argument('--apikey',
                    default='api_key1',
                    help='the api key')
parser.add_argument('--timeout', type=int,
                    default=1000,
                    help='affects the speed of the trader')

args = parser.parse_args()

print("Random Trader", "endpoint:", args.endpoint, "apikey:", args.apikey)
client = FxClient(args.endpoint, args.apikey)
timeout = args.timeout

GBPCHFbid = []
GBPCHFsel = []
EURGBPbid = []
EURGBPsel = []
EURCHFbid = []
EURCHFsel = []
USDCHFbid = []
USDCHFsel = []
EURUSDbid = []
EURUSDsel = []
GBPUSDbid = []
GBPUSDsel = []

asks = (GBPCHFsel, EURGBPsel, EURCHFsel, USDCHFsel, EURUSDsel, GBPUSDsel)
bids = (GBPCHFbid, EURGBPbid, EURCHFbid, USDCHFbid, EURUSDbid, GBPUSDbid)
smallMovingAvgs = defaultdict(list)
largeMovingAvgs = defaultdict(list) 

try:
  while True:
    timeNow = time.time()
    account = client.account()
    marketnow = client.market()

    if "error" in account:
        print("could not get account details", account["error"])  
        continue
  
    print("account", account)      


    # in the while loop:
    np.append(GBPCHFbid, [float(marketnow['GBPCHF'].split(' ')[1])])
    np.append(GBPCHFsel, [float(marketnow['GBPCHF'].split(' ')[2])])

    np.append(EURGBPbid, [float(marketnow['EURGBP'].split(' ')[1])])
    np.append(EURGBPsel, [float(marketnow['EURGBP'].split(' ')[2])])

    np.append(EURCHFbid, [float(marketnow['EURCHF'].split(' ')[1])])
    np.append(EURCHFsel, [float(marketnow['EURCHF'].split(' ')[2])])

    np.append(USDCHFbid, [float(marketnow['USDCHF'].split(' ')[1])])
    np.append(USDCHFsel, [float(marketnow['USDCHF'].split(' ')[2])])

    np.append(EURUSDbid, [float(marketnow['EURUSD'].split(' ')[1])])
    np.append(EURUSDsel, [float(marketnow['EURUSD'].split(' ')[2])])

    np.append(GBPUSDbid, [float(marketnow['GBPUSD'].split(' ')[1])])
    np.append(GBPUSDsel, [float(marketnow['GBPUSD'].split(' ')[2])])

    for ask in asks:

        largeMovingAvgs[ask].append(tools.getMovingAverage(ask, 15))
        smallMovingAvgs[ask].append(tools.getMovingAverage(ask, 10))

    for bid in bids:
        largeMovingAvgs[bid].append(tools.getMovingAverage(bid, 15))
        smallMovingAvgs[bid].append(tools.getMovingAverage(bid, 10))

      
    print(tools.getMovingAverage(USDCHFbid, 100))
    print(time.time() - timeNow)

except(FxClientError):
    print("error contacting the endpoint")
except(KeyboardInterrupt):
    print()
    print("final holdings", client.account())

""" if "USD" in account and account["USD"] > 1:
          account = client.sell("USDGBP", account["USD"])
      elif "GBP" in account and account["GBP"] > 1:
          account = client.sell("GBPUSD", account["GBP"])
      elif "EUR" in account and account["EUR"] > 1:
          account = client.sell("EURGBP", account["EUR"])
      elif "CHF" in account and account["CHF"] > 1:
          account = client.sell("CHFGBP", account["CHF"])
      else:
          print("you're broke!")

      if "error" in account:
          print("failed to sell", account["error"])
       """