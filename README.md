## Description
The script loads the official Ant model (a quadruped robot with 8 actuated joints) from OpenAI Gym’s MuJoCo assets, applies random control inputs to its joints, and runs a real-time simulation. The viewer displays the Ant’s movements, which appear chaotic due to the random controls, at approximately 60 FPS.
![Ant-Mujoco](https://github.com/user-attachments/assets/03ea6e2f-9725-4d29-9ff9-1a51508bbe31)

## Prerequisites
- **Python**: 3.8 or higher
- **Operating System**: Tested on Ubuntu (Linux); should work on macOS/Windows with minor adjustments.
- **Dependencies**:
  - `mujoco`: Python bindings for MuJoCo.
  - `numpy`: For generating random control inputs.
  - `requests`: To fetch the Ant XML from GitHub.

## Setup Instructions
1. **Createව

2. **Create a Virtual Environment** (Recommended):
   ```bash
   python3 -m venv mujoco_env
   ```
3. **Activate the Environment**:
   - Linux/Mac: 
     ```bash
     source mujoco_env/bin/activate
     ```
   - Windows: 
     ```bash
     mujoco_env\Scripts\activate
     ```
4. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   The `requirements.txt` file contains:
   ```
   mujoco
   numpy
   requests
   ```

5. **Run the Simulation**:
   ```bash
   python ant_simulation.py
   ```
## Output
- **Terminal Output**: Confirms the number of actuators (8).
- **Viewer**: Displays the Ant robot in a 3D simulation, moving chaotically due to random controls applied to its 8 joints (hip and ankle for each of the 4 legs).
