# TwoPlus Earbuds X Manufacturing Optimization

## Description
This project simulates the manufacturing optimization for TwoPlus Earbuds X, a Bluetooth headset designed for the TwoPlus 7T smartphone. The goal is to determine the optimal number of earbuds to produce within a one-month sale window, maximizing profit while minimizing waste.

## Problem Context
TwoPlus Earbuds X must be manufactured with these constraints:
- **Demand**: Normally distributed with a mean of 150 units and a standard deviation of 20 units.
- **Costs**:
  - Manufacturing and logistics: $28.50 per unit.
  - Disposal (unsold units): $8.50 per unit (or $17 if additional taxes are imposed with a 50% probability).
- **Retail Price**: $150 per unit.

## Objectives
1. Identify the optimal production quantity to maximize profit.
2. Simulate and analyze demand and profit variability using Monte Carlo techniques.
3. Incorporate uncertainty due to potential additional disposal taxes.

## Features
- **Simulation with Random Demand**: Generates 1000 instances of demand following a normal distribution.
- **Profit Calculation**: Computes profit for each demand scenario based on production levels and tax conditions.
- **Optimization**: Identifies the production quantity that maximizes average profit.
- **Monte Carlo Simulations**: Runs multiple simulations to ensure robust results.

## Getting Started

### Prerequisites
- Python 3.x
- NumPy library (`pip install numpy`)

### Running the Code
Clone this repository:
   ```bash
   git clone <repository_url>
   cd <repository_folder>
