# MUAVTargetTracking

**Multi-UAV Target Detection and Tracking**

An educational and research-oriented Python project focused on distributed multi-UAV control, ground target detection, visual tracking, and multi-agent reinforcement learning.

## Project Objectives

- Simulate multiple UAVs in a 2D environment.
- Model UAV motion using kinematic equations.
- Implement camera field-of-view geometry.
- Develop image-based target detection and tracking.
- Enable communication and cooperation between UAVs.
- Investigate distributed control using multi-agent reinforcement learning (MAPPO).

## Current Implementation

The current version includes:

- A 2D UAV kinematic model.
- Multi-UAV trajectory simulation.
- Stationary ground targets.
- Geometric camera field-of-view calculations.
- Visualization using Matplotlib.

**Note:** Camera-based image detection, inter-UAV communication, and reinforcement learning are planned features and have not yet been implemented.

## Project Structure

```text
MUAVTargetTracking/
├── drone.py
├── target.py
├── camera.py
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Run

```bash
python main.py
```

## Development Environment

- Python 3
- Ubuntu 24.04
- Visual Studio Code

## Research Roadmap

1. UAV kinematics and trajectory simulation
2. Camera geometry and synthetic image generation
3. Computer vision-based target detection
4. Target tracking and visual feature extraction
5. Distributed inter-UAV communication
6. Baseline cooperative control
7. Multi-agent reinforcement learning using MAPPO
8. Evaluation and performance comparison

## Status

Early development — geometric simulation and field-of-view modeling.
