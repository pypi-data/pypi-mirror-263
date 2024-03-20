from fileformats.medimage.nifti import Nifti1
from pathlib import Path
from pydra.engine import ShellCommandTask
from pydra.engine import specs
import typing as ty

input_fields = [
    (
        "in_files",
        ty.List[Nifti1],
        {
            "help_string": "input file to 3dTcat",
            "argstr": " {in_files}",
            "copyfile": False,
            "mandatory": True,
            "position": -1,
        },
    ),
    (
        "out_file",
        Path,
        {
            "help_string": "output image file name",
            "argstr": "-prefix {out_file}",
            "output_file_template": "{in_files}_tcat",
        },
    ),
    (
        "rlt",
        ty.Any,
        {
            "help_string": "Remove linear trends in each voxel time series loaded from each input dataset, SEPARATELY. Option -rlt removes the least squares fit of 'a+b*t' to each voxel time series. Option -rlt+ adds dataset mean back in. Option -rlt++ adds overall mean of all dataset timeseries back in.",
            "argstr": "-rlt{rlt}",
            "position": 1,
        },
    ),
    (
        "verbose",
        bool,
        {
            "help_string": "Print out some verbose output as the program",
            "argstr": "-verb",
        },
    ),
    ("num_threads", int, 1, {"help_string": "set number of threads"}),
    ("outputtype", ty.Any, {"help_string": "AFNI output filetype"}),
]
TCat_input_spec = specs.SpecInfo(
    name="Input", fields=input_fields, bases=(specs.ShellSpec,)
)

output_fields = []
TCat_output_spec = specs.SpecInfo(
    name="Output", fields=output_fields, bases=(specs.ShellOutSpec,)
)


class TCat(ShellCommandTask):
    """
    Examples
    -------

    >>> from fileformats.medimage.nifti import Nifti1
    >>> from pydra.tasks.afni.auto.t_cat import TCat

    >>> task = TCat()
    >>> task.inputs.in_files = None
    >>> task.inputs.out_file = ""functional_tcat.nii""
    >>> task.inputs.rlt = ""+""
    >>> task.cmdline
    '3dTcat -rlt+ -prefix functional_tcat.nii functional.nii functional2.nii'


    """

    input_spec = TCat_input_spec
    output_spec = TCat_output_spec
    executable = "3dTcat"
