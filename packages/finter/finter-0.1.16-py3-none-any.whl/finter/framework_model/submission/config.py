from enum import Enum
from finter.data import ModelData


class ModelTypeConfig(Enum):
    ALPHA = {"class_name": "Alpha", "file_name": "am.py"}
    PORTFOLIO = {"class_name": "Portfolio", "file_name": "pf.py"}

    @property
    def class_name(self):
        return self.value["class_name"]

    @property
    def file_name(self):
        return self.value["file_name"]

    @classmethod
    def available_options(cls):
        return ", ".join([item.name for item in cls])


class DefaultBenchmark(Enum):
    KOSPI = "KOSPI"
    KOSDAQ = "KOSDAQ"

    @classmethod
    def available_options(cls):
        return [item.name for item in cls]
    
    def get_benchmark_df(self):
        df = ModelData.load("content.fnguide.ftp.economy.index_close.1d")
        return df[self.value]

class ModelUniverseConfig(Enum):
    KR_STOCK = {"benchmark": DefaultBenchmark.KOSPI.value}

    def get_config(self, model_type: ModelTypeConfig):
        if self == ModelUniverseConfig.KR_STOCK:
            return {
                "exchange": "krx",
                "universe": "krx",
                "instrument_type": "stock",
                "freq": "1d",
                "position_type": "target",
                "type": model_type.name.lower(),
                "exposure": "long_only",
            }
        else:
            raise ValueError(f"Unknown universe: {self}")

    def get_benchmark(self, benchmark):
        if benchmark is None:
            return self.value["benchmark"]
        else:
            return benchmark

    @classmethod
    def available_options(cls):
        return ", ".join([item.name for item in cls])
