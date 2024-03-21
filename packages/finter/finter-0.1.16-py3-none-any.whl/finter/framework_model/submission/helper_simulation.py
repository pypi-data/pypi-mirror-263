import json
from enum import Enum

import pandas as pd
from finter.framework_model.simulation import adj_stat_container_helper
from finter.framework_model.submission.config import DefaultBenchmark
from finter.settings import logger
from finter.utils.timer import timer


@timer
def run_simulation(model_info, start, end, **kwargs):
    """
    Runs a simulation based on the given model information and time range, applying additional specified settings.

    This function initializes the simulation with default parameters, which can be overridden by the kwargs argument. It processes the model statistics using the 'adj_stat_container_helper' function, then creates and returns a ModelStat object populated with the simulation results and any additional settings.

    Parameters:
    - model_info: An object containing model configuration information.
    - start (datetime): The start date of the simulation.
    - end (datetime): The end date of the simulation.
    - **kwargs: Optional keyword arguments to specify additional simulation settings. Default values are:
        - volcap_pct: 1 (Volume cap percentage),
        - decay: 1 (Decay factor for the model),
        - cost_list: ["hi_low", "fee_tax"] (List of transaction costs to consider),
        - slippage: 10 (Slippage in the model's transactions),
        - return_calc_method: "arithmetic" (Method for calculating returns),
        - turnover_calc_method: "diff" (Method for calculating turnover),
        - booksize: 1e8 (Size of the book in the simulation),
        - close: True (Whether to close the positions at the end of the simulation),
        - adj_dividend: False (Whether to adjust for dividends).

    Returns:
    - A ModelStat object containing the results of the simulation along with the settings used for the simulation.

    The 'kwargs' argument allows for flexible configuration of the simulation, accommodating various scenarios and model behaviors.
    """
    defaults = {
        "volcap_pct": 1,
        "decay": 1,
        "cost_list": ["hi_low", "fee_tax"],
        "slippage": 10,
        "return_calc_method": "arithmetic",
        "turnover_calc_method": "diff",
        "booksize": 1e8,
        "close": True,
        "adj_dividend": False,
    }

    for key, value in defaults.items():
        kwargs.setdefault(key, value)

    benchmark = kwargs.pop("benchmark", None)

    model_stat = adj_stat_container_helper(
        model_info=model_info, start=start, end=end, **kwargs
    )

    kwargs.pop("position", None)

    return ModelStat(model_stat, benchmark, **kwargs)


class ModelStat:
    class Frequency(Enum):
        WholePeriod = "WholePeriod"
        Yearly = "Yearly"
        HalfYearly = "HalfYearly"
        Quarterly = "Quarterly"
        Monthly = "Monthly"
        Weekly = "Weekly"
        Daily = "Daily"

    def __init__(self, model_stat, benchmark, **kwargs):
        """Initialize the ModelStat object with statistical data.

        Parameters:
        - statistics: A dictionary containing statistical data.
        """
        self.model_stat = model_stat
        self.benchmark = benchmark
        self.kwargs = kwargs

        if benchmark is not False:
            self.bm = DefaultBenchmark(self.benchmark).get_benchmark_df()

    def extract_statistics(self, frequency):
        """
        Extracts statistical data for a specified frequency and returns it as a pandas DataFrame.

        This method transforms model statistical data into a DataFrame based on the specified frequency. Valid frequencies are 'WholePeriod', 'Yearly', 'HalfYearly', 'Quarterly', 'Monthly', 'Weekly', and 'Daily'.

        Parameters:
        - frequency (str): The frequency of the statistical data to be extracted. Valid options are 'WholePeriod', 'Yearly', 'HalfYearly', 'Quarterly', 'Monthly', 'Weekly', 'Daily'.

        Returns:
        - pandas DataFrame: A DataFrame containing the statistical data for the specified frequency.

        Raises:
        - ValueError: If the specified frequency is not one of the valid options.
        """
        try:
            frequency = self.Frequency(frequency).value
        except ValueError:
            valid_options = ", ".join(
                [f"'{option.value}'" for option in self.Frequency]
            )
            raise ValueError(
                f"Frequency must be one of the following: {valid_options}. Please choose one."
            ) from None

        parsed_json = json.loads(self.model_stat["statistics"][frequency])

        df = pd.DataFrame(
            parsed_json["data"],
            columns=parsed_json["columns"],
            index=pd.to_datetime(parsed_json["index"]),
        )
        df.index = pd.to_datetime(df.index).date

        return df

    @property
    def whole_period(self):
        return self.extract_statistics("WholePeriod")

    @property
    def yearly(self):
        return self.extract_statistics("Yearly")

    @property
    def half_yearly(self):
        return self.extract_statistics("HalfYearly")

    @property
    def quarterly(self):
        return self.extract_statistics("Quarterly")

    @property
    def monthly(self):
        return self.extract_statistics("Monthly")

    @property
    def weekly(self):
        return self.extract_statistics("Weekly")

    @property
    def daily(self):
        return self.extract_statistics("Daily")

    @property
    def cummulative_return(self):
        cum_ret = pd.read_json(self.model_stat["cum_ret"], orient="records").set_index(
            "index"
        )["data"]
        cum_ret.index = pd.to_datetime(cum_ret.index).date

        if self.benchmark is False:
            cum_ret.columns = ["model"]
        else:
            logger.info(f"benchmark: {self.benchmark if self.benchmark else 'default'}")

            bm = self.bm.reindex(cum_ret.index)
            bm = bm.pct_change(fill_method=None).fillna(0)
            if self.kwargs["return_calc_method"] == "arithmetic":
                bm = bm.cumsum()
            else:
                bm = (1 + bm).cumprod() - 1
            cum_ret = pd.concat([cum_ret, bm], axis=1)
            cum_ret.columns = ["model", self.benchmark]
        return cum_ret

    @property
    def raw_return(self):
        if self.kwargs["return_calc_method"] == "arithmetic":
            raw_ret = self.cummulative_return.diff()
        else:
            raw_ret = (1 + self.cummulative_return).pct_change(fill_method=None)
        return raw_ret
