import mujoco
import numpy as np
from mujoco import viewer
import requests
import time  

ANT_URL = "https://raw.githubusercontent.com/openai/gym/master/gym/envs/mujoco/assets/ant.xml"

def load_ant_model():
    response = requests.get(ANT_URL)
    if response.status_code != 200:
        raise Exception("Failed to fetch Ant XML from GitHub")
    return response.text

def main():
    ant_xml = load_ant_model()
    model = mujoco.MjModel.from_xml_string(ant_xml)
    data = mujoco.MjData(model)

    n_controls = model.nu
    print(f"Number of actuators: {n_controls}")

    with viewer.launch_passive(model, data) as v:
        for _ in range(10000):
            data.ctrl[:] = np.random.uniform(low=-1.0, high=1.0, size=n_controls)
            mujoco.mj_step(model, data)
            v.sync()
            time.sleep(1 / 60)  

if __name__ == "__main__":
    main()
