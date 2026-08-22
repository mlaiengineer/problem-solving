import pandas as pd
from typing import List


def getDataframeSize(players: pd.DataFrame) -> List[int]:
    return list(players.shape)


players = pd.DataFrame([
    [1, 2],
    [1, 2],
    [1, 2]
])

print(getDataframeSize(players))