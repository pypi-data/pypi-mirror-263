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
            "help_string": "input file to 3dDetrend",
            "argstr": "{in_file}",
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
            "output_file_template": "{in_file}_detrend",
        },
    ),
    ("num_threads", int, 1, {"help_string": "set number of threads"}),
    ("outputtype", ty.Any, {"help_string": "AFNI output filetype"}),
]
Detrend_input_spec = specs.SpecInfo(
    name="Input", fields=input_fields, bases=(specs.ShellSpec,)
)

output_fields = []
Detrend_output_spec = specs.SpecInfo(
    name="Output", fields=output_fields, bases=(specs.ShellOutSpec,)
)


class Detrend(ShellCommandTask):
    """
    Examples
    -------

    >>> from fileformats.medimage.nifti import Nifti1
    >>> from pydra.tasks.afni.auto.detrend import Detrend

    >>> task = Detrend()
    >>> task.inputs.in_file = Nifti1.mock()
    >>> task.inputs.outputtype = ""AFNI""
    >>> task.cmdline
    '3dDetrend -polort 2 -prefix functional_detrend functional.nii'


    """

    input_spec = Detrend_input_spec
    output_spec = Detrend_output_spec
    executable = "3dDetrend"
