# The Plan

The Plan:  build frr from source inside a Docker container using the official github repo:

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

In the cloned github repo directory frr/ (on the host):
~~~
$ docker build -t frr-ubuntu22:latest -f docker/ubuntu-ci/Dockerfile .

$ docker run -d --init --privileged --name frr-ubuntu22 --mount type=bind,source=/lib/modules,target=/lib/modules frr-ubuntu22:latest

$ docker ps

$ docker exec frr-ubuntu22 bash -c 'cd ~/frr/tests/topotests/ospf_topo1 ; sudo pytest test_ospf_topo1.py'
~~~


#  Looking at an example test in tests/topotest/example_test

The frr repo contains some extension set of tests.  They appear to be based off NetDEF tests, which is a CI for testing FRR.

A simple test involving 2 hosts and 2 routers can be found in: `frr/tests/topotests/ospf_topo2/test_example.py`.  The tests are driven by mininet and sample 'frr.conf' files can be found which prove quite instructive.  I think frr.conf contain vtysh commands?

