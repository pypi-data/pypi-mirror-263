from ...interface import IPacker


class FinSaveBaseTickListParamDataPacker(IPacker):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    def obj_to_tuple(self):
        ret = [str(self._obj.ExchangeID),
               str(self._obj.InstrumentID),
               list(self._obj.ActionDayList),
               list(self._obj.ActionTimeList),
               list(self._obj.UpdateMillSecList),
               list(self._obj.LastPriceList),
               list(self._obj.LastVolumeList),
               list(self._obj.BidPriceList),
               list(self._obj.BidVolumeList),
               list(self._obj.AskPriceList),
               list(self._obj.AskVolumeList),
               list(self._obj.TotalTurnoverList),
               list(self._obj.TotalVolumeList),
               list(self._obj.OpenInterestList),
               float(self._obj.PreClosePrice),
               float(self._obj.PreSettlementPrice),
               float(self._obj.PreOpenInterest),
               str(self._obj.BasePath)]
        return ret

    def tuple_to_obj(self, t):
        if len(t) >= 18:
            self._obj.ExchangeID = t[0]
            self._obj.InstrumentID = t[1]
            self._obj.ActionDayList = t[2]
            self._obj.ActionTimeList = t[3]
            self._obj.UpdateMillSecList = t[4]
            self._obj.LastPriceList = t[5]
            self._obj.LastVolumeList = t[6]
            self._obj.BidPriceList = t[7]
            self._obj.BidVolumeList = t[8]
            self._obj.AskPriceList = t[9]
            self._obj.AskVolumeList = t[10]
            self._obj.TotalTurnoverList = t[11]
            self._obj.TotalVolumeList = t[12]
            self._obj.OpenInterestList = t[13]
            self._obj.PreClosePrice = t[14]
            self._obj.PreSettlementPrice = t[15]
            self._obj.PreOpenInterest = t[16]
            self._obj.BasePath = t[17]
            return True
        return False
