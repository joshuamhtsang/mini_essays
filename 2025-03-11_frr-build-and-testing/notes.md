# The Plan

The Plan:  build FRR from source inside a Docker container using the official github repo:

https://github.com/FRRouting/frr

# Attempting my own Dockerfile for FRR

https://docs.frrouting.org/en/latest/installation.html

The following packages are required:
https://docs.frrouting.org/projects/dev-guide/en/latest/building-frr-for-ubuntu2404.html

Using the Dockerfile:
~~~
$ docker build -t frr_test .

$ docker run -it frr_test:latest bash
~~~

This builds but I'm unsure how to progress with this.


# Dockerfile in frr repo

There is actually a Dockerfile included with the frr repo:
https://github.com/FRRouting/frr/blob/master/docker/ubuntu-ci/Dockerfile

With some instructions on the Docker image build process:
https://docs.frrouting.org/projects/dev-guide/en/latest/building-docker.html#

In the cloned github repo directory frr/ (on the host), run a frr container:
~~~
$ docker build -t frr-ubuntu22:latest -f docker/ubuntu-ci/Dockerfile .

$ docker run -d --init --privileged --name frr-ubuntu22 --mount type=bind,source=/lib/modules,target=/lib/modules frr-ubuntu22:latest

$ docker ps
~~~

Running the topo1 test in Docker:

~~~
$ docker exec frr-ubuntu22 bash -c 'cd ~/frr/tests/topotests/ospf_topo1 ; sudo pytest test_ospf_topo1.py'
============================= test session starts ==============================
platform linux -- Python 3.10.12, pytest-8.3.5, pluggy-1.5.0
rootdir: /home/frr/frr/tests/topotests
configfile: pytest.ini
plugins: xdist-3.6.1
collected 11 items

test_ospf_topo1.py ..........s                                           [100%]

=============================== warnings summary ===============================
../../../../../../usr/local/lib/python3.10/dist-packages/_pytest/config/__init__.py:1441
  /usr/local/lib/python3.10/dist-packages/_pytest/config/__init__.py:1441: PytestConfigWarning: Unknown config option: asyncio_default_fixture_loop_scope
  
    self._warn_or_fail_if_strict(f"Unknown config option: {key}\n")

../../../../../../usr/local/lib/python3.10/dist-packages/_pytest/config/__init__.py:1441
  /usr/local/lib/python3.10/dist-packages/_pytest/config/__init__.py:1441: PytestConfigWarning: Unknown config option: asyncio_mode
  
    self._warn_or_fail_if_strict(f"Unknown config option: {key}\n")

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------- generated xml file: /tmp/topotests/topotests.xml ---------------
================== 10 passed, 1 skipped, 2 warnings in 43.76s ==================
~~~


#  Looking at an example test in tests/topotest/example_test

The frr repo contains an extensive set of tests.  They appear to be based off NetDEF tests, which is a CI for testing FRR.

A simple test involving 2 hosts and 2 routers can be found in: `frr/tests/topotests/example_test`. Run the tests in docker by using the image built above:

~~~
$ docker exec frr-ubuntu22 bash -c 'cd ~/frr/tests/topotests/example_test ; sudo pytest test_template.py'
~~~

The output is:
~~~
============================= test session starts ==============================
platform linux -- Python 3.10.12, pytest-8.3.5, pluggy-1.5.0
rootdir: /home/frr/frr/tests/topotests
configfile: pytest.ini
plugins: xdist-3.6.1
collected 5 items

test_template.py ..xss                                                   [100%]

=============================== warnings summary ===============================
../../../../../../usr/local/lib/python3.10/dist-packages/_pytest/config/__init__.py:1441
  /usr/local/lib/python3.10/dist-packages/_pytest/config/__init__.py:1441: PytestConfigWarning: Unknown config option: asyncio_default_fixture_loop_scope
  
    self._warn_or_fail_if_strict(f"Unknown config option: {key}\n")

../../../../../../usr/local/lib/python3.10/dist-packages/_pytest/config/__init__.py:1441
  /usr/local/lib/python3.10/dist-packages/_pytest/config/__init__.py:1441: PytestConfigWarning: Unknown config option: asyncio_mode
  
    self._warn_or_fail_if_strict(f"Unknown config option: {key}\n")

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------- generated xml file: /tmp/topotests/topotests.xml ---------------
============= 2 passed, 2 skipped, 1 xfailed, 2 warnings in 3.08s ==============
~~~



The tests are driven by mininet and sample 'frr.conf' files can be found which prove quite instructive.  I think frr.conf contain vtysh commands?

Some observations:

1.  Most of the Python test scripts use the tools in the `lib/` directory, for example the `topogen.py` structures are used a lot:
~~~
frr/tests/topotests/lib/topogen.py
~~~
which includes the `Topogen` class.  This class uses `lib.micronet_compat` to create the network topologies using Mininet.

2.  The 'Munet' ('mu-net') package is used to create and test network topologies.  Mininet is used.  Look in `frr/tests/topotests/lib/micronet_compat.py` for details.

3.  A relatively simple example of a topology test that used the OSPF daemon is:
~~~~
frr/blob/master/tests/topotests/example_test/test_template.py
~~~~
It is composed of a few essential steps like creating the `tgen` class (topology generator), building the network topology and doing some tests of connectivity etc.

For each router, there is a separate directory.  So if this tests has routers 'r1' and 'r2', then there are 2 *.conf files:
~~~
r1/zebra.conf
r2/zebra.conf
~~~
And these conf (configuration) files contain definitions of the interfaces on the router and what ip address and subnet they are on etc.

For `r1/zebra.conf`, it contains:
~~~
interface r1-eth0
  ip address 192.168.1.1/24

interface r1-eth1
  ip address 192.168.2.1/24

interface r1-eth2
  ip address 192.168.3.1/24
~~~

I think the image at: [https://github.com/FRRouting/frr/blob/master/tests/topotests/example_test/test_template.jpg] is now out-of-date.

4.  The FRR documentation contains extensive notes on 'Topotests':

https://docs.frrouting.org/projects/dev-guide/en/latest/topotests.html

