from fileformats.generic import File
from fileformats.medimage.nifti import Nifti1
from pydra.engine import ShellCommandTask
from pydra.engine import specs


def clip_val_callable(output_dir, inputs, stdout, stderr):
    outputs = _list_outputs(
        output_dir=output_dir, inputs=inputs, stdout=stdout, stderr=stderr
    )
    return outputs["clip_val"]


input_fields = [
    (
        "in_file",
        Nifti1,
        {
            "help_string": "input file to 3dClipLevel",
            "argstr": "{in_file}",
            "mandatory": True,
            "position": -1,
        },
    ),
    (
        "mfrac",
        float,
        {
            "help_string": "Use the number ff instead of 0.50 in the algorithm",
            "argstr": "-mfrac {mfrac}",
            "position": 2,
        },
    ),
    (
        "doall",
        bool,
        {
            "help_string": "Apply the algorithm to each sub-brick separately.",
            "argstr": "-doall",
            "position": 3,
            "xor": "grad",
        },
    ),
    (
        "grad",
        File,
        {
            "help_string": "Also compute a 'gradual' clip level as a function of voxel position, and output that to a dataset.",
            "argstr": "-grad {grad}",
            "position": 3,
            "xor": "doall",
        },
    ),
]
ClipLevel_input_spec = specs.SpecInfo(
    name="Input", fields=input_fields, bases=(specs.ShellSpec,)
)

output_fields = [
    ("clip_val", float, {"help_string": "output", "callable": "clip_val_callable"})
]
ClipLevel_output_spec = specs.SpecInfo(
    name="Output", fields=output_fields, bases=(specs.ShellOutSpec,)
)


class ClipLevel(ShellCommandTask):
    """
    Examples
    -------

    >>> from fileformats.generic import File
    >>> from fileformats.medimage.nifti import Nifti1
    >>> from pydra.tasks.afni.auto.clip_level import ClipLevel

    >>> task = ClipLevel()
    >>> task.inputs.in_file = Nifti1.mock()
    >>> task.inputs.grad = File.mock()
    >>> task.cmdline
    '3dClipLevel anatomical.nii'


    """

    input_spec = ClipLevel_input_spec
    output_spec = ClipLevel_output_spec
    executable = "3dClipLevel"
