from fileformats.generic import File
from fileformats.medimage.nifti import Nifti1
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.auto.align_epi_anat_py import AlignEpiAnatPy
import pytest


@pytest.mark.xfail
def test_alignepianatpy_1():
    task = AlignEpiAnatPy()
    task.inputs.in_file = Nifti1.sample(seed=0)
    task.inputs.anat = Nifti1.sample(seed=1)
    task.inputs.anat2epi = False
    task.inputs.epi2anat = False
    task.inputs.suffix = "_al"
    task.inputs.epi_strip = "3dSkullStrip"
    task.inputs.volreg = "on"
    task.inputs.tshift = "on"
    task.inputs.outputtype = "AFNI"
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(plugin=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_alignepianatpy_2():
    task = AlignEpiAnatPy()
    task.inputs.in_file = Nifti1.sample(seed=0)
    task.inputs.anat = Nifti1.sample(seed=1)
    task.inputs.epi_base = 0
    task.inputs.save_skullstrip = True
    task.inputs.epi_strip = "3dAutomask"
    task.inputs.volreg = "off"
    task.inputs.tshift = "off"
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(plugin=PassAfterTimeoutWorker)
    print("RESULT: ", res)
