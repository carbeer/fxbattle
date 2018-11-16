account = client.account()
marketnow = client.market()

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

# in the while loop:
GBPCHFbid.append(float(marketnow['GBPCHF'].split(' ')[1]))
GBPCHFsel.append(float(marketnow['GBPCHF'].split(' ')[2]))

EURGBPbid.append(float(marketnow['EURGBP'].split(' ')[1]))
EURGBPsel.append(float(marketnow['EURGBP'].split(' ')[2]))

EURCHFbid.append(float(marketnow['EURCHF'].split(' ')[1]))
EURCHFsel.append(float(marketnow['EURCHF'].split(' ')[2]))

USDCHFbid.append(float(marketnow['USDCHF'].split(' ')[1]))
USDCHFsel.append(float(marketnow['USDCHF'].split(' ')[2]))

EURUSDbid.append(float(marketnow['EURUSD'].split(' ')[1]))
EURUSDsel.append(float(marketnow['EURUSD'].split(' ')[2]))

GBPUSDbid.append(float(marketnow['GBPUSD'].split(' ')[1]))
GBPUSDsel.append(float(marketnow['GBPUSD'].split(' ')[2]))