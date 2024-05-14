
# Resources

An excellent article by Hangbin Liu:
https://developers.redhat.com/articles/2022/04/06/introduction-linux-bridging-commands-and-features#

Routerology Blog YouTube video:
https://www.youtube.com/watch?v=oVu0O0UMBCc

Pretty encyclopedia description of many 'ip' utility commands, creating bridges, veth pairs etc.
https://baturin.org/docs/iproute2/

# Key Points:

1. 'iproute2' is a collection of userspace utilities for controlling and monitoring various networking
features in the Linux kernel.

2. It's time to stop using 'ifconfig' and 'route' utilities, both are effectively superceded by the 
utilities provided in 'iproute2'.  However, both utilities are kept in Linux distributions for
backward compatibility.

3. Some of the utilities provided by 'iproute2' are:
   - ip:
     One set of common usages is 'ip link':
     - ip -j link show : Shows the links/network interfaces in the root network namespace 'netns' in
     JSON format (-j flag).  This is similar to the old command 'ifconfig'.
     - ip -c -s link show <link-name>: Show basic and stats (-s flag) information about the interface
     <link-name> e.g. enp4s0 in colorful output (-c flag).  Example output:
     ```
     $ ip -c -s link show enp4s0
      3: enp4s0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP mode DEFAULT group default qlen 1000
      link/ether 1c:1b:0d:9b:4d:c3 brd ff:ff:ff:ff:ff:ff
      RX:  bytes packets errors dropped  missed   mcast           
       242709104  212325      0     719       0     279 
      TX:  bytes packets errors dropped carrier collsns           
       12502613   55025      0       0       0       0
     ```
     - ip link set dev <blah> [up/down]:  Set a network interface to 'up' or 'down' state.  By default, new
     interfaces are created in the 'down' state.
     - ip link add name <name> type bridge:  Create a bridge interface, which is like a virtual Ethernet switch.
     - ip link set dev <interface_name> master <bridge_name>:  Create a virtual bridge port on the bridge e.g 'br0' 
     that connects to the designated interface.
     Another set of common usages are:
     - 'ip addr' : Shows layer 3 IP networking information, as opposed to 'ip link' which shows layer 2 ethernet information.
     - 'ip neighbour' : Shows information about neighbours.  Only interface that are in the 'up' state may have neighbours.
     - 'ip route' : Control and manage Routing tables.  Adding 'default gateways' etc. Note that the Linus kernel does not
     keep route with unreachable next hops, and thus routes using a link that goes down are permanently removed from the
     routing table.  One can use other routing protocol suites like FreeRangeRouting to track link states and restore routes.
     - 'ip netns' : Manage and control network namespaces (netns) in the Linux kernel.  Similar to containers, each new netns 
     has its own isolated network stack separate from the root/default namespace and other newly created namespaces.  Namespaces 
     are so important that doing 'ip -n <netns_name> <ip_style_command>' allows you to execute ip-style commands in the namespace
     'netns_name'.
   - bridge:
   - tc

4. 


# The difference between 'ip link show' and 'ip addr show':

It is instructuve to explore the differences between these two commands, and in so doing reveal something of the natural 
differences between layer 2 and layer 3 protocols.



   

