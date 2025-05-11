import numpy as np
import math

def compute_RM(theta):

    try:
        if not isinstance(theta, (int, float)):
            raise TypeError("Invalid value for theta")
        
        if math.isnan(theta) or math.isinf(theta):
            raise ValueError("Theta should be a finite number")
        
        theta = math.radians(theta)
        RM = np.array([[math.cos(theta), math.sin(theta)],
                    [-math.sin(theta), math.cos(theta)]])
        return RM
    
    except(TypeError, ValueError) as err:
        print(f"Input error: {err}")
        raise

if __name__ == "__main__":
    theta = float(input("Please enter a value of theta in degrees: "))
    RM = compute_RM(theta)
    print(f"The rotation matrix is: {RM}")