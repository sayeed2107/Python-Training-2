import numpy as np

def zet_score(ts: np.ndarray) -> np.ndarray:
    """Z-Score

    Args:
        ts (np.ndarray): _description_

    Returns:
        np.ndarray: _description_
    """
    ts_filtred: np.ndarray = ts.copy()
    n: int = len(ts_filtred)

    temp_avg: float = np.average(ts[:,1:])
    std: float = ts[:,1:].std()
    print(std)
    se_z: float = std / (n ** 0.5) # скобки для читабельности
    
    for i in range(n):
        ts_filtred[i][1] = float((ts_filtred[i][1] - temp_avg) / std)
    
    # TODO Заменить все что больше 3 и меньше -3 на nan, вернуть оригинальный вектор
    
    return ts_filtred
