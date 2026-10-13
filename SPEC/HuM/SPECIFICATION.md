# HuM Specification

> **Document info**: Version 0.1 (prototype) | Status: dynamics-simulation prototype | Author: NOHN AI
> **Basis**: README-zh
> 中文版本：[`SPECIFICATION-zh.md`](./SPECIFICATION-zh.md)
>
> This specification describes the public specification surface of the **Humanoid drive system with aerodynamics (HuM)**: module contracts, covered disciplines and runtime interface. HuM is a Python dynamics-simulation prototype fusing physics, biomechanics and mechanical transmission.

## 1. Scope and Positioning

### 1.1 Positioning

Evolves from bio-inspired actuation primitives into a closed-loop humanoid system spanning "perception–decision–thermal–reliability–biomechanics"; covers biomechanics (Hill muscle), dynamics (SLIP / spring-mass-damper), stability (CoM–ZMP), aerodynamics (crosswind), thermal management, reliability engineering and cost modelling.

## 2. Terms and Definitions

| Term | Definition |
|---|---|
| Hill muscle model | Muscle mechanics model with force–length / force–velocity characteristics |
| SLIP | Spring-Loaded Inverted Pendulum, spring-mass gait model |
| CoM / CoP / ZMP | Centre of mass / centre of pressure / zero-moment-point stability criterion |
| Overturn margin | Aerodynamic anti-overturn safety margin under crosswind |
| Self-healing MTBF | Reliability metric with self-healing mechanism |
| Lumped-C thermal model | Blocked-heat-capacitance simplified model of the human thermal budget |

## 3. Core Specification

### 3.1 Module Contracts (`hum/` package)

| Module | Contract |
|---|---|
| `bio.py` | Lever / Hill muscle, force–length–velocity, real SLIP spring-mass ODE gait |
| `stability.py` | CoM / CoP / ZMP and support-polygon criterion |
| `aero.py` | Aerodynamic drag / crosswind lateral force / overturn margin |
| `thermal.py` | Steady + transient lumped-C human thermal budget and torque attenuation |
| `reliability.py` | Redundancy availability, self-healing MTBF, collision-impedance model |
| `cpg.py` | Hopf oscillator network (anti-phase / gait mutual coupling) |
| `fusion.py` | Kalman CoM-height fusion (IMU control input + asynchronous vision) |
| `cost.py` | Parametric TCO decomposition + single-DOF cost index |
| `loop.py` | Full-system report (closed-loop ZMP→CPG / thermal→SLIP coupling) |
| `plot.py` | Visualisation |

### 3.2 Runtime Interface

- `python demo_hum.py`

### 3.3 Dependencies

- `requirements.txt` manages dependencies.

## 4. Conformance Statement

An implementation conforming to this specification should satisfy: module contracts consistent with §3.1; default entry point runs and outputs a system report.

## 5. Version and Changes

- Roadmap: full-body closed-loop gait generation (perception-driven state estimation); multi-modal sensor fusion for real-time CoM tracking; lifecycle simulation of thermal–reliability coupling.
- Shares the dynamics-simulation-prototype lineage with DMU; roadmap directions are related (DMU's VSA / pneumatic coupling is "in the same direction as HuM").

## 6. License and References

- Dual-track license (non-open): free for personal non-commercial research; written paid license for government / enterprise.
- Reference: README-zh.
