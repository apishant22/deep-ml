import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
    """
	Calculate the magnitude and direction of a gradient vector.
	
	Args:
		gradient: A list representing the gradient vector
	
	Returns:
		Dictionary containing:
		- magnitude: The L2 norm of the gradient
		- direction: Unit vector in direction of steepest ascent
		- descent_direction: Unit vector in direction of steepest descent
    """
    mag = np.linalg.norm(gradient)

    if mag == 0:
        direction = np.zeros(len(gradient))
    else:
        direction = np.array(gradient) / mag
    descent_direction = -direction

    return {
        "magnitude": mag,
        "direction": direction,
        "descent_direction": descent_direction
    }