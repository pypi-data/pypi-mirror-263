from fileformats.generic import File
from fileformats.medimage.nifti import Nifti1
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.auto.center_mass import CenterMass
import pytest


@pytest.mark.xfail
def test_centermass_1():
    task = CenterMass()
    task.inputs.in_file = Nifti1.sample(seed=0)
    task.inputs.mask_file = File.sample(seed=2)
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(plugin=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_centermass_2():
    task = CenterMass()
    task.inputs.in_file = Nifti1.sample(seed=0)
    task.inputs.cm_file = "cm.txt"
    task.inputs.roi_vals = [2, 10]
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(plugin=PassAfterTimeoutWorker)
    print("RESULT: ", res)
