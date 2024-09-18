#!/usr/bin/env python3
"""Example experiment application that uses the WEI client to run a test workflow."""

import requests
from pathlib import Path

from wei import ExperimentClient


def run_camera(database, camera, verbose):
    url = "http://146.137.240.84:8001/execute-script/"
    payload = {"database": database, "camera": camera, "verbose": verbose}

    response = requests.post(url, json=payload).json().get("text")
    print(response)
    return response


def main() -> None:
    stored_data = []
    exp = ExperimentClient("localhost", "8000", "mir_test")
    exp._register_experiment()
    wf_path = Path(__file__).parent.parent / "workflows" / "test_workflow.yaml"
    payload = {
        "waypoint_1": "[-5.45778870979418, -2.095121046105856, 2.1441996733294886, -0.05430622518573003, 1.8396282196044922, 0.010314404033124447]",
        "waypoint_2": "[-0.13808589185898898, -0.3343258604018853, 0.0228316443656502, 1.3892169444793483, -0.7786089780873691, 0.7682852134633944]",
    }

    for _ in range(1):
        exp.start_run(wf_path.resolve(), payload=payload)
        data = run_camera(
            database="mir.db", camera="CALIB_Logi_RPL_20240508/", verbose=True
        )
        # exp.start_run(ur_path.resolve(), payload=payload)

        stored_data.append(data)
        print(stored_data)

    # print("Base timeline for un-optimized camera communication: ", time_avg/10)
    # print(json.dumps(run_info, indent=2))


if __name__ == "__main__":
    main()
