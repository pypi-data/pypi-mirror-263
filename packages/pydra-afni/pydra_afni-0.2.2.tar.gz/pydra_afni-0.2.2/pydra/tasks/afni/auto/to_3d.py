from fileformats.generic import Directory
from pathlib import Path
from pydra.engine import ShellCommandTask
from pydra.engine import specs
import typing as ty

input_fields = [
    (
        "out_file",
        Path,
        {
            "help_string": "output image file name",
            "argstr": "-prefix {out_file}",
            "output_file_template": "{in_folder}",
        },
    ),
    (
        "in_folder",
        Directory,
        {
            "help_string": "folder with DICOM images to convert",
            "argstr": "{in_folder}/*.dcm",
            "mandatory": True,
            "position": -1,
        },
    ),
    (
        "filetype",
        ty.Any,
        {"help_string": "type of datafile being converted", "argstr": "-{filetype}"},
    ),
    (
        "skipoutliers",
        bool,
        {"help_string": "skip the outliers check", "argstr": "-skip_outliers"},
    ),
    (
        "assumemosaic",
        bool,
        {
            "help_string": "assume that Siemens image is mosaic",
            "argstr": "-assume_dicom_mosaic",
        },
    ),
    (
        "datatype",
        ty.Any,
        {"help_string": "set output file datatype", "argstr": "-datum {datatype}"},
    ),
    (
        "funcparams",
        str,
        {
            "help_string": "parameters for functional data",
            "argstr": "-time:zt {funcparams} alt+z2",
        },
    ),
    ("num_threads", int, 1, {"help_string": "set number of threads"}),
    ("outputtype", ty.Any, {"help_string": "AFNI output filetype"}),
]
To3D_input_spec = specs.SpecInfo(
    name="Input", fields=input_fields, bases=(specs.ShellSpec,)
)

output_fields = []
To3D_output_spec = specs.SpecInfo(
    name="Output", fields=output_fields, bases=(specs.ShellOutSpec,)
)


class To3D(ShellCommandTask):
    """
    Examples
    -------

    >>> from fileformats.generic import Directory
    >>> from pydra.tasks.afni.auto.to_3d import To3D

    >>> task = To3D()
    >>> task.inputs.out_file = ""dicomdir.nii""
    >>> task.inputs.in_folder = "".""
    >>> task.inputs.filetype = ""anat""
    >>> task.inputs.datatype = ""float""
    >>> task.cmdline
    'to3d -datum float -anat -prefix dicomdir.nii ./*.dcm'


    """

    input_spec = To3D_input_spec
    output_spec = To3D_output_spec
    executable = "to3d"
