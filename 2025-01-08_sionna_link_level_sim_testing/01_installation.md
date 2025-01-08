# Installing and running Sionna

## Installing in Win 11 with VS Code

1.  Install Git for Windows (64 bit):
    In order to checkout/clone the repo you need to have gitbash.  Download it here:
    https://git-scm.com/downloads/win

    The Git installation for Windows will include 'git bash'.

2.  Use gitbash to clone the Sionna github repo:

    `$ git clone https://github.com/NVlabs/sionna.git`

3.  Install Python 3.11.9:  
    At the time of writing, the latest Python version is Python 3.13.x, so it's likely you'll need to find the older version as the later versions of Python like 3.12.x do not have the compatible Tensorflow version in pip.  Find the appropriate Windows installer here:  https://www.python.org/downloads/windows/

4.  Clone the Sionna repo and install in a `venv` environment:
    Open the cloned Sionna repo in VS Code and use the Command Palette to `'Python: Create Environment'` using `venv` and the Python 3.11.9 interpreter.  Select package installation using the `requirements.txt` file.

5.  Test the installation:  
    Restart the VS Code terminal run `python` ensuring it's using the 3.11.9 interpreter.  Then try:

    ```
    >>> import sionna
    >>> print(sionna.__version__)
    0.19.1
    ```

    You're now runnning Sionna, well done!

6.  Next steps:
    Try running the tutorial ipynb notebooks in the Sionna repo.