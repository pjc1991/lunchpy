from lunchpy.stores import store_collector as store_collector
from lunchpy.stores.matzip_db import saveMatzip, loadMatzip, updateMatzip
from lunchpy.stores.matzip import Matzip

def test():
    updateMatzip(Matzip("test", 0, "test", 0))