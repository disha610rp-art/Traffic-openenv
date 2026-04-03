# Autonomous Traffic Control OpenEnv Environment

## Overview
This project simulates a 4-way traffic intersection controlled by an AI agent.
The agent controls traffic lights to minimize congestion and prioritize emergency vehicles.

## Observation Space
- north_queue
- south_queue
- east_queue
- west_queue
- signal
- emergency
- time_step

## Action Space
- NS_GREEN
- EW_GREEN
- ALL_RED

## Reward Function
Reward = cars_passed - waiting_penalty + emergency_bonus - signal_switch_penalty

## Tasks
- Easy: Low traffic, no emergency
- Medium: Random traffic
- Hard: Heavy traffic + emergency vehicles

## Run
python baseline/run_baseline.py

## Docker
docker build -t traffic-env .
docker run traffic-env