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
            "help_string": "input file to 3dDespike",
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
            "output_file_template": "{in_file}_despike",
        },
    ),
    ("num_threads", int, 1, {"help_string": "set number of threads"}),
    ("outputtype", ty.Any, {"help_string": "AFNI output filetype"}),
]
Despike_input_spec = specs.SpecInfo(
    name="Input", fields=input_fields, bases=(specs.ShellSpec,)
)

output_fields = []
Despike_output_spec = specs.SpecInfo(
    name="Output", fields=output_fields, bases=(specs.ShellOutSpec,)
)


class Despike(ShellCommandTask):
    """
    Examples
    -------

    >>> from fileformats.medimage.nifti import Nifti1
    >>> from pydra.tasks.afni.auto.despike import Despike

    >>> task = Despike()
    >>> task.inputs.in_file = Nifti1.mock()
    >>> task.cmdline
    '3dDespike -prefix functional_despike functional.nii'


    """

    input_spec = Despike_input_spec
    output_spec = Despike_output_spec
    executable = "3dDespike"
