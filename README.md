# Smart Traffic Management System using Computer Vision
### Real-Time Vehicle Density Analysis using YOLOv8 & Computer Vision
![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-red?style=for-the-badge)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green?style=for-the-badge&logo=opencv)
![Status](https://img.shields.io/badge/Project-Completed-brightgreen?style=for-the-badge)
![License](https://img.shields.io/badge/License-Educational-blueviolet?style=for-the-badge)

## 🚦 Project Goal
Traditional traffic lights use fixed timers, leading to congestion. This project uses **AI/Computer Vision** to calculate vehicle density in real-time and dynamically adjust signal timings to improve urban mobility.

---

## 📌 Problem Statement

Traditional traffic signal systems operate on fixed timers regardless of real-time road conditions. This leads to:

- 🚗 Traffic congestion  
- ⛽ Fuel wastage  
- 🌍 Increased carbon emissions  
- ⏳ Longer waiting times  

An adaptive, AI-driven traffic control system is required to optimize signal timing based on real-time vehicle density.

---

## 💡 Solution Overview

This project implements a Computer Vision-based Smart Traffic Management System that:

- Detects vehicles in real-time using YOLOv8  
- Calculates vehicle density dynamically  
- Classifies congestion levels (Low / Moderate / Heavy)  
- Adjusts green signal duration accordingly  
- Simulates intelligent smart city traffic control  

---

## 🏗️ System Architecture

1. **Video Input Layer** – Live camera or recorded traffic video  
2. **Detection Layer** – YOLOv8 Nano Model  
3. **Density Calculation Engine** – Counts detected vehicles  
4. **Decision Engine** – Applies adaptive signal timing logic  
5. **Visualization Layer** – Displays bounding boxes and signal duration  

---

## 🧠 Technology Stack

| Component | Technology |
|-----------|------------|
| Programming Language | Python |
| AI Model | YOLOv8 (Nano) |
| Computer Vision | OpenCV |
| Visualization | Cvzone |
| IDE | VS Code |

---

## 📊 Traffic Density Logic

| Vehicle Count | Traffic Category | Green Signal Duration |
|---------------|------------------|-----------------------|
| `< 5`         | Low Traffic      | 30 seconds            |
| `5 – 15`      | Moderate Traffic | 40 seconds            |
| `> 15`        | Heavy Traffic    | 50 seconds            |

### 🔁 Core Decision Logic
  python
base_time = 30

if count > 15:
    signal_time = base_time + 20
    status = "HEAVY TRAFFIC"
elif count > 5:
    signal_time = base_time + 10
    status = "MODERATE TRAFFIC"
else:
    signal_time = base_time
    status = "LOW TRAFFIC"

## 🚀 Installation & Setup
**1️⃣ Clone the Repository**
git clone https://github.com/your-username/ai-smart-traffic-system.git
cd ai-smart-traffic-system

**2️⃣ Install Dependenciespip**
pip install opencv-python ultralytics cvzone

**3️⃣ Run the Application**
  python traffic_manager.py
  Press Q to exit.

## 🎯 Key Features
+ ✅ Real-time AI vehicle detection

+ ✅ Dynamic traffic density classification

+ ✅ Adaptive signal timing algorithm

+ ✅ Smart city simulation model

+ ✅ Lightweight YOLOv8 Nano for efficient performance

## 🔮 Future Scope
+ Multi-lane intersection management

+ IoT-based real traffic signal integration

+ Emergency vehicle priority detection

+ AI-based traffic prediction models

+ Cloud dashboard monitoring

## 🏙 Real-World Applications

+ Smart City Infrastructure

+ Urban Traffic Monitoring

+ AI Surveillance Systems

+ Government Traffic Control Systems

## 👩‍💻 Author

**Tanvi Barve**
**Future-Ready Software & AI Engineer**
**Building Intelligent Real-World AI Solutions**

## ⭐ If you found this project useful, consider giving it a star!
