from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.auto.nwarp_cat import NwarpCat
import pytest


@pytest.mark.xfail
def test_nwarpcat_1():
    task = NwarpCat()
    task.inputs.interp = "wsinc5"
    task.inputs.num_threads = 1
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(plugin=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_nwarpcat_2():
    task = NwarpCat()
    task.inputs.in_files = ["Q25_warp+tlrc.HEAD", ("IDENT", "structural.nii")]
    task.inputs.out_file = "Fred_total_WARP"
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(plugin=PassAfterTimeoutWorker)
    print("RESULT: ", res)
