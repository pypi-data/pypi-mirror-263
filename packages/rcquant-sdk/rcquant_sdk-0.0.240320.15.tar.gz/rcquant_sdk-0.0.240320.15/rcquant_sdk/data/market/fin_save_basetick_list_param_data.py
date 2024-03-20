from typing import List
from ...interface import IData
from ...packer.market.fin_save_basetick_list_param_data_packer import FinSaveBaseTickListParamDataPacker


class FinSaveBaseTickListParamData(IData):
    _PreClosePrice: float = -1.0

    def __init__(self, exchange_id: str = '', instrument_id: str = '', action_day_list: List[str] = [], action_time_list: List[str] = [],
                 update_mill_sec_list: List[int] = [], last_price_list: List[float] = [], last_volume_list: List[int] = [],
                 bid_price_list: List[float] = [], bid_volume_list: List[int] = [], ask_price_list: List[float] = [], ask_volume_list: List[int] = [],
                 total_turnover_list: List[float] = [], total_volume_list: List[int] = [], open_interest_list: List[float] = [],
                 pre_close_price: float = -1.0, pre_settlement_price: float = -1.0, pre_open_interest: float = -1.0, base_path: str = '',
                 ):
        super().__init__(FinSaveBaseTickListParamDataPacker(self))
        self._ExchangeID: str = exchange_id
        self._InstrumentID: str = instrument_id
        self._ActionDayList: List[str] = action_day_list
        self._ActionTimeList: List[str] = action_time_list
        self._UpdateMillSecList: List[int] = update_mill_sec_list
        self._LastPriceList: List[float] = last_price_list
        self._LastVolumeList: List[int] = last_volume_list
        self._BidPriceList: List[float] = bid_price_list
        self._BidVolumeList: List[int] = bid_volume_list
        self._AskPriceList: List[float] = ask_price_list
        self._AskVolumeList: List[int] = ask_volume_list
        self._TotalTurnoverList: List[float] = total_turnover_list
        self._TotalVolumeList: List[int] = total_volume_list
        self._OpenInterestList: List[float] = open_interest_list
        self._PreClosePrice: float = float(pre_close_price)
        self._PreSettlementPrice: float = float(pre_settlement_price)
        self._PreOpenInterest: float = float(pre_open_interest)
        self._BasePath: str = base_path

    @property
    def ExchangeID(self):
        return self._ExchangeID

    @ExchangeID.setter
    def ExchangeID(self, value: str):
        self._ExchangeID = value

    @property
    def InstrumentID(self):
        return self._InstrumentID

    @InstrumentID.setter
    def InstrumentID(self, value: str):
        self._InstrumentID = value

    @property
    def ActionDayList(self):
        return self._ActionDayList

    @ActionDayList.setter
    def ActionDay(self, value: List[str]):
        self._ActionDayList = value

    @property
    def ActionTimeList(self):
        return self._ActionTimeList

    @ActionTimeList.setter
    def ActionTimeList(self, value: List[str]):
        self._ActionTimeList = value

    @property
    def UpdateMillSecList(self):
        return self._UpdateMillSecList

    @UpdateMillSecList.setter
    def UpdateMillSecList(self, value: List[int]):
        self._UpdateMillSecList = value

    @property
    def LastPriceList(self):
        return self._LastPriceList

    @LastPriceList.setter
    def LastPriceList(self, value: List[float]):
        self._LastPriceList = value

    @property
    def LastVolumeList(self):
        return self._LastVolumeList

    @LastVolumeList.setter
    def LastVolumeList(self, value: List[int]):
        self._LastVolumeList = value

    @property
    def BidPriceList(self):
        return self._BidPriceList

    @BidPriceList.setter
    def BidPriceList(self, value: List[float]):
        self._BidPriceList = value

    @property
    def BidVolumeList(self):
        return self._BidVolumeList

    @BidVolumeList.setter
    def BidVolumeList(self, value: List[int]):
        self._BidVolumeList = value

    @property
    def AskPriceList(self):
        return self._AskPriceList

    @AskPriceList.setter
    def AskPriceList(self, value: List[float]):
        self._AskPriceList = value

    @property
    def AskVolumeList(self):
        return self._AskVolumeList

    @AskVolumeList.setter
    def AskVolumeList(self, value: List[int]):
        self._AskVolumeList = value

    @property
    def TotalTurnoverList(self):
        return self._TotalTurnoverList

    @TotalTurnoverList.setter
    def TotalTurnoverList(self, value: List[float]):
        self._TotalTurnoverList = value

    @property
    def TotalVolumeList(self):
        return self._TotalVolumeList

    @TotalVolumeList.setter
    def TotalVolumeList(self, value: List[int]):
        self._TotalVolumeList = value

    @property
    def OpenInterestList(self):
        return self._OpenInterestList

    @OpenInterestList.setter
    def OpenInterestList(self, value: List[float]):
        self._OpenInterestList = value

    @property
    def PreClosePrice(self):
        return self._PreClosePrice

    @PreClosePrice.setter
    def PreClosePrice(self, value: float):
        self._PreClosePrice = value

    @property
    def PreSettlementPrice(self):
        return self._PreSettlementPrice

    @PreSettlementPrice.setter
    def PreSettlementPrice(self, value: float):
        self._PreSettlementPrice = value

    @property
    def PreOpenInterest(self):
        return self._PreOpenInterest

    @PreOpenInterest.setter
    def PreOpenInterest(self, value: float):
        self._PreOpenInterest = value

    @property
    def BasePath(self):
        return self._BasePath

    @BasePath.setter
    def BasePath(self, value: str):
        self._BasePath = value
