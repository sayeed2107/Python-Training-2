import numpy as np

from filters.n_sigma import nsigma
from filters.exponential_smoothing import exp_smooth
from filters.double_exponential_smoothing import exp2_smooth
from filters.time_averaging import time_avg
from filters.z_score import zet_score

# выгружаем данные
arr: np.ndarray = np.loadtxt("data/MLTempDataset1.csv", delimiter=",", dtype=object) 

# приводим к нужнему формату
ts: np.ndarray = arr[1:,1:] 
ts[:,1:] = ts[:,1:].astype(float)

# Фильтр "правило трех\n сигм"
ts_nsigma: np.ndarray = nsigma(ts, 3)

# Фильтр "экспоненциальное сглаживание"
ts_exp: np.ndarray = exp_smooth(ts)

# Фильтр "двойное экспоненциальное сглаживание"
ts_exp2: np.ndarray = exp2_smooth(ts)

# Фильтр "временное усреднение"
ts_time_avg: np.ndarray = time_avg(ts, window=3)

# Фильтр "z-score"
ts_z_score: np.ndarray = zet_score(ts)





