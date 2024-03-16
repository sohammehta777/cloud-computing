Soham Mehta (W1650151)

Task 1
----------------------
Q1. What is the output of "nodes" and "net"?

mininet> nodes
available nodes are:
c0 h1 h2 h3 h4 h5 h6 h7 h8 s1 s2 s3 s4 s5 s6 s7
mininet>

mininet> net
h1 h1-eth0:s3-eth2
h2 h2-eth0:s3-eth3
h3 h3-eth0:s4-eth2
h4 h4-eth0:s4-eth3
h5 h5-eth0:s6-eth2
h6 h6-eth0:s6-eth3
h7 h7-eth0:s7-eth2
h8 h8-eth0:s7-eth3
s1 lo:  s1-eth1:s2-eth1 s1-eth2:s5-eth1
s2 lo:  s2-eth1:s1-eth1 s2-eth2:s3-eth1 s2-eth3:s4-eth1
s3 lo:  s3-eth1:s2-eth2 s3-eth2:h1-eth0 s3-eth3:h2-eth0
s4 lo:  s4-eth1:s2-eth3 s4-eth2:h3-eth0 s4-eth3:h4-eth0
s5 lo:  s5-eth1:s1-eth2 s5-eth2:s6-eth1 s5-eth3:s7-eth1
s6 lo:  s6-eth1:s5-eth2 s6-eth2:h5-eth0 s6-eth3:h6-eth0
s7 lo:  s7-eth1:s5-eth3 s7-eth2:h7-eth0 s7-eth3:h8-eth0
c0
mininet>

Q2. What is the output of "h7 ifconfig"?

mininet> h7 ifconfig
h7-eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
    	inet 10.0.0.7  netmask 255.0.0.0  broadcast 10.255.255.255
    	inet6 fe80::28a8:96ff:feb2:b3df  prefixlen 64  scopeid 0x20<link>
    	ether 2a:a8:96:b2:b3:df  txqueuelen 1000  (Ethernet)
    	RX packets 85  bytes 6406 (6.4 KB)
    	RX errors 0  dropped 0  overruns 0  frame 0
    	TX packets 13  bytes 1006 (1.0 KB)
    	TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
    	inet 127.0.0.1  netmask 255.0.0.0
    	inet6 ::1  prefixlen 128  scopeid 0x10<host>
    	loop  txqueuelen 1000  (Local Loopback)
    	RX packets 0  bytes 0 (0.0 B)
    	RX errors 0  dropped 0  overruns 0  frame 0
    	TX packets 0  bytes 0 (0.0 B)
    	TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

mininet>


Task 2
----------------------
Q1. Draw the function call graph of this controller. For example, once a packet comes to the controller, which function is the first to be called, which one is the second, and so forth?


Upon switch activation, the controller operates through a sequential four-step process:
1. Packet Processing
2. Hub Functionality Invocation
3. Packet Rebroadcasting
4. Message Packet Dispatch

The sequence of function calls is as follows:
`launch()` triggers `_handle_PacketIn()`, which then calls `act_like_hub()`. Following this, `resend_packet()` is executed, culminating in the transmission of the message to the designated port.

Q2. Have h1 ping h2, and h1 ping h8 for 100 times (e.g., h1 ping -c100 h2).
    a. How long does it take (on average) to ping for each case?
    b. What is the minimum and maximum ping you have observed?
    c. What is the difference, and why?

h1 to h2 communication:
--- Statistics for pinging 10.0.0.2 ---
100 packets exchanged, with all 100 successfully received, indicating 0% packet loss over a period of 99157ms.
Round Trip Time (RTT) metrics: minimum = 1.030ms, average = 1.702ms, maximum = 2.263ms, with a standard deviation of 0.285ms.

h1 to h8 communication:
--- Statistics for pinging 10.0.0.8 ---
100 packets exchanged, with all 100 successfully received, indicating 0% packet loss over a period of 99155ms.
Round Trip Time (RTT) metrics: minimum = 3.078ms, average = 6.277ms, maximum = 7.752ms, with a standard deviation of 1.008ms.

Analysis:
a. Average RTT: The average RTT from h1 to h2 is significantly lower at 1.702ms compared to 6.277ms from h1 to h8, demonstrating a quicker response time within closer network proximity.
b. RTT Range: For h1 to h2, the RTT spans from a minimum of 1.030ms to a maximum of 2.263ms. In contrast, for h1 to h8, the RTT extends from a minimum of 3.078ms to a maximum of 7.752ms, highlighting the increased latency over longer network paths.
c. The discrepancy in average RTT times between h1 to h2 and h1 to h8 can be attributed to the network topology. The direct or near-direct connection between h1 and h2 results in lower latency. Conversely, the connection to h8 traverses through a more complex network path, incurring additional delays, which is reflected in the quadrupled average RTT time.

Q3. Run "iperf h1 h2" and "iperf h1 h8"
    a. What is "iperf" used for?
    b. What is the throughput for each case?
    c. What is the difference, and explain the reasons for the difference.

mininet> iperf h1 h2
*** Iperf: testing TCP bandwidth between h1 and h2
*** Results: ['21.3 Mbits/sec', '21.1 Mbits/sec']
mininet>

mininet> iperf h1 h8
*** Iperf: testing TCP bandwidth between h1 and h8
*** Results: ['20.0 Mbits/sec', '19.7 Mbits/sec']
mininet>

a. iperf serves as a comprehensive network performance measurement tool, primarily employed to assess the bandwidth capacity of networks. It enables the generation of traffic between hosts and measures the throughput of the network that can be achieved on that pathway, thereby providing key metrics for network performance optimization.


Execution of "iperf h1 h2" yielded the following: Engaging in TCP bandwidth evaluation between h1 and h2:

Recorded Results: ['21.3 Mbits/sec', '21.1 Mbits/sec']

Execution of "iperf h1 h8" yielded the following: Engaging in TCP bandwidth evaluation between h1 and h8:

Recorded Results: ['20.0 Mbits/sec', '19.7 Mbits/sec']

c. The observed data reveals a discernible variance in throughput between the two scenarios. The connection between h1 and h2 showcases a marginally superior throughput compared to the h1 to h8 connection. This variation can be attributed to the intricacies of network topology and the number of intermediate switches involved. Specifically, the path from h1 to h2 is more direct or involves fewer network hops, leading to lesser impedance and thus, a slightly enhanced throughput. Conversely, the path from h1 to h8, potentially encompassing more intermediate nodes, introduces increased latency and the possibility of network congestion, culminating in a modest decrease in throughput.




Q4. Which of the switches observe traffic? Please describe your way for observing such traffic on switches (e.g., adding some functions in the "of_tutorial" controller).

Incorporating the following line into the _handle_PacketIn function, which acts as an event listener, enables the logging of switch traffic whenever packet flooding occurs. This is because the switches, upon detecting the traffic, invoke this specific function:
log.info("Traffic observation on switch: %s" % (self.connection))

This modification ensures that any traffic passing through the switches is duly noted, leveraging the function's role in monitoring packet flow within the network.


Q2. Have h1 ping h2, and h1 ping h8 for 100 times (e.g., h1 ping -c100 p2).
    a. How long did it take (on average) to ping for each case?
    b. What is the minimum and maximum ping you have observed?
    c. Any difference from Task 2 and why do you think there is a change if there is?

a. Interaction from h1 to h2
--- Ping results for 10.0.0.2 ---
100 packets were sent, with all 100 successfully arriving, showcasing a 0% loss rate over 99348ms.
The round-trip time (RTT) details: the shortest was 1.682ms, the average stood at 2.896ms, the longest at 14.076ms, and the deviation at 1.534ms.

Interaction from h1 to h8
--- Ping results for 10.0.0.8 ---
Similarly, 100 packets were dispatched, with a full 100% reception rate, indicating no loss over a span of 99303ms.
RTT specifics reveal: a minimum of 7.956ms, an average of 20.043ms, a maximum of 63.214ms, with a standard deviation of 12.501ms.

b. - For the connection from h1 to h2, the average response time recorded is 2.896ms.
- Conversely, when h1 reaches out to h8, the mean response time observed is 20.043ms.

- The quickest response from h1 to h2 was marked at 1.682ms, while the slowest reached 14.076ms.
 
- In contrast, pings from h1 to h8 demonstrated a minimum latency of 7.956ms and a peak at 63.214ms.


c. Comparing the outcomes with Task 2's findings, we observe a negligible difference in timings between h1 pinging h2 and h1 pinging h8. Interestingly, the duration for the latter is slightly reduced. This improvement can be attributed to the switch's ability to learn the hosts' locations rather than indiscriminately flooding all nodes. It efficiently routes packets by consulting the "mac_to_port" mapping, which stores destination MAC addresses. This strategic approach notably diminishes network congestion.

Q.3 Run "iperf h1 h2" and "iperf h1 h8".
    a. What is the throughput for each case?
    b. What is the difference from Task 2 and why do you think there is a change if there is?

a. mininet> iperf h1 h2
*** Iperf: testing TCP bandwidth between h1 and h2
*** Results: ['26.43 Mbits/sec', '32.07 Mbits/sec']

mininet> iperf h1 h8
*** Iperf: testing TCP bandwidth between h1 and h8
*** Results: ['10.67 Mbits/sec', '11.15 Mbits/sec']

b. The throughput observed in Task 3 significantly exceeds that of Task 2 for both scenarios. This increase is attributed to the switch's capability to identify destination MAC addresses, thereby streamlining packet delivery. By avoiding unnecessary broadcast to all network ports and hosts, network congestion is markedly reduced. Remarkably, the data transfer rate in Task 3 is approximately fourfold compared to the results noted in Task 2.

