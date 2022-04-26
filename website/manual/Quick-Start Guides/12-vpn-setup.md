# 12 - VPN Addon Setup

### Prerequisites
1. Ensure internet for the container is working PRIOR to adding the VPN connection
2. Obtain either a Wireguard Configuration or a OpenVPN configuration file
    - Wireguard ends in a .conf
    - OpenVPN ends in a .ovpn
3. Know both your kubernetes LAN and your personal LAN



### Preparing Configuration Files
#### Wireguard
1. Delete the entire line that contains "DNS"
2. Remove ALL mentions of IPv6
    - Usually after the IPv4 addresses
    - ```::/0``` is the IPv6 syntax.

Here is an example Wireguard configuration. 
Note the Deleted IPv6 addresses, and Deleted DNS line.
```
[Interface]
PrivateKey = cFuYkobFFgdfghdffdghdfghdfghdfgh
Address = 10.64.48.226/32

[Peer]
PublicKey = Casdfgsdfghsdfghsdfghsdfghs
AllowedIPs = 0.0.0.0/0
Endpoint = 198.54.128.58:51820

```
##### Additional Information
Ignore any keys, public private, psk etc. 
We have not had any issue keeping all keys within a configuration.



#### OpenVPN
1. Add the two following lines to your configuration
    - ```pull-filter ignore "ifconfig-ipv6 "```

    - ```pull-filter ignore "route-ipv6 "```

    These two lines will ensure IPv6 is ignored, which is vital for a stable VPN connection.

Note The two added lines
Here is an example OpenVPN configuration
```
client
dev tun
proto udp
remote us-denver.privacy.network 1198
resolv-retry infinite
nobind
persist-key
persist-tun
cipher aes-128-cbc
auth sha1
tls-client
remote-cert-tls server
pull-filter ignore "ifconfig-ipv6 "
pull-filter ignore "route-ipv6 "

auth-user-pass
compress
verb 1
reneg-sec 0
<crl-verify>
-----BEGIN X509 CRL-----
MIIFqzCCBJOgAwIBAgIJAKZ7D5Yv87qDMA0GCSqGSIb3DQEBDQUAMIHoMQswCQYD
YDQ8z9v+DMO6iwyIDRiU

-----END X509 CRL-----
</crl-verify>

<ca>
-----BEGIN CERTIFICATE-----
MIIFqzCCBJOgAwIBAgIJAKZ7D5Yv87qDMA0GCSqGSIb3DQEBDQUAMIHoMQswCQYD
YDQ8z9v+DMO6iwyIDRiU
-----END CERTIFICATE-----
</ca>

disable-occ
```


### Edit Configuration
The next step enable the addon in our edit configuration

1. Scale GUI 
    1. Apps
    2. Installed Applications
2. Find the app you want, Click the top 3 dots to the right of your application
    1. Click ```Edit```
    2. Scroll to the bottom until you see ```Addons```
    3. CLick the dropdown under ```Type```
    4. Choose Wireguard or OpenVPN
        1. OpenVPN
            - Type in your Credentials for your vpn provider.
    5. Check "Enable Killswitch"
        - Click ```Add``` Next to ```Configure Killswitch Excluded IPv4 networks```
        - Click ```Add``` For EACH network.
        - ```172.16.0.0/16``` is the default Kubernetes Network, you want this in your killswitch so kubernetes can still communicate with the application
        - ```192.168.0.0/24``` is my personal LAN, this needs to be in there so YOU can communicate with the container
    6. Finally, Add the filepath where you saved your modified configuration file
        - EX: ```/mnt/speed/vpn/wireguard/jackett2.conf```

By now your screen should look somewhat like this:
<a href="https://truecharts.org/_static/img/vpn/vpn1.png"><img src="https://truecharts.org/_static/img/vpn/vpn1.png" width="100%"/></a>




#### Video Guide

![type:video](https://www.youtube.com/embed/zSNApt-Ojng)

##### Additional Documentation


