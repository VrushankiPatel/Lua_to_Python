Installation
============
These instructions presume that you have a local copy of the source code tree that you obtained by using "git clone" or by unzipping a tarball or zip file. Additionally, they presume that Python 3.10 or later be installed and available under the name "python."

Python venv, ###
Make a virtualenv, most likely in the source root directory:

python -m venv venv


Activate venv (linux/mac): 
bash 
source venv/bin/activate
which python
#Python should now point to venv/bin/python after running the command.


venv may be activated using Windows PowerShell by typing:
 powershell
venv may be activated using Windows PowerShell by typing:


Activate.ps1
#'where.exe python' should point to the venv's python binary


The package can now be installed using "pip" as explained below under "Install as developer" or "Install as standard package"

Turn off venv when finished

deactivate


Install as developer: ###
Run the following commands to install as a developer while the virtual environment is active as previously mentioned:

pip install -r requirements.txt
pip install -e.

(The abbreviation "-e" stands for "--editable").

Pip installs the package as symlinks referring to the source code tree when the "editable" flag is set. As a result, changes made to the package's source code are reflected in the installed version without the need for a fresh installation.
