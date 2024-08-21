#!/usr/bin/env python3
"""Example experiment application that uses the WEI client to run a test workflow."""

import json
from pathlib import Path

from wei import ExperimentClient


def main() -> None:
    
    exp = ExperimentClient("localhost", "8000", "mir_test")
    wf_path = Path(__file__).parent.parent / "workflows" / "test_workflow.yaml"

    for _ in range(5): # Maybe "test_workflow" should just input # of times to run, or other experiment params, and links to mir_module workflow which contains the three actions, instead of looping submit workflow.
        run_info = exp.start_run(
            wf_path.resolve(),
        )

    print(json.dumps(run_info, indent=2))

if __name__ == "__main__":
    main()
