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
            "help_string": "input dataset",
            "argstr": "{in_file}",
            "mandatory": True,
            "position": -2,
        },
    ),
    (
        "mask",
        File,
        {
            "help_string": "only count voxels within the given mask",
            "argstr": "-mask {mask}",
            "xor": ["autoclip", "automask"],
        },
    ),
    (
        "qthr",
        ty.Any,
        0.001,
        {
            "help_string": "indicate a value for q to compute alpha",
            "argstr": "-qthr {qthr:.5}",
        },
    ),
    (
        "autoclip",
        bool,
        False,
        {
            "help_string": "clip off small voxels",
            "argstr": "-autoclip",
            "xor": ["mask"],
        },
    ),
    (
        "automask",
        bool,
        False,
        {
            "help_string": "clip off small voxels",
            "argstr": "-automask",
            "xor": ["mask"],
        },
    ),
    (
        "fraction",
        bool,
        False,
        {
            "help_string": "write out the fraction of masked voxels which are outliers at each timepoint",
            "argstr": "-fraction",
        },
    ),
    (
        "interval",
        bool,
        False,
        {
            "help_string": "write out the median + 3.5 MAD of outlier count with each timepoint",
            "argstr": "-range",
        },
    ),
    ("save_outliers", bool, False, {"help_string": "enables out_file option"}),
    (
        "outliers_file",
        File,
        {"help_string": "output image file name", "argstr": "-save {outliers_file}"},
    ),
    (
        "polort",
        int,
        {
            "help_string": "detrend each voxel timeseries with polynomials",
            "argstr": "-polort {polort}",
        },
    ),
    (
        "legendre",
        bool,
        False,
        {"help_string": "use Legendre polynomials", "argstr": "-legendre"},
    ),
    (
        "out_file",
        Path,
        {
            "help_string": "capture standard output",
            "output_file_template": "{in_file}_outliers",
        },
    ),
]
OutlierCount_input_spec = specs.SpecInfo(
    name="Input", fields=input_fields, bases=(specs.ShellSpec,)
)

output_fields = [("out_outliers", File, {"help_string": "output image file name"})]
OutlierCount_output_spec = specs.SpecInfo(
    name="Output", fields=output_fields, bases=(specs.ShellOutSpec,)
)


class OutlierCount(ShellCommandTask):
    """
    Examples
    -------

    >>> from fileformats.generic import File
    >>> from fileformats.medimage.nifti import Nifti1
    >>> from pydra.tasks.afni.auto.outlier_count import OutlierCount

    >>> task = OutlierCount()
    >>> task.inputs.in_file = Nifti1.mock()
    >>> task.inputs.mask = File.mock()
    >>> task.inputs.outliers_file = File.mock()
    >>> task.cmdline
    '3dToutcount -qthr 0.00100 functional.nii'


    """

    input_spec = OutlierCount_input_spec
    output_spec = OutlierCount_output_spec
    executable = "3dToutcount"
