import numpy as np

def descriptive_statistics(data: list | np.ndarray) -> dict:
    """
    Calculate various descriptive statistics metrics for a given dataset.
    
    Args:
        data: List or numpy array of numerical values
    
    Returns:
        Dictionary containing mean, median, mode, variance, standard deviation,
        percentiles (25th, 50th, 75th), and interquartile range (IQR)
    """
    data = np.asarray(data, dtype=float)

    if data.size == 0:
        raise ValueError("Data cannot be empty.")

    # Calculate mode
    values, counts = np.unique(data, return_counts=True)
    mode = values[np.argmax(counts)].item()

    # Calculate percentiles
    percentile_25 = np.percentile(data, 25)
    percentile_50 = np.percentile(data, 50)
    percentile_75 = np.percentile(data, 75)

    return {
        "mean": float(np.mean(data)),
        "median": float(np.median(data)),
        "mode": mode,
        "variance": float(np.var(data)),
        "standard_deviation": float(np.std(data)),
        "25th_percentile": float(percentile_25),
        "50th_percentile": float(percentile_50),
        "75th_percentile": float(percentile_75),
        "interquartile_range": float(percentile_75 - percentile_25)
    }