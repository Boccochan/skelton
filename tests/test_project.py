import os 
import filecmp

from src.skepy import skeleton 


class TestCopyTemplate:
    def test_copy_template_to_current_dir_as_test_project(self, tmpdir):
        tmpdir.chdir()

        proj = skeleton.Project('test_project')
        proj.copy_template()

        assert os.path.exists("test_project")

    def test_copy_contents_of_template_to_current_dir(self, tmpdir):
        tmpdir.chdir()
        import sys
        dir_path = os.path.dirname(sys.modules[__name__].__file__)
        print(dir_path)
        # assert filecmp.cmpfiles('./', '')