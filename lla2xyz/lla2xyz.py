import math

def compute_lla2xyz(lat, lon, alt):
    try:
        if not all(isinstance(val, (int, float)) for val in [lat, lon, alt]):
            raise TypeError("Invalid Type")
        
        if not (-math.pi/2 <= math.radians(lat) <= math.pi/2):
            raise ValueError("Invalid Value")
        
        if not (-math.pi <= math.radians(lon) <= math.pi):
            raise ValueError("Invalid Value")
        
        a = 6378137
        e = 0.08181919
        lat = math.radians(lat)
        lon = math.radians(lon)

        R = a/math.sqrt(1 - (math.pow(e, 2)*math.pow(math.sin(lat), 2)))

        X = (R+alt)*math.cos(lat)*math.cos(lon)
        Y = (R+alt)*math.cos(lat)*math.sin(lon)
        Z = (R*(1-math.pow(e, 2)) + alt)*math.sin(lat)
        return X, Y, Z
    
    except(TypeError, ValueError) as err:
        print(f"Input error: {err}")
        raise


if __name__ == "__main__":
    lat = float(input("Please enter a latitude value in degrees: "))
    lon = float(input("Please enter a longitude value in degrees: "))
    alt = float(input("Please enter a altitude value in meters: "))
    X, Y, Z = compute_lla2xyz(lat, lon, alt)
    print(f"The values of X, Y, Z are: \n X: {X} m \n Y: {Y} m \n Z: {Z} m")