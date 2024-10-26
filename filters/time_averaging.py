import numpy as np

def time_avg (ts: np.ndarray, window: int = 5) -> np.ndarray:
    """Временное усреднение

    Args:
        ts (np.ndarray): временной ряд подлежащий фильтрации
        window (float): интервал времени в часах для усреднения

    Returns:
        np.ndarray: светлое фильтрованное
    """
    ts_filtered: np.ndarray = np.array(ts[0])
    k = 1
    while (True):
        try:
            ts_filtered: np.ndarray = np.vstack((ts_filtered, ts[k * window]))
            k += 1
        except IndexError:
            break
    
    return ts_filtered
