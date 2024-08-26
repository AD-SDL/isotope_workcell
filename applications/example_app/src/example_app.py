#!/usr/bin/env python3
"""Example experiment application that uses the WEI client to run a test workflow."""

import json
import time
from pathlib import Path

from wei import ExperimentClient


def main() -> None:
    
    exp = ExperimentClient("localhost", "8000", "mir_test")
    wf_path = Path(__file__).parent.parent / "workflows" / "test_workflow.yaml"

    for _ in range(20): # Maybe "test_workflow" should just input # of times to run, or other experiment params, and links to mir_module workflow which contains the three actions, instead of looping submit workflow.
        run_info = exp.start_run(
            wf_path.resolve(),
        )
        ## RUN CAMERAS
        time.sleep(150)

    print(json.dumps(run_info, indent=2))

if __name__ == "__main__":
    main()
