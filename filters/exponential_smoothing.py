import numpy as np

def exp_smooth (ts: np.ndarray, a: float = 0.33) -> np.ndarray:
    """Экспоненциальное сглаживание

    Args:
        ts (np.ndarray): временной ряд, подлежащий фильтрации
        a (float, optional): коэффициент сглаживания - Defaults to 0.33.

    Returns:
        np.ndarray: светлый фильтрованный
    """
    ts_filtered: np.ndarray = ts.copy()
    k = 0

    for line in ts_filtered:
        temp: float = line[1]
        temp_smoothed: float = ts_filtered[k][1]
        next_temp: float = a * temp + (1 - a) * temp_smoothed

        try:
            ts_filtered[k + 1][1] = next_temp
            k += 1
        except:
            break

    return ts_filtered


