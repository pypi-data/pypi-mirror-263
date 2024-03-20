import logging
import time
import warnings

from .__version__ import (
    __title__,
    __description__,
    __url__,
    __version__,
)

from .time_series import TimeSeries
from .forecasting import Forecasting
from .authentication import DirectLicense, AzureKeyVaultLicense
from .auto_forecasting import AutoForecasting

warnings.simplefilter("ignore")
logging.basicConfig(
    level=logging.DEBUG,
    format='{"logtimestamp":"%(asctime)s.%(msecs)03dZ","level":"%(levelname)s","msg":"%(message)s","module":"%(module)s:%(funcName)s:%(lineno)d"}',
    datefmt="%Y-%m-%dT%H:%M:%S"
)
logging.Formatter.converter = time.gmtime
