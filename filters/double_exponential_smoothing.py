import numpy as np

def exp2_smooth (ts: np.ndarray, a: float = 0.33, b: float = 0.33) -> np.ndarray:
    """Двойное экспоненциальное сглаживание

    Args:
        ts (np.ndarray): временной ряд, подлежащий фильтрации
        a (float, optional): коэффициент сглаживания - Defaults to 0.33.
        b (float, optional): кэффициент сглаживания тренда - Defaults to 0.33.

    Returns:
        np.ndarray: светлый фильтрованный
    """
    ts_filtered: np.ndarray = ts.copy()
    trend_arr: np.ndarray = ts.copy()
    trend_arr[0][1] = trend_arr[1][1] - trend_arr[0][1]
    k = 0

    for line in ts_filtered:
        temp: float = line[1]
        temp_smoothed: float = ts_filtered[k][1]
        trend_val: float = trend_arr[k][1]

        next_temp = a * temp + (1 - a) * (temp_smoothed + trend_val)
        next_trend = b * (next_temp - temp_smoothed) + (1 - b) * trend_val

        
        try:
            ts_filtered[k + 1][1] = next_temp
            trend_arr[k + 1][1] = next_trend
            k += 1
        except:
            break

    return ts_filtered