from fileformats.medimage.surface import Gifti
from fileformats.medimage_afni import Dset
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.auto.convert_dset import ConvertDset
import pytest


@pytest.mark.xfail
def test_convertdset_1():
    task = ConvertDset()
    task.inputs.in_file = Gifti.sample(seed=0)
    task.inputs.num_threads = 1
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(plugin=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_convertdset_2():
    task = ConvertDset()
    task.inputs.in_file = Gifti.sample(seed=0)
    task.inputs.out_file = "lh.pial_converted.niml.dset"
    task.inputs.out_type = "niml_asc"
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(plugin=PassAfterTimeoutWorker)
    print("RESULT: ", res)
