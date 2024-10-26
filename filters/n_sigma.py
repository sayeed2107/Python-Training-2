import numpy as np


def nsigma(ts: np.ndarray, n: int = 3) -> np.ndarray:
    """Фильтр по N сигма

    Args:
        ts (np.ndarray): временной ряд, подлежащий фильтрации

    Returns:
        np.ndarray: светлый фильтрованный
    """
    ts_filtered: np.ndarray = ts.copy()
    values: np.ndarray = ts_filtered[:,1]

    mean: float = values.mean()
    sigma = (((values - mean)**2).mean())**.5
    
    upper_edge = mean + n* sigma
    lower_edge = mean - n* sigma

    condition = ((ts_filtered[:,1] >= lower_edge) & (ts_filtered[:,1] <= upper_edge))

    ts_filtered[~condition, 1] = np.nan

    return ts_filtered
