# HuM — Humanoid-Morphic Actuation System (incl. Aerodynamics)

[简体中文](README-zh.md) | English

**Python dynamics simulation prototype** blending physics, biomechanics, and mechanical transmission: human lever/Hill muscle models, force-length/velocity characteristics, SLIP energy-storing gait, CoM/CoP/ZMP stability, and crosswind aerodynamic anti-overturn analysis.

## Positioning

Evolving from biomimetic actuation primitives into a closed-loop humanoid system spanning "perception – decision – thermal – reliability – biomechanics".

## Repository Structure

```
HuM/
├── hum/
│   ├── bio.py         # Lever / Hill muscle, force-length-velocity, real SLIP spring-mass ODE gait
│   ├── stability.py   # CoM / CoP / ZMP and support-polygon criteria
│   ├── aero.py        # Aerodynamic drag / crosswind side force / anti-overturn margin
│   ├── thermal.py     # Steady-state + transient (lumped-C) human thermal budget & torque fade
│   ├── reliability.py # Redundant availability, self-healing MTBF, collision impedance model
│   ├── cpg.py         # Hopf oscillator network with anti-phase (gait) mutual coupling
│   ├── fusion.py      # Kalman CoM-height fusion with IMU control input + asynchronous vision
│   ├── cost.py        # Parametric TCO breakdown & per-DOF cost index
│   ├── loop.py        # Full-system report with closed-loop ZMP -> CPG / thermal -> SLIP coupling
│   ├── plot.py        # Visualization bundle (returns the files generated in this run)
│   └── __init__.py
├── demo_hum.py        # Run entry point
├── requirements.txt
└── README.md
```

## Run

```bash
cd HuM
pip install -r requirements.txt
python demo_hum.py
```

## Covered Disciplines

Biomechanics (Hill muscle), dynamics (SLIP / mass-spring-damper), stability (CoM–ZMP), aerodynamics (crosswind), thermal management, reliability engineering, and cost modelling.

## Roadmap

- Whole-body closed-loop gait generation with perception-driven state estimation
- Multimodal sensor fusion for real-time CoM tracking
- Coupled thermal-reliability lifecycle simulation
