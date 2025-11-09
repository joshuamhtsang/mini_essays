# Installing and running Sionna

## Installing in Ubuntu 24.04 using `uv`

Initiate the uv project:
~~~
$ uv init
~~~

Add the sionna package to a venv:
~~~
$ uv add sionna
~~~

Show the version of sionna installed:
~~~
$ uv pip show sionna
Name: sionna
Version: 1.2.1
~~~

Note that you should NOT do the following:

~~~
$ uv add numpy matplotlib ... sionna
~~~

as this seems to install the older Sionna version 0.8 instead.

## Enabling GPU CUDA computation

Ensure you have the CUDA toolkit installed.

~~~
$ sudo apt update
$ sudo apt install nvidia-cuda-toolkit
~~~


## Basic Test for Running Sionna (Version 1.2.1 in October 2025)

https://nvlabs.github.io/sionna/phy/tutorials/Hello_World.html

~~~
$ uv run main.py

gpu_num: 0
Hello from 01-installation!
~~~

