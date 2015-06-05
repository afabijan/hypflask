import pandas as pd
import numpy as np

def process():
    d = pd.read_csv("data/unsucc.csv", index_col=0, parse_dates=True)
    newD = pd.concat({"f_on": d["unsuccPacketSwitchingPagingUmts"]["2014-01-5":"2014-01-10"],
           "f_off": d["unsuccPacketSwitchingPagingUmts"]["2014-01-11":"2014-01-15"]}, axis=1).fillna(0)
    return newD.to_json()