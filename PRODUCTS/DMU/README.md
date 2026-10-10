# DMU — Direct-Motion Unity Drive System

[简体中文](README-zh.md) | English

**Python dynamics simulation prototype** for gear-free, electromagnetic direct-drive single-DOF mechanical actuation, including cascaded servo-loop simulation, multi-DOF kinematics, CPG gait generation, thermal budget, reliability, and cost modelling.

## Positioning

A light-to-medium payload, high-precision, compliant robotic motion platform guided by the principle of "trade software for hardware, bandwidth for volume, and energy efficiency for cost".

## Repository Structure

```
DMU/
├── dmu/
│   ├── dynamics.py    # Motor dynamics T = J*alpha + B*omega + T_f; direct-drive vs gearbox comparison
│   ├── servo.py       # Cascaded current -> speed -> position servo loop (torque saturation + anti-windup)
│   ├── robot.py       # Joint dynamics simulation + plotting
│   ├── multidof.py    # Multi-DOF arm kinematics simulation
│   ├── thermal.py     # Lumped-parameter winding thermal model (transient, dt-aware)
│   ├── fusion.py      # Kalman joint-state fusion with torque control input + RMSE report
│   ├── cpg.py         # Hopf limit-cycle oscillator network with phase-locking mutual coupling
│   ├── reliability.py # Component/m-of-n redundant reliability (MTBF, availability)
│   ├── cost.py        # Torque-scaled parametric cost breakdown & per-axis cost index
│   ├── system.py      # Full-system report with thermal-derating closed-loop feedback
│   ├── plot.py        # Visualization bundle (returns the files generated in this run)
│   └── __init__.py
├── demo_dmu.py        # Run entry point
├── requirements.txt
└── README.md
```

## Run

```bash
cd DMU
pip install -r requirements.txt
python demo_dmu.py          # or: python -m dmu.robot
```

## Use Cases

Compliant humanoid/quadruped legs, surgical robots, precision assembly, rehabilitation exoskeletons, research prototypes, light-duty service robots.

## Roadmap

- Full-body multi-DOF dynamics (DH / Newton–Euler)
- Variable-stiffness actuators (VSA) and pneumatic coupling (shared direction with HuM)
