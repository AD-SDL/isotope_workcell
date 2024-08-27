#!/usr/bin/env python3
"""Example experiment application that uses the WEI client to run a test workflow."""

import json
import time
import math
import requests
from pathlib import Path

from wei import ExperimentClient

def run_camera(database, camera, verbose):
    start = time.time()
    url = "http://146.137.240.84:8001/execute-script/"
    payload = {
        "database": database,
        "camera": camera,
        "verbose": verbose
    }
    
    response = requests.post(url, json=payload).json().get("text")
    end = time.time()
    time_taken = end - start
    print(response)
    
    return response, time_taken

def main() -> None:

    time_avg = 0
    stored_data = []
    
    exp = ExperimentClient("localhost", "8000", "mir_test")
    wf_path = Path(__file__).parent.parent / "workflows" / "test_workflow.yaml"

    for _ in range(10): 
    #     run_info = exp.start_run(
    #         wf_path.resolve(),
    #     )
    #     ## RUN CAMERAS
        data, time_taken = run_camera(
            database="mir.db",
            camera="CALIB_Logi_RPL_20240508/",
            verbose=True
            )
        stored_data.append(data)
        time_avg += time_taken
    #     time.sleep(150)
    
    print("Base timeline for un-optimized camera communication: ", time_avg/10)
    # print(json.dumps(run_info, indent=2))

if __name__ == "__main__":
    main()
