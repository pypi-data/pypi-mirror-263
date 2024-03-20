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
            "help_string": "input file to 3dSkullStrip",
            "argstr": "-input {in_file}",
            "copyfile": False,
            "mandatory": True,
            "position": 1,
        },
    ),
    (
        "out_file",
        Path,
        {
            "help_string": "output to the file",
            "argstr": "-prefix {out_file}",
            "position": -1,
            "output_file_template": "{in_file}_blur",
        },
    ),
    (
        "mask",
        Nifti1,
        {
            "help_string": "Mask dataset, if desired.  Blurring will occur only within the mask. Voxels NOT in the mask will be set to zero in the output.",
            "argstr": "-mask {mask}",
        },
    ),
    (
        "multimask",
        File,
        {
            "help_string": "Multi-mask dataset -- each distinct nonzero value in dataset will be treated as a separate mask for blurring purposes.",
            "argstr": "-Mmask {multimask}",
        },
    ),
    (
        "automask",
        bool,
        {
            "help_string": "Create an automask from the input dataset.",
            "argstr": "-automask",
        },
    ),
    (
        "fwhm",
        float,
        {
            "help_string": "fwhm kernel size",
            "argstr": "-FWHM {fwhm}",
            "mandatory": True,
        },
    ),
    (
        "preserve",
        bool,
        {
            "help_string": "Normally, voxels not in the mask will be set to zero in the output. If you want the original values in the dataset to be preserved in the output, use this option.",
            "argstr": "-preserve",
        },
    ),
    (
        "float_out",
        bool,
        {
            "help_string": "Save dataset as floats, no matter what the input data type is.",
            "argstr": "-float",
        },
    ),
    ("options", str, {"help_string": "options", "argstr": "{options}", "position": 2}),
    ("num_threads", int, 1, {"help_string": "set number of threads"}),
    ("outputtype", ty.Any, {"help_string": "AFNI output filetype"}),
]
BlurInMask_input_spec = specs.SpecInfo(
    name="Input", fields=input_fields, bases=(specs.ShellSpec,)
)

output_fields = []
BlurInMask_output_spec = specs.SpecInfo(
    name="Output", fields=output_fields, bases=(specs.ShellOutSpec,)
)


class BlurInMask(ShellCommandTask):
    """
    Examples
    -------

    >>> from fileformats.generic import File
    >>> from fileformats.medimage.nifti import Nifti1
    >>> from pydra.tasks.afni.auto.blur_in_mask import BlurInMask

    >>> task = BlurInMask()
    >>> task.inputs.in_file = Nifti1.mock()
    >>> task.inputs.mask = Nifti1.mock()
    >>> task.inputs.multimask = File.mock()
    >>> task.inputs.fwhm = "5.0"
    >>> task.cmdline
    '3dBlurInMask -input functional.nii -FWHM 5.000000 -mask mask.nii -prefix functional_blur'


    """

    input_spec = BlurInMask_input_spec
    output_spec = BlurInMask_output_spec
    executable = "3dBlurInMask"
