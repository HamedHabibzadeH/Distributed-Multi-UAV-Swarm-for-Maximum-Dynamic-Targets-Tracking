import math
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge

from drone import Drone
from target import Target
from camera import relative_angle, is_in_fov


# Simulation parameters
dt = 0.1
total_time = 20
steps = int(total_time / dt)

omega1 = 0
omega2 = math.pi / 8


# Create drones
drone1 = Drone(10, 20, 0, 3)
drone2 = Drone(30, 40, math.pi / 2, 3)


# Create ground targets
target1 = Target(40, 50)
target2 = Target(70, 30)


# Store initial positions
x1_history = [drone1.x]
y1_history = [drone1.y]

x2_history = [drone2.x]
y2_history = [drone2.y]


# Run simulation
for k in range(steps):

    drone1.step(omega1, dt)
    drone2.step(omega2, dt)

    x1_history.append(drone1.x)
    y1_history.append(drone1.y)

    x2_history.append(drone2.x)
    y2_history.append(drone2.y)


# Check simulation results
print("Simulation steps:", steps)
print("UAV 1 samples:", len(x1_history))
print("UAV 2 samples:", len(x2_history))


# Camera geometry test
test_drone = Drone(0, 0, 0, 3)

test_targets = [
    Target(10, 0),
    Target(10, 10),
    Target(40, 0)
]

for i, target in enumerate(test_targets, start=1):
    angle = relative_angle(test_drone, target)
    visible = is_in_fov(test_drone, target)

    print(
        f"Test target {i}: "
        f"angle={math.degrees(angle):.1f} deg, "
        f"in_fov={visible}"
    )


# Plot drone trajectories
fig, axes = plt.subplots(1, 2, figsize=(13, 6))

ax1 = axes[0]

ax1.plot(x1_history, y1_history, label="UAV 1")
ax1.plot(x2_history, y2_history, label="UAV 2")

ax1.scatter(
    [target1.x, target2.x],
    [target1.y, target2.y],
    color="red",
    marker="x",
    s=100,
    label="Ground Targets"
)

ax1.set_title("Multi-UAV Trajectories")
ax1.set_xlabel("X Position (m)")
ax1.set_ylabel("Y Position (m)")
ax1.axis("equal")
ax1.grid(True)
ax1.legend()


# Plot camera field of view
ax2 = axes[1]

camera_fov = Wedge(
    center=(test_drone.x, test_drone.y),
    r=30,
    theta1=math.degrees(test_drone.theta) - 30,
    theta2=math.degrees(test_drone.theta) + 30,
    alpha=0.2,
    color="blue"
)

ax2.add_patch(camera_fov)

ax2.scatter(
    test_drone.x,
    test_drone.y,
    color="blue",
    label="Test UAV"
)

for i, target in enumerate(test_targets, start=1):
    visible = is_in_fov(test_drone, target)

    ax2.scatter(
        target.x,
        target.y,
        color="green" if visible else "red",
        marker="x",
        s=100
    )

    ax2.annotate(
        f"T{i}",
        (target.x, target.y),
        xytext=(5, 5),
        textcoords="offset points"
    )

ax2.set_xlim(-5, 45)
ax2.set_ylim(-35, 35)
ax2.set_title("Camera Field of View")
ax2.set_xlabel("X Position (m)")
ax2.set_ylabel("Y Position (m)")
ax2.set_aspect("equal")
ax2.grid(True)
ax2.legend()

plt.tight_layout()
plt.show()
