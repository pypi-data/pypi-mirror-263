from pathlib import Path
from pydra.engine import ShellCommandTask
from pydra.engine import specs
import typing as ty

input_fields = [
    (
        "in_file",
        list,
        {
            "help_string": "list of tuples of mfiles and associated opkeys",
            "argstr": "{in_file}",
            "mandatory": True,
            "position": -2,
        },
    ),
    (
        "out_file",
        Path,
        {
            "help_string": "File to write concattenated matvecs to",
            "argstr": " > {out_file}",
            "mandatory": True,
            "position": -1,
            "output_file_template": "{in_file}_cat.aff12.1D",
        },
    ),
    (
        "matrix",
        bool,
        {
            "help_string": "indicates that the resulting matrix willbe written to outfile in the 'MATRIX(...)' format (FORM 3).This feature could be used, with clever scripting, to inputa matrix directly on the command line to program 3dWarp.",
            "argstr": "-MATRIX",
            "xor": ["oneline", "fourxfour"],
        },
    ),
    (
        "oneline",
        bool,
        {
            "help_string": "indicates that the resulting matrixwill simply be written as 12 numbers on one line.",
            "argstr": "-ONELINE",
            "xor": ["matrix", "fourxfour"],
        },
    ),
    (
        "fourxfour",
        bool,
        {
            "help_string": "Output matrix in augmented form (last row is 0 0 0 1)This option does not work with -MATRIX or -ONELINE",
            "argstr": "-4x4",
            "xor": ["matrix", "oneline"],
        },
    ),
    ("num_threads", int, 1, {"help_string": "set number of threads"}),
    ("outputtype", ty.Any, {"help_string": "AFNI output filetype"}),
]
CatMatvec_input_spec = specs.SpecInfo(
    name="Input", fields=input_fields, bases=(specs.ShellSpec,)
)

output_fields = []
CatMatvec_output_spec = specs.SpecInfo(
    name="Output", fields=output_fields, bases=(specs.ShellOutSpec,)
)


class CatMatvec(ShellCommandTask):
    """
    Examples
    -------

    >>> from pydra.tasks.afni.auto.cat_matvec import CatMatvec

    >>> task = CatMatvec()
    >>> task.inputs.in_file = "[("structural.BRIK::WARP_DATA","I")]"
    >>> task.inputs.out_file = ""warp.anat.Xat.1D""
    >>> task.cmdline
    'cat_matvec structural.BRIK::WARP_DATA -I > warp.anat.Xat.1D'


    """

    input_spec = CatMatvec_input_spec
    output_spec = CatMatvec_output_spec
    executable = "cat_matvec"
