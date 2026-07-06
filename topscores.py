import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from api import get_topscorers

(topscorers, ) = get_topscorers()
print(topscorers)

