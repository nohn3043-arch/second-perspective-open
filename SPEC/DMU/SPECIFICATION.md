# DMU Specification

> **Document info**: Version 0.1 (prototype) | Status: dynamics-simulation prototype | Author: NOHN AI
> **Basis**: README-zh
> 中文版本：[`SPECIFICATION-zh.md`](./SPECIFICATION-zh.md)
>
> This specification describes the public specification surface of the **Direct-Drive Motion Unified actuator system (DMU)**: module contracts, dynamics model and runtime interface. DMU is a Python dynamics-simulation prototype for gearless, electromagnetically direct-driven single-degree-of-freedom actuation.

## 1. Scope and Positioning

### 1.1 Positioning

A direct-drive motion platform covering cascaded servo-loop simulation, multi-DOF kinematics, CPG gait generation, thermal budget, reliability and cost modelling; follows the principle "trade hardware for software, trade volume for bandwidth, trade cost for energy efficiency".

### 1.2 Applicable Scenarios

Compliant humanoid / quadruped legs, surgical robots, precision assembly, rehabilitation exoskeletons, research prototypes, light-duty service robots.

## 2. Terms and Definitions

| Term | Definition |
|---|---|
| Direct drive | Gearless, electromagnetic direct drive |
| Cascaded servo loop | Three-loop cascade: current → speed → position |
| Hopf limit-cycle oscillator | Basis dynamics for CPG gait generation |
| m-of-n redundancy | Reliability redundancy structure |
| Thermal derating | Torque-derating closed loop caused by winding temperature rise |
| Lumped-parameter thermal model | Simplified model of the winding thermal network |

## 3. Core Specification

### 3.1 Module Contracts (`dmu/` package)

| Module | Contract |
|---|---|
| `dynamics.py` | Motor dynamics `T = J·alpha + B·omega + T_f`; direct-drive vs gearbox comparison |
| `servo.py` | Cascaded current→speed→position servo loop; torque saturation + anti-windup |
| `robot.py` | Robot body model |
| `multidof.py` | Multi-DOF kinematics |
| `thermal.py` | Lumped-parameter winding thermal model (transient dt-aware) |
| `fusion.py` | Kalman joint-state fusion + RMSE report |
| `cpg.py` | Hopf limit-cycle oscillator network (phase-locked mutual coupling) |
| `reliability.py` | Component / m-of-n redundancy reliability (MTBF, availability) |
| `cost.py` | Parametric cost decomposition scaled by torque + single-axis cost index |
| `system.py` | Full-system report (incl. thermal-derating closed-loop feedback) |
| `plot.py` | Visualisation |

### 3.2 Runtime Interface

- `python demo_dmu.py`
- `python -m dmu.robot`

### 3.3 Dependencies

- `requirements.txt` manages dependencies.

## 4. Conformance Statement

An implementation conforming to this specification should satisfy: module contracts consistent with §3.1; default entry point runs and outputs a system report.

## 5. Version and Changes

- Roadmap: full-body multi-DOF dynamics (DH / Newton–Euler); variable-stiffness actuator (VSA) and pneumatic coupling (shared direction with HuM).

## 6. License and References

- Dual-track license (non-open): free for personal non-commercial research; written paid license for government / enterprise.
- Reference: README-zh.
