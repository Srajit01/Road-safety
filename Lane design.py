import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

pedestrian_lane_width = 1.8
cyclist_lane_width = 2.5
twowheeler_lane_width = 3.0
barrier_height = 1.2

pedestrian_surface_friction = 0.6
cyclist_surface_friction = 0.5

drainage_slope = 1.5 / 100

pedestrian_load = 0.5
cyclist_load = 0.75
twowheeler_load = 2.0

def compute_total_load(widths, loads):
    return sum(w * l for w, l in zip(widths, loads))

lane_widths = [pedestrian_lane_width, cyclist_lane_width, twowheeler_lane_width]
lane_loads = [pedestrian_load, cyclist_load, twowheeler_load]
total_load = compute_total_load(lane_widths, lane_loads)

fig, ax = plt.subplots(figsize=(12, 6))

ax.add_patch(plt.Rectangle((0, 0), pedestrian_lane_width, 3, color='lightgreen', label='Pedestrian Lane (Friction: 0.6)'))
ax.add_patch(plt.Rectangle((pedestrian_lane_width, 0), cyclist_lane_width, 3, color='lightblue', label='Cyclist Lane (Friction: 0.5)'))
ax.add_patch(plt.Rectangle((pedestrian_lane_width + cyclist_lane_width, 0), twowheeler_lane_width, 3, color='lightcoral', label='Two-Wheeler Lane'))

ax.plot([pedestrian_lane_width, pedestrian_lane_width], [0, barrier_height], color='black', linewidth=2, label='Barrier (Height: 1.2m)')
ax.plot([pedestrian_lane_width + cyclist_lane_width, pedestrian_lane_width + cyclist_lane_width], [0, barrier_height], color='black', linewidth=2)

ax.plot([0, pedestrian_lane_width + cyclist_lane_width + twowheeler_lane_width], [0, (pedestrian_lane_width + cyclist_lane_width + twowheeler_lane_width) * drainage_slope], color='blue', linestyle='dashed', label='Drainage Slope (1.5%)')

ax.set_xlim(0, pedestrian_lane_width + cyclist_lane_width + twowheeler_lane_width)
ax.set_ylim(0, 3)
ax.set_xlabel("Lane Width (meters)")
ax.set_ylabel("Height (meters)")
ax.set_title("Cross-Section of Lanes with Barriers and Drainage Slope")
ax.legend()

plt.show()

ramp_length = np.linspace(0, 12, 100)
max_ramp_gradient_ratio = 1 / 12
steep_ramp_gradient_ratio = 1 / 8

ramp_height_accessible = ramp_length * max_ramp_gradient_ratio
ramp_height_steep = ramp_length * steep_ramp_gradient_ratio

fig = go.Figure()
fig.add_trace(go.Scatter(x=ramp_length, y=ramp_height_accessible, mode='lines', name='Ramp Gradient (1:12, Accessible)'))
fig.add_trace(go.Scatter(x=ramp_length, y=ramp_height_steep, mode='lines', name='Ramp Gradient (1:8, Steep)'))

fig.update_layout(
    title="Ramp Gradient Visualization",
    xaxis_title="Ramp Length (meters)",
    yaxis_title="Ramp Height (meters)",
    legend_title="Ramp Types"
)

fig.show()

print("Surface friction coefficients are set to ensure slip resistance for pedestrians (0.6) and cyclists (0.5).")
print("Drainage slope designed at 1.5% to prevent water accumulation.")
print("Barrier height maintained at 1.2 meters for user protection.")
print(f"Total load capacity requirement calculated as {total_load:.2f} kN/m.")

print("Design visualization complete. Modify parameters as needed.")