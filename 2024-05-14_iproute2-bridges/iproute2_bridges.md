
# Resources

An excellent article by Hangbin Liu:
https://developers.redhat.com/articles/2022/04/06/introduction-linux-bridging-commands-and-features#

Routerology Blog YouTube video:
https://www.youtube.com/watch?v=oVu0O0UMBCc

Pretty encyclopedia description of many `ip` utility commands, creating bridges, veth pairs etc.
https://baturin.org/docs/iproute2/

# Key Points:

1. 'iproute2' is a collection of userspace utilities for controlling and monitoring various networking
features in the Linux kernel.

2. It's time to stop using `ifconfig` and `route` utilities, both are effectively superceded by the 
utilities provided in `iproute2`.  However, both utilities are kept in Linux distributions for
backward compatibility.

3. Some of the utilities provided by 'iproute2' are:
   - `ip`:
     One set of common usages is 'ip link':
     - `ip -j link show` : Shows the links/network interfaces in the root network namespace 'netns' in
     JSON format (-j flag).  This is similar to the old command 'ifconfig'.
     - `ip -c -s link show <link-name>` : Show basic and stats (-s flag) information about the interface
     `<link-name>` e.g. enp4s0 in colorful output (-c flag).  Example output:
     ```
     $ ip -c -s link show enp4s0
      3: enp4s0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP mode DEFAULT group default qlen 1000
      link/ether 1c:1b:0d:9b:4d:c3 brd ff:ff:ff:ff:ff:ff
      RX:  bytes packets errors dropped  missed   mcast           
       242709104  212325      0     719       0     279 
      TX:  bytes packets errors dropped carrier collsns           
       12502613   55025      0       0       0       0
     ```
     - `ip link set dev <blah> [up/down]` :  Set a network interface to 'up' or 'down' state.  By default, new
     interfaces are created in the 'down' state.
     - `ip link add name <bridge_name> type bridge` :  Create a bridge interface, which is like a virtual Ethernet switch.
     - `ip link set dev <interface_name> master <bridge_name>` :  Create a virtual bridge port on the bridge e.g 'br0' 
     that connects to the designated interface.
     - `ip link add name <name> type <type>` : The `ip link add` syntax can create much more than just bridges.  It can
     also create other `type` of links:
       - `veth` :  A pair of interfaces that are linked by a bi-directional pipe.  You can think of it as a network cable
       with unattached ports at each end.
       - blah
     Another set of common usages are:
     - `ip addr` : Shows layer 3 IP networking information, as opposed to 'ip link' which shows layer 2 ethernet information.
     - `ip neighbour` : Shows information about neighbours.  Only interface that are in the 'up' state may have neighbours.
     - `ip route` : Control and manage Routing tables.  Adding 'default gateways' etc. Note that the Linus kernel does not
     keep route with unreachable next hops, and thus routes using a link that goes down are permanently removed from the
     routing table.  One can use other routing protocol suites like FreeRangeRouting to track link states and restore routes.
     - `ip netns` : Manage and control network namespaces (netns) in the Linux kernel.  Similar to containers, each new netns 
     has its own isolated network stack separate from the root/default namespace and other newly created namespaces.  Namespaces 
     are so important that doing `ip -n <netns_name> <ip_style_command>` allows you to execute ip-style commands in the namespace
     `<netns_name>`.
   - `bridge` : A utility for controlling and managing Linux kernel bridges.  Note that bridges can be created by the `ip` command
   using syntax like `ip link add <br_name> type bridge`.
   - `tc` : traffic control utility.

4. 


# The difference between `ip link show` and `ip addr show`:

It is instructive to explore the differences between these two commands, and in so doing reveal something of the  
differences between layer 2 and layer 3 protocols.

```
joshua@joshua-ubuntu-1:~/josh_things/mini_essays$ ip -c -br addr show
lo               UNKNOWN        127.0.0.1/8 ::1/128 
enp5s0           DOWN           
enp4s0           UP             192.168.1.12/24 fe80::9103:3fce:2b07:af8a/64 
virbr0           DOWN           192.168.122.1/24 
docker0          DOWN           172.17.0.1/16 
joshua@joshua-ubuntu-1:~/josh_things/mini_essays$ ip -c -br link show
lo               UNKNOWN        00:00:00:00:00:00 <LOOPBACK,UP,LOWER_UP> 
enp5s0           DOWN           1c:1b:0d:9b:4d:c1 <NO-CARRIER,BROADCAST,MULTICAST,UP> 
enp4s0           UP             1c:1b:0d:9b:4d:c3 <BROADCAST,MULTICAST,UP,LOWER_UP> 
virbr0           DOWN           52:54:00:c8:8f:16 <NO-CARRIER,BROADCAST,MULTICAST,UP> 
docker0          DOWN           02:42:d0:21:fb:aa <NO-CARRIER,BROADCAST,MULTICAST,UP>
```

Note that the `-br` flag is not anything to do with bridges, but in fact stands for 'brieviate' i.e to 
make brief/short.  You can see that `ip addr show` shows IP addresses (both IPv4 and IPv6) with subnet 
prefixes while `ip link show` shows mac/ethernet addresses.



# Veth pairs and connecting two network namespaces together directly (not via bridge)

See valuable resource [https://baturin.org/docs/iproute2/#ip-netns-veth-connect]

| netns1 | veth1 <------> veth2 | netns2 |  

A quick overview of the strategy is:
- Create a veth pair with link names `veth1` and `veth2`.  By default, both
ends of the veth pair will reside in the default namespace.
- Create two network namespaces `netns1` and `netns2`.
- Move each link interface to the corresponding namespaces with:
  `ip link set dev <interface_name> netns <netns_name>`
- Set device statuses to 'UP'.
- Attempt ping between the two namespaces using both IPv6 and IPv4.


1. Create the veth pair, with one end interface named 'veth1', and the other 'veth2':
   ```
   $ sudo ip link add veth1 type veth peer veth2
   ```
   You can see the veth pair is created, and their association is displayed with an '@' linking them:
   ```
   $ ip link show type veth
   7: veth2@veth1: <BROADCAST,MULTICAST,M-DOWN> mtu 1500 qdisc noop state DOWN mode DEFAULT group default qlen 1000
       link/ether fe:18:2d:67:0f:d7 brd ff:ff:ff:ff:ff:ff
   8: veth1@veth2: <BROADCAST,MULTICAST,M-DOWN> mtu 1500 qdisc noop state DOWN mode DEFAULT group default qlen 1000
       link/ether 76:01:2f:09:fc:bd brd ff:ff:ff:ff:ff:ff
   ```

2. Create two network namespaces `netns1` and `netns2`:
   ```
   $ sudo ip netns add netns1
   $ sudo ip netns add netns2
   ```
   You see the the two namespaces created:
   ```
   $ ip netns show
   netns2
   netns1
   ```
   
3. Move each end of the veth interface into a corresponding namespace:
   Move 'veth1' into 'netns1':
   ```
   $ sudo ip link set dev veth1 netns netns1
   ```
   Notice how the interface disappears from the default namespace once it is
   moved into 'netns1', the other end of the veth pair is now 'if8'.:
   ```
   $ ip link show type veth
   7: veth2@if8: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN mode DEFAULT group default qlen 1000
       link/ether fe:18:2d:67:0f:d7 brd ff:ff:ff:ff:ff:ff link-netns netns1
   ```
   In addition, the metadata tells you `link-netns netns1` to indicate the other
   end is in namespace 'netns1'.
   
   So do the same for 'veth2' and move 'veth2' into 'netsn2':
   ```
   $ sudo ip link set dev veth2 netns netns2
   ```

4. Observe the veth interface ends inside the corresponding namespaces.
   This can be done by executing `ip` commands within the corresponding namespace
   with the `-n` flag:
   ```
   $ sudo ip -n netns1 link show type veth
   8: veth1@if7: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN mode DEFAULT group default qlen 1000
       link/ether 76:01:2f:09:fc:bd brd ff:ff:ff:ff:ff:ff link-netns netns2
   ```

5. Set the veth interfaces to state up:
   ```
   $ sudo ip -n netns1 link set dev veth1 up
   $ sudo ip -n netns2 link set dev veth2 up
   ```
   You can see this changes the "operstate" to "UP" and also displays a "LOWER_UP"
   flag to indicate the L1 (Physical layer) is up:
   ```
   $ sudo ip -j -n netns1 link show type veth | jq
   "flags": [
         "BROADCAST",
         "MULTICAST",
         "UP",
         "LOWER_UP"
       ],
   "operstate": "UP",
   ```

6. Ping between the 2 network namespaces using the IPv6 addresses.
   Let try pinging from `netns1` to `netns2`.  First, find the IPv6 address of
   the veth interface in `netns2` using `ip addr show`:
   ```
   $ sudo ip -n netns2 addr show type veth
   7: veth2@if8: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000
       link/ether fe:18:2d:67:0f:d7 brd ff:ff:ff:ff:ff:ff link-netns netns1
       inet6 fe80::fc18:2dff:fe67:fd7/64 scope link 
          valid_lft forever preferred_lft forever
   ```
   Then execute a `ping` from `netns1` using the `ip netns exec` syntax:
   ```
   $ sudo ip netns exec netns1 ping fe80::fc18:2dff:fe67:fd7
   PING fe80::fc18:2dff:fe67:fd7(fe80::fc18:2dff:fe67:fd7) 56 data bytes
   64 bytes from fe80::fc18:2dff:fe67:fd7%veth1: icmp_seq=1 ttl=64 time=0.037 ms
   64 bytes from fe80::fc18:2dff:fe67:fd7%veth1: icmp_seq=2 ttl=64 time=0.049 ms
   64 bytes from fe80::fc18:2dff:fe67:fd7%veth1: icmp_seq=3 ttl=64 time=0.048 ms
   ```
   You can see that the ping does indeed go through!  Note that you cannot use the
   `-n` syntax to execute `ping`, but must use `ip netns exec <netns_name>` to do so.
   However, the question is now "how does one do a ping with IPv4?"  The answer is 
   to assign IPv4 addresses to the veth 
   interfaces.

7. Use `ip addr addr` inside each namespace to set IPv4 address and mask to the
   corresponding interfaces:
   ```
   $ sudo ip -n netns1 addr add 192.168.88.1/24 dev veth1
   $ sudo ip -n netns2 addr add 192.168.88.2/24 dev veth2
   ```
   You will now see the IPv4 address appearing as 'inet':
   ```
   $ sudo ip -n netns2 addr show type veth
   7: veth2@if8: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000
       link/ether fe:18:2d:67:0f:d7 brd ff:ff:ff:ff:ff:ff link-netns netns1
       inet 192.168.88.2/24 scope global veth2
          valid_lft forever preferred_lft forever
       inet6 fe80::fc18:2dff:fe67:fd7/64 scope link 
          valid_lft forever preferred_lft forever
   ```
   The ping will now work from `netns1` to `netns2`:
   ```
   $ sudo ip netns exec netns1 ping 192.168.88.2
   PING 192.168.88.2 (192.168.88.2) 56(84) bytes of data.
   64 bytes from 192.168.88.2: icmp_seq=1 ttl=64 time=0.024 ms
   64 bytes from 192.168.88.2: icmp_seq=2 ttl=64 time=0.039 ms
   64 bytes from 192.168.88.2: icmp_seq=3 ttl=64 time=0.044 ms
   ```




# Connecting two network namespaces together (this time via bridge!)

Similar to above but create a bridge in the default namespace and 
two veth pairs will be needed this time.  See the YouTube video.

   

