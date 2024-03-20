from fileformats.medimage.nifti import Nifti1
from pathlib import Path
from pydra.engine import ShellCommandTask
from pydra.engine import specs
import typing as ty


def x_max_callable(output_dir, inputs, stdout, stderr):
    outputs = _list_outputs(
        output_dir=output_dir, inputs=inputs, stdout=stdout, stderr=stderr
    )
    return outputs["x_max"]


def x_min_callable(output_dir, inputs, stdout, stderr):
    outputs = _list_outputs(
        output_dir=output_dir, inputs=inputs, stdout=stdout, stderr=stderr
    )
    return outputs["x_min"]


def y_max_callable(output_dir, inputs, stdout, stderr):
    outputs = _list_outputs(
        output_dir=output_dir, inputs=inputs, stdout=stdout, stderr=stderr
    )
    return outputs["y_max"]


def y_min_callable(output_dir, inputs, stdout, stderr):
    outputs = _list_outputs(
        output_dir=output_dir, inputs=inputs, stdout=stdout, stderr=stderr
    )
    return outputs["y_min"]


def z_max_callable(output_dir, inputs, stdout, stderr):
    outputs = _list_outputs(
        output_dir=output_dir, inputs=inputs, stdout=stdout, stderr=stderr
    )
    return outputs["z_max"]


def z_min_callable(output_dir, inputs, stdout, stderr):
    outputs = _list_outputs(
        output_dir=output_dir, inputs=inputs, stdout=stdout, stderr=stderr
    )
    return outputs["z_min"]


input_fields = [
    (
        "in_file",
        Nifti1,
        {
            "help_string": "input file",
            "argstr": "-input {in_file}",
            "copyfile": False,
            "mandatory": True,
        },
    ),
    (
        "padding",
        int,
        {
            "help_string": "Number of extra voxels to pad on each side of box",
            "argstr": "-npad {padding}",
        },
    ),
    (
        "out_file",
        Path,
        {
            "help_string": "",
            "argstr": "-prefix {out_file}",
            "output_file_template": "{in_file}_autobox",
        },
    ),
    (
        "no_clustering",
        bool,
        {
            "help_string": "Don't do any clustering to find box. Any non-zero voxel will be preserved in the cropped volume. The default method uses some clustering to find the cropping box, and will clip off small isolated blobs.",
            "argstr": "-noclust",
        },
    ),
    ("num_threads", int, 1, {"help_string": "set number of threads"}),
    ("outputtype", ty.Any, {"help_string": "AFNI output filetype"}),
]
Autobox_input_spec = specs.SpecInfo(
    name="Input", fields=input_fields, bases=(specs.ShellSpec,)
)

output_fields = [
    ("x_min", int, {"callable": "x_min_callable"}),
    ("x_max", int, {"callable": "x_max_callable"}),
    ("y_min", int, {"callable": "y_min_callable"}),
    ("y_max", int, {"callable": "y_max_callable"}),
    ("z_min", int, {"callable": "z_min_callable"}),
    ("z_max", int, {"callable": "z_max_callable"}),
]
Autobox_output_spec = specs.SpecInfo(
    name="Output", fields=output_fields, bases=(specs.ShellOutSpec,)
)


class Autobox(ShellCommandTask):
    """
    Examples
    -------

    >>> from fileformats.medimage.nifti import Nifti1
    >>> from pydra.tasks.afni.auto.autobox import Autobox

    >>> task = Autobox()
    >>> task.inputs.in_file = Nifti1.mock()
    >>> task.inputs.padding = "5"
    >>> task.cmdline
    '3dAutobox -input structural.nii -prefix structural_autobox -npad 5'


    """

    input_spec = Autobox_input_spec
    output_spec = Autobox_output_spec
    executable = "3dAutobox"
