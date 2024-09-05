#!/usr/bin/env python3
"""Example experiment application that uses the WEI client to run a test workflow."""

import json
import time
import math
import requests
from pathlib import Path

from wei import ExperimentClient

# def run_camera(database, camera, verbose):
#     start = time.time()
#     url = "http://146.137.240.84:8001/execute-script/"
#     payload = {
#         "database": database,
#         "camera": camera,
#         "verbose": verbose
#     }
    
#     response = requests.post(url, json=payload).json().get("text")
#     end = time.time()
#     time_taken = end - start
#     #print(response)
    
#     return response, time_taken

def main() -> None:

    # time_avg = 0
    # stored_data = []
    
    exp = ExperimentClient("localhost", "8000", "mir_test")
    exp._register_experiment()
    mir_path = Path(__file__).parent.parent / "workflows" / "test_workflow.yaml"
    ur_path = Path(__file__).parent.parent / "workflows" / "ur_joint_disconnect_workflow.yaml"
    payload = {
        "waypoint_1" : "[-4.88745, -1.42041, 2.08027, -0.63891, 1.4028, -0.02912]",
        "waypoint_2" : "[-5.40313, -1.48324, 2.38776, -0.88424, 1.89998, -0.00733]",
        "waypoint_3" : "[-5.3892, -1.01121, 2.48123, -1.45123, 1.91534, -0.01163]",
        "waypoint_4" : "[-5.38928, -0.97805, 2.47837, -1.48201, 1.91513, -0.01191]"
    }

    for _ in range(1): 
        run_info = exp.start_run(
            mir_path.resolve(),
        )
        run_info = exp.start_run(
            ur_path.resolve(), payload=payload
        )

        # data, time_taken = run_camera(
        #     database="mir.db",
        #     camera="CALIB_Logi_RPL_20240508/",
        #     verbose=True
        #     )
        # stored_data.append(data)
        # time_avg += time_taken
        
    
    #print("Base timeline for un-optimized camera communication: ", time_avg/10)
    #print(json.dumps(run_info, indent=2))

if __name__ == "__main__":
    main()
