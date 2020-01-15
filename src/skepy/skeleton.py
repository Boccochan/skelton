import os
import sys
import shutil
from distutils.dir_util import copy_tree
from jinja2 import Template, Environment, FileSystemLoader


class SkeletonException(Exception):
    ''' Skeleton exception '''


class SkepyCancelled(SkeletonException):
    ''' skepy has been cancelled '''


class Project: 
    def __init__(self, project_name: str = None):
        if project_name is None:
            self._project_path = os.getcwd()
        else:
            self._project_path = os.path.join(os.getcwd(), project_name)

    def copy_template(self):
        dir_path = os.path.dirname(sys.modules[__name__].__file__)
        template_path = os.path.join(dir_path, 'template')        

        if os.path.exists(self._project_path):
            answer = input('Do you want to create your project here? (Y/n):')

            if answer != 'Y':
                raise SkepyCancelled

            copy_tree(template_path, self._project_path)

        else:
            shutil.copytree(template_path, self._project_path)

    def apply_pkg_name_to_src_dir(self):
        project_name = self._project_path.rsplit(os.path.sep, 1)[-1]
        proj_path = os.path.join(self._project_path, 'src', project_name)
        pkg_path = os.path.join(self._project_path, 'src', 'pkg_name')

        if os.path.exists(proj_path):
            shutil.rmtree(proj_path)

        os.rename(pkg_path, proj_path)

    def _apply_pkg_name_to_file(self, path: str, project_name: str):
        os.environ['PKG_NAME'] = project_name

        expandedvars_setup_py = self._expandvars(path)

        with open(path, 'w') as f:
            f.write(expandedvars_setup_py)

    def apply_pkg_name_to_files(self):
        project_name = self._project_path.rsplit(os.path.sep, 1)[-1]

        setup_py_path = os.path.join(self._project_path, 'setup.py')
        self._apply_pkg_name_to_file(setup_py_path, project_name)

        setup_py_path = os.path.join(self._project_path, 'src', project_name, 'cli.py')
        self._apply_pkg_name_to_file(setup_py_path, project_name)

    def _expandvars(self, path):
        with open(path, 'r') as f:
            return os.path.expandvars(f.read())

