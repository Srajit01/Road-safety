import time
import random

def adjust_ebike_speed(desired_speed_kmh: float) -> float:
    """
    Adjusts e-bike speed based on a fixed maximum speed.
    """
    max_speed_kmh = 30.0
    adjusted_speed = min(desired_speed_kmh, max_speed_kmh)
    return adjusted_speed

def camera_check() -> bool:
    """
    Simulates camera detection of potential overtaking situations
    with a fixed probability.
    """
    time.sleep(0.1)
    return random.choice([True, False])

def detect_overtake(is_overtaking: bool) -> bool:
    """
    Simulates overtake detection and prevents overtaking if necessary.
    """
    if is_overtaking:
        print("Overtaking detected. Slowing down for safety.")
        return False
    else:
        return True

if __name__ == "__main__":
    print("E-bike Speed Control System (Fixed Rules)")

    # E-bike desired speed:
    ebike_desired_speed = float(input("Enter desired e-bike speed (km/hr): ").strip())

    # Adjust e-bike speed:
    regulated_ebike_speed = adjust_ebike_speed(ebike_desired_speed)
    print(f"E-bike speed adjusted to: {regulated_ebike_speed:.2f} km/hr")

    # Overtake Prevention:
    is_overtaking = camera_check()
    can_overtake = detect_overtake(is_overtaking)

    if not can_overtake:
        print("Overtaking not allowed at the moment.")

    print("System is now running in safe and controlled mode.")