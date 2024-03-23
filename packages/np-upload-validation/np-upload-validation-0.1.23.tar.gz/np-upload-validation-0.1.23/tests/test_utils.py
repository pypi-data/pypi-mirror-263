# import pytest
# import pathlib

# from np_upload_validation import utils


# @pytest.mark.parametrize("args, expected", [
#     (
#         (
#             pathlib.Path('//allen/programs/mindscope/workgroups/dynamicrouting/PilotEphys/Task 2 pilot/DRpilot_686176_20231206/DRpilot_686176_20231206/Record Node 104/experiment1/recording2/continuous/Neuropix-PXI-100.ProbeD-AP/continuous.dat'),
#             pathlib.Path('aind-ephys-data/ecephys_686176_2023-12-06_13-03-34/ecephys_compressed/experiment1_Record Node 104#Neuropix-PXI-100.ProbeD-AP.zarr'),
#         ),
#         False,
#     )
# ])
# def test_compare_paths(args, expected) -> None:
#     assert utils.compare_paths(*args) == expected
