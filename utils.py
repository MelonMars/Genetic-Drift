import numpy as np

colors = [(0,0,255),(0,255,0),(255,0,0)]


def calculate_closeness(color_map:np.ndarray) -> float:
    distances = np.sqrt(np.sum((color_map[:, np.newaxis] - color_map) ** 2, axis=-1))
    avg_distance = np.mean(distances)
    if np.max(distances) != 0:
        return 1.0 - (avg_distance / np.max(distances))
    else:
        return 1