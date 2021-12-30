#!/usr/bin/python3
import os
import subprocess
import sys

def enverr(e):
    print(f"Error: Openlane backend needs environment variable '{e}' to be set")
    exit(1)

if 'flow.tcl' in sys.argv[1]:
    openlane_root = os.environ.get('OPENLANE_ROOT') or enverr('OPENLANE_ROOT')
    pdk_root      = os.environ.get('PDK_ROOT') or enverr('PDK_ROOT')
    (build_root, work) = os.path.split(os.getcwd())

    image = "efabless/openlane:mpw-3a"

    prefix = ["docker", "run",
              "-v", f"{openlane_root}:/openLANE_flow",
              "-v", f"{pdk_root}:{pdk_root}",
              "-v", f"{build_root}:/project",
              "-e", f"PDK_ROOT={pdk_root}",
              "-u", f"{os.getuid()}:{os.getgid()}",
              "-w", f"/project/{work}",
              image]
    sys.exit(subprocess.call(prefix+sys.argv[1:]))
