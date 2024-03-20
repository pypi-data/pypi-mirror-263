from fileformats.generic import File
from fileformats.medimage.nifti import Nifti1
from pathlib import Path
from pydra.engine import ShellCommandTask
from pydra.engine import specs
import typing as ty

input_fields = [
    (
        "in_file",
        Nifti1,
        {
            "help_string": "input file to 3dCM",
            "argstr": "{in_file}",
            "copyfile": True,
            "mandatory": True,
            "position": -2,
        },
    ),
    (
        "cm_file",
        Path,
        {
            "help_string": "File to write center of mass to",
            "argstr": "> {cm_file}",
            "position": -1,
            "output_file_template": "{in_file}_cm.out",
        },
    ),
    (
        "mask_file",
        File,
        {
            "help_string": "Only voxels with nonzero values in the provided mask will be averaged.",
            "argstr": "-mask {mask_file}",
        },
    ),
    (
        "automask",
        bool,
        {"help_string": "Generate the mask automatically", "argstr": "-automask"},
    ),
    (
        "set_cm",
        ty.Any,
        {
            "help_string": "After computing the center of mass, set the origin fields in the header so that the center of mass will be at (x,y,z) in DICOM coords.",
            "argstr": "-set {set_cm[0]} {set_cm[1]} {set_cm[2]}",
        },
    ),
    (
        "local_ijk",
        bool,
        {
            "help_string": "Output values as (i,j,k) in local orientation",
            "argstr": "-local_ijk",
        },
    ),
    (
        "roi_vals",
        list,
        {
            "help_string": "Compute center of mass for each blob with voxel value of v0, v1, v2, etc. This option is handy for getting ROI centers of mass.",
            "argstr": "-roi_vals {roi_vals}",
        },
    ),
    (
        "all_rois",
        bool,
        {
            "help_string": "Don't bother listing the values of ROIs you want: The program will find all of them and produce a full list",
            "argstr": "-all_rois",
        },
    ),
]
CenterMass_input_spec = specs.SpecInfo(
    name="Input", fields=input_fields, bases=(specs.ShellSpec,)
)

output_fields = [
    ("out_file", File, {"help_string": "output file"}),
    ("cm", list, {"help_string": "center of mass"}),
]
CenterMass_output_spec = specs.SpecInfo(
    name="Output", fields=output_fields, bases=(specs.ShellOutSpec,)
)


class CenterMass(ShellCommandTask):
    """
    Examples
    -------

    >>> from fileformats.generic import File
    >>> from fileformats.medimage.nifti import Nifti1
    >>> from pydra.tasks.afni.auto.center_mass import CenterMass

    >>> task = CenterMass()
    >>> task.inputs.in_file = Nifti1.mock()
    >>> task.inputs.cm_file = ""cm.txt""
    >>> task.inputs.mask_file = File.mock()
    >>> task.inputs.roi_vals = "[2, 10]"
    >>> task.cmdline
    '3dCM -roi_vals 2 10 structural.nii > cm.txt'


    """

    input_spec = CenterMass_input_spec
    output_spec = CenterMass_output_spec
    executable = "3dCM"
