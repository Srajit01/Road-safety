import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import time

LDR_THRESHOLD = 500
PIEZO_THRESHOLD = 100
MAX_DISTANCE = 200
ENERGY_CONVERSION_FACTOR = 0.05

bridge_sections = np.zeros(5)

def read_ldr():
    return np.random.randint(300, 700)

def read_piezo():
    return np.random.randint(0, 200)

def measure_distance():
    return np.random.randint(50, 300)

def handle_lighting(ldr_value):
    if ldr_value < LDR_THRESHOLD:
        print("Turning lights ON (Low ambient light)")
    else:
        print("Turning lights OFF (High ambient light)")

def monitor_pedestrian_activity(piezo_value, distance):
    if piezo_value > PIEZO_THRESHOLD:
        print("Foot pressure detected! Generating energy...")
        energy = piezo_value * ENERGY_CONVERSION_FACTOR
        print(f"Energy Generated: {energy:.2f} Joules")
        update_bridge_density(distance)

def handle_emergency(piezo_value):
    if piezo_value > PIEZO_THRESHOLD * 3:
        print("🚨 Emergency detected! Triggering alert...")

def update_bridge_density(distance):
    section_index = min(int(distance / (MAX_DISTANCE / len(bridge_sections))), len(bridge_sections) - 1)
    bridge_sections[section_index] += 1

ldr_values = []
piezo_values = []
distance_values = []

print("Smart Foot Over-Bridge System Simulation Starting...\n")
for _ in range(20):
    ldr_value = read_ldr()
    piezo_value = read_piezo()
    distance = measure_distance()

    ldr_values.append(ldr_value)
    piezo_values.append(piezo_value)
    distance_values.append(distance)

    handle_lighting(ldr_value)
    monitor_pedestrian_activity(piezo_value, distance)
    handle_emergency(piezo_value)

    print("-" * 40)
    time.sleep(0.5)

plt.figure(figsize=(14, 5))

plt.subplot(1, 3, 1)
plt.plot(ldr_values, marker='o', color='orange')
plt.title("LDR Sensor Values")
plt.xlabel("Time (cycles)")
plt.ylabel("LDR Value")

plt.subplot(1, 3, 2)
plt.plot(piezo_values, marker='o', color='green')
plt.title("Piezoelectric Sensor Values")
plt.xlabel("Time (cycles)")
plt.ylabel("Piezo Value")

plt.subplot(1, 3, 3)
plt.plot(distance_values, marker='o', color='blue')
plt.title("Ultrasonic Distance Measurements")
plt.xlabel("Time (cycles)")
plt.ylabel("Distance (cm)")

plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 4))
sns.heatmap([bridge_sections], annot=True, cmap="Blues", cbar=True, xticklabels=["Section 1", "Section 2", "Section 3", "Section 4", "Section 5"])
plt.title("Pedestrian Density on Bridge Sections")
plt.show()