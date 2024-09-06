import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    l = []
    s = players.shape
    for x in s:
        l.append(x)
    return l
