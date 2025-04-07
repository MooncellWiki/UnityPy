import os
from tempfile import TemporaryDirectory

from UnityPy.tools.extractor import extract_assets

SAMPLES = os.path.join(os.path.dirname(os.path.abspath(__file__)), "samples")


def test_ak():
    os.environ['UNITYPY_AK'] = '1'
    
    temp_dir = TemporaryDirectory(prefix="unitypy_test_ak")
    extract_assets(
        SAMPLES,
        temp_dir.name,
        True,
    )
    files = [
        os.path.relpath(os.path.join(root, f), temp_dir.name)
        for root, dirs, files in os.walk(temp_dir.name)
        for f in files
    ]
    print(files)
    temp_dir.cleanup()
    assert len(files) == 46


if __name__ == "__main__":
    test_ak()
