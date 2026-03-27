# uf
"""
Compatibility layer for Coot 0.9.x → Coot 1.x

This code is based on existing scripts from markus, oli, and others.

Modified and extended by uf.

2026-03-27
"""


print('load coot 9.x compatible layer')

import sys
import os
import re
import getpass
import math
import platform
import subprocess
import glob
import shutil
import re
import gzip
import string
import importlib.util
from gi.repository import Gtk, Gio, GLib
import gi

# Initialize GTK 4
try:
    gi.require_version('Gtk', '4.0')
except (ValueError, AttributeError):
    pass
coot_dir = os.environ.get("COOT_PREFIX", r"/opt/homebrew/Cellar/coot/1.1.20")

############# ------- Core Coot Modules --------- #############
import coot
import coot_gui
import coot_utils
import coot_fitting
import coot_gui_api
import generic_objects
import coot_fitting

set_font_size                  = coot.set_font_size
set_scroll_by_wheel_mouse      = coot.set_scroll_by_wheel_mouse
ROTAMERSEARCHLOWRES            = coot.ROTAMERSEARCHLOWRES
set_map_sampling_rate          = coot.set_map_sampling_rate
set_smooth_scroll_flag         = coot.set_smooth_scroll_flag
set_rotation_centre_size       = coot.set_rotation_centre_size
set_show_environment_distances = coot.set_show_environment_distances
allow_duplicate_sequence_numbers = coot.allow_duplicate_sequence_numbers
delete_checked_waters_baddies  = coot.delete_checked_waters_baddies
set_imol_refinement_map        = coot.set_imol_refinement_map
imol_refinement_map            = coot.imol_refinement_map
set_contour_level_in_sigma     = coot.set_contour_level_in_sigma
get_contour_level_in_sigma     = coot.get_contour_level_in_sigma
set_contour_level_absolute     = coot.set_contour_level_absolute
get_contour_level_absolute     = coot.get_contour_level_absolute
set_map_displayed              = coot.set_map_displayed
map_is_displayed               = coot.map_is_displayed
map_is_difference_map          = coot.map_is_difference_map
set_mol_displayed              = coot.set_mol_displayed
mol_is_displayed               = coot.mol_is_displayed
save_coordinates               = coot.save_coordinates
write_pdb_file                 = coot.write_pdb_file
read_pdb                       = coot.read_pdb
read_cif_dictionary            = coot.read_cif_dictionary
close_molecule                 = coot.close_molecule
graphics_draw                  = coot.graphics_draw
set_rotation_centre            = coot.set_rotation_centre
set_zoom                       = coot.set_zoom
zoom_factor                    = coot.zoom_factor
residue_name                   = coot.residue_name
set_residue_name               = coot.set_residue_name
mutate                         = coot.mutate
mutate_base                    = coot.mutate_base
mutate_by_overlap              = coot.mutate_by_overlap
refine_zone                    = coot.refine_zone
#rigid_body_refine_zone         = coot.rigid_body_refine_zone
def rigid_body_refine_zone(res_start, res_end, ch_id, mol_id):
    try:
        return coot.rigid_body_refine_zone(mol_id, ch_id, res_start, res_end)
    except Exception as e:
        print(f"rigid_body_refine_zone failed: mol={mol_id} chain={ch_id} res={res_start}-{res_end}: {e}")
        return None
refine_residues                = coot.refine_residues_py
accept_regularizement          = coot.accept_regularizement
delete_residue                 = coot.delete_residue
delete_residue_range           = coot.delete_residue_range
delete_residue_sidechain       = coot.delete_residue_sidechain
delete_hydrogens               = coot.delete_hydrogens
delete_residue_hydrogens       = coot.delete_residue_hydrogens
renumber_residue_range         = coot.renumber_residue_range
add_terminal_residue           = coot.add_terminal_residue
get_monomer                    = coot.get_monomer
n_models                       = coot.n_models
is_valid_model_molecule        = coot.is_valid_model_molecule
is_protein_chain_p             = coot.is_protein_chain_p
is_nucleotide_chain_p          = coot.is_nucleotide_chain_p
resname_from_serial_number     = coot.resname_from_serial_number
average_temperature_factor     = coot.average_temperature_factor
median_temperature_factor      = coot.median_temperature_factor
standard_deviation_temperature_factor = coot.standard_deviation_temperature_factor
set_molecule_bonds_colour_map_rotation = coot.set_molecule_bonds_colour_map_rotation
generic_object_clear           = coot.generic_object_clear
set_display_generic_object     = coot.set_display_generic_object
residue_info                   = coot.residue_info_py
seqnum_from_serial_number      = coot.seqnum_from_serial_number
insertion_code_from_serial_number = coot.insertion_code_from_serial_number
add_key_binding                = coot_utils.add_key_binding
post_go_to_atom_window         = coot.post_go_to_atom_window
set_go_to_atom_chain_residue_atom_name = coot.set_go_to_atom_chain_residue_atom_name
new_molecule_by_atom_selection      = coot.new_molecule_by_atom_selection
set_unpathed_backup_file_names = coot.set_unpathed_backup_file_names
accept_moving_atoms            = coot.accept_moving_atoms_py
add_extra_bond_restraint       = coot.add_extra_bond_restraint
add_linked_residue             = coot.add_linked_residue_py
add_status_bar_text            = coot.add_status_bar_text
add_terminal_residue_using_phi_psi = coot.add_terminal_residue_using_phi_psi
add_view_here                  = coot.add_view_here
apply_lsq_matches              = coot.apply_lsq_matches_py
apply_redo                     = coot.apply_redo
apply_undo                     = coot.apply_undo
attach_generic_object_to_molecule = coot.attach_generic_object_to_molecule
auto_fit_best_rotamer          = coot.auto_fit_best_rotamer
auto_read_make_and_draw_maps   = coot.auto_read_make_and_draw_maps
blob_under_pointer_to_screen_centre = coot.blob_under_pointer_to_screen_centre
cell                           = coot.cell_py
chain_n_residues               = coot.chain_n_residues
change_chain_id_with_result    = coot.change_chain_id_with_result_py
clear_and_update_model_molecule_from_file = coot.clear_and_update_model_molecule_from_file
clear_ball_and_stick           = coot.clear_ball_and_stick
clear_lsq_matches              = coot.clear_lsq_matches
coot_get_url                   = coot.coot_get_url
copy_from_ncs_master_to_others = coot.copy_from_ncs_master_to_others
db_mainchain                   = coot.db_mainchain
default_new_atoms_b_factor     = coot.default_new_atoms_b_factor
delete_all_extra_restraints    = coot.delete_all_extra_restraints
delete_atom                    = coot.delete_atom
delete_extra_restraint         = coot.delete_extra_restraint_py
do_180_degree_side_chain_flip  = coot.do_180_degree_side_chain_flip
does_residue_exist_p           = coot.does_residue_exist_p
draw_ncs_ghosts_state          = coot.draw_ncs_ghosts_state
edit_chi_angles                = coot.edit_chi_angles
export_map_fragment            = coot.export_map_fragment
fit_chain_to_map_by_random_jiggle = coot.fit_chain_to_map_by_random_jiggle
fit_molecule_to_map_by_random_jiggle = coot.fit_molecule_to_map_by_random_jiggle
fit_to_map_by_random_jiggle    = coot.fit_to_map_by_random_jiggle
fix_nomenclature_errors        = coot.fix_nomenclature_errors
get_map_colour                 = coot.get_map_colour_py
get_map_radius                 = coot.get_map_radius
get_rotamer_name               = coot.get_rotamer_name_py
get_show_symmetry              = coot.get_show_symmetry
go_to_view_number              = coot.go_to_view_number
graphics_n_molecules           = coot.graphics_n_molecules
graphics_to_b_factor_representation = coot.graphics_to_b_factor_representation
graphics_to_bonds_representation = coot.graphics_to_bonds_representation
graphics_to_ca_plus_ligands_and_sidechains_representation = coot.graphics_to_ca_plus_ligands_and_sidechains_representation
graphics_to_ca_plus_ligands_representation = coot.graphics_to_ca_plus_ligands_representation
graphics_to_rainbow_representation = coot.graphics_to_rainbow_representation
graphics_to_user_defined_atom_colours_all_atoms_representation = coot.graphics_to_user_defined_atom_colours_all_atoms_representation
graphics_to_user_defined_atom_colours_representation = coot.graphics_to_user_defined_atom_colours_representation
hardware_stereo_angle_factor_state = coot.hardware_stereo_angle_factor_state
hetify_residue                 = coot.hetify_residue
hydrogenate_region             = coot.hydrogenate_region
is_solvent_chain_p             = coot.is_solvent_chain_p
is_valid_map_molecule          = coot.is_valid_map_molecule
jed_flip                       = coot.jed_flip
jed_flip_intermediate_atoms    = coot.jed_flip_intermediate_atoms
list_extra_restraints          = coot.list_extra_restraints_py
make_and_draw_map_with_reso_with_refmac_params = coot.make_and_draw_map_with_reso_with_refmac_params
make_and_draw_patterson        = coot.make_and_draw_patterson
make_backup                    = coot.make_backup
make_ball_and_stick            = coot.make_ball_and_stick
make_directory_maybe           = coot.make_directory_maybe
make_ncs_ghosts_maybe          = coot.make_ncs_ghosts_maybe
map_cell                       = coot.cell_py
map_parameters                 = coot.map_parameters_py
mark_multiple_atoms_as_fixed   = coot.mark_multiple_atoms_as_fixed_py
merge_molecules                = coot.merge_molecules_py
missing_atom_info              = coot.missing_atom_info_py
molecule_name                  = coot.molecule_name
molecule_name_stub             = coot.molecule_name_stub_py
move_waters_to_around_protein  = coot.move_waters_to_around_protein
n_rotamers                     = coot.n_rotamers
ncs_control_change_ncs_master_to_chain_id = coot.ncs_control_change_ncs_master_to_chain_id
new_molecule_by_residue_type_selection = coot.new_molecule_by_residue_type_selection
place_atom_at_pointer          = coot.place_atom_at_pointer
place_typed_atom_at_pointer    = coot.place_typed_atom_at_pointer
post_display_control_window    = coot.post_display_control_window
remove_all_atom_labels         = coot.remove_all_atom_labels
renumber_waters                = coot.renumber_waters
rigid_body_refine_by_atom_selection = coot.rigid_body_refine_by_atom_selection
rotamer_score                  = coot.rotamer_score
rotate_y_scene                 = coot.rotate_y_scene
screendump_image               = coot.screendump_image
scroll_wheel_map               = coot.scroll_wheel_map
set_all_maps_displayed         = coot.set_all_maps_displayed
set_background_colour          = coot.set_background_colour
set_colour_by_chain            = coot.set_colour_by_chain
set_draw_axes                  = coot.set_draw_axes
set_draw_hydrogens             = coot.set_draw_hydrogens
set_draw_map_standard_lines    = coot.set_draw_map_standard_lines
set_draw_ncs_ghosts            = coot.set_draw_ncs_ghosts
set_draw_solid_density_surface = coot.set_draw_solid_density_surface
set_flat_shading_for_solid_density_surface = coot.set_flat_shading_for_solid_density_surface
set_hardware_stereo_angle_factor = coot.set_hardware_stereo_angle_factor
set_limit_aniso                = coot.set_limit_aniso
set_map_colour                 = coot.set_map_colour
set_molecule_name              = coot.set_molecule_name
set_refinement_immediate_replacement = coot.set_refinement_immediate_replacement
set_residue_to_rotamer_number  = coot.set_residue_to_rotamer_number
set_rotation_center_size       = coot.set_rotation_centre_size
set_scroll_wheel_map           = coot.set_scroll_wheel_map
set_scrollable_map             = coot.set_scrollable_map
set_show_extra_restraints      = coot.set_show_extra_restraints
set_show_symmetry_master       = coot.set_show_symmetry_master
set_show_unit_cells_all        = coot.set_show_unit_cells_all
set_symmetry_whole_chain       = coot.set_symmetry_whole_chain
set_undo_molecule              = coot.set_undo_molecule
setup_backbone_torsion_edit    = coot.setup_backbone_torsion_edit
setup_torsion_general          = coot.setup_torsion_general
sharpen                        = coot.sharpen
show_rotamers_dialog           = coot.show_rotamers_dialog
sort_chains                    = coot.sort_chains
sort_residues                  = coot.sort_residues
spin_N_py                      = coot.spin_N_py
sprout_hydrogens               = coot.sprout_hydrogens
start_ligand_builder_gui       = coot.start_ligand_builder_gui
superpose                      = coot.superpose
symmetry_as_calphas            = coot.symmetry_as_calphas
to_generic_object_add_dashed_line = coot.to_generic_object_add_dashed_line
turn_off_backup                = coot.turn_off_backup
turn_on_backup                 = coot.turn_on_backup
undo_symmetry_view             = coot.undo_symmetry_view
update_go_to_atom_from_current_position = coot.update_go_to_atom_from_current_position
fill_partial_residue           = coot.fill_partial_residue
simple_fill_partial_residues   = coot.simple_fill_partial_residues
set_run_state_file_status      = coot.set_run_state_file_status
set_show_chiral_volume_errors_dialog = coot.set_show_chiral_volume_errors_dialog
set_nomenclature_errors_on_read      = coot.set_nomenclature_errors_on_read
set_console_display_commands_state   = coot.set_console_display_commands_state
set_refine_ramachandran_angles      = coot.set_refine_ramachandran_angles
set_go_to_atom_molecule             = coot.set_go_to_atom_molecule
set_matrix                          = coot.set_matrix
vt_surface                          = coot.vt_surface
set_rotamer_search_mode             = coot.set_rotamer_search_mode
set_clipping_front                  = coot.set_clipping_front
set_clipping_back                   = coot.set_clipping_back
set_map_radius                      = coot.set_map_radius
set_show_aniso                      = coot.set_show_aniso
set_aniso_probability               = coot.set_aniso_probability
set_refine_hydrogen_bonds           = coot.set_refine_hydrogen_bonds
set_do_probe_dots_post_refine       = coot.set_do_probe_dots_post_refine
set_do_probe_dots_on_rotamers_and_chis = coot.set_do_probe_dots_on_rotamers_and_chis
set_add_terminal_residue_do_post_refine = coot.set_add_terminal_residue_do_post_refine
set_mutate_auto_fit_do_post_refine  = coot.set_mutate_auto_fit_do_post_refine
set_default_temperature_factor_for_new_atoms = coot.set_default_temperature_factor_for_new_atoms
set_refine_with_torsion_restraints  = coot.set_refine_with_torsion_restraints
set_b_factor_residue_range = coot.set_b_factor_residue_range
add_planar_peptide_restraints       = coot.add_planar_peptide_restraints
delete_residue_with_full_spec       = coot.delete_residue_with_full_spec
ideal_nucleic_acid                  = coot.ideal_nucleic_acid
do_distance_define                  = coot.do_distance_define
#mutate_residue_range                = coot.mutate_residue_range
def mutate_residue_range(mol,chain_id,start_resno,
        end_resno,residue):
    if isinstance(residue, str):
        residue = residue.strip().upper()
    return coot.mutate_residue_range(mol,
        chain_id,
        start_resno,
        end_resno,
        residue)

def user_defined_click(n_clicks, old_callback):
    """
    Compatibility wrapper for old Coot 0.9.x scripts.
    Reorders arguments from Coot 1 (user_defined_click_py)
    to match the old expected format.
    """

    def wrapper(*args):
        # Convert tuple to list so we can modify it
        args = list(args)
        print('UFDEBUG: args1:',args[:])

        # Unwrap if single tuple argument
        if len(args) == 1 and isinstance(args[0], (tuple, list)):
            args = list(args[0])

        # Swap first two elements: (mol, -1, ...) → (-1, mol, ...)
        if len(args) >= 2:
            #args[0], args[1] = args[1], args[0]
            args[1]=args[1]+1
        
        # debug
        print('UFDEBUG: args2:',args[:])

        # Call original callback with reordered arguments
        return old_callback(args)

    # Call the new API
    coot.user_defined_click_py(n_clicks, wrapper)

# --- GUI & Window Settings ---
try: 
    set_browser_interface = coot.set_browser_interface
except: 
    pass
set_graphics_window_size = coot.set_graphics_window_size
set_graphics_window_position = coot.set_graphics_window_position

try: 
    set_go_to_atom_window_position = coot.set_go_to_atom_window_position
except: 
    pass # Some older Coots might not have this specific one

set_ramachandran_plot_dialog_position = coot.set_ramachandran_plot_dialog_position
set_rotate_translate_dialog_position = coot.set_rotate_translate_dialog_position
set_delete_dialog_position = coot.set_delete_dialog_position
set_display_control_dialog_position = coot.set_display_control_dialog_position
set_model_fit_refine_dialog_position = coot.set_model_fit_refine_dialog_position

# --- Map & Display Settings ---
set_views_play_speed = coot.set_views_play_speed
set_residue_selection_flash_frames_number = coot.set_residue_selection_flash_frames_number
set_map_sharpening_scale_limit = coot.set_map_sharpening_scale_limit
set_default_initial_contour_level_for_difference_map = coot.set_default_initial_contour_level_for_difference_map
set_default_initial_contour_level_for_map = coot.set_default_initial_contour_level_for_map
set_colour_map_rotation_on_read_pdb_flag = coot.set_colour_map_rotation_on_read_pdb_flag
set_display_lists_for_maps = coot.set_display_lists_for_maps
set_brief_atom_labels = coot.set_brief_atom_labels
set_show_paths_in_display_manager = coot.set_show_paths_in_display_manager
set_default_bond_thickness = coot.set_default_bond_thickness
set_use_variable_bond_thickness = coot.set_use_variable_bond_thickness
add_omega_torsion_restriants = coot.add_omega_torsion_restriants

# --- Symmetry & Visuals ---
set_symmetry_atom_labels_expanded = coot.set_symmetry_atom_labels_expanded
set_symmetry_colour_merge = coot.set_symmetry_colour_merge
set_symmetry_colour = coot.set_symmetry_colour
set_symmetry_size = coot.set_symmetry_size
set_show_pointer_distances = coot.set_show_pointer_distances
set_raster3d_water_sphere = coot.set_raster3d_water_sphere
set_raster3d_shadows_enabled = coot.set_raster3d_shadows_enabled

# --- Refinement & Waters ---
set_add_alt_conf_split_type_number = coot.set_add_alt_conf_split_type_number
set_delete_water_mode = coot.set_delete_water_mode
set_ligand_water_to_protein_distance_limits = coot.set_ligand_water_to_protein_distance_limits
set_ligand_water_n_cycles = coot.set_ligand_water_n_cycles
set_pointer_atom_molecule = coot.set_pointer_atom_molecule
set_check_waters_b_factor_limit = coot.set_check_waters_b_factor_limit
set_auto_fit_best_rotamer_clash_flag = coot.set_auto_fit_best_rotamer_clash_flag
set_add_terminal_residue_n_phi_psi_trials = coot.set_add_terminal_residue_n_phi_psi_trials
set_refinement_drag_elasticity = coot.set_refinement_drag_elasticity
set_active_map_drag_flag = coot.set_active_map_drag_flag
set_idle_function_rotate_angle = coot.set_idle_function_rotate_angle
set_show_environment_distances_bumps = coot.set_show_environment_distances_bumps
set_show_environment_distances_h_bonds = coot.set_show_environment_distances_h_bonds
set_environment_distances_distance_limits = coot.set_environment_distances_distance_limits
set_terminal_residue_do_rigid_body_refine = coot.set_terminal_residue_do_rigid_body_refine
set_refine_max_residues = coot.set_refine_max_residues

# --- GUI Update Callbacks (Try/Except for safety) ---
try:
    update_go_to_atom_window_on_changed_mol = coot.update_go_to_atom_window_on_changed_mol
    update_go_to_atom_window_on_new_mol = coot.update_go_to_atom_window_on_new_mol
    update_go_to_atom_window_on_other_molecule_chosen = coot.update_go_to_atom_window_on_other_molecule_chosen
except AttributeError:
    # If Coot doesn't have these, define empty pass functions to prevent errors
    def update_go_to_atom_window_on_changed_mol(*args):
        pass
    def update_go_to_atom_window_on_new_mol(*args):
        pass
    def update_go_to_atom_window_on_other_molecule_chosen(*args):
        pass

# GUI Mappings
generic_single_entry           = coot_gui.generic_single_entry
alt_confs_gui                  = coot_gui.alt_confs_gui
cis_peptides_gui               = coot_gui.cis_peptides_gui
generic_button_dialog          = coot_gui.generic_button_dialog
interesting_residues_gui       = coot_gui.interesting_residues_gui
interesting_things_gui         = coot_gui.interesting_things_gui
missing_atoms_gui              = coot_gui.missing_atoms_gui
molecule_chooser_gui           = coot_gui.molecule_chooser_gui

# Utils Mappings
rotation_centre                = coot_utils.rotation_centre
guess_refinement_map           = coot_utils.guess_refinement_map
active_residue                 = coot_utils.active_residue
move_molecule_here             = coot_utils.move_molecule_here
is_solvent_chain_qm            = coot_utils.is_solvent_chain_qm
model_molecule_list            = coot_utils.model_molecule_list
molecule_number_list           = coot_utils.molecule_number_list
map_molecule_list              = coot_utils.map_molecule_list
chain_ids                      = coot_utils.chain_ids
residue_alt_confs              = coot_utils.residue_alt_confs
atom_spec_to_residue_spec      = coot_utils.atom_spec_to_residue_spec
atom_specs                     = coot_utils.atom_specs
flip_active_ligand             = coot_utils.flip_active_ligand
get_atom                       = coot_utils.get_atom
get_directory                  = coot_utils.get_directory
label_all_active_residue_atoms = coot_utils.label_all_active_residue_atoms
merge_solvent_chains           = coot_utils.merge_solvent_chains
overlay_my_ligands             = coot_utils.overlay_my_ligands
print_sequence                 = coot_utils.print_sequence
print_sequence_chain           = coot.print_sequence_chain
prodrg_ify                     = coot_utils.prodrg_ify
regularize_zone                = coot.regularize_zone
residue_exists_qm              = coot_utils.residue_exists_qm
residue_spec_to_chain_id       = coot_utils.residue_spec_to_chain_id
residue_spec_to_ins_code       = coot_utils.residue_spec_to_ins_code
residue_spec_to_res_no         = coot_utils.residue_spec_to_res_no
residues_matching_criteria     = coot_utils.residues_matching_criteria
residues_with_alt_confs        = coot_utils.residues_with_alt_confs
set_b_factor_molecule          = coot_utils.set_b_factor_molecule
split_active_water             = coot_utils.split_active_water
toggle_display_mol             = coot_utils.toggle_display_mol
valid_map_molecule_qm          = coot_utils.valid_map_molecule_qm
valid_model_molecule_qm        = coot_utils.valid_model_molecule_qm
view_matrix                    = coot_utils.view_matrix
with_auto_accept               = coot_utils.with_auto_accept
is_protein_chain_qm            = coot_utils.is_protein_chain_qm

# Fitting Mappings
refine_active_residue          = coot_fitting.refine_active_residue
refine_active_residue_triple   = coot_fitting.refine_active_residue_triple
auto_fit_rotamer_active_residue = coot.auto_fit_rotamer_active_residue
pepflip_active_residue         = coot_fitting.pepflip_active_residue
fit_waters                     = coot_fitting.fit_waters
manual_refine_residues         = coot_fitting.manual_refine_residues
sphere_refine                  = coot_fitting.sphere_refine
sphere_refine_plus             = coot_fitting.sphere_refine_plus

# Regularization Mappings
regularize_zone                = coot.regularize_zone
regularize_residues            = coot.regularize_residues_py

# Loaded Internal Mappings
def _load_internal(mod_name, file_name):
    base_path = os.path.dirname(coot.__file__)
    full_path = os.path.join(base_path, "coot", file_name)
    if not os.path.exists(full_path):
        full_path = os.path.join(base_path, file_name)
    spec = importlib.util.spec_from_file_location(mod_name, full_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

_gap_lib = _load_internal("coot_gap_internal", "gap.py")
_obj_lib = _load_internal("coot_obj_internal", "generic_objects.py")
_ncs_lib = _load_internal("coot_ncs_internal", "coot_ncs.py")
_mut_lib = _load_internal("coot_mutate_internal", "mutate.py")
_hol_lib = _load_internal("coot_hole_internal", "gui_hole.py")
_gen_lib = _load_internal("coot_gen_internal", "coot_generator_3d_import.py")

fit_gap                        = _gap_lib.fit_gap
generic_object_with_name       = _obj_lib.generic_object_with_name
ncs_master_chain_id            = _ncs_lib.ncs_master_chain_id
probe                          = _obj_lib.probe
probe_local_sphere             = _obj_lib.probe_local_sphere
three_letter_code2single_letter = _mut_lib.three_letter_code2single_letter
hole_ify                       = _hol_lib.hole_ify
new_molecule_by_smiles_string  = _gen_lib.new_molecule_by_smiles_string


########ufDEBUG old menu compatible layer###############
from gi.repository import Gio
import coot_gui_api

# --- global app/menu objects ---
app = coot_gui_api.application()
main_menubar = coot_gui_api.main_menumodel()
_menus = {}

# --- helper: universal callback adapter ---
def _activate_cb(action, param, cb):
    """
    Accept both:
        lambda func: ...
        lambda: ...
    """
    try:
        cb()          # new-style (no args)
    except TypeError:
        try:
            cb(None)  # old-style (expects 1 arg)
        except Exception as e:
            print(f"[coot compat] callback error: {e}")

# --- Wrapper for top-level and submenus ---
class MenuWrapper:
    def __init__(self, gio_menu=None):
        self.gio_menu = gio_menu if gio_menu else Gio.Menu()
        self.children = []

    def append(self, menuitem):
        # Accept FakeMenuItem from old code
        if hasattr(menuitem, 'label'):

            # --- submenu case ---
            if getattr(menuitem, 'submenu', None):
                self.gio_menu.append_submenu(
                    menuitem.label,
                    menuitem.submenu.gio_menu
                )

            # --- normal item ---
            else:
                act_name = f"act_{id(menuitem)}"
                action = Gio.SimpleAction.new(act_name, None)

                if hasattr(menuitem, 'callback') and menuitem.callback:
                    # IMPORTANT FIX HERE
                    action.connect("activate", _activate_cb, menuitem.callback)

                app.add_action(action)
                self.gio_menu.append(menuitem.label, f"app.{act_name}")

            self.children.append(menuitem)

        else:
            # fallback
            self.gio_menu.append(str(menuitem), None)

    def get_children(self):
        return self.children

# --- GTK MenuItem / Menu shim ---
class FakeMenuItem:
    def __init__(self, label=""):
        self.label = label
        self.submenu = None
        self.callback = None

    def set_submenu(self, menu):
        self.submenu = menu

    def get_submenu(self):
        return self.submenu

    def get_child(self):
        return self

    def get_text(self):
        return self.label

    def show(self):
        pass  # no-op for compatibility

# --- fake gtk namespace ---
class gtk:
    Menu = MenuWrapper
    MenuItem = FakeMenuItem

# --- top-level menu function ---
def coot_menubar_menu(name):
    if name not in _menus:
        _menus[name] = MenuWrapper(Gio.Menu())
        main_menubar.append_submenu(name, _menus[name].gio_menu)
    return _menus[name]

# --- add menu item (old function) ---
def add_simple_coot_menu_menuitem(menu, label, callback):
    item = FakeMenuItem(label)
    item.callback = callback
    menu.append(item)

######ufDEBUG: end new menu method#####
from gi.repository import Gio
import coot_gui_api

app = coot_gui_api.application()
main_menubar = coot_gui_api.main_menumodel()

new_menu = Gio.Menu()
main_menubar.append_submenu("NM", new_menu)

action = Gio.SimpleAction.new("hello", None)
action.connect("activate", lambda a, p: print("Hello world"))
app.add_action(action)
new_menu.append("Say Hello", "app.hello")
#########ufDEBUG: end2################################################


# The single-value input window is this:
def generic_single_entry_(label, default_text, button_text, callback):
    w = Gtk.Window(title=label)
    w.set_default_size(300, -1)
    vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
    w.set_child(vbox)
    lbl = Gtk.Label(label=label)
    entry = Gtk.Entry()
    entry.set_text(str(default_text))
    vbox.append(lbl)
    vbox.append(entry)
    def on_click(btn):
        val = entry.get_text()
        w.destroy()
        callback(val)
    btn = Gtk.Button(label=button_text)
    btn.connect("clicked", on_click)
    vbox.append(btn)
    w.show()

######### -----toolbar buttons---########################
# --- internal helpers ---
def _resolve_icon(icon_name):
    """
    Try to resolve icon path from coot installation.
    Falls back to Gtk themed icon if file not found.
    flip_peptide_svg = os.path.join(coot_dir, "share", "coot", "pixmaps", "flip-peptide.svg")
    """
    if not icon_name:
        return None

    # Try coot pixmaps directory
    if coot_dir:
        candidate = os.path.join(coot_dir, "share", "coot", "pixmaps", icon_name)
        if os.path.exists(candidate):
            return Gtk.Image.new_from_file(candidate)
    else:
        print('To define coot_dir like: coot_dir = os.environ.get("COOT_PREFIX", r"/opt/homebrew/Cellar/coot/1.1.20")')
    # Fallback: try as themed icon
    return Gtk.Image.new_from_icon_name(icon_name)


def _wrap_callback(callback):
    """
    Convert old-style string callback into callable.
    """
    if callable(callback):
        return callback

    if isinstance(callback, str):
        def _cb(*_):
            try:
                eval(callback, globals())
            except Exception as e:
                print(f"[coot compat] callback error: {e}")
        return _cb

    raise TypeError("Unsupported callback type")


# --- public compatibility API ---
def coot_toolbar_button(label, callback, icon_name=None, tooltip=None):
    """
    Compatible with coot 0.9.x:
        coot_toolbar_button("savePDB", "quicksave_active()", icon_name="coot-save.png")
    """
    btn = Gtk.Button()

    # tooltip
    if tooltip:
        btn.set_tooltip_text(tooltip)
    else:
        btn.set_tooltip_text(label)

    # icon
    img = _resolve_icon(icon_name)
    if img:
        btn.set_child(img)
    else:
        btn.set_label(label)

    # callback
    btn.connect("clicked", lambda *_: _wrap_callback(callback)())

    # add to toolbar
    coot_gui_api.main_toolbar().append(btn)

    return btn


def coot_toolbar_separator():
    """
    Equivalent of old separator
    """
    sep = Gtk.Separator(orientation=Gtk.Orientation.VERTICAL)
    sep.set_margin_start(4)
    sep.set_margin_end(4)
    coot_gui_api.main_toolbar().append(sep)

    return sep

###########################################################

######### ----- compat: add_key_binding -----##############
REGISTERED_KEYBINDING_CALLBACKS = []
def add_key_binding(name, key, thunk):
    ctrl_key = 0
    key_value = key
    if isinstance(key, str) and key.startswith("Control_"):
        ctrl_key = 1
        key_value = key[len("Control_"):]
    def wrapped_thunk():
        try:
            return thunk()
        except Exception:
            import traceback
            print("coot_trimmings keybinding failure:", name, "key=", key_value)
            traceback.print_exc()
            return None
    REGISTERED_KEYBINDING_CALLBACKS.append(wrapped_thunk)
    coot.add_key_binding_gtk4_py(key_value, ctrl_key, wrapped_thunk, name)
