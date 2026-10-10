# HuM — 人形驱动系统（含空气动力学）

[English](README.md) | 简体中文

**Python 动力学仿真原型**，融合物理学、生物力学与机械传动：人体杠杆/Hill 肌肉模型、力–长度/速度特性、SLIP 储能步态、CoM/CoP/ZMP 稳定性，以及侧风气动抗倾覆分析。

## 定位

从仿生作动原语演进为一个闭环人形系统，横跨"感知 – 决策 – 热 – 可靠性 – 生物力学"。

## 仓库结构

```
HuM/
├── hum/
│   ├── bio.py         # 杠杆 / Hill 肌肉、力–长度–速度、真实 SLIP 弹簧-质量 ODE 步态
│   ├── stability.py   # CoM / CoP / ZMP 与支撑多边形判据
│   ├── aero.py        # 气动阻力 / 侧风侧向力 / 抗倾覆裕度
│   ├── thermal.py     # 稳态 + 瞬态（集总-C）人体热预算 & 转矩衰减
│   ├── reliability.py # 冗余可用度、自愈 MTBF、碰撞阻抗模型
│   ├── cpg.py         # Hopf 振荡器网络，含反相（步态）相互耦合
│   ├── fusion.py      # 卡尔曼 CoM 高度融合，含 IMU 控制输入 + 异步视觉
│   ├── cost.py        # 参数化 TCO 分解 & 单自由度成本指数
│   ├── loop.py        # 全系统报告，含闭环 ZMP -> CPG / 热 -> SLIP 耦合
│   ├── plot.py        # 可视化打包（返回本次运行生成的文件）
│   └── __init__.py
├── demo_hum.py        # 运行入口
├── requirements.txt
└── README.md
```

## 运行

```bash
cd HuM
pip install -r requirements.txt
python demo_hum.py
```

## 覆盖学科

生物力学（Hill 肌肉）、动力学（SLIP / 弹簧-质量-阻尼）、稳定性（CoM–ZMP）、空气动力学（侧风）、热管理、可靠性工程与成本建模。

## 路线图

- 全身闭环步态生成，含感知驱动的状态估计
- 多模态传感器融合，实现实时 CoM 跟踪
- 热–可靠性耦合的生命周期仿真
