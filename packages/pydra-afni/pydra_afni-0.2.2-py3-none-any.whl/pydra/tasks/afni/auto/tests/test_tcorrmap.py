from fileformats.generic import File
from fileformats.medimage.nifti import Nifti1
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.auto.t_corr_map import TCorrMap
import pytest


@pytest.mark.xfail
def test_tcorrmap_1():
    task = TCorrMap()
    task.inputs.in_file = Nifti1.sample(seed=0)
    task.inputs.seeds = File.sample(seed=1)
    task.inputs.mask = Nifti1.sample(seed=2)
    task.inputs.regress_out_timeseries = File.sample(seed=6)
    task.inputs.num_threads = 1
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(plugin=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_tcorrmap_2():
    task = TCorrMap()
    task.inputs.in_file = Nifti1.sample(seed=0)
    task.inputs.mask = Nifti1.sample(seed=2)
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(plugin=PassAfterTimeoutWorker)
    print("RESULT: ", res)
