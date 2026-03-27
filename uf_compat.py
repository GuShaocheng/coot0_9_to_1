# uf
# DEBUG
# LOAD COOT 0.9.x scripts
# 2026-03-27
import sys
import os
import coot
coot.load_tutorial_model_and_data()

print('UFDEBUG coot 0.9 compat layer')
compat=f"{os.path.expanduser("~")}/.config/Coot/compat/"
coot.run_python_script(f"{compat}/uf_compat_0_9.py")

