# import os
# import dotenv
# import pytest
# from click.testing import CliRunner

# from np_upload_validation.scripts import main


# dotenv.load_dotenv()

# RAW_PATH = os.getenv("RAW_PATH")

# @pytest.mark.skipif(
#     RAW_PATH is None,
#     reason="No raw path."
# )
# # @pytest.mark.slow
# # @pytest.mark.onprem
# def test_memoize_raw_medians(tmp_path) -> None:
#     channel_index = 0
#     runner = CliRunner()
#     # Test without name
#     result = runner.invoke(
#         main.memoize_raw_medians,
#         [
#             RAW_PATH,
#             str(tmp_path),
#             f"{channel_index}",
#         ],
#     )
#     assert result.exit_code == 0
