#!/usr/bin/env python3

"""
  Arbitrage trader

  usage arbitrage_trader.py --endpoint 'http://localhost:8080' --apikey 'api_key1' --timeout '1000'
"""
import argparse
from collections import defaultdict
from fxbattleclient import FxClient, FxClientError
from time import sleep
import time
import random
import tools
from itertools import permutations, combinations

# Get right ordering to fetch market course according to API
def getCourse(a, b):
    if a == "CHF":
        return 1 / float(marketnow[b+a].split(' ')[1])
    elif a == "EUR":
        return float(marketnow[a+b].split(' ')[1])
    elif a == "GBP":
        if b == "EUR":
            return 1 / float(marketnow[b+a].split(' ')[1])
        else:
            return float(marketnow[a+b].split(' ')[1])
    elif a == "USD":
        if b == "CHF":
            return float(marketnow[a+b].split(' ')[1])
        else:
            return 1 / float(marketnow[b+a].split(' ')[1])


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

print("Arbitrage Trader", "endpoint:", args.endpoint, "apikey:", args.apikey)
client = FxClient(args.endpoint, args.apikey)
timeout = args.timeout

try:
  while True:
    timeNow = time.time()
    account = client.account()
    marketnow = client.market()

    if "error" in account:
        print("could not get account details", account["error"])  
        continue
  
    print("account", account)      
    currencies = ("CHF", "EUR", "USD")

    # Check for possible arbitrage options
    for permutation in list(permutations(currencies)):
        combins = list(combinations(permutation, 2))
        for comb in combins:
            if getCourse("GBP", comb[0]) * getCourse(comb[0], comb[1]) * getCourse(comb[1], "GBP") > 1.01:  
                client.sell("GBP" + comb[0], account["GBP"])
                client.sell(comb[0] + comb[1], account[comb[0]])
                client.sell(comb[1] + "GBP", account[comb[1]])
                break

        comb = permutation
        if getCourse("GBP", permutation[0]) * getCourse(permutation[0], permutation[1]) * getCourse(permutation[1], permutation[2]) * getCourse(permutation[2], "GBP") > 1.01:
            client.sell("GBP" + comb[0], account["GBP"])
            client.sell(comb[0] + comb[1], account[comb[0]])
            client.sell(comb[1] + comb[2], account[comb[1]])
            client.sell(comb[2] + "GBP", account[comb[2]])
            break

except(FxClientError):
    print("error contacting the endpoint")
except(KeyboardInterrupt):
    print()
    print("final holdings", client.account())
