from fileformats.medimage.nifti import Nifti1
from fileformats.medimage_afni import OneD
from pathlib import Path
from pydra.engine import ShellCommandTask
from pydra.engine import specs
import typing as ty

input_fields = [
    (
        "xset",
        Nifti1,
        {
            "help_string": "3d+time dataset input",
            "argstr": " {xset}",
            "copyfile": False,
            "mandatory": True,
            "position": -2,
        },
    ),
    (
        "y_1d",
        OneD,
        {
            "help_string": "1D time series file input",
            "argstr": " {y_1d}",
            "mandatory": True,
            "position": -1,
        },
    ),
    (
        "out_file",
        Path,
        {
            "help_string": "output filename prefix",
            "argstr": "-prefix {out_file}",
            "output_file_template": "{xset}_correlation.nii.gz",
        },
    ),
    (
        "pearson",
        bool,
        {
            "help_string": "Correlation is the normal Pearson correlation coefficient",
            "argstr": " -pearson",
            "position": 1,
            "xor": ["spearman", "quadrant", "ktaub"],
        },
    ),
    (
        "spearman",
        bool,
        {
            "help_string": "Correlation is the Spearman (rank) correlation coefficient",
            "argstr": " -spearman",
            "position": 1,
            "xor": ["pearson", "quadrant", "ktaub"],
        },
    ),
    (
        "quadrant",
        bool,
        {
            "help_string": "Correlation is the quadrant correlation coefficient",
            "argstr": " -quadrant",
            "position": 1,
            "xor": ["pearson", "spearman", "ktaub"],
        },
    ),
    (
        "ktaub",
        bool,
        {
            "help_string": "Correlation is the Kendall's tau_b correlation coefficient",
            "argstr": " -ktaub",
            "position": 1,
            "xor": ["pearson", "spearman", "quadrant"],
        },
    ),
    ("num_threads", int, 1, {"help_string": "set number of threads"}),
    ("outputtype", ty.Any, {"help_string": "AFNI output filetype"}),
]
TCorr1D_input_spec = specs.SpecInfo(
    name="Input", fields=input_fields, bases=(specs.ShellSpec,)
)

output_fields = []
TCorr1D_output_spec = specs.SpecInfo(
    name="Output", fields=output_fields, bases=(specs.ShellOutSpec,)
)


class TCorr1D(ShellCommandTask):
    """
    Examples
    -------

    >>> from fileformats.medimage.nifti import Nifti1
    >>> from fileformats.medimage_afni import OneD
    >>> from pydra.tasks.afni.auto.t_corr_1d import TCorr1D

    >>> task = TCorr1D()
    >>> task.inputs.xset = Nifti1.mock()
    >>> task.inputs.y_1d = OneD.mock()
    >>> task.cmdline
    '3dTcorr1D -prefix u_rc1s1_Template_correlation.nii.gz u_rc1s1_Template.nii seed.1D'


    """

    input_spec = TCorr1D_input_spec
    output_spec = TCorr1D_output_spec
    executable = "3dTcorr1D"
