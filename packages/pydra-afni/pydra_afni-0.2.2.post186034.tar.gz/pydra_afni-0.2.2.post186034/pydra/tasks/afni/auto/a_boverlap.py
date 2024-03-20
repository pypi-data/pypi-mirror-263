from fileformats.medimage.nifti import Nifti1
from fileformats.text import TextFile
from pathlib import Path
from pydra.engine import ShellCommandTask
from pydra.engine import specs
import typing as ty

input_fields = [
    (
        "in_file_a",
        Nifti1,
        {
            "help_string": "input file A",
            "argstr": "{in_file_a}",
            "copyfile": False,
            "mandatory": True,
            "position": -3,
        },
    ),
    (
        "in_file_b",
        Nifti1,
        {
            "help_string": "input file B",
            "argstr": "{in_file_b}",
            "copyfile": False,
            "mandatory": True,
            "position": -2,
        },
    ),
    (
        "out_file",
        Path,
        {
            "help_string": "collect output to a file",
            "argstr": " |& tee {out_file}",
            "position": -1,
        },
    ),
    (
        "no_automask",
        bool,
        {"help_string": "consider input datasets as masks", "argstr": "-no_automask"},
    ),
    (
        "quiet",
        bool,
        {
            "help_string": "be as quiet as possible (without being entirely mute)",
            "argstr": "-quiet",
        },
    ),
    (
        "verb",
        bool,
        {
            "help_string": "print out some progress reports (to stderr)",
            "argstr": "-verb",
        },
    ),
    ("num_threads", int, 1, {"help_string": "set number of threads"}),
    ("outputtype", ty.Any, {"help_string": "AFNI output filetype"}),
]
ABoverlap_input_spec = specs.SpecInfo(
    name="Input", fields=input_fields, bases=(specs.ShellSpec,)
)

output_fields = [("out_file", TextFile, {"help_string": "output file"})]
ABoverlap_output_spec = specs.SpecInfo(
    name="Output", fields=output_fields, bases=(specs.ShellOutSpec,)
)


class ABoverlap(ShellCommandTask):
    """
    Examples
    -------

    >>> from fileformats.medimage.nifti import Nifti1
    >>> from fileformats.text import TextFile
    >>> from pydra.tasks.afni.auto.a_boverlap import ABoverlap

    >>> task = ABoverlap()
    >>> task.inputs.in_file_a = Nifti1.mock()
    >>> task.inputs.in_file_b = Nifti1.mock()
    >>> task.inputs.out_file = " "out.mask_ae_overlap.txt""
    >>> task.cmdline
    '3dABoverlap functional.nii structural.nii |& tee out.mask_ae_overlap.txt'


    """

    input_spec = ABoverlap_input_spec
    output_spec = ABoverlap_output_spec
    executable = "3dABoverlap"
