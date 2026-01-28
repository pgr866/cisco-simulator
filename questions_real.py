# Banco de preguntas Cisco Network Security - REAL

questions_real = [
    {
        "id": 1001,
        "type": "matching",
        "question": "Match the type of ASA ACLs to the description. (Not all options are used.)",
        "image": None,
        "left_items": [
            "standard access list",
            "extended access list",
            "EtherType access list",
            "webtype access list"
        ],
        "right_items": [
            "used to identify the destination IP addresses only",
            "used to specify source and destination addresses and protocol, ports, or the ICMP type",
            "used only if the security appliance is running in transparent mode",
            "used to support filtering for clientless SSL VPN",
            "used to determine which IPv6 traffic to block or to forward at router interfaces",
        ],
        "correct": [0, 1, 2, 3],
        "explanation": "Place the options in the following order:\n- extended access lists: used to specify source and destination addresses and protocol, ports, or the ICMP type\n- webtype access lists: used to support filtering for clientless SSL VPN\n- standard access lists: used to identify the destination IP addresses only\n- EtherType access lists: used only if the security appliance is running in transparent mode"
    },
    {
        "id": 1002,
        "type": "radio",
        "question": "Which statement describes a difference between the Cisco ASA IOS CLI feature and the router IOS CLI feature?",
        "image": None,
        "options": [
            "ASA uses the ? command whereas a router uses the help command to receive help on a brief description and the syntax of a command.",
            "To use a show command in a general configuration mode, ASA can use the command directly whereas a router will need to enter the do command before issuing the show command.",
            "To complete a partially typed command, ASA uses the Ctrl+Tab key combination whereas a router uses the Tab key.",
            "To indicate the CLI EXEC mode, ASA uses the % symbol whereas a router uses the # symbol."
        ],
        "correct": [1],
        "explanation": "The ASA CLI is a proprietary OS which has a similar look and feel to the Cisco router IOS. Although it shares some common features with the router IOS, it has its unique features. For example, an ASA CLI command can be executed regardless of the current configuration mode prompt. The IOS do command is not required or recognized. Both the ASA CLI and the router CLI use the # symbol to indicate the EXEC mode. Both CLIs use the Tab key to complete a partially typed command. Different from the router IOS, the ASA provides a help command that provides a brief command description and syntax for certain commands."
    },
    {
        "id": 1003,
        "type": "radio",
        "question": "Refer to the exhibit. A network administrator is configuring AAA implementation on an ASA device. What does the option link3 indicate?",
        "image": "/static/images/1003.png",
        "options": [
            "the network name where the AAA server resides",
            "the specific AAA server name",
            "the sequence of servers in the AAA server group",
            "the interface name"
        ],
        "correct": [3],
        "explanation": "The option link3 indicates the interface name on the ASA device where the AAA server is connected."
    },
    {
        "id": 1004,
        "type": "radio",
        "question": "What provides both secure segmentation and threat defense in a Secure Data Center solution?",
        "image": None,
        "options": [
            "Cisco Security Manager software",
            "AAA server",
            "Adaptive Security Appliance",
            "intrusion prevention system"
        ],
        "correct": [2],
        "explanation": "The Adaptive Security Appliance (ASA) provides both secure segmentation and threat defense capabilities in a Secure Data Center solution."
    },
    {
        "id": 1005,
        "type": "checkbox",
        "question": "What are the three core components of the Cisco Secure Data Center solution? (Choose three.)",
        "image": None,
        "options": [
            "mesh network",
            "secure segmentation",
            "visibility",
            "threat defense",
            "servers",
            "infrastructure"
        ],
        "correct": [1, 2, 3],
        "explanation": "Secure segmentation is used when managing and organizing data in a data center. Threat defense includes a firewall and intrusion prevention system (IPS). Data center visibility is designed to simplify operations and compliance reporting by providing consistent security policy enforcement."
    },
    {
        "id": 1006,
        "type": "checkbox",
        "question": "What are three characteristics of ASA transparent mode? (Choose three.)",
        "image": None,
        "options": [
            "This mode does not support VPNs, QoS, or DHCP Relay.",
            "It is the traditional firewall deployment mode.",
            "This mode is referred to as a \"bump in the wire.\"",
            "NAT can be implemented between connected networks.",
            "In this mode the ASA is invisible to an attacker.",
            "The interfaces of the ASA separate Layer 3 networks and require IP addresses in different subnets."
        ],
        "correct": [0, 2, 4],
        "explanation": "In transparent mode, the ASA acts as a Layer 2 device (bump in the wire), is invisible to attackers, and does not support VPNs, QoS, or DHCP Relay. The traditional firewall deployment mode is routed mode, not transparent mode."
    },
    {
        "id": 1007,
        "type": "radio",
        "question": "What is needed to allow specific traffic that is sourced on the outside network of an ASA firewall to reach an internal network?",
        "image": None,
        "options": [
            "ACL",
            "NAT",
            "dynamic routing protocols",
            "outside security zone level 0"
        ],
        "correct": [0],
        "explanation": "In order to explicitly permit traffic from an interface with a lower security level to an interface with a higher security level, an ACL must be configured. By default, traffic will only flow from a higher security level to a lower."
    },
    {
        "id": 1008,
        "type": "radio",
        "question": "What will be the result of failed login attempts if the following command is entered into a router?\n\nlogin block-for 150 attempts 4 within 90",
        "image": None,
        "options": [
            "All login attempts will be blocked for 150 seconds if there are 4 failed attempts within 90 seconds.",
            "All login attempts will be blocked for 90 seconds if there are 4 failed attempts within 150 seconds.",
            "All login attempts will be blocked for 1.5 hours if there are 4 failed attempts within 150 seconds.",
            "All login attempts will be blocked for 4 hours if there are 90 failed attempts within 150 seconds."
        ],
        "correct": [0],
        "explanation": "The components of the login block-for 150 attempts 4 within 90 command are as follows:\n- The expression block-for 150 is the time in seconds that logins will be blocked.\n- The expression attempts 4 is the number of failed attempts that will trigger the blocking of login requests.\n- The expression within 90 is the time in seconds in which the 4 failed attempts must occur."
    },
    {
        "id": 1009,
        "type": "checkbox",
        "question": "Which two tasks are associated with router hardening? (Choose two.)",
        "image": None,
        "options": [
            "placing the router in a secure room",
            "disabling unused ports and interfaces",
            "installing the maximum amount of memory possible",
            "securing administrative access",
            "using uninterruptible power supplies"
        ],
        "correct": [1, 3],
        "explanation": "Router hardening involves disabling unused ports and interfaces and securing administrative access. Physical security (secure room) and power supplies are infrastructure concerns, not specifically router hardening tasks."
    },
    {
        "id": 1010,
        "type": "radio",
        "question": "Which threat protection capability is provided by Cisco ESA?",
        "image": None,
        "options": [
            "web filtering",
            "cloud access security",
            "spam protection",
            "Layer 4 traffic monitoring"
        ],
        "correct": [2],
        "explanation": "Email is a top attack vector for security breaches. Cisco ESA includes many threat protection capabilities for email such as spam protection, forged email detection, and Cisco advanced phishing protection."
    },
    {
        "id": 1011,
        "type": "checkbox",
        "question": "What are two security measures used to protect endpoints in the borderless network? (Choose two.)",
        "image": None,
        "options": [
            "denylisting",
            "Snort IPS",
            "DLP",
            "DMZ",
            "rootkit"
        ],
        "correct": [0, 2],
        "explanation": "Security measures for endpoints:\n- antimalware software: Protect endpoints from malware.\n- spam filtering: Prevent spam emails from reaching endpoints.\n- blocklisting: Prevent endpoints from connecting to websites with bad reputations by immediately blocking connections based on the latest reputation intelligence.\n- data loss prevention (DLP): Prevent sensitive information from being lost or stolen."
    },
    {
        "id": 1012,
        "type": "checkbox",
        "question": "Which three types of traffic are allowed when the authentication port-control auto command has been issued and the client has not yet been authenticated? (Choose three.)",
        "image": None,
        "options": [
            "CDP",
            "802.1Q",
            "IPsec",
            "TACACS+",
            "STP",
            "EAPOL"
        ],
        "correct": [0, 4, 5],
        "explanation": "Until the workstation is authenticated, 802.1X access control enables only Extensible Authentication Protocol over LAN (EAPOL), Cisco Discovery Protocol (CDP), and Spanning Tree Protocol (STP) traffic through the port to which the workstation is connected. After authentication succeeds, normal traffic can pass through the port."
    },
    {
        "id": 1013,
        "type": "radio",
        "question": "Which statement describes a characteristic of the IKE protocol?",
        "image": None,
        "options": [
            "It uses UDP port 500 to exchange IKE information between the security gateways.",
            "IKE Phase 1 can be implemented in three different modes: main, aggressive, or quick.",
            "It allows for the transmission of keys directly across a network.",
            "The purpose of IKE Phase 2 is to negotiate a security association between two IKE peers."
        ],
        "correct": [0],
        "explanation": "IKE uses UDP port 500 to exchange IKE information between security gateways. Quick mode is part of Phase 2, not Phase 1. Keys are not transmitted directly; they are negotiated using Diffie-Hellman."
    },
    {
        "id": 1014,
        "type": "radio",
        "question": "Which action do IPsec peers take during the IKE Phase 2 exchange?",
        "image": None,
        "options": [
            "exchange of DH keys",
            "negotiation of IPsec policy",
            "negotiation of IKE policy sets",
            "verification of peer identity"
        ],
        "correct": [1],
        "explanation": "The IKE protocol executes in two phases. During Phase 1 the two sides negotiate IKE policy sets, authenticate each other, and set up a secure channel. During the second phase IKE negotiates security associations between the peers."
    },
    {
        "id": 1015,
        "type": "checkbox",
        "question": "What are two hashing algorithms used with IPsec AH to guarantee authenticity? (Choose two.)",
        "image": None,
        "options": [
            "SHA",
            "RSA",
            "DH",
            "MD5",
            "AES"
        ],
        "correct": [0, 3],
        "explanation": "The IPsec framework uses various protocols and algorithms to provide data confidentiality, data integrity, authentication, and secure key exchange. Two popular algorithms used to ensure that data is not intercepted and modified (data integrity and authenticity) are MD5 and SHA."
    },
    {
        "id": 1016,
        "type": "radio",
        "question": "Which command raises the privilege level of the ping command to 7?",
        "image": None,
        "options": [
            "user exec ping level 7",
            "authorization exec ping level 7",
            "accounting exec level 7 ping",
            "privilege exec level 7 ping"
        ],
        "correct": [3],
        "explanation": "The privilege exec level command is used to change the privilege level of a command. The syntax is: privilege exec level [level] [command]."
    },
    {
        "id": 1017,
        "type": "radio",
        "question": "What is a characteristic of a role-based CLI view of router configuration?",
        "image": None,
        "options": [
            "A CLI view has a command hierarchy, with higher and lower views.",
            "When a superview is deleted, the associated CLI views are deleted.",
            "A single CLI view can be shared within multiple superviews.",
            "Only a superview user can configure a new view and add or remove commands from the existing views."
        ],
        "correct": [2],
        "explanation": "A CLI view has no command hierarchy, and therefore, no higher or lower views. Deleting a superview does not delete the associated CLI views. Only a root view user can configure a new view and add or remove commands from the existing views."
    },
    {
        "id": 1018,
        "type": "radio",
        "question": "What is a limitation to using OOB management on a large enterprise network?",
        "image": None,
        "options": [
            "Production traffic shares the network with management traffic.",
            "Terminal servers can have direct console connections to user devices needing management.",
            "OOB management requires the creation of VPNs.",
            "All devices appear to be attached to a single management network."
        ],
        "correct": [3],
        "explanation": "OOB management provides a dedicated management network without production traffic. Devices within that network, such as terminal servers, have direct console access for management purposes. Because in-band management runs over the production network, secure tunnels or VPNs may be needed. Failures on the production network may not be communicated to the OOB network administrator because the OOB management network may not be affected."
    },
    {
        "id": 1019,
        "type": "radio",
        "question": "Refer to the exhibit. A corporate network is using NTP to synchronize the time across devices. What can be determined from the displayed output?",
        "image": "/static/images/1019.png",
        "options": [
            "Router03 is a stratum 2 device that can provide NTP service to other devices in the network.",
            "The time on Router03 may not be reliable because it is offset by more than 7 seconds to the time server.",
            "The interface on Router03 that connects to the time sever has the IPv4 address 209.165.200.225.",
            "Router03 time is synchronized to a stratum 2 time server."
        ],
        "correct": [0],
        "explanation": "The show ntp status command displays that Router03 is now a stratum 2 device synchronized with the NTP server at 209.165.220.225 and can provide NTP service to other devices in the network. The clock offset is only 7.0883 milliseconds, not 7.0883 seconds."
    },
    {
        "id": 1020,
        "type": "checkbox",
        "question": "Refer to the exhibit. Which two conclusions can be drawn from the syslog message that was generated by the router? (Choose two.)",
        "image": "/static/images/1020.jpg",
        "options": [
            "This message resulted from an unusual error requiring reconfiguration of the interface.",
            "This message indicates that service timestamps have been configured.",
            "This message indicates that the interface changed state five times.",
            "This message is a level 5 notification message.",
            "This message indicates that the interface should be replaced."
        ],
        "correct": [1, 3],
        "explanation": "The message is a level 5 notification message as shown in the %LINEPROTO-5 section of the output. Messages reporting the link status are common and do not require replacing the interface or reconfiguring the interface. The date and time displayed at the beginning of the message indicates that service timestamps have been configured on the router."
    },
    {
        "id": 1021,
        "type": "checkbox",
        "question": "Which two types of hackers are typically classified as grey hat hackers? (Choose two.)",
        "image": None,
        "options": [
            "hacktivists",
            "cyber criminals",
            "vulnerability brokers",
            "script kiddies",
            "state-sponsored hackers"
        ],
        "correct": [0, 2],
        "explanation": "Grey hat hackers may do unethical or illegal things, but not for personal gain or to cause damage. Hacktivists use their hacking as a form of political or social protest, and vulnerability brokers hack to uncover weaknesses and report them to vendors. Depending on the perspective one possesses, state-sponsored hackers are either white hat or black hat operators. Script kiddies create hacking scripts to cause damage or disruption. Cyber criminals use hacking to obtain financial gain by illegal means."
    },
    {
        "id": 1022,
        "type": "radio",
        "question": "When describing malware, what is a difference between a virus and a worm?",
        "image": None,
        "options": [
            "A virus focuses on gaining privileged access to a device, whereas a worm does not.",
            "A virus replicates itself by attaching to another file, whereas a worm can replicate itself independently.",
            "A virus can be used to launch a DoS attack (but not a DDoS), but a worm can be used to launch both DoS and DDoS attacks.",
            "A virus can be used to deliver advertisements without user consent, whereas a worm cannot."
        ],
        "correct": [1],
        "explanation": "Malware can be classified as follows:\n- Virus (self-replicates by attaching to another program or file)\n- Worm (replicates independently of another program)\n- Trojan horse (masquerades as a legitimate file or program)\n- Rootkit (gains privileged access to a machine while concealing itself)\n- Spyware (collects information from a target system)\n- Adware (delivers advertisements with or without consent)\n- Bot (waits for commands from the hacker)\n- Ransomware (holds a computer system or data captive until payment is received)"
    },
    {
        "id": 1023,
        "type": "radio",
        "question": "Which type of packet is unable to be filtered by an outbound ACL?",
        "image": None,
        "options": [
            "multicast packet",
            "ICMP packet",
            "broadcast packet",
            "router-generated packet"
        ],
        "correct": [3],
        "explanation": "Traffic that originates within a router such as pings from a command prompt, remote access from a router to another device, or routing updates are not affected by outbound access lists. The traffic must flow through the router in order for the router to apply the ACEs."
    },
    {
        "id": 1024,
        "type": "radio",
        "question": "Consider the access list command applied outbound on a router serial interface.\n\naccess-list 100 deny icmp 192.168.10.0 0.0.0.255 any echo reply\n\nWhat is the effect of applying this access list command?",
        "image": None,
        "options": [
            "The only traffic denied is echo-replies sourced from the 192.168.10.0/24 network. All other traffic is allowed.",
            "The only traffic denied is ICMP-based traffic. All other traffic is allowed.",
            "No traffic will be allowed outbound on the serial interface.",
            "Users on the 192.168.10.0/24 network are not allowed to transmit traffic to any other destination."
        ],
        "correct": [2],
        "explanation": "This ACL denies ICMP echo-replies from the 192.168.10.0/24 network. However, because there is an implicit deny all at the end of every ACL, and no permit statement is included, no traffic will be allowed outbound on the serial interface."
    },
    {
        "id": 1025,
        "type": "radio",
        "question": "Which command is used to activate an IPv6 ACL named ENG_ACL on an interface so that the router filters traffic prior to accessing the routing table?",
        "image": None,
        "options": [
            "ipv6 access-class ENG_ACL in",
            "ipv6 traffic-filter ENG_ACL out",
            "ipv6 traffic-filter ENG_ACL in",
            "ipv6 access-class ENG_ACL out"
        ],
        "correct": [2],
        "explanation": "For the purpose of applying an access list to a particular interface, the ipv6 traffic-filter IPv6 command is equivalent to the access-group IPv4 command. The direction in which the traffic is examined (in or out) is also required."
    },
    {
        "id": 1026,
        "type": "radio",
        "question": "What technology has a function of using trusted third-party protocols to issue credentials that are accepted as an authoritative identity?",
        "image": None,
        "options": [
            "digital signatures",
            "hashing algorithms",
            "PKI certificates",
            "symmetric keys"
        ],
        "correct": [2],
        "explanation": "Digital certificates are used to prove the authenticity and integrity of PKI certificates, but a PKI Certificate Authority is a trusted third-party entity that issues PKI certificates. PKI certificates are public information and are used to provide authenticity, confidentiality, integrity, and nonrepudiation services that can scale to large requirements."
    },
    {
        "id": 1027,
        "type": "checkbox",
        "question": "What are two methods to maintain certificate revocation status? (Choose two.)",
        "image": None,
        "options": [
            "subordinate CA",
            "OCSP",
            "DNS",
            "LDAP",
            "CRL"
        ],
        "correct": [1, 4],
        "explanation": "A digital certificate might need to be revoked if its key is compromised or it is no longer needed. The certificate revocation list (CRL) and Online Certificate Status Protocol (OCSP), are two common methods to check a certificate revocation status."
    },
    {
        "id": 1028,
        "type": "radio",
        "question": "Which protocol is an IETF standard that defines the PKI digital certificate format?",
        "image": None,
        "options": [
            "SSL/TLS",
            "X.500",
            "LDAP",
            "X.509"
        ],
        "correct": [3],
        "explanation": "To address the interoperability of different PKI vendors, IETF published the Internet X.509 Public Key Infrastructure Certificate Policy and Certification Practices Framework (RFC 2527). The standard defines the format of a digital certificate."
    },
    {
        "id": 1029,
        "type": "radio",
        "question": "A network administrator is configuring DAI on a switch. Which command should be used on the uplink interface that connects to a router?",
        "image": None,
        "options": [
            "ip arp inspection trust",
            "ip dhcp snooping",
            "ip arp inspection vlan",
            "spanning-tree portfast"
        ],
        "correct": [0],
        "explanation": "In general, a router serves as the default gateway for the LAN or VLAN on the switch. Therefore, the uplink interface that connects to a router should be a trusted port for forwarding ARP requests."
    },
    {
        "id": 1030,
        "type": "radio",
        "question": "What is the best way to prevent a VLAN hopping attack?",
        "image": None,
        "options": [
            "Disable trunk negotiation for trunk ports and statically set nontrunk ports as access ports.",
            "Disable STP on all nontrunk ports.",
            "Use VLAN 1 as the native VLAN on trunk ports.",
            "Use ISL encapsulation on all trunk links."
        ],
        "correct": [0],
        "explanation": "VLAN hopping attacks rely on the attacker being able to create a trunk link with a switch. Disabling DTP and configuring user-facing ports as static access ports can help prevent these types of attacks. Disabling the Spanning Tree Protocol (STP) will not eliminate VLAN hopping attacks."
    },
    {
        "id": 1031,
        "type": "radio",
        "question": "What would be the primary reason an attacker would launch a MAC address overflow attack?",
        "image": None,
        "options": [
            "so that the switch stops forwarding traffic",
            "so that legitimate hosts cannot obtain a MAC address",
            "so that the attacker can see frames that are destined for other hosts",
            "so that the attacker can execute arbitrary code on the switch"
        ],
        "correct": [2],
        "explanation": "A MAC address overflow attack floods the switch with fake MAC addresses to fill the CAM table. When the table is full, the switch can no longer learn new MAC addresses and starts flooding traffic out all ports, allowing the attacker to see frames destined for other hosts."
    },
    {
        "id": 1032,
        "type": "radio",
        "question": "What is the main difference between the implementation of IDS and IPS devices?",
        "image": None,
        "options": [
            "An IDS can negatively impact the packet flow, whereas an IPS can not.",
            "An IDS needs to be deployed together with a firewall device, whereas an IPS can replace a firewall.",
            "An IDS would allow malicious traffic to pass before it is addressed, whereas an IPS stops it immediately.",
            "An IDS uses signature-based technology to detect malicious packets, whereas an IPS uses profile-based technology."
        ],
        "correct": [2],
        "explanation": "An IPS is deployed in inline mode and will not allow malicious traffic to enter the internal network without first analyzing it. An advantage of this is that it can stop an attack immediately. An IDS is deployed in promiscuous mode. It copies the traffic patterns and analyzes them offline, thus it cannot stop the attack immediately and it relies on another device to take further actions once it detects an attack. Being deployed in inline mode, an IPS can negatively impact the traffic flow. Both IDS and IPS can use signature-based technology to detect malicious packets. An IPS cannot replace other security devices, such as firewalls, because they perform different tasks."
    },
    {
        "id": 1033,
        "type": "radio",
        "question": "Which attack is defined as an attempt to exploit software vulnerabilities that are unknown or undisclosed by the vendor?",
        "image": None,
        "options": [
            "zero-day",
            "Trojan horse",
            "brute-force",
            "man-in-the-middle"
        ],
        "correct": [0],
        "explanation": "A zero-day attack exploits software vulnerabilities that are unknown or undisclosed by the vendor. These attacks are particularly dangerous because there are no patches or defenses available at the time of the attack."
    },
    {
        "id": 1034,
        "type": "matching",
        "question": "Match the network monitoring technology with the description.",
        "image": None,
        "left_items": [
            "IDS",
            "RSPAN",
            "TAP",
            "IPS"
        ],
        "right_items": [
            "passively monitors network traffic",
            "uses VLANs to monitor traffic on remote switches",
            "a passive traffic splitting device implemented inline between a device of interest and the network",
            "can perform a packet drop to stop the trigger packets"
        ],
        "correct": [0, 1, 2, 3],
        "explanation": "Place the options in the following order:\n- passively monitors network traffic: IDS\n- uses VLANs to monitor traffic on remote switches: RSPAN\n- a passive traffic splitting device implemented inline between a device of interest and the network: TAP\n- can perform a packet drop to stop the trigger packets: IPS"
    },
    {
        "id": 1035,
        "type": "checkbox",
        "question": "What are the three signature levels provided by Snort IPS on the 4000 Series ISR? (Choose three.)",
        "image": None,
        "options": [
            "security",
            "drop",
            "reject",
            "connectivity",
            "inspect",
            "balanced"
        ],
        "correct": [0, 3, 5],
        "explanation": "Snort IPS on the 4000 Series ISR provides three signature levels: security, connectivity, and balanced. These levels determine the trade-off between security protection and network performance."
    },
    {
        "id": 1036,
        "type": "checkbox",
        "question": "What are three attributes of IPS signatures? (Choose three.)",
        "image": None,
        "options": [
            "action",
            "length",
            "trigger",
            "type",
            "depth",
            "function"
        ],
        "correct": [0, 2, 3],
        "explanation": "IPS signatures have three distinctive attributes:\n- type\n- trigger (alarm)\n- action"
    },
    {
        "id": 1037,
        "type": "matching",
        "question": "Match each IPS signature trigger category with the description.",
        "image": None,
        "left_items": [
            "pattern-based detection",
            "anomaly-based detection",
            "policy-based detection",
            "honey pot-based detection"
        ],
        "right_items": [
            "simplest triggering mechanism which searches for a specific and pre-defined atomic or composite pattern",
            "involves first defining a profile of what is considered normal network or host activity",
            "requires an administrator to manually define behaviors that are suspicious based on historical analysis",
            "uses a decoy server to divert attacks away from production devices"
        ],
        "correct": [0, 1, 2, 3],
        "explanation": "(ESTA PREGUNTA PUEDE APARECER EN VARIOS FORMATOS)\nIPS signature trigger categories:\n- pattern-based detection: simplest triggering mechanism which searches for a specific and pre-defined atomic or composite pattern\n- anomaly-based detection: involves first defining a profile of what is considered normal network or host activity\n- policy-based detection: requires an administrator to manually define behaviors that are suspicious based on historical analysis\n- honey pot-based detection: uses a decoy server to divert attacks away from production devices"
    },
    {
        "id": 1038,
        "type": "checkbox",
        "question": "Which two features are included by both TACACS+ and RADIUS protocols? (Choose two.)",
        "image": None,
        "options": [
            "SIP support",
            "password encryption",
            "802.1X support",
            "separate authentication and authorization processes",
            "utilization of transport layer protocols"
        ],
        "correct": [1, 4],
        "explanation": "Both TACACS+ and RADIUS support password encryption (TACACS+ encrypts all communication) and use Layer 4 protocol (TACACS+ uses TCP and RADIUS uses UDP). TACACS+ supports separation of authentication and authorization processes, while RADIUS combines authentication and authorization as one process. RADIUS supports remote access technology, such as 802.1x and SIP; TACACS+ does not."
    },
    {
        "id": 1039,
        "type": "radio",
        "question": "What function is provided by the RADIUS protocol?",
        "image": None,
        "options": [
            "RADIUS provides encryption of the complete packet during transfer.",
            "RADIUS provides separate AAA services.",
            "RADIUS provides separate ports for authorization and accounting.",
            "RADIUS provides secure communication using TCP port 49."
        ],
        "correct": [2],
        "explanation": "When an AAA user is authenticated, RADIUS uses UDP port 1645 or 1812 for authentication and UDP port 1646 or 1813 for accounting. TACACS provides separate authorization and accounting services. When a RADIUS client is authenticated, it is also authorized. TACACS provides secure connectivity using TCP port 49. RADIUS hides passwords during transmission and does not encrypt the complete packet."
    },
    {
        "id": 1040,
        "type": "checkbox",
        "question": "What are three characteristics of the RADIUS protocol? (Choose three.)",
        "image": None,
        "options": [
            "utilizes TCP port 49",
            "uses UDP ports for authentication and accounting",
            "supports 802.1X and SIP",
            "separates the authentication and authorization processes",
            "encrypts the entire body of the packet",
            "is an open RFC standard AAA protocol"
        ],
        "correct": [1, 2, 5],
        "explanation": "RADIUS is an open-standard AAA protocol using UDP port 1645 or 1812 for authentication and UDP port 1646 or 1813 for accounting. It combines authentication and authorization into one process; thus, a password is encrypted for transmission while the rest of the packet will be sent in plain text. RADIUS offers the expedited service and more comprehensive accounting desired by remote-access providers but provides lower security and less potential for customization than TACACS+."
    },
    {
        "id": 1041,
        "type": "radio",
        "question": "Which zone-based policy firewall zone is system-defined and applies to traffic destined for the router or originating from the router?",
        "image": None,
        "options": [
            "local zone",
            "inside zone",
            "self zone",
            "system zone",
            "outside zone"
        ],
        "correct": [2],
        "explanation": "Zone-based policy firewalls typically have the private (internal or trusted) zone, the public (external or untrusted) zone, and the default self zone, which does not require any interfaces. The private or internal zone is commonly used for internal LANs. The public zone would include the interfaces that connect to an external (outside the business) interface."
    },
    {
        "id": 1042,
        "type": "checkbox",
        "question": "What are two benefits of using a ZPF rather than a Classic Firewall? (Choose two.)",
        "image": None,
        "options": [
            "ZPF allows interfaces to be placed into zones for IP inspection.",
            "The ZPF is not dependent on ACLs.",
            "Multiple inspection actions are used with ZPF.",
            "ZPF policies are easy to read and troubleshoot.",
            "With ZPF, the router will allow packets unless they are explicitly blocked."
        ],
        "correct": [1, 3],
        "explanation": "There are several benefits of a ZPF:\n- It is not dependent on ACLs.\n- The router security posture is to block unless explicitly allowed.\n- Policies are easy to read and troubleshoot with C3PL.\n- One policy affects any given traffic, instead of needing multiple ACLs and inspection actions.\n\nIn addition, an interface cannot be simultaneously configured as a security zone member and for IP inspection."
    },
    {
        "id": 1043,
        "type": "matching",
        "question": "Place the steps for configuring zone-based policy (ZPF) firewalls in order from first to last. (Not all options are used.)",
        "image": None,
        "left_items": [
            "1st",
            "2nd",
            "3rd",
            "4th",
            "5th"
        ],
        "right_items": [
            "Apply policies.",
            "Assign zones to interfaces.",
            "Create access lists.",
            "Create policies.",
            "Create zones.",
            "Define traffic classes."
        ],
        "correct": [4, 5, 3, 0, 1],
        "explanation": "The correct order for configuring ZPF firewalls is:\n1st - Create zones.\n2nd - Define traffic classes.\n3rd - Create policies.\n4th - Apply policies.\n5th - Assign zones to interfaces.\n\n'Create access lists' is not used in this process."
    },
    {
        "id": 1044,
        "type": "radio",
        "question": "How does a firewall handle traffic when it is originating from the private network and traveling to the DMZ network? (SOSPECHOSA)",
        "image": None,
        "options": [
            "The traffic is selectively denied based on service requirements.",
            "The traffic is usually permitted with little or no restrictions.",
            "The traffic is selectively permitted and inspected.",
            "The traffic is usually blocked."
        ],
        "correct": [1],
        "explanation": "Traffic originating from the private network is inspected as it travels toward the public or DMZ network. This traffic is permitted with little or no restriction. Inspected traffic returning from the DMZ or public network to the private network is permitted.(TAMBIÉN PUEDE SER LA OPCIÓN 3: The traffic is selectively permitted and inspected.)"
    },
    {
        "id": 1045,
        "type": "checkbox",
        "question": "Which two protocols generate connection information within a state table and are supported for stateful filtering? (Choose two.)",
        "image": None,
        "options": [
            "ICMP",
            "UDP",
            "DHCP",
            "TCP",
            "HTTP"
        ],
        "correct": [3, 4],
        "explanation": "Stateful firewalls maintain connection state information in a state table. TCP and HTTP are connection-oriented protocols that generate connection information that can be tracked. TCP uses a three-way handshake to establish connections, and HTTP runs over TCP, both creating entries in the state table. UDP and ICMP are connectionless protocols that don't maintain state information in the same way. DHCP uses UDP as its transport protocol."
    },
    {
        "id": 1046,
        "type": "radio",
        "question": "Which type of firewall is supported by most routers and is the easiest to implement?",
        "image": None,
        "options": [
            "next generation firewall",
            "stateless firewall",
            "stateful firewall",
            "proxy firewall"
        ],
        "correct": [1],
        "explanation": "Packet Filtering (Stateless) Firewall uses a simple policy table look-up that filters traffic based on specific criteria and is considered the easiest firewall to implement."
    },
    {
        "id": 1047,
        "type": "radio",
        "question": "What network testing tool would an administrator use to assess and validate system configurations against security policies and compliance standards?",
        "image": None,
        "options": [
            "Tripwire",
            "L0phtcrack",
            "Nessus",
            "Metasploit"
        ],
        "correct": [0],
        "explanation": "Tripwire – This tool assesses and validates IT configurations against internal policies, compliance standards, and security best practices."
    },
    {
        "id": 1048,
        "type": "radio",
        "question": "What type of network security test can detect and report changes made to network systems?",
        "image": None,
        "options": [
            "vulnerability scanning",
            "network scanning",
            "integrity checking",
            "penetration testing"
        ],
        "correct": [2],
        "explanation": "Integrity checking is used to detect and report changes made to systems. Vulnerability scanning is used to find weaknesses and misconfigurations on network systems. Network scanning is used to discover available resources on the network."
    },
    {
        "id": 1049,
        "type": "radio",
        "question": "What network security testing tool has the ability to provide details on the source of suspicious network activity?",
        "image": None,
        "options": [
            "SIEM",
            "SuperScan",
            "Zenmap",
            "Tripwire"
        ],
        "correct": [0],
        "explanation": "There are various network security tools available for network security testing and evaluation. SuperScan is a Microsoft port scanning software that detects open TCP and UDP ports on systems. Nmap and Zenmap are low-level network scanners available to the public. Tripwire is used to assess if network devices are compliant with network security policies. SIEM is used to provide real-time reporting of security events on the network."
    },
    {
        "id": 1050,
        "type": "radio",
        "question": "How do modern cryptographers defend against brute-force attacks?",
        "image": None,
        "options": [
            "Use statistical analysis to eliminate the most common encryption keys.",
            "Use a keyspace large enough that it takes too much money and too much time to conduct a successful attack.",
            "Use an algorithm that requires the attacker to have both ciphertext and plaintext to conduct a successful attack.",
            "Use frequency analysis to ensure that the most popular letters used in the language are not used in the cipher message."
        ],
        "correct": [1],
        "explanation": "In a brute-force attack, an attacker tries every possible key with the decryption algorithm knowing that eventually one of them will work. To defend against the brute-force attacks, modern cryptographers have as an objective to have a keyspace (a set of all possible keys) large enough so that it takes too much money and too much time to accomplish a brute-force attack. A security policy requiring passwords to be changed in a predefined interval further defend against the brute-force attacks. The idea is that passwords will have been changed before an attacker exhausts the keyspace."
    },
    {
        "id": 1051,
        "type": "radio",
        "question": "How does a Caesar cipher work on a message?",
        "image": None,
        "options": [
            "Letters of the message are replaced by another letter that is a set number of places away in the alphabet.",
            "Letters of the message are rearranged randomly.",
            "Letters of the message are rearranged based on a predetermined pattern.",
            "Words of the message are substituted based on a predetermined pattern."
        ],
        "correct": [0],
        "explanation": "A Caesar cipher is a substitution cipher where each letter in the plaintext is shifted a certain number of places down or up the alphabet."
    },
    {
        "id": 1052,
        "type": "radio",
        "question": "What is the main factor that ensures the security of encryption of modern algorithms?",
        "image": None,
        "options": [
            "complexity of the hashing algorithm",
            "the use of 3DES over AES",
            "secrecy of the keys",
            "secrecy of the algorithm"
        ],
        "correct": [2],
        "explanation": "With most modern algorithms, successful decryption requires knowledge of the appropriate cryptographic keys. This means that the security of encryption lies in the secrecy of the keys, not the algorithm."
    },
    {
        "id": 1053,
        "type": "radio",
        "question": "What is the next step in the establishment of an IPsec VPN after IKE Phase 1 is complete?",
        "image": None,
        "options": [
            "negotiation of the ISAKMP policy",
            "negotiation of the IPsec SA policy",
            "detection of interesting traffic",
            "authentication of peers"
        ],
        "correct": [1],
        "explanation": "Establishing an IPsec tunnel involves five steps:\n1. detection of interesting traffic defined by an ACL\n2. IKE Phase 1 in which peers negotiate ISAKMP SA policy\n3. IKE Phase 2 in which peers negotiate IPsec SA policy\n4. Creation of the IPsec tunnel\n5. Termination of the IPsec tunnel"
    },
    {
        "id": 1054,
        "type": "radio",
        "question": "Refer to the exhibit. What algorithm will be used for providing confidentiality?",
        "image": "/static/images/1054.jpg",
        "options": [
            "RSA",
            "Diffie-Hellman",
            "DES",
            "AES"
        ],
        "correct": [3],
        "explanation": "The IPsec framework uses various protocols and algorithms to provide data confidentiality, data integrity, authentication, and secure key exchange. Two popular algorithms that are used to ensure that data is not intercepted and modified (data integrity) are MD5 and SHA. AES is an encryption protocol and provides data confidentiality. DH (Diffie-Hellman) is an algorithm that is used for key exchange. RSA is an algorithm used for authentication."
    },
    {
        "id": 1055,
        "type": "radio",
        "question": "After issuing a show run command, an analyst notices the following command:\n\ncrypto ipsec transform-set MYSET esp-aes 256 esp-md5-hmac\n\nWhat is the purpose of this command?",
        "image": None,
        "options": [
            "It establishes the set of encryption and hashing algorithms used to secure the data sent through an IPsec tunnel.",
            "It defines the default ISAKMP policy list used to establish the IKE Phase 1 tunnel.",
            "It establishes the criteria to force the IKE Phase 1 negotiations to begin.",
            "It indicates that IKE will be used to establish the IPsec tunnel for protecting the traffic."
        ],
        "correct": [0],
        "explanation": "The crypto ipsec transform-set command defines the encryption (esp-aes 256) and hashing (esp-md5-hmac) algorithms used to secure data in an IPsec tunnel."
    },
    {
        "id": 1056,
        "type": "radio",
        "question": "Which algorithm can ensure data integrity?",
        "image": None,
        "options": [
            "RSA",
            "AES",
            "MD5",
            "PKI"
        ],
        "correct": [2],
        "explanation": "Data integrity guarantees that the message was not altered in transit. Integrity is ensured by implementing either of the Secure Hash Algorithms (SHA-2 or SHA-3). The MD5 message digest algorithm is still widely in use."
    },
    {
        "id": 1057,
        "type": "checkbox",
        "question": "A company implements a security policy that ensures that a file sent from the headquarters office to the branch office can only be opened with a predetermined code. This code is changed every day. Which two algorithms can be used to achieve this task? (Choose two.)",
        "image": None,
        "options": [
            "HMAC",
            "MD5",
            "3DES",
            "SHA-1",
            "AES"
        ],
        "correct": [2, 4],
        "explanation": "The task to ensure that only authorized personnel can open a file is data confidentiality, which can be implemented with encryption. AES and 3DES are two encryption algorithms. HMAC can be used for ensuring origin authentication. MD5 and SHA-1 can be used to ensure data integrity."
    },
    {
        "id": 1058,
        "type": "radio",
        "question": "A network technician has been asked to design a virtual private network between two branch routers. Which type of cryptographic key should be used in this scenario?",
        "image": None,
        "options": [
            "hash key",
            "symmetric key",
            "asymmetric key",
            "digital signature"
        ],
        "correct": [1],
        "explanation": "A symmetric key requires that both routers have access to the secret key that is used to encrypt and decrypt exchanged data."
    },
    {
        "id": 1059,
        "type": "checkbox",
        "question": "Which two options can limit the information discovered from port scanning? (Choose two.)",
        "image": None,
        "options": [
            "intrusion prevention system",
            "firewall",
            "authentication",
            "passwords",
            "encryption"
        ],
        "correct": [0, 1],
        "explanation": "Using an intrusion prevention system (IPS) and firewall can limit the information that can be discovered with a port scanner. Authentication, encryption, and passwords provide no protection from loss of information from port scanning."
    },
    {
        "id": 1060,
        "type": "radio",
        "question": "An administrator discovers that a user is accessing a newly established website that may be detrimental to company security. What action should the administrator take first in terms of the security policy?",
        "image": None,
        "options": [
            "Ask the user to stop immediately and inform the user that this constitutes grounds for dismissal.",
            "Create a firewall rule blocking the respective website.",
            "Revise the AUP immediately and get all users to sign the updated AUP.",
            "Immediately suspend the network privileges of the user."
        ],
        "correct": [2],
        "explanation": "The first action should be to revise the Acceptable Use Policy (AUP) to address the newly established website and ensure all users sign the updated policy. This establishes a clear policy framework before taking punitive actions against users."
    },
    {
        "id": 1061,
        "type": "checkbox",
        "question": "If AAA is already enabled, which three CLI steps are required to configure a router with a specific view? (Choose three.)",
        "image": None,
        "options": [
            "Create a superview using the parser view view-name command.",
            "Associate the view with the root view.",
            "Assign users who can use the view.",
            "Create a view using the parser view command.",
            "Assign a secret password to the view.",
            "Assign commands to the view."
        ],
        "correct": [3, 4, 5],
        "explanation": "There are five steps involved to create a view on a Cisco router:\n1) AAA must be enabled.\n2) the view must be created.\n3) a secret password must be assigned to the view.\n4) commands must be assigned to the view.\n5) view configuration mode must be exited."
    },
    {
        "id": 1062,
        "type": "radio",
        "question": "Refer to the exhibit. A network administrator configures a named ACL on the router. Why is there no output displayed when the show command is issued?",
        "image": "/static/images/1062.png",
        "options": [
            "The ACL is not activated.",
            "The ACL name is case sensitive.",
            "The ACL has not been applied to an interface.",
            "No packets have matched the ACL statements yet."
        ],
        "correct": [1],
        "explanation": "ACL names are case sensitive. The show command must use the exact case as the ACL was created."
    },
    {
        "id": 1063,
        "type": "checkbox",
        "question": "ACLs are used primarily to filter traffic. What are two additional uses of ACLs? (Choose two.)",
        "image": None,
        "options": [
            "specifying internal hosts for NAT",
            "identifying traffic for QoS",
            "specifying source addresses for authentication",
            "reorganizing traffic into VLANs",
            "filtering VTP packets"
        ],
        "correct": [0, 1],
        "explanation": "ACLs are used to filter traffic to determine which packets will be permitted or denied through the router and which packets will be subject to policy-based routing. ACLs can also be used to identify traffic that requires NAT and QoS services. Prefix lists are used to control which routes will be redistributed or advertised to other routers."
    },
    {
        "id": 1064,
        "type": "checkbox",
        "question": "What two features are added in SNMPv3 to address the weaknesses of previous versions of SNMP? (Choose two.)",
        "image": None,
        "options": [
            "authentication",
            "authorization with community string priority",
            "bulk MIB objects retrieval",
            "ACL management filtering",
            "encryption"
        ],
        "correct": [0, 4],
        "explanation": "SNMPv3 adds authentication and encryption to address the security weaknesses of previous SNMP versions."
    },
    {
        "id": 1065,
        "type": "radio",
        "question": "What network testing tool is used for password auditing and recovery?",
        "image": None,
        "options": [
            "Nessus",
            "Metasploit",
            "L0phtcrack",
            "SuperScan"
        ],
        "correct": [2],
        "explanation": "The Nessus tool provides remote vulnerability scanning that focuses on remote access, password misconfiguration, and DoS against the TCP/IP stack. L0phtcrack provides password auditing and recovery. Metasploit provides information about vulnerabilities and aids in penetration testing and IDS signature development."
    },
    {
        "id": 1066,
        "type": "radio",
        "question": "Which type of firewall makes use of a server to connect to destination devices on behalf of clients?",
        "image": None,
        "options": [
            "packet filtering firewall",
            "proxy firewall",
            "stateless firewall",
            "stateful firewall"
        ],
        "correct": [1],
        "explanation": "An application gateway firewall, also called a proxy firewall, filters information at Layers 3, 4, 5, and 7 of the OSI model. It uses a proxy server to connect to remote servers on behalf of clients. Remote servers will see only a connection from the proxy server, not from the individual clients."
    },
    {
        "id": 1067,
        "type": "radio",
        "question": "Refer to the exhibit. What will be displayed in the output of the show running-config object command after the exhibited configuration commands are entered on an ASA 5506-X?",
        "image": "/static/images/1067.jpg",
        "options": [
            "host 192.168.1.4",
            "range 192.168.1.10 192.168.1.20",
            "host 192.168.1.3, host 192.168.1.4, and range 192.168.1.10 192.168.1.20",
            "host 192.168.1.3",
            "host 192.168.1.3 and host 192.168.1.4",
            "host 192.168.1.4 and range 192.168.1.10 192.168.1.20"
        ],
        "correct": [1],
        "explanation": "The show running-config object command is used to display or verify the IP address/mask pair within the object. There can only be one statement in the network object. Entering a second IP address/mask pair will replace the existing configuration."
    },
    {
        "id": 1068,
        "type": "checkbox",
        "question": "Refer to the exhibit. According to the command output, which three statements are true about the DHCP options entered on the ASA? (Choose three.)",
        "image": "/static/images/1068.jpg",
        "options": [
            "The dhcpd address [ start-of-pool ]-[ end-of-pool ] inside command was issued to enable the DHCP server.",
            "The dhcpd address [ start-of-pool ]-[ end-of-pool ] inside command was issued to enable the DHCP client.",
            "The dhcpd enable inside command was issued to enable the DHCP server.",
            "The dhcpd auto-config outside command was issued to enable the DHCP client.",
            "The dhcpd auto-config outside command was issued to enable the DHCP server.",
            "The dhcpd enable inside command was issued to enable the DHCP client."
        ],
        "correct": [0, 2, 3],
        "explanation": "The dhcpd address command configures the DHCP address pool, the dhcpd enable inside command enables the DHCP server on the inside interface, and the dhcpd auto-config outside command enables the DHCP client on the outside interface."
    },
    {
        "id": 1069,
        "type": "checkbox",
        "question": "Which two statements describe the characteristics of symmetric algorithms? (Choose two.)",
        "image": None,
        "options": [
            "They are commonly used with VPN traffic.",
            "They use a pair of a public key and a private key.",
            "They are commonly implemented in the SSL and SSH protocols.",
            "They provide confidentiality, integrity, and availability.",
            "They are referred to as a pre-shared key or secret key."
        ],
        "correct": [0, 4],
        "explanation": "Symmetric encryption algorithms use the same key (also called shared secret) to encrypt and decrypt the data. In contrast, asymmetric encryption algorithms use a pair of keys, one for encryption and another for decryption."
    },
    {
        "id": 1070,
        "type": "radio",
        "question": "A web server administrator is configuring access settings to require users to authenticate first before accessing certain web pages. Which requirement of information security is addressed through the configuration?",
        "image": None,
        "options": [
            "availability",
            "integrity",
            "scalability",
            "confidentiality"
        ],
        "correct": [3],
        "explanation": "Confidentiality ensures that data is accessed only by authorized individuals. Authentication will help verify the identity of the individuals."
    },
    {
        "id": 1071,
        "type": "radio",
        "question": "The use of 3DES within the IPsec framework is an example of which of the five IPsec building blocks?",
        "image": None,
        "options": [
            "authentication",
            "nonrepudiation",
            "integrity",
            "Diffie-Hellman",
            "confidentiality"
        ],
        "correct": [4],
        "explanation": "The IPsec framework consists of five building blocks. Each building block performs a specific security function via specific protocols. The function of providing confidentiality is provided by protocols such as DES, 3DES, and AES."
    },
    {
        "id": 1072,
        "type": "radio",
        "question": "What function is provided by Snort as part of the Security Onion?",
        "image": None,
        "options": [
            "to generate network intrusion alerts by the use of rules and signatures",
            "to normalize logs from various NSM data logs so they can be represented, stored, and accessed through a common schema",
            "to display full-packet captures for analysis",
            "to view pcap transcripts generated by intrusion detection tools"
        ],
        "correct": [0],
        "explanation": "Snort is a NIDS integrated into Security Onion. It is an important source of the alert data that is indexed in the Sguil analysis tool. Snort uses rules and signatures to generate alerts."
    },
    {
        "id": 1073,
        "type": "checkbox",
        "question": "What are two drawbacks to using HIPS? (Choose two.)",
        "image": None,
        "options": [
            "With HIPS, the success or failure of an attack cannot be readily determined.",
            "With HIPS, the network administrator must verify support for all the different operating systems used in the network.",
            "HIPS has difficulty constructing an accurate network picture or coordinating events that occur across the entire network.",
            "If the network traffic stream is encrypted, HIPS is unable to access unencrypted forms of the traffic.",
            "HIPS installations are vulnerable to fragmentation attacks or variable TTL attacks."
        ],
        "correct": [1, 2],
        "explanation": "Two disadvantages of deploying HIPS are (1) that it cannot create a complete view of the network or have knowledge of events that might be occurring beyond an individual host and (2) every host operating system within the organization must be supported. However, an advantage of using HIPS is that it can monitor and protect the operating system as well as critical system processes on each network host."
    },
    {
        "id": 1074,
        "type": "radio",
        "question": "In an AAA-enabled network, a user issues the configure terminal command from the privileged executive mode of operation. What AAA function is at work if this command is rejected?",
        "image": None,
        "options": [
            "authorization",
            "authentication",
            "auditing",
            "accounting"
        ],
        "correct": [0],
        "explanation": "Authentication must ensure that devices or end users are legitimate. Authorization is concerned with allowing and disallowing authenticated users access to certain areas and programs on the network. The configure terminal command is rejected because the user is not authorized to execute the command."
    },
    {
        "id": 1075,
        "type": "radio",
        "question": "A company has a file server that shares a folder named Public. The network security policy specifies that the Public folder is assigned Read-Only rights to anyone who can log into the server while the Edit rights are assigned only to the network admin group. Which component is addressed in the AAA network service framework?",
        "image": None,
        "options": [
            "automation",
            "accounting",
            "authentication",
            "authorization"
        ],
        "correct": [3],
        "explanation": "After a user is successfully authenticated (logged into the server), the authorization is the process of determining what network resources the user can access and what operations (such as read or edit) the user can perform."
    },
    {
        "id": 1076,
        "type": "radio",
        "question": "What is a characteristic of a DMZ zone?",
        "image": None,
        "options": [
            "Traffic originating from the inside network going to the DMZ network is not permitted.",
            "Traffic originating from the outside network going to the DMZ network is selectively permitted.",
            "Traffic originating from the DMZ network going to the inside network is permitted.",
            "Traffic originating from the inside network going to the DMZ network is selectively permitted."
        ],
        "correct": [1],
        "explanation": "The characteristics of a DMZ zone are as follows:\n- Traffic originating from the inside network going to the DMZ network is permitted.\n- Traffic originating from the outside network going to the DMZ network is selectively permitted.\n- Traffic originating from the DMZ network going to the inside network is denied."
    },
    {
        "id": 1077,
        "type": "radio",
        "question": "Which measure can a security analyst take to perform effective security monitoring against network traffic encrypted by SSL technology?",
        "image": None,
        "options": [
            "Use a Syslog server to capture network traffic.",
            "Deploy a Cisco SSL Appliance.",
            "Require remote access connections through IPsec VPN.",
            "Deploy a Cisco ASA."
        ],
        "correct": [1],
        "explanation": "Deploy a Cisco SSL Appliance to decrypt SSL traffic and send it to intrusion prevention system (IPS) appliances to identify risks normally hidden by SSL."
    },
    {
        "id": 1078,
        "type": "radio",
        "question": "Refer to the exhibit. Port security has been configured on the Fa 0/12 interface of switch S1. What action will occur when PC1 is attached to switch S1 with the applied configuration?",
        "image": "/static/images/1078.png",
        "options": [
            "Frames from PC1 will be forwarded since the switchport port-security violation command is missing.",
            "Frames from PC1 will be forwarded to its destination, and a log entry will be created.",
            "Frames from PC1 will be forwarded to its destination, but a log entry will not be created.",
            "Frames from PC1 will cause the interface to shut down immediately, and a log entry will be made.",
            "Frames from PC1 will be dropped, and there will be no log of the violation.",
            "Frames from PC1 will be dropped, and a log message will be created."
        ],
        "correct": [3],
        "explanation": "Manual configuration of the single allowed MAC address has been entered for port fa0/12. PC1 has a different MAC address and when attached will cause the port to shut down (the default action), a log message to be automatically created, and the violation counter to increment. The default action of shutdown is recommended because the restrict option might fail if an attack is underway."
    },
    {
        "id": 1079,
        "type": "radio",
        "question": "What security countermeasure is effective for preventing CAM table overflow attacks?",
        "image": None,
        "options": [
            "DHCP snooping",
            "Dynamic ARP Inspection",
            "IP source guard",
            "port security"
        ],
        "correct": [3],
        "explanation": "Port security is the most effective method for preventing CAM table overflow attacks. Port security gives an administrator the ability to manually specify what MAC addresses should be seen on given switch ports. It provides a method for limiting the number of MAC addresses that can be dynamically learned over a switch port."
    },
    {
        "id": 1080,
        "type": "checkbox",
        "question": "What are two examples of DoS attacks? (Choose two.)",
        "image": None,
        "options": [
            "port scanning",
            "SQL injection",
            "ping of death",
            "phishing",
            "buffer overflow"
        ],
        "correct": [2, 4],
        "explanation": "The buffer overflow and ping of death DoS attacks exploit system memory-related flaws on a server by sending an unexpected amount of data or malformed data to the server."
    },
    {
        "id": 1081,
        "type": "radio",
        "question": "Which method is used to identify interesting traffic needed to create an IKE phase 1 tunnel?",
        "image": None,
        "options": [
            "transform sets",
            "a permit access list entry",
            "hashing algorithms",
            "a security association"
        ],
        "correct": [1],
        "explanation": "A permit access list entry is used to identify interesting traffic that triggers the creation of an IKE Phase 1 tunnel."
    },
    {
        "id": 1082,
        "type": "checkbox",
        "question": "When the CLI is used to configure an ISR for a site-to-site VPN connection, which two items must be specified to enable a crypto map policy? (Choose two.)",
        "image": None,
        "options": [
            "the hash",
            "the peer",
            "encryption",
            "the ISAKMP policy",
            "a valid access list",
            "IP addresses on all active interfaces",
            "the IKE Phase 1 policy"
        ],
        "correct": [1, 4],
        "explanation": "After the crypto map command in global configuration mode has been issued, the new crypto map will remain disabled until a peer and a valid access list have been configured."
    },
    {
        "id": 1083,
        "type": "radio",
        "question": "How does a firewall handle traffic when it is originating from the public network and traveling to the DMZ network?",
        "image": None,
        "options": [
            "Traffic that is originating from the public network is inspected and selectively permitted when traveling to the DMZ network.",
            "Traffic that is originating from the public network is usually permitted with little or no restriction when traveling to the DMZ network.",
            "Traffic that is originating from the public network is usually forwarded without inspection when traveling to the DMZ network.",
            "Traffic that is originating from the public network is usually blocked when traveling to the DMZ network."
        ],
        "correct": [0],
        "explanation": "Traffic originating from the public network and traveling toward the DMZ is selectively permitted and inspected. This type of traffic is typically email, DNS, HTTP, or HTTPS traffic. Return traffic from the DMZ to the public network is dynamically permitted."
    },
    {
        "id": 1084,
        "type": "radio",
        "question": "A client connects to a Web server. Which component of this HTTP connection is not examined by a stateful firewall?",
        "image": None,
        "options": [
            "the source IP address of the client traffic",
            "the destination port number of the client traffic",
            "the actual contents of the HTTP connection",
            "the source port number of the client traffic"
        ],
        "correct": [2],
        "explanation": "Stateful firewalls cannot prevent application layer attacks because they do not examine the actual contents of the HTTP connection."
    },
    {
        "id": 1085,
        "type": "radio",
        "question": "Which network monitoring technology uses VLANs to monitor traffic on remote switches?",
        "image": None,
        "options": [
            "IPS",
            "IDS",
            "TAP",
            "RSPAN"
        ],
        "correct": [3],
        "explanation": "Remote SPAN (RSPAN) enables a network administrator to use the flexibility of VLANs to monitor traffic on remote switches."
    },
    {
        "id": 1086,
        "type": "radio",
        "question": "Which rule action will cause Snort IPS to block and log a packet?",
        "image": None,
        "options": [
            "log",
            "drop",
            "alert",
            "Sdrop"
        ],
        "correct": [1],
        "explanation": "Snort IPS mode can perform all the IDS actions plus the following:\n- Drop – Block and log the packet.\n- Reject – Block the packet, log it, and then send a TCP reset if the protocol is TCP or an ICMP port unreachable message if the protocol is UDP.\n- Sdrop – Block the packet but do not log it."
    },
    {
        "id": 1087,
        "type": "radio",
        "question": "What is typically used to create a security trap in the data center facility?",
        "image": None,
        "options": [
            "IDs, biometrics, and two access doors",
            "high resolution monitors",
            "redundant authentication servers",
            "a server without all security patches applied"
        ],
        "correct": [0],
        "explanation": "Security traps provide access to the data halls where data center data is stored. A security trap is similar to an air lock. A person must first enter the security trap using their badge ID proximity card. After the person is inside the security trap, facial recognition, fingerprints, or other biometric verifications are used to open the second door. The user must repeat the process to exit the data hall."
    },
    {
        "id": 1088,
        "type": "radio",
        "question": "A company is concerned with leaked and stolen corporate data on hard copies. Which data loss mitigation technique could help with this situation?",
        "image": None,
        "options": [
            "strong PC security settings",
            "strong passwords",
            "shredding",
            "encryption"
        ],
        "correct": [2],
        "explanation": "Confidential data should be shredded when no longer required. Otherwise, a thief could retrieve discarded reports and gain valuable information."
    },
    {
        "id": 1089,
        "type": "radio",
        "question": "Upon completion of a network security course, a student decides to pursue a career in cryptanalysis. What job would the student be doing as a cryptanalyst?",
        "image": None,
        "options": [
            "cracking code without access to the shared secret key",
            "creating hashing codes to authenticate data",
            "making and breaking secret codes",
            "creating transposition and substitution ciphers"
        ],
        "correct": [0],
        "explanation": "Cryptanalysis is the practice and study of determining the meaning of encrypted information (cracking the code), without access to the shared secret key. This is also known as codebreaking."
    },
    {
        "id": 1090,
        "type": "radio",
        "question": "What command is used on a switch to set the port access entity type so the interface acts only as an authenticator and will not respond to any messages meant for a supplicant?",
        "image": None,
        "options": [
            "dot1x pae authenticator",
            "authentication port-control auto",
            "aaa authentication dot1x default group radius",
            "dot1x system-auth-control"
        ],
        "correct": [0],
        "explanation": "Sets the Port Access Entity (PAE) type.\ndot1x pae [supplicant | authenticator | both]\n\n- supplicant—The interface acts only as a supplicant and does not respond to messages that are meant for an authenticator.\n- authenticator—The interface acts only as an authenticator and does not respond to any messages meant for a supplicant.\n- both—The interface behaves both as a supplicant and as an authenticator and thus does respond to all dot1x messages."
    },
    {
        "id": 1091,
        "type": "checkbox",
        "question": "What are two disadvantages of using an IDS? (Choose two.)",
        "image": None,
        "options": [
            "The IDS does not stop malicious traffic.",
            "The IDS works offline using copies of network traffic.",
            "The IDS has no impact on traffic.",
            "The IDS analyzes actual forwarded packets.",
            "The IDS requires other devices to respond to attacks."
        ],
        "correct": [0, 4],
        "explanation": "The disadvantage of operating with mirrored traffic is that the IDS cannot stop malicious single-packet attacks from reaching the target before responding to the attack. Also, an IDS often requires assistance from other networking devices, such as routers and firewalls, to respond to an attack. An advantage of an IDS is that by working offline using mirrored traffic, it has no impact on traffic flow."
    },
    {
        "id": 1092,
        "type": "radio",
        "question": "Refer to the exhibit. The ip verify source command is applied on untrusted interfaces. Which type of attack is mitigated by using this configuration?",
        "image": "/static/images/1092.jpg",
        "options": [
            "DHCP spoofing",
            "DHCP starvation",
            "STP manipulation",
            "MAC and IP address spoofing"
        ],
        "correct": [3],
        "explanation": "To protect against MAC and IP address spoofing, apply the IP Source Guard security feature, using the ip verify source command, on untrusted ports."
    },
    {
        "id": 1093,
        "type": "radio",
        "question": "What ports can receive forwarded traffic from an isolated port that is part of a PVLAN?",
        "image": None,
        "options": [
            "other isolated ports and community ports",
            "only promiscuous ports",
            "all other ports within the same community",
            "only isolated ports"
        ],
        "correct": [1],
        "explanation": "PVLANs are used to provide Layer 2 isolation between ports within the same broadcast domain. The level of isolation can be specified with three types of PVLAN ports:\n- Promiscuous ports that can forward traffic to all other ports\n- Isolated ports that can only forward traffic to promiscuous ports\n- Community ports that can forward traffic to other community ports and promiscuous ports"
    },
    {
        "id": 1094,
        "type": "radio",
        "question": "A user complains about being locked out of a device after too many unsuccessful AAA login attempts. What could be used by the network administrator to provide a secure authentication access method without locking a user out of a device?",
        "image": None,
        "options": [
            "Use the login delay command for authentication attempts.",
            "Use the login local command for authenticating user access.",
            "Use the aaa local authentication attempts max-fail global configuration mode command with a higher number of acceptable failures.",
            "Use the none keyword when configuring the authentication method list."
        ],
        "correct": [0],
        "explanation": "The login delay command introduces a delay between failed login attempts without locking the account. This provides a user with unlimited attempts at accessing a device without causing the user account to become locked and thus requiring administrator intervention."
    },
    {
        "id": 1095,
        "type": "checkbox",
        "question": "What are two drawbacks in assigning user privilege levels on a Cisco router? (Choose two.)",
        "image": None,
        "options": [
            "Only a root user can add or remove commands.",
            "Privilege levels must be set to permit access control to specific device interfaces, ports, or slots.",
            "Assigning a command with multiple keywords allows access to all commands using those keywords.",
            "Commands from a lower level are always executable at a higher level.",
            "AAA must be enabled."
        ],
        "correct": [2, 3],
        "explanation": "Privilege levels may not provide desired flexibility and specificity because higher levels always inherit commands from lower levels, and commands with multiple keywords give the user access to all commands available for each keyword. Privilege levels cannot specify access control to interfaces, ports, or slots. AAA is not required to set privilege levels, but is required in order to create role-based views. The role of root user does not exist in privilege levels."
    },
    {
        "id": 1096,
        "type": "radio",
        "question": "Refer to the exhibit. Which conclusion can be made from the show crypto map command output that is shown on R1?",
        "image": "/static/images/1096.jpg",
        "options": [
            "The crypto map has not yet been applied to an interface.",
            "The current peer IP address should be 172.30.2.1.",
            "There is a mismatch between the transform sets.",
            "The tunnel configuration was established and can be tested with extended pings."
        ],
        "correct": [0],
        "explanation": "According to the show crypto map command output, all required SAs are in place, but no interface is currently using the crypto map. To complete the tunnel configuration, the crypto map has to be applied to the outbound interface of each router."
    },
    {
        "id": 1097,
        "type": "checkbox",
        "question": "What are two reasons to enable OSPF routing protocol authentication on a network? (Choose two.)",
        "image": None,
        "options": [
            "to prevent data traffic from being redirected and then discarded",
            "to ensure faster network convergence",
            "to provide data security through encryption",
            "to prevent redirection of data traffic to an insecure link",
            "to ensure more efficient routing"
        ],
        "correct": [0, 3],
        "explanation": "The reason to configure OSPF authentication is to mitigate against routing protocol attacks like redirection of data traffic to an insecure link, and redirection of data traffic to discard it. OSPF authentication does not provide faster network convergence, more efficient routing, or encryption of data traffic."
    },
    {
        "id": 1098,
        "type": "checkbox",
        "question": "Which three functions are provided by the syslog logging service? (Choose three.)",
        "image": None,
        "options": [
            "gathering logging information",
            "authenticating and encrypting data sent over the network",
            "retaining captured messages on the router when a router is rebooted",
            "specifying where captured information is stored",
            "distinguishing between information to be captured and information to be ignored",
            "setting the size of the logging buffer"
        ],
        "correct": [0, 3, 4],
        "explanation": "Syslog operations include gathering information, selecting which type of information to capture, and directing the captured information to a storage location. The logging service stores messages in a logging buffer that is time-limited, and cannot retain the information when a router is rebooted. Syslog does not authenticate or encrypt messages."
    },
    {
        "id": 1099,
        "type": "checkbox",
        "question": "What two ICMPv6 message types must be permitted through IPv6 access control lists to allow resolution of Layer 3 addresses to Layer 2 MAC addresses? (Choose two.)",
        "image": None,
        "options": [
            "neighbor solicitations",
            "echo requests",
            "neighbor advertisements",
            "echo replies",
            "router solicitations",
            "router advertisements"
        ],
        "correct": [0, 2],
        "explanation": "Neighbor solicitations and neighbor advertisements are ICMPv6 message types used for address resolution (similar to ARP in IPv4) and must be permitted through IPv6 ACLs."
    },
    {
        "id": 1100,
        "type": "checkbox",
        "question": "Which three services are provided through digital signatures? (Choose three.)",
        "image": None,
        "options": [
            "accounting",
            "authenticity",
            "compression",
            "nonrepudiation",
            "integrity",
            "encryption"
        ],
        "correct": [1, 3, 4],
        "explanation": "Digital signatures use a mathematical technique to provide three basic security services: Integrity, Authenticity, Nonrepudiation."
    },
    {
        "id": 1101,
        "type": "radio",
        "question": "A technician is to document the current configurations of all network devices in a college, including those in off-site buildings. Which protocol would be best to use to securely access the network devices?",
        "image": None,
        "options": [
            "FTP",
            "HTTP",
            "SSH",
            "Telnet"
        ],
        "correct": [2],
        "explanation": "Telnet sends passwords and other information in clear text, while SSH encrypts its data. FTP and HTTP do not provide remote device access for configuration purposes."
    },
    {
        "id": 1102,
        "type": "checkbox",
        "question": "An administrator is trying to develop a BYOD security policy for employees that are bringing a wide range of devices to connect to the company network. Which three objectives must the BYOD security policy address? (Choose three.)",
        "image": None,
        "options": [
            "All devices must be insured against liability if used to compromise the corporate network.",
            "All devices must have open authentication with the corporate network.",
            "Rights and activities permitted on the corporate network must be defined.",
            "Safeguards must be put in place for any personal device being compromised.",
            "The level of access of employees when connecting to the corporate network must be defined.",
            "All devices should be allowed to attach to the corporate network flawlessly."
        ],
        "correct": [2, 3, 4],
        "explanation": "A BYOD security policy should define the rights and activities permitted on the corporate network, put safeguards in place for compromised devices, and define the level of access for employees connecting to the network."
    },
    {
        "id": 1103,
        "type": "radio",
        "question": "What is the function of the pass action on a Cisco IOS Zone-Based Policy Firewall?",
        "image": None,
        "options": [
            "logging of rejected or dropped packets",
            "inspecting traffic between zones for traffic control",
            "tracking the state of connections between zones",
            "forwarding traffic from one zone to another"
        ],
        "correct": [3],
        "explanation": "The pass action performed by Cisco IOS ZPF permits forwarding of traffic in a manner similar to the permit statement in an access control list."
    },
    {
        "id": 1104,
        "type": "radio",
        "question": "Refer to the exhibit. Based on the security levels of the interfaces on ASA1, what traffic will be allowed on the interfaces?",
        "image": "/static/images/1104.png",
        "options": [
            "Traffic from the Internet and DMZ can access the LAN.",
            "Traffic from the Internet and LAN can access the DMZ.",
            "Traffic from the Internet can access both the DMZ and the LAN.",
            "Traffic from the LAN and DMZ can access the Internet."
        ],
        "correct": [3],
        "explanation": "ASA devices have security levels assigned to each interface that are not part of a configured ACL. These security levels allow traffic from more secure interfaces, such as security level 100, to access less secure interfaces, such as level 0. By default, they allow traffic from more secure interfaces (higher security level) to access less secure interfaces (lower security level). Traffic from the less secure interfaces is blocked from accessing more secure interfaces."
    },
    {
        "id": 1105,
        "type": "radio",
        "question": "What network testing tool can be used to identify network layer protocols running on a host?",
        "image": None,
        "options": [
            "SIEM",
            "Nmap",
            "L0phtcrack",
            "Tripwire"
        ],
        "correct": [1],
        "explanation": "Nmap is a network scanning tool that can identify network layer protocols and services running on hosts."
    },
    {
        "id": 1106,
        "type": "radio",
        "question": "In the implementation of security on multiple devices, how do ASA ACLs differ from Cisco IOS ACLs?",
        "image": None,
        "options": [
            "Cisco IOS routers utilize both named and numbered ACLs and Cisco ASA devices utilize only numbered ACLs.",
            "Cisco IOS ACLs are configured with a wildcard mask and Cisco ASA ACLs are configured with a subnet mask.",
            "Cisco IOS ACLs are processed sequentially from the top down and Cisco ASA ACLs are not processed sequentially.",
            "Cisco IOS ACLs utilize an implicit deny all and Cisco ASA ACLs end with an implicit permit all."
        ],
        "correct": [1],
        "explanation": "The Cisco IOS ACLs are configured with a wildcard mask and the Cisco ASA ACLs are configured with a subnet mask. Both devices use an implicit deny, top down sequential processing, and named or numbered ACLs."
    },
    {
        "id": 1107,
        "type": "radio",
        "question": "Which statement describes an important characteristic of a site-to-site VPN?",
        "image": None,
        "options": [
            "It must be statically set up.",
            "It is ideally suited for use by mobile workers.",
            "It requires using a VPN client on the host PC.",
            "After the initial connection is established, it can dynamically change connection information.",
            "It is commonly implemented over dialup and cable modem networks."
        ],
        "correct": [0],
        "explanation": "A site-to-site VPN is created between the network devices of two separate networks. The VPN is static and stays established. The internal hosts of the two networks have no knowledge of the VPN."
    },
    {
        "id": 1108,
        "type": "checkbox",
        "question": "Which two options are security best practices that help mitigate BYOD risks? (Choose two.)",
        "image": None,
        "options": [
            "Use paint that reflects wireless signals and glass that prevents the signals from going outside the building.",
            "Keep the device OS and software updated.",
            "Only allow devices that have been approved by the corporate IT team.",
            "Only turn on Wi-Fi when using the wireless network.",
            "Decrease the wireless antenna gain level.",
            "Use wireless MAC address filtering."
        ],
        "correct": [1, 3],
        "explanation": "Many companies now support employees and visitors attaching and using wireless devices that connect to and use the corporate wireless network. This practice is known as a bring-your-own-device policy or BYOD. Commonly, BYOD security practices are included in the security policy..BYOD security best practices include:\n- Use unique passwords for each device and account.\n- Turn off Wi-Fi and Bluetooth connectivity when not being used. Only connect to trusted networks.\n- Keep the device OS and other software updated.\n- Backup any data stored on the device.\n- Subscribe to a device locator service with a remote wipe feature.\n- Provide antivirus software for approved BYODs.\n- Use Mobile Device Management (MDM) software."
    },
    {
        "id": 1109,
        "type": "radio",
        "question": "Refer to the exhibit. A network administrator configures AAA authentication on R1. Which statement describes the effect of the keyword single-connection in the configuration?",
        "image": "/static/images/1109.jpg",
        "options": [
            "R1 will open a separate connection to the TACACS+ server for each user authentication session.",
            "The authentication performance is enhanced by keeping the connection to the TACACS+ server open.",
            "The TACACS+ server only accepts one successful try for a user to authenticate with it.",
            "R1 will open a separate connection to the TACACS server on a per source IP address basis for each authentication session."
        ],
        "correct": [1],
        "explanation": "The single-connection keyword enhances TCP performance with TACACS+ by maintaining a single TCP connection for the life of the session. Without the single-connection keyword, a TCP connection is opened and closed per session."
    },
    {
        "id": 1110,
        "type": "radio",
        "question": "A recently created ACL is not working as expected. The admin determined that the ACL had been applied inbound on the interface and that was the incorrect direction. How should the admin fix this issue?(SOSPECHOSO)",
        "image": None,
        "options": [
            "Delete the original ACL and create a new ACL, applying it outbound on the interface.",
            "Add an association of the ACL outbound on the same interface.",
            "Fix the ACE statements so that it works as desired inbound on the interface.",
            "Remove the inbound association of the ACL on the interface and reapply it outbound."
        ],
        "correct": [3],
        "explanation": "To fix the ACL direction issue, remove the inbound association and reapply the ACL outbound on the interface.(TAMBIEN PUEDE SER LA OPCION 1: Delete the original ACL and create a new ACL, applying it outbound on the interface.)"
    },
    {
        "id": 1111,
        "type": "radio",
        "question": "What characteristic of the Snort term-based subscriptions is true for both the community and the subscriber rule sets?",
        "image": None,
        "options": [
            "Both have a 30-day delayed access to updated signatures.",
            "Both use Cisco Talos to provide coverage in advance of exploits.",
            "Both are fully supported by Cisco and include Cisco customer support.",
            "Both offer threat protection against security threats."
        ],
        "correct": [3],
        "explanation": "There are two types of term-based subscriptions:\n\n- Community Rule Set – Available for free, this subscription offers limited coverage against threats. The community rule set focuses on reactive response to security threats versus proactive research work. There is also a 30-day delayed access to updated signatures. No Cisco customer support available.\n\n- Subscriber Rule Set – Available for a fee, this service provides the best protection against threats. It includes coverage of advance exploits by using the research work of the Cisco Talos security experts. Fully supported by Cisco."
    },
    {
        "id": 1112,
        "type": "radio",
        "question": "A security analyst is configuring Snort IPS. The analyst has just downloaded and installed the Snort OVA file. What is the next step?",
        "image": None,
        "options": [
            "Verify Snort IPS.",
            "Configure Virtual Port Group interfaces.",
            "Enable IPS globally or on desired interfaces.",
            "Activate the virtual services."
        ],
        "correct": [1],
        "explanation": "To deploy Snort IPS on supported devices, perform the following steps:\n1. Download the Snort OVA file.\n2. Install the OVA file.\n3. Configure Virtual Port Group interfaces.\n4. Activate the virtual services.\n5. Configure Snort specifics.\n6. Enable IPS globally or on desired interfaces.\n7. Verify Snort IPS."
    },
    {
        "id": 1113,
        "type": "radio",
        "question": "The security policy in a company specifies that employee workstations can initiate HTTP and HTTPS connections to outside websites and the return traffic is allowed. However, connections initiated from outside hosts are not allowed. Which parameter can be used in extended ACLs to meet this requirement?",
        "image": None,
        "options": [
            "dscp",
            "precedence",
            "eq",
            "established"
        ],
        "correct": [3],
        "explanation": "The established keyword in extended ACLs allows return traffic for TCP connections that were initiated from inside the network."
    },
    {
        "id": 1114,
        "type": "checkbox",
        "question": "A researcher is comparing the differences between a stateless firewall and a proxy firewall. Which two additional layers of the OSI model are inspected by a proxy firewall? (Choose two.)",
        "image": None,
        "options": [
            "Layer 3",
            "Layer 4",
            "Layer 5",
            "Layer 6",
            "Layer 7"
        ],
        "correct": [2, 4],
        "explanation": "Packet filtering firewalls are usually part of a router firewall, which permits or denies traffic based on Layer 3 and Layer 4 information. An application gateway firewall (proxy firewall) filters information at Layers 3, 4, 5, and 7 of the OSI reference model."
    },
    {
        "id": 1115,
        "type": "radio",
        "question": "Refer to the exhibit. A network administrator is configuring a VPN between routers R1 and R2. Which commands would correctly configure a pre-shared key for the two routers?",
        "image": "/static/images/1115.jpg",
        "options": [
            "R1(config)# username R2 password 5tayout!\nR2(config)# username R1 password 5tayout!",
            "R1(config)# crypto isakmp key 5tayout! address 64.100.0.2\nR2(config)# crypto isakmp key 5tayout! address 64.100.0.1",
            "R1(config)# crypto isakmp key 5tayout! hostname R1\nR2(config)# crypto isakmp key 5tayout! hostname R2",
            "R1(config-if)# ppp pap sent-username R1 password 5tayout!\nR2(config-if)# ppp pap sent-username R2 password 5tayout!"
        ],
        "correct": [1],
        "explanation": "The crypto isakmp key command is used to configure a pre-shared key for IKE authentication. The key must be the same on both routers, and each router must reference the other router's IP address."
    },
    {
        "id": 1116,
        "type": "radio",
        "question": "Refer to the exhibit. Which statement is true about the effect of this Cisco IOS zone-based policy firewall configuration?",
        "image": "/static/images/1116.jpg",
        "options": [
            "The firewall will automatically drop all HTTP, HTTPS, and FTP traffic.",
            "The firewall will automatically allow HTTP, HTTPS, and FTP traffic from s0/0/0 to g0/0 and will track the connections. Tracking the connection allows only return traffic to be permitted through the firewall in the opposite direction.",
            "The firewall will automatically allow HTTP, HTTPS, and FTP traffic from s0/0/0 to g0/0, but will not track the state of connections. A corresponding policy must be applied to allow return traffic to be permitted through the firewall in the opposite direction.",
            "The firewall will automatically allow HTTP, HTTPS, and FTP traffic from g0/0 to s0/0/0 and will track the connections. Tracking the connection allows only return traffic to be permitted through the firewall in the opposite direction.",
            "Return traffic to be permitted through the firewall in the opposite direction.",
            "The firewall will automatically allow HTTP, HTTPS, and FTP traffic from g0/0 to s0/0/0, but will not track the state of connections. A corresponding policy must be applied to allow return traffic to be permitted through the firewall in the opposite direction."
        ],
        "correct": [3],
        "explanation": "The pass action allows traffic but does not track the state of connections. Because the policy uses 'pass' instead of 'inspect', return traffic is not automatically allowed and a corresponding policy must be applied in the opposite direction."
    },
    {
        "id": 1117,
        "type": "radio",
        "question": "Which privilege level has the most access to the Cisco IOS?",
        "image": None,
        "options": [
            "level 0",
            "level 15",
            "level 7",
            "level 16",
            "level 1"
        ],
        "correct": [1],
        "explanation": "Privilege level 15 has the most access to the Cisco IOS. Level 0 has limited commands, Level 1 is user EXEC mode, and Level 15 is privileged EXEC mode with full access."
    },
    {
        "id": 1118,
        "type": "radio",
        "question": "Refer to the exhibit. A network administrator has configured NAT on an ASA device. What type of NAT is used?",
        "image": "/static/images/1118.jpg",
        "options": [
            "inside NAT",
            "static NAT",
            "bidirectional NAT",
            "outside NAT"
        ],
        "correct": [0],
        "explanation": "NAT can be deployed on an ASA using one of these methods:\n- inside NAT – when a host from a higher-security interface has traffic destined for a lower-security interface and the ASA translates the internal host address to a global address\n- outside NAT – when traffic from a lower-security interface destined for a host on the higher-security interface is translated\n- bidirectional NAT – when both inside NAT and outside NAT are used together\n\nBecause the nat command is applied so that the inside interface is mapped to the outside interface, the NAT type is inside. Also, the dynamic keyword in the nat command indicates that it is a dynamic mapping."
    },
    {
        "id": 1119,
        "type": "radio",
        "question": "A network analyst is configuring a site-to-site IPsec VPN. The analyst has configured both the ISAKMP and IPsec policies. What is the next step?",
        "image": None,
        "options": [
            "Configure the hash as SHA and the authentication as pre-shared.",
            "Apply the crypto map to the appropriate outbound interfaces.",
            "Issue the show crypto ipsec sa command to verify the tunnel.",
            "Verify that the security feature is enabled in the IOS."
        ],
        "correct": [1],
        "explanation": "After configuring ISAKMP and IPsec policies, the next step is to apply the crypto map to the outbound interface."
    },
    {
        "id": 1120,
        "type": "radio",
        "question": "When an inbound Internet-traffic ACL is being implemented, what should be included to prevent the spoofing of internal networks?",
        "image": None,
        "options": [
            "ACEs to prevent traffic from private address spaces",
            "ACEs to prevent broadcast address traffic",
            "ACEs to prevent ICMP traffic",
            "ACEs to prevent HTTP traffic",
            "ACEs to prevent SNMP traffic"
        ],
        "correct": [0],
        "explanation": "Common ACEs to assist with antispoofing include blocking packets that have a source address in the 127.0.0.0/8 range, any private address, or any multicast addresses. Furthermore, the administrator should not allow any outbound packets with a source address other than a valid address that is used in the internal networks of the organization."
    },
    {
        "id": 1121,
        "type": "matching",
        "question": "Match the security term to the appropriate description. (Not all options are used.)",
        "image": None,
        "left_items": [
            "vulnerability",
            "exploit",
            "assets",
            "threat",
            "mitigation",
            "risk"
        ],
        "right_items": [
            "a weakness in the design of a system that can be exploited by a threat",
            "a mechanism that takes advantage of a vulnerability",
            "the network equipment and confidential data owned by the organization",
            "a potential danger to the data and network functionality of a company",
            "the counter-measure to reduce the severity of a potential threat"
        ],
        "correct": [0, 1, 2, 3, 4],
        "explanation": "Place the options in the following order:\n- vulnerability: a weakness in the design of a system that can be exploited by a threat\n- exploit: a mechanism that takes advantage of a vulnerability\n- assets: the network equipment and confidential data owned by the organization\n- threat: a potential danger to the data and network functionality of a company\n- mitigation: the counter-measure to reduce the severity of a potential threat"
    },
    {
        "id": 1122,
        "type": "checkbox",
        "question": "Which two types of attacks are examples of reconnaissance attacks? (Choose two.)",
        "image": None,
        "options": [
            "brute force",
            "port scan",
            "ping sweep",
            "man-in-the-middle",
            "SYN flood"
        ],
        "correct": [1, 2],
        "explanation": "Reconnaissance attacks attempt to gather information about the targets. Ping sweeps will indicate which hosts are up and responding to pings, whereas port scans will indicate on which TCP and UDP ports the target is listening for incoming connections. Man-in-the-middle and brute force attacks are both examples of access attacks, and a SYN flood is an example of a denial of service (DoS) attack."
    },
    {
        "id": 1123,
        "type": "radio",
        "question": "Which Cisco solution helps prevent ARP spoofing and ARP poisoning attacks?",
        "image": None,
        "options": [
            "Dynamic ARP Inspection",
            "IP Source Guard",
            "DHCP Snooping",
            "Port Security"
        ],
        "correct": [0],
        "explanation": "Dynamic ARP Inspection (DAI) is a security feature that validates ARP packets in a network. DAI intercepts, logs, and discards ARP packets with invalid IP-to-MAC address bindings, protecting the network against ARP spoofing and ARP poisoning attacks."
    },
    {
        "id": 1124,
        "type": "radio",
        "question": "When the Cisco NAC appliance evaluates an incoming connection from a remote device against the defined network policies, what feature is being used?",
        "image": None,
        "options": [
            "posture assessment",
            "remediation of noncompliant systems",
            "authentication and authorization",
            "quarantining of noncompliant systems"
        ],
        "correct": [0],
        "explanation": "Posture assessment is the process of evaluating an incoming connection from a remote device against defined network policies. It checks the device's compliance with security requirements before granting network access."
    },
    {
        "id": 1125,
        "type": "checkbox",
        "question": "Which two steps are required before SSH can be enabled on a Cisco router? (Choose two.)",
        "image": None,
        "options": [
            "Give the router a host name and domain name.",
            "Create a banner that will be displayed to users when they connect.",
            "Generate a set of secret keys to be used for encryption and decryption.",
            "Set up an authentication server to handle incoming connection requests.",
            "Enable SSH on the physical interfaces where the incoming connection requests will be received."
        ],
        "correct": [0, 2],
        "explanation": "There are four steps to configure SSH on a Cisco router. First, set the host name and domain name. Second, generate a set of RSA keys to be used for encrypting and decrypting the traffic. Third, create the user IDs and passwords of the users who will be connecting. Lastly, enable SSH on the vty lines on the router. SSH does not need to be set up on any physical interfaces, nor does an external authentication server need to be used. While it is a good idea to configure a banner to display legal information for connecting users, it is not required to enable SSH."
    },
    {
        "id": 1126,
        "type": "radio",
        "question": "The network administrator for an e-commerce website requires a service that prevents customers from claiming that legitimate orders are fake. What service provides this type of guarantee?",
        "image": None,
        "options": [
            "confidentiality",
            "authentication",
            "integrity",
            "nonrepudiation"
        ],
        "correct": [3],
        "explanation": "Nonrepudiation is a service that prevents a party from denying previous actions. In the context of e-commerce, it ensures that customers cannot deny placing legitimate orders."
    },
    {
        "id": 1127,
        "type": "matching",
        "question": "Match the security technology with the description.",
        "image": None,
        "left_items": [
            "digital signatures",
            "digital certificates",
            "PKI"
        ],
        "right_items": [
            "used to authenticate and verify that a user who is sending a message is who they claim to be",
            "used to assure the authenticity and integrity of software code",
            "used to support large-scale distribution and identification of public encryption keys"
        ],
        "correct": [0, 1, 2],
        "explanation": "Place the options in the following order:\n- digital signatures: used to authenticate and verify that a user who is sending a message is who they claim to be\n- digital certificates: used to assure the authenticity and integrity of software code\n- PKI: used to support large-scale distribution and identification of public encryption keys"
    },
    {
        "id": 1128,
        "type": "radio",
        "question": "What functionality is provided by Cisco SPAN in a switched network?",
        "image": None,
        "options": [
            "It mirrors traffic that passes through a switch port or VLAN to another port for traffic analysis.",
            "It prevents traffic on a LAN from being disrupted by a broadcast storm.",
            "It protects the switched network from receiving BPDUs on ports that should not be receiving them.",
            "It copies traffic that passes through a switch interface and sends the data directly to a syslog or SNMP server for analysis.",
            "It inspects voice protocols to ensure that SIP, SCCP, H.323, and MGCP requests conform to voice standards.",
            "It mitigates MAC address overflow attacks."
        ],
        "correct": [0],
        "explanation": "SPAN is a Cisco technology used by network administrators to monitor suspicious traffic or to capture traffic to be analyzed."
    },
    {
        "id": 1129,
        "type": "checkbox",
        "question": "Which three statements are generally considered to be best practices in the placement of ACLs? (Choose three.)",
        "image": None,
        "options": [
            "Filter unwanted traffic before it travels onto a low-bandwidth link.",
            "Place standard ACLs close to the destination IP address of the traffic.",
            "Place standard ACLs close to the source IP address of the traffic.",
            "Place extended ACLs close to the destination IP address of the traffic.",
            "Place extended ACLs close to the source IP address of the traffic.",
            "For every inbound ACL placed on an interface, there should be a matching outbound ACL."
        ],
        "correct": [0, 1, 4],
        "explanation": "Extended ACLs should be placed as close as possible to the source IP address, so that traffic that needs to be filtered does not cross the network and use network resources. Because standard ACLs do not specify a destination address, they should be placed as close to the destination as possible. Placing a standard ACL close to the source may have the effect of filtering all traffic, and limiting services to other hosts. Filtering unwanted traffic before it enters low-bandwidth links preserves bandwidth and supports network functionality. Decisions on placing ACLs inbound or outbound are dependent on the requirements to be met."
    },
    {
        "id": 1130,
        "type": "radio",
        "question": "What function is performed by the class maps configuration object in the Cisco modular policy framework?",
        "image": None,
        "options": [
            "identifying interesting traffic",
            "applying a policy to an interface",
            "applying a policy to interesting traffic",
            "restricting traffic through an interface"
        ],
        "correct": [0],
        "explanation": "There are three configuration objects in the MPF; class maps, policy maps, and service policy. The class maps configuration object uses match criteria to identify interesting traffic."
    },
    {
        "id": 1131,
        "type": "checkbox",
        "question": "In an attempt to prevent network attacks, cyber analysts share unique identifiable attributes of known attacks with colleagues. What three types of attributes or indicators of compromise are helpful to share? (Choose three.)",
        "image": None,
        "options": [
            "IP addresses of attack servers",
            "changes made to end system software",
            "netbios names of compromised firewalls",
            "features of malware files",
            "BIOS of attacking systems",
            "system ID of compromised systems"
        ],
        "correct": [0, 1, 3],
        "explanation": "Many network attacks can be prevented by sharing information about indicators of compromise (IOC). Each attack has unique identifiable attributes. Indicators of compromise are the evidence that an attack has occurred. IOCs can be identifying features of malware files, IP addresses of servers that are used in the attack, filenames, and characteristic changes made to end system software."
    },
    {
        "id": 1132,
        "type": "checkbox",
        "question": "What two assurances does digital signing provide about code that is downloaded from the Internet? (Choose two.)",
        "image": None,
        "options": [
            "The code is authentic and is actually sourced by the publisher.",
            "The code contains no errors.",
            "The code has not been modified since it left the software publisher.",
            "The code contains no viruses.",
            "The code was encrypted with both a private and public key."
        ],
        "correct": [0, 2],
        "explanation": "Digitally signing code provides several assurances about the code: The code is authentic and is actually sourced by the publisher. The code has not been modified since it left the software publisher. The publisher undeniably published the code. This provides nonrepudiation of the act of publishing."
    },
    {
        "id": 1133,
        "type": "radio",
        "question": "Refer to the exhibit. What algorithm is being used to provide public key exchange?",
        "image": "/static/images/1133.png",
        "options": [
            "SHA",
            "RSA",
            "Diffie-Hellman",
            "AES"
        ],
        "correct": [2],
        "explanation": "The IPsec framework uses various protocols and algorithms to provide data confidentiality, data integrity, authentication, and secure key exchange. DH (Diffie-Hellman) is an algorithm used for key exchange. DH is a public key exchange method and allows two IPsec peers to establish a shared secret key over an insecure channel."
    },
    {
        "id": 1134,
        "type": "checkbox",
        "question": "Which two statements describe the use of asymmetric algorithms? (Choose two.)",
        "image": None,
        "options": [
            "Public and private keys may be used interchangeably.",
            "If a public key is used to encrypt the data, a public key must be used to decrypt the data.",
            "If a private key is used to encrypt the data, a public key must be used to decrypt the data.",
            "If a public key is used to encrypt the data, a private key must be used to decrypt the data.",
            "If a private key is used to encrypt the data, a private key must be used to decrypt the data."
        ],
        "correct": [2, 3],
        "explanation": "Asymmetric algorithms use two keys: a public key and a private key. Both keys are capable of the encryption process, but the complementary matched key is required for decryption. If a public key encrypts the data, the matching private key decrypts the data. The opposite is also true. If a private key encrypts the data, the corresponding public key decrypts the data."
    },
    {
        "id": 1135,
        "type": "radio",
        "question": "Which statement is a feature of HMAC?",
        "image": None,
        "options": [
            "HMAC uses a secret key that is only known to the sender and defeats man-in-the-middle attacks.",
            "HMAC uses protocols such as SSL or TLS to provide session layer confidentiality.",
            "HMAC uses a secret key as input to the hash function, adding authentication to integrity assurance.",
            "HMAC is based on the RSA hash function."
        ],
        "correct": [2],
        "explanation": "A keyed-hash message authentication code (HMAC or KHMAC) is a type of message authentication code (MAC). HMACs use an additional secret key as input to the hash function, adding authentication to data integrity assurance."
    },
    {
        "id": 1136,
        "type": "radio",
        "question": "What is the purpose of the webtype ACLs in an ASA?",
        "image": None,
        "options": [
            "to inspect outbound traffic headed towards certain web sites",
            "to restrict traffic that is destined to an ASDM",
            "to monitor return traffic that is in response to web server requests that are initiated from the inside interface",
            "to filter traffic for clientless SSL VPN users"
        ],
        "correct": [3],
        "explanation": "The webtype ACLs are used in a configuration that supports filtering for clientless SSL VPN users."
    },
    {
        "id": 1137,
        "type": "checkbox",
        "question": "Which two statements describe the effect of the access control list wildcard mask 0.0.0.15? (Choose two.)",
        "image": None,
        "options": [
            "The first 28 bits of a supplied IP address will be matched.",
            "The last four bits of a supplied IP address will be matched.",
            "The first 28 bits of a supplied IP address will be ignored.",
            "The last four bits of a supplied IP address will be ignored.",
            "The last five bits of a supplied IP address will be ignored.",
            "The first 32 bits of a supplied IP address will be matched."
        ],
        "correct": [0, 3],
        "explanation": "A wildcard mask uses 0s to indicate that bits must match. 0s in the first three octets represent 24 bits and four more zeros in the last octet, represent a total of 28 bits that must match. The four 1s represented by the decimal value of 15 represents the four bits to ignore."
    },
    {
        "id": 1138,
        "type": "radio",
        "question": "Which type of firewall is the most common and allows or blocks traffic based on Layer 3, Layer 4, and Layer 5 information?",
        "image": None,
        "options": [
            "stateless firewall",
            "packet filtering firewall",
            "next generation firewall",
            "stateful firewall"
        ],
        "correct": [3],
        "explanation": "Stateful firewalls are the most common type and allow or block traffic based on Layer 3, Layer 4, and Layer 5 information. They track the state of connections and make decisions based on the context of the traffic."
    },
    {
        "id": 1139,
        "type": "radio",
        "question": "Which protocol or measure should be used to mitigate the vulnerability of using FTP to transfer documents between a teleworker and the company file server?",
        "image": None,
        "options": [
            "SCP",
            "TFTP",
            "ACLs on the file server",
            "out-of-band communication channel"
        ],
        "correct": [0],
        "explanation": "File transfer using FTP is transmitted in plain text. The username and password would be easily captured if the data transmission is intercepted. Secure Copy Protocol (SCP) conducts the authentication and file transfer under SSH, thus the communication is encrypted. Like FTP, TFTP transfers files unencrypted. ACLs provide network traffic filtering but not encryption. Using an out-of-band communication channel (OOB) either requires physical access to the file server or, if done through the internet, does not necessarily encrypt the communication."
    },
    {
        "id": 1140,
        "type": "radio",
        "question": "Refer to the exhibit. The IPv6 access list LIMITED_ACCESS is applied on the S0/0/0 interface of R1 in the inbound direction. Which IPv6 packets from the ISP will be dropped by the ACL on R1?",
        "image": "/static/images/1140.png",
        "options": [
            "HTTPS packets to PC1",
            "ICMPv6 packets that are destined to PC1",
            "packets that are destined to PC1 on port 80",
            "neighbor advertisements that are received from the ISP router"
        ],
        "correct": [1],
        "explanation": "The access list LIMITED_ACCESS will block ICMPv6 packets from the ISP. Both port 80, HTTP traffic, and port 443, HTTPS traffic, are explicitly permitted by the ACL. The neighbor advertisements from the ISP router are implicitly permitted by the implicit permit icmp any any nd-na statement at the end of all IPv6 ACLs."
    },
    {
        "id": 1141,
        "type": "radio",
        "question": "What tool is available through the Cisco IOS CLI to initiate security audits and to make recommended configuration changes with or without administrator input?",
        "image": None,
        "options": [
            "Control Plane Policing",
            "Cisco AutoSecure",
            "Cisco ACS",
            "Simple Network Management Protocol"
        ],
        "correct": [1],
        "explanation": "Cisco AutoSecure is a feature available through the Cisco IOS CLI that helps secure a router by disabling common IP services that can be exploited for network attacks and enabling IP services that can help in the defense of a network."
    },
    {
        "id": 1142,
        "type": "radio",
        "question": "Refer to the exhibit. Which pair of crypto isakmp key commands would correctly configure PSK on the two routers?",
        "image": "/static/images/1142.jpg",
        "options": [
            "R1(config)# crypto isakmp key cisco123 address 209.165.200.227\nR2(config)# crypto isakmp key cisco123 address 209.165.200.226",
            "R1(config)# crypto isakmp key cisco123 address 209.165.200.226\nR2(config)# crypto isakmp key cisco123 address 209.165.200.227",
            "R1(config)# crypto isakmp key cisco123 hostname R1\nR2(config)# crypto isakmp key cisco123 hostname R2",
            "R1(config)# crypto isakmp key cisco123 address 209.165.200.226\nR2(config)# crypto isakmp key secure address 209.165.200.227"
        ],
        "correct": [0],
        "explanation": "The correct syntax of the crypto isakmp key command is: crypto isakmp key keystring address peer-address. Each router must reference the other router's IP address. So R1 uses R2's address (209.165.200.227) and R2 uses R1's address (209.165.200.226)."
    },
    {
        "id": 1143,
        "type": "checkbox",
        "question": "Which two technologies provide enterprise-managed VPN solutions? (Choose two.)",
        "image": None,
        "options": [
            "Layer 3 MPLS VPN",
            "Frame Relay",
            "site-to-site VPN",
            "Layer 2 MPLS VPN",
            "remote access VPN"
        ],
        "correct": [2, 4],
        "explanation": "Enterprise-managed VPNs include site-to-site VPN and remote access VPN. These are managed by the enterprise rather than a service provider. MPLS VPNs are provider-managed solutions."
    },
    {
        "id": 1144,
        "type": "checkbox",
        "question": "What are the three components of an STP bridge ID? (Choose three.)",
        "image": None,
        "options": [
            "the date and time that the switch was brought online",
            "the hostname of the switch",
            "the MAC address of the switch",
            "the extended system ID",
            "the bridge priority value",
            "the IP address of the management VLAN"
        ],
        "correct": [2, 3, 4],
        "explanation": "The STP bridge ID consists of three components: the bridge priority value, the extended system ID (VLAN ID), and the MAC address of the switch."
    },
    {
        "id": 1145,
        "type": "checkbox",
        "question": "What are two differences between stateful and packet filtering firewalls? (Choose two.)",
        "image": None,
        "options": [
            "A packet filtering firewall will prevent spoofing by determining whether packets belong to an existing connection while a stateful firewall follows pre-configured rule sets.",
            "A stateful firewall provides more stringent control over security than a packet filtering firewall.",
            "A packet filtering firewall is able to filter sessions that use dynamic port negotiations while a stateful firewall cannot.",
            "A stateful firewall will provide more logging information than a packet filtering firewall.",
            "A stateful firewall will examine each packet individually while a packet filtering firewall observes the state of a connection."
        ],
        "correct": [1, 3],
        "explanation": "There are many differences between a stateless and stateful firewall. Stateful firewalls: are often used as a primary means of defense by filtering unwanted, unnecessary, or undesirable traffic; strengthen packet filtering by providing more stringent control over security; improve performance over packet filters or proxy servers; defend against spoofing and DoS attacks by determining whether packets belong to an existing connection or are from an unauthorized source; provide more log information than a packet filtering firewall."
    },
    {
        "id": 1146,
        "type": "radio",
        "question": "Which portion of the Snort IPS rule header identifies the destination port?\n\nalert tcp $HOME_NET any -> $EXTERNAL_NET $HTTP_PORTS",
        "image": None,
        "options": [
            "any",
            "$HTTP_PORTS",
            "$HOME_NET",
            "tcp"
        ],
        "correct": [1],
        "explanation": "In a Snort rule header, the format is: action protocol source_ip source_port -> dest_ip dest_port. The $HTTP_PORTS variable identifies the destination port in this rule."
    },
    {
        "id": 1147,
        "type": "matching",
        "question": "Match each SNMP operation to the corresponding description. (Not all options are used.)",
        "image": None,
        "left_items": [
            "set-request",
            "get-bulk-request",
            "get-next-request",
            "get-response"
        ],
        "right_items": [
            "storing a value in a specific variable",
            "retrieving multiple rows in a table in a single transmission",
            "sequentially searching tables to retrieve a value from a variable",
            "replying to GET request and SET request messages that are sent by an NMS"
        ],
        "correct": [0, 1, 2, 3],
        "explanation": "Place the options in the following order:\n- set-request: storing a value in a specific variable\n- get-bulk-request: retrieving multiple rows in a table in a single transmission\n- get-next-request: sequentially searching tables to retrieve a value from a variable\n- get-response: replying to GET request and SET request messages that are sent by an NMS"
    },
    {
        "id": 1148,
        "type": "radio",
        "question": "What port state is used by 802.1X if a workstation fails authorization?",
        "image": None,
        "options": [
            "disabled",
            "down",
            "unauthorized",
            "blocking"
        ],
        "correct": [2],
        "explanation": "802.1X uses the unauthorized port state when a workstation fails authorization. The port remains in this state until the workstation successfully authenticates."
    },
    {
        "id": 1149,
        "type": "matching",
        "question": "Match the ASA special hardware modules to the description.",
        "image": None,
        "left_items": [
            "Content Security and Control (CSC)",
            "Advanced Inspection and Prevention (AIP)",
            "Cisco Advanced Inspection and Prevention Security Services Module (AIP-SSM)"
        ],
        "right_items": [
            "support antimalware capabilities",
            "support advanced IPS capability",
            "support protection against tens of thousands of known exploits"
        ],
        "correct": [0, 1, 2],
        "explanation": "The advanced threat control and containment services of an ASA firewall are provided by integrating special hardware modules with the ASA architecture. AIP supports advanced IPS capability. CSC supports antimalware capabilities. AIP-SSM supports protection against tens of thousands of known exploits."    },
    {
        "id": 1150,
        "type": "checkbox",
        "question": "Refer to the exhibit. Which two ACLs, if applied to the G0/1 interface of R2, would permit only the two LAN networks attached to R1 to access the network that connects to R2 G0/1 interface? (Choose two.)",
        "image": "/static/images/1150.jpg",
        "options": [
            "access-list 3 permit 192.168.10.128 0.0.0.63",
            "access-list 1 permit 192.168.10.0 0.0.0.127",
            "access-list 4 permit 192.168.10.0 0.0.0.255",
            "access-list 2 permit host 192.168.10.9\naccess-list 2 permit host 192.168.10.69",
            "access-list 5 permit 192.168.10.0 0.0.0.63\naccess-list 5 permit 192.168.10.64 0.0.0.63"
        ],
        "correct": [1, 4],
        "explanation": "The permit 192.168.10.0 0.0.0.127 command ignores bit positions 1 through 7, which means that addresses 192.168.10.0 through 192.168.10.127 are allowed through. The two ACEs of permit 192.168.10.0 0.0.0.63 and permit 192.168.10.64 0.0.0.63 allow the same address range through the router."
    },
    {
        "id": 1151,
        "type": "checkbox",
        "question": "Which two characteristics apply to role-based CLI access superviews? (Choose two.)",
        "image": None,
        "options": [
            "A specific superview cannot have commands added to it directly.",
            "CLI views have passwords, but superviews do not have passwords.",
            "A single superview can be shared among multiple CLI views.",
            "Deleting a superview deletes all associated CLI views.",
            "Users logged in to a superview can access all commands specified within the associated CLI views."
        ],
        "correct": [0, 4],
        "explanation": "By using a superview an administrator can assign users or groups of users to CLI views which contain a specific set of commands those users can access. Commands cannot be added directly to a superview but rather must be added to a CLI view and the CLI view added to the superview."
    },
    {
        "id": 1152,
        "type": "matching",
        "question": "Match the IPS alarm type to the description.",
        "image": None,
        "left_items": [
            "true positive",
            "true negative",
            "false positive",
            "false negative"
        ],
        "right_items": [
            "verified attack traffic is generating an alarm",
            "normal user traffic is not generating an alarm",
            "normal user traffic is generating an alarm",
            "attack traffic is not generating an alarm"
        ],
        "correct": [0, 1, 2, 3],
        "explanation": "Place the options in the following order:\n- true positive: verified attack traffic is generating an alarm\n- true negative: normal user traffic is not generating an alarm\n- false positive: normal user traffic is generating an alarm\n- false negative: attack traffic is not generating an alarm"
    },
    {
        "id": 1153,
        "type": "checkbox",
        "question": "What are two security features commonly found in a WAN design? (Choose two.)",
        "image": None,
        "options": [
            "WPA2 for data encryption of all data between sites",
            "firewalls protecting the main and remote sites",
            "outside perimeter security including continuous video surveillance",
            "port security on all user-facing ports",
            "VPNs used by mobile workers between sites"
        ],
        "correct": [1, 4],
        "explanation": "WANs span a wide area and commonly have connections from a main site to remote sites including a branch office, regional site, SOHO sites, and mobile workers. WANs typically connect over a public internet connection. Each site commonly has a firewall and VPNs used by remote workers between sites."
    },
]