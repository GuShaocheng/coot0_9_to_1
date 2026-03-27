# uf
# DEBUG
# LOAD COOT 0.9.x scripts
# 2026-03-27
import sys
import os
import coot
coot.load_tutorial_model_and_data()

# sys.path.insert(0, os.path.expanduser("~/.config/Coot/compat/"))
# from uf_compat09 import *
# coot.add_key_binding_gtk4_py("h",0,lambda: place_helix_with_restraints(),"Place helix here")
# def mutseq():
#     def mutrange_post_click(res1):
#         def mutrange(seq):
#             coot.mutate_residue_range(res1[1], res1[2], res1[3], res1[3]+len(seq)-1, seq)
#             print("mutate:coot.mutate_residue_range(",res1[0], res1[2], res1[3], res1[3]+len(seq)-1, seq,")")
#             print('res1 infor:',res1)
#         generic_single_entry("Mutseq?","","Engage!",mutrange)
#     user_defined_click(1,mutrange_post_click)

print('UFDEBUG coot 0.9 compat layer')
compat=f"{os.path.expanduser("~")}/.config/Coot/compat/"
coot.run_python_script(f"{compat}/uf_compat_0_9.py")
coot.run_python_script(f"{compat}/uf_coot_menu.py")
coot.run_python_script(f"{compat}/uf_coot_functions.py")
coot.run_python_script(f"{compat}/uf_coot_keybinding.py")
Menu = menu_custom()
