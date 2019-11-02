#!/usr/bin/python
import numpy as np
import pandas as pd
## Create date
# Days
dates_d = pd.date_range('20300101', periods=6, freq='D')
print('Day:', dates_d)
