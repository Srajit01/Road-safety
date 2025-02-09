def predict_pedestrian_speed(
        gender: str,
        age_group: str,
        mobile_use: bool,
        luggage: bool,
        group_size: int,
        pedestrian_density: float
    ) -> float:
    base_speed = 58.8
    gender_coefficient = -3.5 if gender.lower() == 'female' else 0
    age_coefficients = {'11-20': 0, '21-40': 0, '>=60': -15.0}
    age_coefficient = age_coefficients.get(age_group, 0)
    mobile_coefficient = -13.063 if mobile_use else 0
    luggage_coefficient = 15.3 if not luggage else 0
    group_coefficient = -16.3 if group_size == 2 else 0
    density_coefficient = -14.9 if pedestrian_density >= 0.51 else 0
    predicted_speed = (base_speed + gender_coefficient + age_coefficient +
                       mobile_coefficient + luggage_coefficient +
                       group_coefficient + density_coefficient)

    return predicted_speed

if __name__ == "__main__":
    print("Pedestrian Speed Prediction Tool")
    gender = input("Enter gender (male/female): ").strip().lower()
    age_group = input("Enter age group (11-20, 21-40, >=60): ").strip()
    mobile_use = input("Using mobile? (yes/no): ").strip().lower() == 'yes'
    luggage = input("Carrying luggage? (yes/no): ").strip().lower() == 'no'
    group_size = int(input("Enter group size (1 or 2): ").strip())
    pedestrian_density = float(input("Enter pedestrian density (ped/m^2): ").strip())

    speed = predict_pedestrian_speed(
        gender, age_group, mobile_use, luggage, group_size, pedestrian_density
    )

    print(f"Predicted pedestrian speed: {speed:.2f} m/min")