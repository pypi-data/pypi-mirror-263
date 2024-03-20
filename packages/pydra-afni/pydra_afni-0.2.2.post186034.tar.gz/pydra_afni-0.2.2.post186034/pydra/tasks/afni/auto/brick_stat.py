from fileformats.medimage.nifti import Nifti1
from fileformats.medimage.nifti import NiftiGz
from pydra.engine import ShellCommandTask
from pydra.engine import specs
import typing as ty


def min_val_callable(output_dir, inputs, stdout, stderr):
    outputs = _list_outputs(
        output_dir=output_dir, inputs=inputs, stdout=stdout, stderr=stderr
    )
    return outputs["min_val"]


input_fields = [
    (
        "in_file",
        Nifti1,
        {
            "help_string": "input file to 3dmaskave",
            "argstr": "{in_file}",
            "mandatory": True,
            "position": -1,
        },
    ),
    (
        "mask",
        NiftiGz,
        {
            "help_string": "-mask dset = use dset as mask to include/exclude voxels",
            "argstr": "-mask {mask}",
            "position": 2,
        },
    ),
    (
        "min",
        bool,
        {
            "help_string": "print the minimum value in dataset",
            "argstr": "-min",
            "position": 1,
        },
    ),
    (
        "slow",
        bool,
        {
            "help_string": "read the whole dataset to find the min and max values",
            "argstr": "-slow",
        },
    ),
    (
        "max",
        bool,
        {"help_string": "print the maximum value in the dataset", "argstr": "-max"},
    ),
    (
        "mean",
        bool,
        {"help_string": "print the mean value in the dataset", "argstr": "-mean"},
    ),
    (
        "sum",
        bool,
        {"help_string": "print the sum of values in the dataset", "argstr": "-sum"},
    ),
    (
        "var",
        bool,
        {"help_string": "print the variance in the dataset", "argstr": "-var"},
    ),
    (
        "percentile",
        ty.Any,
        {
            "help_string": "p0 ps p1 write the percentile values starting at p0% and ending at p1% at a step of ps%. only one sub-brick is accepted.",
            "argstr": "-percentile {percentile[0]:.3} {percentile[1]:.3} {percentile[2]:.3}",
        },
    ),
]
BrickStat_input_spec = specs.SpecInfo(
    name="Input", fields=input_fields, bases=(specs.ShellSpec,)
)

output_fields = [
    ("min_val", float, {"help_string": "output", "callable": "min_val_callable"})
]
BrickStat_output_spec = specs.SpecInfo(
    name="Output", fields=output_fields, bases=(specs.ShellOutSpec,)
)


class BrickStat(ShellCommandTask):
    """
    Examples
    -------

    >>> from fileformats.medimage.nifti import Nifti1
    >>> from fileformats.medimage.nifti import NiftiGz
    >>> from pydra.tasks.afni.auto.brick_stat import BrickStat

    >>> task = BrickStat()
    >>> task.inputs.in_file = Nifti1.mock()
    >>> task.inputs.mask = NiftiGz.mock()
    >>> task.inputs.min = "True"
    >>> task.cmdline
    '3dBrickStat -min -mask skeleton_mask.nii.gz functional.nii'


    """

    input_spec = BrickStat_input_spec
    output_spec = BrickStat_output_spec
    executable = "3dBrickStat"
