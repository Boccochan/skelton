import os
import sys
import shutil
import uuid
from distutils.dir_util import copy_tree


class SkeletonException(Exception):
    ''' Skeleton exception '''


class SkepyCancelled(SkeletonException):
    ''' skepy has been cancelled '''
    

class SkepyTmpdirExist(SkeletonException):
    ''' tmpdir exist. '''


class Project: 
    def __init__(self, project_name: str = None):
        if project_name is None:
            self._project_path = os.getcwd()
        else:
            self._project_path = os.path.join(os.getcwd(), project_name)

        self._module_path = os.path.dirname(sys.modules[__name__].__file__)

        uid = uuid.uuid4()
        dir_path = os.path.dirname(sys.modules[__name__].__file__)
        self._tmpdir_path = os.path.join(dir_path, f'skepy_tmpdir_{uid}') 

    def create_skeleton(self) -> int:
        try:
            if os.path.exists(self._tmpdir_path):
                raise SkepyTmpdirExist
                
            self._copy_template_to_tmpdir()
            self._apply_pkg_name_to_src_dir()
            self._apply_pkg_name_to_files()
            self._copy_templates()

        except SkepyCancelled:
            print('Cancelled', file=sys.stderr)
            return 1 

        except SkepyTmpdirExist:
            print(f'{self._tmpdir_path} already exist.', file=sys.stderr)
            return 2

        finally:
            if os.path.exists(self._tmpdir_path):
                shutil.rmtree(self._tmpdir_path)

        return 0

    def _copy_template_to_tmpdir(self):
        template_path = os.path.join(self._module_path, 'template')        

        copy_tree(template_path, self._tmpdir_path)
    
    def _copy_templates(self):
        if os.path.exists(self._project_path):
            answer = input('Do you want to create your project here? (Y/n):')

            if answer != 'Y':
                raise SkepyCancelled

            copy_tree(self._tmpdir_path, self._project_path)

        else:
            shutil.copytree(self._tmpdir_path, self._project_path)

    def _apply_pkg_name_to_src_dir(self):
        project_name = self._project_path.rsplit(os.path.sep, 1)[-1]

        proj_path = os.path.join(self._tmpdir_path, 'src', project_name)
        if os.path.exists(proj_path):
            shutil.rmtree(proj_path)

        pkg_path = os.path.join(self._tmpdir_path, 'src', 'pkg_name')
        os.rename(pkg_path, proj_path)

    def _apply_pkg_name_to_file(self, path: str, project_name: str):
        with open(path, 'r') as f:
            expandedvars_setup_py = os.path.expandvars(f.read())

        with open(path, 'w') as f:
            f.write(expandedvars_setup_py)

    def _apply_pkg_name_to_files(self):
        os.environ['PKG_NAME'] = self._project_path.rsplit(os.path.sep, 1)[-1]
        project_name = self._project_path.rsplit(os.path.sep, 1)[-1]

        setup_py_path = os.path.join(self._tmpdir_path, 'setup.py')
        self._apply_pkg_name_to_file(setup_py_path, project_name)

        setup_py_path = os.path.join(self._tmpdir_path, 'src', project_name, 'cli.py')
        self._apply_pkg_name_to_file(setup_py_path, project_name)

