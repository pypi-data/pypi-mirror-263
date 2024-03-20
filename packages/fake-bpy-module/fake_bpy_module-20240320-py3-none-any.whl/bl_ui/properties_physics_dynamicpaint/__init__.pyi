import typing
import bpy_types

GenericType = typing.TypeVar("GenericType")

class PHYSICS_UL_dynapaint_surfaces(bpy_types.UIList, bpy_types._GenericUI):
    bl_rna: typing.Any
    id_data: typing.Any

    def append(self, draw_func):
        """

        :param draw_func:
        :type draw_func:
        """
        ...

    def as_pointer(self): ...
    def bl_rna_get_subclass(self): ...
    def bl_rna_get_subclass_py(self): ...
    def draw_item(
        self,
        _context,
        layout,
        _data,
        item,
        icon,
        _active_data,
        _active_propname,
        _index,
    ):
        """

        :param self:
        :type self:
        :param _context:
        :type _context:
        :param layout:
        :type layout:
        :param _data:
        :type _data:
        :param item:
        :type item:
        :param icon:
        :type icon:
        :param _active_data:
        :type _active_data:
        :param _active_propname:
        :type _active_propname:
        :param _index:
        :type _index:
        """
        ...

    def driver_add(self): ...
    def driver_remove(self): ...
    def get(self): ...
    def id_properties_clear(self): ...
    def id_properties_ensure(self): ...
    def id_properties_ui(self): ...
    def is_extended(self): ...
    def is_property_hidden(self): ...
    def is_property_overridable_library(self): ...
    def is_property_readonly(self): ...
    def is_property_set(self): ...
    def items(self): ...
    def keyframe_delete(self): ...
    def keyframe_insert(self): ...
    def keys(self): ...
    def path_from_id(self): ...
    def path_resolve(self): ...
    def pop(self): ...
    def prepend(self, draw_func):
        """

        :param draw_func:
        :type draw_func:
        """
        ...

    def property_overridable_library_set(self): ...
    def property_unset(self): ...
    def remove(self, draw_func):
        """

        :param draw_func:
        :type draw_func:
        """
        ...

    def type_recast(self): ...
    def values(self): ...

class PhysicButtonsPanel:
    bl_context: typing.Any
    bl_region_type: typing.Any
    bl_space_type: typing.Any

    def poll_dyn_canvas(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_canvas_brush(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_canvas_paint(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_output(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_output_maps(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_paint(self, context):
        """

        :param context:
        :type context:
        """
        ...

class PHYSICS_PT_dp_brush_source(
    PhysicButtonsPanel, bpy_types.Panel, bpy_types._GenericUI
):
    COMPAT_ENGINES: typing.Any
    bl_context: typing.Any
    bl_label: typing.Any
    bl_parent_id: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any

    def append(self, draw_func):
        """

        :param draw_func:
        :type draw_func:
        """
        ...

    def as_pointer(self): ...
    def bl_rna_get_subclass(self): ...
    def bl_rna_get_subclass_py(self): ...
    def draw(self, context):
        """

        :param self:
        :type self:
        :param context:
        :type context:
        """
        ...

    def driver_add(self): ...
    def driver_remove(self): ...
    def get(self): ...
    def id_properties_clear(self): ...
    def id_properties_ensure(self): ...
    def id_properties_ui(self): ...
    def is_extended(self): ...
    def is_property_hidden(self): ...
    def is_property_overridable_library(self): ...
    def is_property_readonly(self): ...
    def is_property_set(self): ...
    def items(self): ...
    def keyframe_delete(self): ...
    def keyframe_insert(self): ...
    def keys(self): ...
    def path_from_id(self): ...
    def path_resolve(self): ...
    def poll(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_canvas(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_canvas_brush(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_canvas_paint(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_output(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_output_maps(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_paint(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def pop(self): ...
    def prepend(self, draw_func):
        """

        :param draw_func:
        :type draw_func:
        """
        ...

    def property_overridable_library_set(self): ...
    def property_unset(self): ...
    def remove(self, draw_func):
        """

        :param draw_func:
        :type draw_func:
        """
        ...

    def type_recast(self): ...
    def values(self): ...

class PHYSICS_PT_dp_brush_source_color_ramp(
    PhysicButtonsPanel, bpy_types.Panel, bpy_types._GenericUI
):
    COMPAT_ENGINES: typing.Any
    bl_context: typing.Any
    bl_label: typing.Any
    bl_parent_id: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any

    def append(self, draw_func):
        """

        :param draw_func:
        :type draw_func:
        """
        ...

    def as_pointer(self): ...
    def bl_rna_get_subclass(self): ...
    def bl_rna_get_subclass_py(self): ...
    def draw(self, context):
        """

        :param self:
        :type self:
        :param context:
        :type context:
        """
        ...

    def driver_add(self): ...
    def driver_remove(self): ...
    def get(self): ...
    def id_properties_clear(self): ...
    def id_properties_ensure(self): ...
    def id_properties_ui(self): ...
    def is_extended(self): ...
    def is_property_hidden(self): ...
    def is_property_overridable_library(self): ...
    def is_property_readonly(self): ...
    def is_property_set(self): ...
    def items(self): ...
    def keyframe_delete(self): ...
    def keyframe_insert(self): ...
    def keys(self): ...
    def path_from_id(self): ...
    def path_resolve(self): ...
    def poll(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_canvas(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_canvas_brush(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_canvas_paint(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_output(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_output_maps(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_paint(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def pop(self): ...
    def prepend(self, draw_func):
        """

        :param draw_func:
        :type draw_func:
        """
        ...

    def property_overridable_library_set(self): ...
    def property_unset(self): ...
    def remove(self, draw_func):
        """

        :param draw_func:
        :type draw_func:
        """
        ...

    def type_recast(self): ...
    def values(self): ...

class PHYSICS_PT_dp_brush_velocity(
    PhysicButtonsPanel, bpy_types.Panel, bpy_types._GenericUI
):
    COMPAT_ENGINES: typing.Any
    bl_context: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_parent_id: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any

    def append(self, draw_func):
        """

        :param draw_func:
        :type draw_func:
        """
        ...

    def as_pointer(self): ...
    def bl_rna_get_subclass(self): ...
    def bl_rna_get_subclass_py(self): ...
    def draw(self, context):
        """

        :param self:
        :type self:
        :param context:
        :type context:
        """
        ...

    def driver_add(self): ...
    def driver_remove(self): ...
    def get(self): ...
    def id_properties_clear(self): ...
    def id_properties_ensure(self): ...
    def id_properties_ui(self): ...
    def is_extended(self): ...
    def is_property_hidden(self): ...
    def is_property_overridable_library(self): ...
    def is_property_readonly(self): ...
    def is_property_set(self): ...
    def items(self): ...
    def keyframe_delete(self): ...
    def keyframe_insert(self): ...
    def keys(self): ...
    def path_from_id(self): ...
    def path_resolve(self): ...
    def poll(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_canvas(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_canvas_brush(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_canvas_paint(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_output(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_output_maps(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_paint(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def pop(self): ...
    def prepend(self, draw_func):
        """

        :param draw_func:
        :type draw_func:
        """
        ...

    def property_overridable_library_set(self): ...
    def property_unset(self): ...
    def remove(self, draw_func):
        """

        :param draw_func:
        :type draw_func:
        """
        ...

    def type_recast(self): ...
    def values(self): ...

class PHYSICS_PT_dp_brush_velocity_color_ramp(
    PhysicButtonsPanel, bpy_types.Panel, bpy_types._GenericUI
):
    COMPAT_ENGINES: typing.Any
    bl_context: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_parent_id: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any

    def append(self, draw_func):
        """

        :param draw_func:
        :type draw_func:
        """
        ...

    def as_pointer(self): ...
    def bl_rna_get_subclass(self): ...
    def bl_rna_get_subclass_py(self): ...
    def draw(self, context):
        """

        :param self:
        :type self:
        :param context:
        :type context:
        """
        ...

    def driver_add(self): ...
    def driver_remove(self): ...
    def get(self): ...
    def id_properties_clear(self): ...
    def id_properties_ensure(self): ...
    def id_properties_ui(self): ...
    def is_extended(self): ...
    def is_property_hidden(self): ...
    def is_property_overridable_library(self): ...
    def is_property_readonly(self): ...
    def is_property_set(self): ...
    def items(self): ...
    def keyframe_delete(self): ...
    def keyframe_insert(self): ...
    def keys(self): ...
    def path_from_id(self): ...
    def path_resolve(self): ...
    def poll(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_canvas(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_canvas_brush(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_canvas_paint(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_output(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_output_maps(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_paint(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def pop(self): ...
    def prepend(self, draw_func):
        """

        :param draw_func:
        :type draw_func:
        """
        ...

    def property_overridable_library_set(self): ...
    def property_unset(self): ...
    def remove(self, draw_func):
        """

        :param draw_func:
        :type draw_func:
        """
        ...

    def type_recast(self): ...
    def values(self): ...

class PHYSICS_PT_dp_brush_velocity_smudge(
    PhysicButtonsPanel, bpy_types.Panel, bpy_types._GenericUI
):
    COMPAT_ENGINES: typing.Any
    bl_context: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_parent_id: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any

    def append(self, draw_func):
        """

        :param draw_func:
        :type draw_func:
        """
        ...

    def as_pointer(self): ...
    def bl_rna_get_subclass(self): ...
    def bl_rna_get_subclass_py(self): ...
    def draw(self, context):
        """

        :param self:
        :type self:
        :param context:
        :type context:
        """
        ...

    def draw_header(self, context):
        """

        :param self:
        :type self:
        :param context:
        :type context:
        """
        ...

    def driver_add(self): ...
    def driver_remove(self): ...
    def get(self): ...
    def id_properties_clear(self): ...
    def id_properties_ensure(self): ...
    def id_properties_ui(self): ...
    def is_extended(self): ...
    def is_property_hidden(self): ...
    def is_property_overridable_library(self): ...
    def is_property_readonly(self): ...
    def is_property_set(self): ...
    def items(self): ...
    def keyframe_delete(self): ...
    def keyframe_insert(self): ...
    def keys(self): ...
    def path_from_id(self): ...
    def path_resolve(self): ...
    def poll(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_canvas(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_canvas_brush(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_canvas_paint(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_output(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_output_maps(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_paint(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def pop(self): ...
    def prepend(self, draw_func):
        """

        :param draw_func:
        :type draw_func:
        """
        ...

    def property_overridable_library_set(self): ...
    def property_unset(self): ...
    def remove(self, draw_func):
        """

        :param draw_func:
        :type draw_func:
        """
        ...

    def type_recast(self): ...
    def values(self): ...

class PHYSICS_PT_dp_brush_wave(
    PhysicButtonsPanel, bpy_types.Panel, bpy_types._GenericUI
):
    COMPAT_ENGINES: typing.Any
    bl_context: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_parent_id: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any

    def append(self, draw_func):
        """

        :param draw_func:
        :type draw_func:
        """
        ...

    def as_pointer(self): ...
    def bl_rna_get_subclass(self): ...
    def bl_rna_get_subclass_py(self): ...
    def draw(self, context):
        """

        :param self:
        :type self:
        :param context:
        :type context:
        """
        ...

    def driver_add(self): ...
    def driver_remove(self): ...
    def get(self): ...
    def id_properties_clear(self): ...
    def id_properties_ensure(self): ...
    def id_properties_ui(self): ...
    def is_extended(self): ...
    def is_property_hidden(self): ...
    def is_property_overridable_library(self): ...
    def is_property_readonly(self): ...
    def is_property_set(self): ...
    def items(self): ...
    def keyframe_delete(self): ...
    def keyframe_insert(self): ...
    def keys(self): ...
    def path_from_id(self): ...
    def path_resolve(self): ...
    def poll(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_canvas(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_canvas_brush(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_canvas_paint(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_output(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_output_maps(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_paint(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def pop(self): ...
    def prepend(self, draw_func):
        """

        :param draw_func:
        :type draw_func:
        """
        ...

    def property_overridable_library_set(self): ...
    def property_unset(self): ...
    def remove(self, draw_func):
        """

        :param draw_func:
        :type draw_func:
        """
        ...

    def type_recast(self): ...
    def values(self): ...

class PHYSICS_PT_dp_cache(PhysicButtonsPanel, bpy_types.Panel, bpy_types._GenericUI):
    COMPAT_ENGINES: typing.Any
    bl_context: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_parent_id: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any

    def append(self, draw_func):
        """

        :param draw_func:
        :type draw_func:
        """
        ...

    def as_pointer(self): ...
    def bl_rna_get_subclass(self): ...
    def bl_rna_get_subclass_py(self): ...
    def draw(self, context):
        """

        :param self:
        :type self:
        :param context:
        :type context:
        """
        ...

    def driver_add(self): ...
    def driver_remove(self): ...
    def get(self): ...
    def id_properties_clear(self): ...
    def id_properties_ensure(self): ...
    def id_properties_ui(self): ...
    def is_extended(self): ...
    def is_property_hidden(self): ...
    def is_property_overridable_library(self): ...
    def is_property_readonly(self): ...
    def is_property_set(self): ...
    def items(self): ...
    def keyframe_delete(self): ...
    def keyframe_insert(self): ...
    def keys(self): ...
    def path_from_id(self): ...
    def path_resolve(self): ...
    def poll(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_canvas(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_canvas_brush(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_canvas_paint(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_output(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_output_maps(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_paint(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def pop(self): ...
    def prepend(self, draw_func):
        """

        :param draw_func:
        :type draw_func:
        """
        ...

    def property_overridable_library_set(self): ...
    def property_unset(self): ...
    def remove(self, draw_func):
        """

        :param draw_func:
        :type draw_func:
        """
        ...

    def type_recast(self): ...
    def values(self): ...

class PHYSICS_PT_dp_canvas_initial_color(
    PhysicButtonsPanel, bpy_types.Panel, bpy_types._GenericUI
):
    COMPAT_ENGINES: typing.Any
    bl_context: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_parent_id: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any

    def append(self, draw_func):
        """

        :param draw_func:
        :type draw_func:
        """
        ...

    def as_pointer(self): ...
    def bl_rna_get_subclass(self): ...
    def bl_rna_get_subclass_py(self): ...
    def draw(self, context):
        """

        :param self:
        :type self:
        :param context:
        :type context:
        """
        ...

    def driver_add(self): ...
    def driver_remove(self): ...
    def get(self): ...
    def id_properties_clear(self): ...
    def id_properties_ensure(self): ...
    def id_properties_ui(self): ...
    def is_extended(self): ...
    def is_property_hidden(self): ...
    def is_property_overridable_library(self): ...
    def is_property_readonly(self): ...
    def is_property_set(self): ...
    def items(self): ...
    def keyframe_delete(self): ...
    def keyframe_insert(self): ...
    def keys(self): ...
    def path_from_id(self): ...
    def path_resolve(self): ...
    def poll(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_canvas(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_canvas_brush(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_canvas_paint(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_output(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_output_maps(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_paint(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def pop(self): ...
    def prepend(self, draw_func):
        """

        :param draw_func:
        :type draw_func:
        """
        ...

    def property_overridable_library_set(self): ...
    def property_unset(self): ...
    def remove(self, draw_func):
        """

        :param draw_func:
        :type draw_func:
        """
        ...

    def type_recast(self): ...
    def values(self): ...

class PHYSICS_PT_dp_canvas_output(
    PhysicButtonsPanel, bpy_types.Panel, bpy_types._GenericUI
):
    COMPAT_ENGINES: typing.Any
    bl_context: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_parent_id: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any

    def append(self, draw_func):
        """

        :param draw_func:
        :type draw_func:
        """
        ...

    def as_pointer(self): ...
    def bl_rna_get_subclass(self): ...
    def bl_rna_get_subclass_py(self): ...
    def draw(self, context):
        """

        :param self:
        :type self:
        :param context:
        :type context:
        """
        ...

    def driver_add(self): ...
    def driver_remove(self): ...
    def get(self): ...
    def id_properties_clear(self): ...
    def id_properties_ensure(self): ...
    def id_properties_ui(self): ...
    def is_extended(self): ...
    def is_property_hidden(self): ...
    def is_property_overridable_library(self): ...
    def is_property_readonly(self): ...
    def is_property_set(self): ...
    def items(self): ...
    def keyframe_delete(self): ...
    def keyframe_insert(self): ...
    def keys(self): ...
    def path_from_id(self): ...
    def path_resolve(self): ...
    def poll(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_canvas(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_canvas_brush(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_canvas_paint(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_output(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_output_maps(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_paint(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def pop(self): ...
    def prepend(self, draw_func):
        """

        :param draw_func:
        :type draw_func:
        """
        ...

    def property_overridable_library_set(self): ...
    def property_unset(self): ...
    def remove(self, draw_func):
        """

        :param draw_func:
        :type draw_func:
        """
        ...

    def type_recast(self): ...
    def values(self): ...

class PHYSICS_PT_dp_canvas_output_paintmaps(
    PhysicButtonsPanel, bpy_types.Panel, bpy_types._GenericUI
):
    COMPAT_ENGINES: typing.Any
    bl_context: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_parent_id: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any

    def append(self, draw_func):
        """

        :param draw_func:
        :type draw_func:
        """
        ...

    def as_pointer(self): ...
    def bl_rna_get_subclass(self): ...
    def bl_rna_get_subclass_py(self): ...
    def draw(self, context):
        """

        :param self:
        :type self:
        :param context:
        :type context:
        """
        ...

    def draw_header(self, context):
        """

        :param self:
        :type self:
        :param context:
        :type context:
        """
        ...

    def driver_add(self): ...
    def driver_remove(self): ...
    def get(self): ...
    def id_properties_clear(self): ...
    def id_properties_ensure(self): ...
    def id_properties_ui(self): ...
    def is_extended(self): ...
    def is_property_hidden(self): ...
    def is_property_overridable_library(self): ...
    def is_property_readonly(self): ...
    def is_property_set(self): ...
    def items(self): ...
    def keyframe_delete(self): ...
    def keyframe_insert(self): ...
    def keys(self): ...
    def path_from_id(self): ...
    def path_resolve(self): ...
    def poll(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_canvas(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_canvas_brush(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_canvas_paint(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_output(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_output_maps(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_paint(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def pop(self): ...
    def prepend(self, draw_func):
        """

        :param draw_func:
        :type draw_func:
        """
        ...

    def property_overridable_library_set(self): ...
    def property_unset(self): ...
    def remove(self, draw_func):
        """

        :param draw_func:
        :type draw_func:
        """
        ...

    def type_recast(self): ...
    def values(self): ...

class PHYSICS_PT_dp_canvas_output_wetmaps(
    PhysicButtonsPanel, bpy_types.Panel, bpy_types._GenericUI
):
    COMPAT_ENGINES: typing.Any
    bl_context: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_parent_id: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any

    def append(self, draw_func):
        """

        :param draw_func:
        :type draw_func:
        """
        ...

    def as_pointer(self): ...
    def bl_rna_get_subclass(self): ...
    def bl_rna_get_subclass_py(self): ...
    def draw(self, context):
        """

        :param self:
        :type self:
        :param context:
        :type context:
        """
        ...

    def draw_header(self, context):
        """

        :param self:
        :type self:
        :param context:
        :type context:
        """
        ...

    def driver_add(self): ...
    def driver_remove(self): ...
    def get(self): ...
    def id_properties_clear(self): ...
    def id_properties_ensure(self): ...
    def id_properties_ui(self): ...
    def is_extended(self): ...
    def is_property_hidden(self): ...
    def is_property_overridable_library(self): ...
    def is_property_readonly(self): ...
    def is_property_set(self): ...
    def items(self): ...
    def keyframe_delete(self): ...
    def keyframe_insert(self): ...
    def keys(self): ...
    def path_from_id(self): ...
    def path_resolve(self): ...
    def poll(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_canvas(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_canvas_brush(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_canvas_paint(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_output(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_output_maps(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_paint(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def pop(self): ...
    def prepend(self, draw_func):
        """

        :param draw_func:
        :type draw_func:
        """
        ...

    def property_overridable_library_set(self): ...
    def property_unset(self): ...
    def remove(self, draw_func):
        """

        :param draw_func:
        :type draw_func:
        """
        ...

    def type_recast(self): ...
    def values(self): ...

class PHYSICS_PT_dp_effects(PhysicButtonsPanel, bpy_types.Panel, bpy_types._GenericUI):
    COMPAT_ENGINES: typing.Any
    bl_context: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_parent_id: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any

    def append(self, draw_func):
        """

        :param draw_func:
        :type draw_func:
        """
        ...

    def as_pointer(self): ...
    def bl_rna_get_subclass(self): ...
    def bl_rna_get_subclass_py(self): ...
    def draw(self, _context):
        """

        :param self:
        :type self:
        :param _context:
        :type _context:
        """
        ...

    def driver_add(self): ...
    def driver_remove(self): ...
    def get(self): ...
    def id_properties_clear(self): ...
    def id_properties_ensure(self): ...
    def id_properties_ui(self): ...
    def is_extended(self): ...
    def is_property_hidden(self): ...
    def is_property_overridable_library(self): ...
    def is_property_readonly(self): ...
    def is_property_set(self): ...
    def items(self): ...
    def keyframe_delete(self): ...
    def keyframe_insert(self): ...
    def keys(self): ...
    def path_from_id(self): ...
    def path_resolve(self): ...
    def poll(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_canvas(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_canvas_brush(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_canvas_paint(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_output(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_output_maps(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_paint(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def pop(self): ...
    def prepend(self, draw_func):
        """

        :param draw_func:
        :type draw_func:
        """
        ...

    def property_overridable_library_set(self): ...
    def property_unset(self): ...
    def remove(self, draw_func):
        """

        :param draw_func:
        :type draw_func:
        """
        ...

    def type_recast(self): ...
    def values(self): ...

class PHYSICS_PT_dp_effects_drip(
    PhysicButtonsPanel, bpy_types.Panel, bpy_types._GenericUI
):
    COMPAT_ENGINES: typing.Any
    bl_context: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_parent_id: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any

    def append(self, draw_func):
        """

        :param draw_func:
        :type draw_func:
        """
        ...

    def as_pointer(self): ...
    def bl_rna_get_subclass(self): ...
    def bl_rna_get_subclass_py(self): ...
    def draw(self, context):
        """

        :param self:
        :type self:
        :param context:
        :type context:
        """
        ...

    def draw_header(self, context):
        """

        :param self:
        :type self:
        :param context:
        :type context:
        """
        ...

    def driver_add(self): ...
    def driver_remove(self): ...
    def get(self): ...
    def id_properties_clear(self): ...
    def id_properties_ensure(self): ...
    def id_properties_ui(self): ...
    def is_extended(self): ...
    def is_property_hidden(self): ...
    def is_property_overridable_library(self): ...
    def is_property_readonly(self): ...
    def is_property_set(self): ...
    def items(self): ...
    def keyframe_delete(self): ...
    def keyframe_insert(self): ...
    def keys(self): ...
    def path_from_id(self): ...
    def path_resolve(self): ...
    def poll(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_canvas(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_canvas_brush(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_canvas_paint(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_output(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_output_maps(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_paint(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def pop(self): ...
    def prepend(self, draw_func):
        """

        :param draw_func:
        :type draw_func:
        """
        ...

    def property_overridable_library_set(self): ...
    def property_unset(self): ...
    def remove(self, draw_func):
        """

        :param draw_func:
        :type draw_func:
        """
        ...

    def type_recast(self): ...
    def values(self): ...

class PHYSICS_PT_dp_effects_drip_weights(
    PhysicButtonsPanel, bpy_types.Panel, bpy_types._GenericUI
):
    COMPAT_ENGINES: typing.Any
    bl_context: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_parent_id: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any

    def append(self, draw_func):
        """

        :param draw_func:
        :type draw_func:
        """
        ...

    def as_pointer(self): ...
    def bl_rna_get_subclass(self): ...
    def bl_rna_get_subclass_py(self): ...
    def draw(self, context):
        """

        :param self:
        :type self:
        :param context:
        :type context:
        """
        ...

    def driver_add(self): ...
    def driver_remove(self): ...
    def get(self): ...
    def id_properties_clear(self): ...
    def id_properties_ensure(self): ...
    def id_properties_ui(self): ...
    def is_extended(self): ...
    def is_property_hidden(self): ...
    def is_property_overridable_library(self): ...
    def is_property_readonly(self): ...
    def is_property_set(self): ...
    def items(self): ...
    def keyframe_delete(self): ...
    def keyframe_insert(self): ...
    def keys(self): ...
    def path_from_id(self): ...
    def path_resolve(self): ...
    def poll(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_canvas(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_canvas_brush(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_canvas_paint(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_output(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_output_maps(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_paint(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def pop(self): ...
    def prepend(self, draw_func):
        """

        :param draw_func:
        :type draw_func:
        """
        ...

    def property_overridable_library_set(self): ...
    def property_unset(self): ...
    def remove(self, draw_func):
        """

        :param draw_func:
        :type draw_func:
        """
        ...

    def type_recast(self): ...
    def values(self): ...

class PHYSICS_PT_dp_effects_shrink(
    PhysicButtonsPanel, bpy_types.Panel, bpy_types._GenericUI
):
    COMPAT_ENGINES: typing.Any
    bl_context: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_parent_id: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any

    def append(self, draw_func):
        """

        :param draw_func:
        :type draw_func:
        """
        ...

    def as_pointer(self): ...
    def bl_rna_get_subclass(self): ...
    def bl_rna_get_subclass_py(self): ...
    def draw(self, context):
        """

        :param self:
        :type self:
        :param context:
        :type context:
        """
        ...

    def draw_header(self, context):
        """

        :param self:
        :type self:
        :param context:
        :type context:
        """
        ...

    def driver_add(self): ...
    def driver_remove(self): ...
    def get(self): ...
    def id_properties_clear(self): ...
    def id_properties_ensure(self): ...
    def id_properties_ui(self): ...
    def is_extended(self): ...
    def is_property_hidden(self): ...
    def is_property_overridable_library(self): ...
    def is_property_readonly(self): ...
    def is_property_set(self): ...
    def items(self): ...
    def keyframe_delete(self): ...
    def keyframe_insert(self): ...
    def keys(self): ...
    def path_from_id(self): ...
    def path_resolve(self): ...
    def poll(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_canvas(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_canvas_brush(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_canvas_paint(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_output(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_output_maps(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_paint(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def pop(self): ...
    def prepend(self, draw_func):
        """

        :param draw_func:
        :type draw_func:
        """
        ...

    def property_overridable_library_set(self): ...
    def property_unset(self): ...
    def remove(self, draw_func):
        """

        :param draw_func:
        :type draw_func:
        """
        ...

    def type_recast(self): ...
    def values(self): ...

class PHYSICS_PT_dp_effects_spread(
    PhysicButtonsPanel, bpy_types.Panel, bpy_types._GenericUI
):
    COMPAT_ENGINES: typing.Any
    bl_context: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_parent_id: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any

    def append(self, draw_func):
        """

        :param draw_func:
        :type draw_func:
        """
        ...

    def as_pointer(self): ...
    def bl_rna_get_subclass(self): ...
    def bl_rna_get_subclass_py(self): ...
    def draw(self, context):
        """

        :param self:
        :type self:
        :param context:
        :type context:
        """
        ...

    def draw_header(self, context):
        """

        :param self:
        :type self:
        :param context:
        :type context:
        """
        ...

    def driver_add(self): ...
    def driver_remove(self): ...
    def get(self): ...
    def id_properties_clear(self): ...
    def id_properties_ensure(self): ...
    def id_properties_ui(self): ...
    def is_extended(self): ...
    def is_property_hidden(self): ...
    def is_property_overridable_library(self): ...
    def is_property_readonly(self): ...
    def is_property_set(self): ...
    def items(self): ...
    def keyframe_delete(self): ...
    def keyframe_insert(self): ...
    def keys(self): ...
    def path_from_id(self): ...
    def path_resolve(self): ...
    def poll(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_canvas(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_canvas_brush(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_canvas_paint(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_output(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_output_maps(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_paint(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def pop(self): ...
    def prepend(self, draw_func):
        """

        :param draw_func:
        :type draw_func:
        """
        ...

    def property_overridable_library_set(self): ...
    def property_unset(self): ...
    def remove(self, draw_func):
        """

        :param draw_func:
        :type draw_func:
        """
        ...

    def type_recast(self): ...
    def values(self): ...

class PHYSICS_PT_dp_surface_canvas(
    PhysicButtonsPanel, bpy_types.Panel, bpy_types._GenericUI
):
    COMPAT_ENGINES: typing.Any
    bl_context: typing.Any
    bl_label: typing.Any
    bl_parent_id: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any

    def append(self, draw_func):
        """

        :param draw_func:
        :type draw_func:
        """
        ...

    def as_pointer(self): ...
    def bl_rna_get_subclass(self): ...
    def bl_rna_get_subclass_py(self): ...
    def draw(self, context):
        """

        :param self:
        :type self:
        :param context:
        :type context:
        """
        ...

    def driver_add(self): ...
    def driver_remove(self): ...
    def get(self): ...
    def id_properties_clear(self): ...
    def id_properties_ensure(self): ...
    def id_properties_ui(self): ...
    def is_extended(self): ...
    def is_property_hidden(self): ...
    def is_property_overridable_library(self): ...
    def is_property_readonly(self): ...
    def is_property_set(self): ...
    def items(self): ...
    def keyframe_delete(self): ...
    def keyframe_insert(self): ...
    def keys(self): ...
    def path_from_id(self): ...
    def path_resolve(self): ...
    def poll(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_canvas(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_canvas_brush(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_canvas_paint(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_output(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_output_maps(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_paint(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def pop(self): ...
    def prepend(self, draw_func):
        """

        :param draw_func:
        :type draw_func:
        """
        ...

    def property_overridable_library_set(self): ...
    def property_unset(self): ...
    def remove(self, draw_func):
        """

        :param draw_func:
        :type draw_func:
        """
        ...

    def type_recast(self): ...
    def values(self): ...

class PHYSICS_PT_dp_surface_canvas_paint_dissolve(
    PhysicButtonsPanel, bpy_types.Panel, bpy_types._GenericUI
):
    COMPAT_ENGINES: typing.Any
    bl_context: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_parent_id: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any

    def append(self, draw_func):
        """

        :param draw_func:
        :type draw_func:
        """
        ...

    def as_pointer(self): ...
    def bl_rna_get_subclass(self): ...
    def bl_rna_get_subclass_py(self): ...
    def draw(self, context):
        """

        :param self:
        :type self:
        :param context:
        :type context:
        """
        ...

    def draw_header(self, context):
        """

        :param self:
        :type self:
        :param context:
        :type context:
        """
        ...

    def driver_add(self): ...
    def driver_remove(self): ...
    def get(self): ...
    def id_properties_clear(self): ...
    def id_properties_ensure(self): ...
    def id_properties_ui(self): ...
    def is_extended(self): ...
    def is_property_hidden(self): ...
    def is_property_overridable_library(self): ...
    def is_property_readonly(self): ...
    def is_property_set(self): ...
    def items(self): ...
    def keyframe_delete(self): ...
    def keyframe_insert(self): ...
    def keys(self): ...
    def path_from_id(self): ...
    def path_resolve(self): ...
    def poll(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_canvas(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_canvas_brush(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_canvas_paint(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_output(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_output_maps(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_paint(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def pop(self): ...
    def prepend(self, draw_func):
        """

        :param draw_func:
        :type draw_func:
        """
        ...

    def property_overridable_library_set(self): ...
    def property_unset(self): ...
    def remove(self, draw_func):
        """

        :param draw_func:
        :type draw_func:
        """
        ...

    def type_recast(self): ...
    def values(self): ...

class PHYSICS_PT_dp_surface_canvas_paint_dry(
    PhysicButtonsPanel, bpy_types.Panel, bpy_types._GenericUI
):
    COMPAT_ENGINES: typing.Any
    bl_context: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_parent_id: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any

    def append(self, draw_func):
        """

        :param draw_func:
        :type draw_func:
        """
        ...

    def as_pointer(self): ...
    def bl_rna_get_subclass(self): ...
    def bl_rna_get_subclass_py(self): ...
    def draw(self, context):
        """

        :param self:
        :type self:
        :param context:
        :type context:
        """
        ...

    def draw_header(self, context):
        """

        :param self:
        :type self:
        :param context:
        :type context:
        """
        ...

    def driver_add(self): ...
    def driver_remove(self): ...
    def get(self): ...
    def id_properties_clear(self): ...
    def id_properties_ensure(self): ...
    def id_properties_ui(self): ...
    def is_extended(self): ...
    def is_property_hidden(self): ...
    def is_property_overridable_library(self): ...
    def is_property_readonly(self): ...
    def is_property_set(self): ...
    def items(self): ...
    def keyframe_delete(self): ...
    def keyframe_insert(self): ...
    def keys(self): ...
    def path_from_id(self): ...
    def path_resolve(self): ...
    def poll(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_canvas(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_canvas_brush(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_canvas_paint(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_output(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_output_maps(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_paint(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def pop(self): ...
    def prepend(self, draw_func):
        """

        :param draw_func:
        :type draw_func:
        """
        ...

    def property_overridable_library_set(self): ...
    def property_unset(self): ...
    def remove(self, draw_func):
        """

        :param draw_func:
        :type draw_func:
        """
        ...

    def type_recast(self): ...
    def values(self): ...

class PHYSICS_PT_dynamic_paint(
    PhysicButtonsPanel, bpy_types.Panel, bpy_types._GenericUI
):
    COMPAT_ENGINES: typing.Any
    bl_context: typing.Any
    bl_label: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any

    def append(self, draw_func):
        """

        :param draw_func:
        :type draw_func:
        """
        ...

    def as_pointer(self): ...
    def bl_rna_get_subclass(self): ...
    def bl_rna_get_subclass_py(self): ...
    def draw(self, context):
        """

        :param self:
        :type self:
        :param context:
        :type context:
        """
        ...

    def driver_add(self): ...
    def driver_remove(self): ...
    def get(self): ...
    def id_properties_clear(self): ...
    def id_properties_ensure(self): ...
    def id_properties_ui(self): ...
    def is_extended(self): ...
    def is_property_hidden(self): ...
    def is_property_overridable_library(self): ...
    def is_property_readonly(self): ...
    def is_property_set(self): ...
    def items(self): ...
    def keyframe_delete(self): ...
    def keyframe_insert(self): ...
    def keys(self): ...
    def path_from_id(self): ...
    def path_resolve(self): ...
    def poll(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_canvas(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_canvas_brush(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_canvas_paint(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_output(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_output_maps(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_paint(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def pop(self): ...
    def prepend(self, draw_func):
        """

        :param draw_func:
        :type draw_func:
        """
        ...

    def property_overridable_library_set(self): ...
    def property_unset(self): ...
    def remove(self, draw_func):
        """

        :param draw_func:
        :type draw_func:
        """
        ...

    def type_recast(self): ...
    def values(self): ...

class PHYSICS_PT_dynamic_paint_settings(
    PhysicButtonsPanel, bpy_types.Panel, bpy_types._GenericUI
):
    COMPAT_ENGINES: typing.Any
    bl_context: typing.Any
    bl_label: typing.Any
    bl_parent_id: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any

    def append(self, draw_func):
        """

        :param draw_func:
        :type draw_func:
        """
        ...

    def as_pointer(self): ...
    def bl_rna_get_subclass(self): ...
    def bl_rna_get_subclass_py(self): ...
    def draw(self, context):
        """

        :param self:
        :type self:
        :param context:
        :type context:
        """
        ...

    def driver_add(self): ...
    def driver_remove(self): ...
    def get(self): ...
    def id_properties_clear(self): ...
    def id_properties_ensure(self): ...
    def id_properties_ui(self): ...
    def is_extended(self): ...
    def is_property_hidden(self): ...
    def is_property_overridable_library(self): ...
    def is_property_readonly(self): ...
    def is_property_set(self): ...
    def items(self): ...
    def keyframe_delete(self): ...
    def keyframe_insert(self): ...
    def keys(self): ...
    def path_from_id(self): ...
    def path_resolve(self): ...
    def poll(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_canvas(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_canvas_brush(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_canvas_paint(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_output(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_output_maps(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def poll_dyn_paint(self, context):
        """

        :param context:
        :type context:
        """
        ...

    def pop(self): ...
    def prepend(self, draw_func):
        """

        :param draw_func:
        :type draw_func:
        """
        ...

    def property_overridable_library_set(self): ...
    def property_unset(self): ...
    def remove(self, draw_func):
        """

        :param draw_func:
        :type draw_func:
        """
        ...

    def type_recast(self): ...
    def values(self): ...
