import atexit
import shutil
import site


def uninstall():
    # Path to the folder to be removed
    name = 'PyLLSM5DTools'
    version = '1.0.0'
    #folder_path = f"{site.getsitepackages()[0]}/{name}-{version}.dist-info/MATLAB_Runtime"
    folder_path = '/home/matt/miniconda3/envs/PyLLSM5DTools/PyLLSM5DTools-1.0.0.dist-info/MATLAB_Runtime'

    # Remove the entire folder
    shutil.rmtree(folder_path, ignore_errors=True)


# Register the uninstall function to be called at exit
atexit.register(uninstall)
