# DMU — 直驱运动统一驱动系统

[English](README.md) | 简体中文

**Python 动力学仿真原型**，面向无齿轮、电磁直驱的单自由度机械作动，涵盖级联伺服环仿真、多自由度运动学、CPG 步态生成、热预算、可靠性与成本建模。

## 定位

一款轻中载荷、高精度、柔顺的机器人运动平台，遵循"以软件换硬件、以带宽换体积、以能效换成本"的原则。

## 仓库结构

```
DMU/
├── dmu/
│   ├── dynamics.py    # 电机动力学 T = J*alpha + B*omega + T_f；直驱与齿轮箱对比
│   ├── servo.py       # 级联 电流 -> 转速 -> 位置 伺服环（转矩饱和 + 抗积分饱和）
│   ├── robot.py       # 关节动力学仿真 + 绘图
│   ├── multidof.py    # 多自由度机械臂运动学仿真
│   ├── thermal.py     # 集总参数绕组热模型（瞬态，dt 感知）
│   ├── fusion.py      # 卡尔曼关节状态融合，含转矩控制输入 + RMSE 报告
│   ├── cpg.py         # Hopf 极限环振荡器网络，含锁相相互耦合
│   ├── reliability.py # 元件 / m-of-n 冗余可靠性（MTBF、可用度）
│   ├── cost.py        # 按转矩缩放的参数化成本分解 & 单轴成本指数
│   ├── system.py      # 全系统报告，含热降额闭环反馈
│   ├── plot.py        # 可视化打包（返回本次运行生成的文件）
│   └── __init__.py
├── demo_dmu.py        # 运行入口
├── requirements.txt
└── README.md
```

## 运行

```bash
cd DMU
pip install -r requirements.txt
python demo_dmu.py          # 或：python -m dmu.robot
```

## 适用场景

柔顺的人形/四足腿部、手术机器人、精密装配、康复外骨骼、研究原型、轻载服务机器人。

## 路线图

- 全身多自由度动力学（DH / 牛顿–欧拉）
- 变刚度作动器（VSA）与气动耦合（与 HuM 同方向）
