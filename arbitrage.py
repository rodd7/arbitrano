from collections import defaultdict

def findArbitrage(data):
    finalresult = defaultdict(list)
    count = 0
    for k, v in data.items():
        if (count % 2 == 0):
            max(list(map(int, v)))
