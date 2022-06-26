# Default Ports

This document lists the default ports used by Apps.
These defaults can of course be changed, but as we guarantee "sane, working defaults",
they should provide no or minimal conflicts without being changed.

## Stable

| App                        |     Service     |    Port Name    | Port  | Protocol |       Status        | Note                                             |
| :------------------------- | :-------------: | :-------------: | :---: | :------: | :-----------------: | :----------------------------------------------- |
| custom-app                 |        -        |        -        |   -   |    -     | Service not Defined | -                                                |
| metallb                    |        -        |        -        |   -   |    -     | Service not Defined | -                                                |
| amcrest2mqtt               |      main       |        -        |   -   |    -     | Service is Disabled | -                                                |
| automatic-music-downloader |      main       |        -        |   -   |    -     | Service is Disabled | -                                                |
| ddclient                   |      main       |        -        |   -   |    -     | Service is Disabled | -                                                |
| doplarr                    |      main       |        -        |   -   |    -     | Service is Disabled | -                                                |
| duckdns                    |      main       |        -        |   -   |    -     | Service is Disabled | -                                                |
| leaf2mqtt                  |      main       |        -        |   -   |    -     | Service is Disabled | -                                                |
| protonmail-bridge          |      main       |        -        |   -   |    -     | Service is Disabled | -                                                |
| rsnapshot                  |      main       |        -        |   -   |    -     | Service is Disabled | -                                                |
| tdarr-node                 |      main       |        -        |   -   |    -     | Service is Disabled | -                                                |
| traefik                    |       udp       |        -        |   -   |    -     | Service is Disabled | -                                                |
| unpackerr                  |      main       |        -        |   -   |    -     | Service is Disabled | -                                                |
| webgrabplus                |      main       |        -        |   -   |    -     | Service is Disabled | -                                                |
| promcord                   |      main       |        -        |   -   |    -     |  Port is Disabled   | -                                                |
| speedtest-exporter         |      main       |        -        |   -   |    -     |  Port is Disabled   | -                                                |
| unpoller                   |      main       |        -        |   -   |    -     |  Port is Disabled   | -                                                |
| uptimerobot-prometheus     |      main       |        -        |   -   |    -     |  Port is Disabled   | -                                                |
| anonaddy                   |      smtp       |      smtp       |  25   |   TCP    |       Active        | Potential conflict with: protonmail-bridge       |
| protonmail-bridge          |      smtp       |      smtp       |  25   |   TCP    |       Active        | Potential conflict with: anonaddy                |
| k8s-gateway                |      main       |      main       |  53   |   UDP    |       Active        | -                                                |
| mosdns                     |      main       |      main       |  53   |   UDP    |       Active        | -                                                |
| pihole                     |     dns-tcp     |     dns-tcp     |  53   |   TCP    |       Active        | Potential conflict with: adguard-home technitium |
| pihole                     |       dns       |       dns       |  53   |   UDP    |       Active        | -                                                |
| openldap                   |      main       |      main       |  389  |   TCP    |       Active        | -                                                |
| minisatip                  |      rtsp       |      rtsp       |  554  |   TCP    |       Active        | -                                                |
| openldap                   |      ldaps      |      ldaps      |  636  |   TCP    |       Active        | -                                                |
| strapi                     |      main       |      main       | 1337  |   TCP    |       Active        | -                                                |
| domoticz                   |      comm2      |      comm2      | 1443  |   TCP    |       Active        | -                                                |
| nntp2nntp                  |      main       |      main       | 1563  |   TCP    |       Active        | -                                                |
| kms                        |      main       |      main       | 1688  |   TCP    |       Active        | -                                                |
| freeradius                 |      main       |      main       | 1812  |   UDP    |       Active        | -                                                |
| freeradius                 |   accounting    |   accounting    | 1813  |   UDP    |       Active        | -                                                |
| node-red                   |      main       |      main       | 1880  |   TCP    |       Active        | -                                                |
| mosquitto                  |      main       |      main       | 1883  |   TCP    |       Active        | -                                                |
| minisatip                  |    discovery    |    discovery    | 1900  |   UDP    |       Active        | -                                                |
| owncast                    |      rtmp       |      rtmp       | 1935  |   TCP    |       Active        | Potential conflict with: frigate                 |
| ubooquity                  |      main       |      main       | 2202  |   TCP    |       Active        | -                                                |
| ubooquity                  |      admin      |      admin      | 2203  |   TCP    |       Active        | -                                                |
| gitea                      |       ssh       |       ssh       | 2222  |   TCP    |       Active        | -                                                |
| photoprism                 |      main       |      main       | 2342  |   TCP    |       Active        | -                                                |
| docker-compose             |      main       |      main       | 2376  |   TCP    |       Active        | -                                                |
| valheim                    |     valheim     |    valheim1     | 2456  |   UDP    |       Active        | -                                                |
| valheim                    |     valheim     |    valheim2     | 2457  |   UDP    |       Active        | -                                                |
| valheim                    |     valheim     |    valheim3     | 2458  |   UDP    |       Active        | -                                                |
| wireshark                  |      main       |      main       | 3000  |   TCP    |       Active        | -                                                |
| uptime-kuma                |      main       |      main       | 3001  |   TCP    |       Active        | -                                                |
| vaultwarden                |       ws        |       ws        | 3012  |   TCP    |       Active        | -                                                |
| loki                       |      main       |      main       | 3100  |   HTTP   |       Active        | -                                                |
| jdownloader2               |      myjd       |      myjd       | 3129  |   TCP    |       Active        | -                                                |
| pylon                      |      main       |      main       | 3131  |   TCP    |       Active        | -                                                |
| clamav                     |      main       |      main       | 3310  |   TCP    |       Active        | -                                                |
| ispy-agent-dvr             |      turn       |      turn       | 3478  |   UDP    |       Active        | Potential conflict with: unifi                   |
| unifi                      |      stun       |      stun       | 3478  |   UDP    |       Active        | Potential conflict with: ispy-agent-dvr          |
| logitech-media-server      |    playertcp    |  slimprototcp   | 3483  |   TCP    |       Active        | -                                                |
| logitech-media-server      |    playerudp    |  slimprotoudp   | 3483  |   UDP    |       Active        | -                                                |
| ombi                       |      main       |      main       | 3579  |   TCP    |       Active        | -                                                |
| ipfs                       |    peer-tcp     |    peer-tcp     | 4001  |   TCP    |       Active        | -                                                |
| ipfs                       |    peer-udp     |    peer-udp     | 4001  |   UDP    |       Active        | -                                                |
| quassel-core               |      main       |      main       | 4242  |   TCP    |       Active        | -                                                |
| navidrome                  |      main       |      main       | 4533  |   TCP    |       Active        | -                                                |
| requestrr                  |      main       |      main       | 4545  |   TCP    |       Active        | -                                                |
| guacd                      |      main       |      main       | 4822  |   TCP    |       Active        | -                                                |
| appdaemon                  |      main       |      main       | 5050  |   TCP    |       Active        | -                                                |
| overseerr                  |      main       |      main       | 5055  |   TCP    |       Active        | -                                                |
| nzbhydra                   |      main       |      main       | 5076  |   TCP    |       Active        | -                                                |
| lazylibrarian              |      main       |      main       | 5299  |   TCP    |       Active        | -                                                |
| syslog-ng                  |   syslog-udp    |   syslog-udp    | 5514  |   UDP    |       Active        | -                                                |
| n8n                        |      main       |      main       | 5678  |   TCP    |       Active        | -                                                |
| esphome                    |      main       |      main       | 6052  |   TCP    |       Active        | -                                                |
| novnc                      |      main       |      main       | 6080  |   TCP    |       Active        | -                                                |
| domoticz                   |      comm1      |      comm1      | 6144  |   TCP    |       Active        | -                                                |
| znc                        |      main       |      main       | 6501  |   TCP    |       Active        | -                                                |
| syslog-ng                  |   syslog-tls    |   syslog-tls    | 6514  |   TCP    |       Active        | -                                                |
| embystat                   |      main       |      main       | 6555  |   TCP    |       Active        | -                                                |
| deemix                     |      main       |      main       | 6595  |   TCP    |       Active        | -                                                |
| syslog-ng                  |      main       |      main       | 6601  |   TCP    |       Active        | -                                                |
| ngircd                     |      main       |      main       | 6667  |   TCP    |       Active        | -                                                |
| bazarr                     |      main       |      main       | 6767  |   TCP    |       Active        | -                                                |
| unifi                      |    speedtest    |    speedtest    | 6789  |   TCP    |       Active        | -                                                |
| aria2                      |      main       |      main       | 6800  |   TCP    |       Active        | -                                                |
| qbittorrent                |     torrent     |     torrent     | 6881  |   TCP    |       Active        | -                                                |
| qbittorrent                |   torrentudp    |   torrentudp    | 6881  |   UDP    |       Active        | -                                                |
| aria2                      |     listen      |     listen      | 6888  |   TCP    |       Active        | -                                                |
| logitech-media-server      |      main       |      main       | 7000  |   TCP    |       Active        | -                                                |
| clamav                     |     milter      |     milter      | 7357  |   TCP    |       Active        | -                                                |
| foldingathome              |      main       |      main       | 7396  |   TCP    |       Active        | -                                                |
| haste-server               |      main       |      main       | 7777  |   TCP    |       Active        | -                                                |
| satisfactory               |      main       |      main       | 7777  |   UDP    |       Active        | -                                                |
| nextcloud                  |       hpb       |       hpb       | 7867  |   TCP    |       Active        | -                                                |
| radarr                     |      main       |      main       | 7878  |   TCP    |       Active        | -                                                |
| synapse                    |      main       |      main       | 8008  |   TCP    |       Active        | -                                                |
| omada-controller           |      main       |      main       | 8043  |  HTTPS   |       Active        | -                                                |
| odoo                       |      main       |      main       | 8069  |   TCP    |       Active        | -                                                |
| odoo                       |      odoo       |     xmlrpcs     | 8071  |   TCP    |       Active        | -                                                |
| odoo                       |      odoo       |   longpolling   | 8072  |   TCP    |       Active        | -                                                |
| unifi                      |      comm       |      comm       | 8080  |   TCP    |       Active        | -                                                |
| calibre                    |    webserver    |    webserver    | 8081  |   TCP    |       Active        | -                                                |
| traccar                    |      main       |      main       | 8082  |   TCP    |       Active        | -                                                |
| calibre-web                |      main       |      main       | 8083  |   TCP    |       Active        | -                                                |
| calibre                    |      main       |      main       | 8084  |   TCP    |       Active        | -                                                |
| htpcmanager                |      main       |      main       | 8085  |   TCP    |       Active        | -                                                |
| synclounge                 |      main       |      main       | 8088  |   TCP    |       Active        | -                                                |
| mylar                      |      main       |      main       | 8090  |   TCP    |       Active        | -                                                |
| zwavejs2mqtt               |      main       |      main       | 8091  |   TCP    |       Active        | -                                                |
| jellyfin                   |      main       |      main       | 8096  |   TCP    |       Active        | -                                                |
| deluge                     |      main       |      main       | 8112  |   TCP    |       Active        | -                                                |
| home-assistant             |      main       |      main       | 8123  |   TCP    |       Active        | -                                                |
| tautulli                   |      main       |      main       | 8181  |   TCP    |       Active        | -                                                |
| flaresolverr               |      main       |      main       | 8191  |   TCP    |       Active        | -                                                |
| duplicati                  |      main       |      main       | 8200  |   TCP    |       Active        | -                                                |
| tdarr                      |      main       |      main       | 8265  |   TCP    |       Active        | -                                                |
| tdarr                      |      comm       |      comm       | 8266  |   TCP    |       Active        | -                                                |
| beets                      |      main       |      main       | 8337  |   TCP    |       Active        | -                                                |
| syncthing                  |      main       |      main       | 8384  |   TCP    |       Active        | -                                                |
| unifi                      |      main       |      main       | 8443  |  HTTPS   |       Active        | -                                                |
| synapse                    |   federation    |   federation    | 8448  |   TCP    |       Active        | -                                                |
| gaps                       |      main       |      main       | 8484  |   TCP    |       Active        | -                                                |
| lidarr                     |      main       |      main       | 8686  |   TCP    |       Active        | -                                                |
| readarr                    |      main       |      main       | 8787  |   TCP    |       Active        | -                                                |
| omada-controller           |      comm       |      comm       | 8843  |  HTTPS   |       Active        | Potential conflict with: unifi                   |
| unifi                      |   guestportal   |    websecure    | 8843  |  HTTPS   |       Active        | Potential conflict with: omada-controller        |
| minisatip                  |      main       |      main       | 8875  |   TCP    |       Active        | -                                                |
| unifi                      |   guestportal   |       web       | 8880  |   HTTP   |       Active        | -                                                |
| resilio-sync               |      main       |      main       | 8888  |   TCP    |       Active        | -                                                |
| sonarr                     |      main       |      main       | 8989  |   TCP    |       Active        | -                                                |
| traefik                    |      main       |      main       | 9000  |   HTTP   |       Active        | -                                                |
| valheim                    |      main       |      main       | 9010  |   TCP    |       Active        | -                                                |
| valheim                    |   supervisor    |   supervisor    | 9011  |   TCP    |       Active        | -                                                |
| traefik                    |       tcp       |       web       | 9080  |   HTTP   |       Active        | -                                                |
| pihole                     |      main       |      main       | 9089  |   TCP    |       Active        | -                                                |
| minio-console              |      main       |      main       | 9090  |   TCP    |       Active        | -                                                |
| authelia                   |      main       |      main       | 9091  |   TCP    |       Active        | -                                                |
| synapse                    |   replication   |   replication   | 9092  |   TCP    |       Active        | -                                                |
| synapse                    |     metrics     |     metrics     | 9093  |   TCP    |       Active        | -                                                |
| jackett                    |      main       |      main       | 9117  |   TCP    |       Active        | -                                                |
| unpoller                   |      main       |     metrics     | 9130  |   TCP    |       Active        | -                                                |
| traefik                    |     metrics     |     metrics     | 9180  |   HTTP   |       Active        | -                                                |
| owncloud-ocis              |      main       |      main       | 9200  |  HTTPS   |       Active        | -                                                |
| traefik                    |       tcp       |    websecure    | 9443  |  HTTPS   |       Active        | -                                                |
| prowlarr                   |      main       |      main       | 9696  |   TCP    |       Active        | -                                                |
| uptimerobot-prometheus     |      main       |     metrics     | 9705  |   TCP    |       Active        | -                                                |
| kodi-headless              |      esall      |      esall      | 9777  |   UDP    |       Active        | -                                                |
| speedtest-exporter         |      main       |     metrics     | 9798  |   TCP    |       Active        | -                                                |
| tvheadend                  |      main       |      main       | 9981  |   TCP    |       Active        | -                                                |
| tvheadend                  |      htsp       |      htsp       | 9982  |   TCP    |       Active        | -                                                |
| teamspeak3                 |      voice      |      voice      | 9987  |   UDP    |       Active        | -                                                |
| guacamole-client           |      main       |      main       | 9998  |   TCP    |       Active        | -                                                |
| stash                      |      main       |      main       | 9999  |   TCP    |       Active        | -                                                |
| ser2sock                   |      main       |      main       | 10000 |   TCP    |       Active        | -                                                |
| deconz                     |    websocket    |    websocket    | 10001 |   TCP    |       Active        | -                                                |
| deconz                     |       vnc       |       vnc       | 10002 |   TCP    |       Active        | -                                                |
| external-service           |      main       |      main       | 10003 |   TCP    |       Active        | -                                                |
| nullserv                   |      main       |      main       | 10004 |   TCP    |       Active        | -                                                |
| nullserv                   |      https      |      https      | 10005 |   TCP    |       Active        | -                                                |
| apache-musicindex          |      main       |      main       | 10006 |   TCP    |       Active        | -                                                |
| cryptofolio                |      main       |      main       | 10007 |   TCP    |       Active        | -                                                |
| deconz                     |      main       |      main       | 10008 |   TCP    |       Active        | -                                                |
| dsmr-reader                |      main       |      main       | 10009 |   TCP    |       Active        | -                                                |
| freshrss                   |      main       |      main       | 10010 |   TCP    |       Active        | -                                                |
| teamspeak3                 |      main       |      main       | 10011 |   TCP    |       Active        | -                                                |
| grav                       |      main       |      main       | 10012 |   TCP    |       Active        | -                                                |
| grocy                      |      main       |      main       | 10013 |   TCP    |       Active        | -                                                |
| heimdall                   |      main       |      main       | 10014 |   TCP    |       Active        | -                                                |
| kanboard                   |      main       |      main       | 10015 |   TCP    |       Active        | -                                                |
| librespeed                 |      main       |      main       | 10016 |   TCP    |       Active        | -                                                |
| lychee                     |      main       |      main       | 10017 |   TCP    |       Active        | -                                                |
| mealie                     |      main       |      main       | 10018 |   TCP    |       Active        | -                                                |
| muximux                    |      main       |      main       | 10019 |   TCP    |       Active        | -                                                |
| nextcloud                  |      main       |      main       | 10020 |   TCP    |       Active        | -                                                |
| octoprint                  |      main       |      main       | 10021 |   TCP    |       Active        | -                                                |
| organizr                   |      main       |      main       | 10022 |   TCP    |       Active        | -                                                |
| gonic                      |      main       |      main       | 10023 |   TCP    |       Active        | -                                                |
| pgadmin                    |      main       |      main       | 10024 |   TCP    |       Active        | -                                                |
| photoshow                  |      main       |      main       | 10025 |   TCP    |       Active        | -                                                |
| phpldapadmin               |      main       |      main       | 10026 |   TCP    |       Active        | -                                                |
| pixapop                    |      main       |      main       | 10028 |   TCP    |       Active        | -                                                |
| recipes                    |      main       |      main       | 10029 |   TCP    |       Active        | -                                                |
| smokeping                  |      main       |      main       | 10030 |   TCP    |       Active        | -                                                |
| truecommand                |      main       |      main       | 10031 |   TCP    |       Active        | -                                                |
| audacity                   |      main       |      main       | 10032 |   TCP    |       Active        | -                                                |
| digikam                    |      main       |      main       | 10033 |   TCP    |       Active        | -                                                |
| doublecommander            |      main       |      main       | 10034 |   TCP    |       Active        | -                                                |
| filezilla                  |      main       |      main       | 10035 |   TCP    |       Active        | -                                                |
| flood                      |      main       |      main       | 10036 |   TCP    |       Active        | -                                                |
| gitea                      |      main       |      main       | 10037 |   TCP    |       Active        | -                                                |
| grafana                    |      main       |      main       | 10038 |   TCP    |       Active        | -                                                |
| icantbelieveitsnotvaletudo |      main       |      main       | 10039 |   TCP    |       Active        | -                                                |
| littlelink                 |      main       |      main       | 10040 |   TCP    |       Active        | -                                                |
| mstream                    |      main       |      main       | 10041 |   TCP    |       Active        | -                                                |
| remmina                    |      main       |      main       | 10042 |   TCP    |       Active        | -                                                |
| onlyoffice-document-server |      main       |      main       | 10043 |   TCP    |       Active        | -                                                |
| dashdot                    |      main       |      main       | 10044 |   TCP    |       Active        | -                                                |
| wikijs                     |      main       |      main       | 10045 |   TCP    |       Active        | -                                                |
| zwavejs2mqtt               |       ws        |       ws        | 10046 |   TCP    |       Active        | -                                                |
| airsonic                   |      main       |      main       | 10047 |   TCP    |       Active        | -                                                |
| booksonic-air              |      main       |      main       | 10048 |   TCP    |       Active        | -                                                |
| deepstack                  |      main       |      main       | 10049 |   TCP    |       Active        | -                                                |
| spotweb                    |      main       |      main       | 10050 |   TCP    |       Active        | -                                                |
| firefox-syncserver         |      main       |      main       | 10051 |   TCP    |       Active        | -                                                |
| whoogle                    |      main       |      main       | 10052 |   TCP    |       Active        | -                                                |
| handbrake                  |      main       |      main       | 10053 |   TCP    |       Active        | -                                                |
| jdownloader2               |      main       |      main       | 10054 |   TCP    |       Active        | -                                                |
| handbrake                  |       vnc       |       vnc       | 10055 |   TCP    |       Active        | -                                                |
| jdownloader2               |       vnc       |       vnc       | 10056 |   TCP    |       Active        | -                                                |
| nzbget                     |      main       |      main       | 10057 |   TCP    |       Active        | -                                                |
| friendica                  |      main       |      main       | 10058 |   TCP    |       Active        | -                                                |
| logitech-media-server      |       cli       |       cli       | 10059 |   TCP    |       Active        | -                                                |
| etherpad                   |      main       |      main       | 10060 |   TCP    |       Active        | -                                                |
| thelounge                  |      main       |      main       | 10061 |   TCP    |       Active        | -                                                |
| oscam                      |      main       |      main       | 10062 |   TCP    |       Active        | -                                                |
| code-server                |      main       |      main       | 10063 |   TCP    |       Active        | -                                                |
| headphones                 |      main       |      main       | 10064 |   TCP    |       Active        | -                                                |
| hyperion-ng                |      main       |      main       | 10065 |   TCP    |       Active        | -                                                |
| sickgear                   |      main       |      main       | 10066 |   TCP    |       Active        | -                                                |
| sickchill                  |      main       |      main       | 10067 |   TCP    |       Active        | -                                                |
| medusa                     |      main       |      main       | 10068 |   TCP    |       Active        | -                                                |
| babybuddy                  |      main       |      main       | 10069 |   TCP    |       Active        | -                                                |
| cloud9                     |      main       |      main       | 10070 |   TCP    |       Active        | -                                                |
| dizquetv                   |      main       |      main       | 10071 |   TCP    |       Active        | -                                                |
| focalboard                 |      main       |      main       | 10072 |   TCP    |       Active        | -                                                |
| golinks                    |      main       |      main       | 10073 |   TCP    |       Active        | -                                                |
| healthchecks               |      main       |      main       | 10074 |   TCP    |       Active        | -                                                |
| pyload                     |      main       |      main       | 10075 |   TCP    |       Active        | -                                                |
| shorturl                   |      main       |      main       | 10076 |   TCP    |       Active        | -                                                |
| static                     |      main       |      main       | 10077 |   TCP    |       Active        | -                                                |
| twtxt                      |      main       |      main       | 10078 |   TCP    |       Active        | -                                                |
| emby                       |      main       |      main       | 10079 |   TCP    |       Active        | -                                                |
| davos                      |      main       |      main       | 10081 |   TCP    |       Active        | -                                                |
| fireflyiii                 |      main       |      main       | 10082 |   TCP    |       Active        | -                                                |
| fossil                     |      main       |      main       | 10083 |   TCP    |       Active        | -                                                |
| gotify                     |      main       |      main       | 10084 |   TCP    |       Active        | -                                                |
| komga                      |      main       |      main       | 10085 |   TCP    |       Active        | -                                                |
| prometheus                 |      main       |      main       | 10086 |   HTTP   |       Active        | -                                                |
| prometheus                 |  alertmanager   |  alertmanager   | 10087 |   HTTP   |       Active        | -                                                |
| owncast                    |      main       |      main       | 10088 |   TCP    |       Active        | -                                                |
| prometheus                 |     promop      |     promop      | 10089 |   HTTP   |       Active        | -                                                |
| openkm                     |      main       |      main       | 10090 |   TCP    |       Active        | -                                                |
| miniflux                   |      main       |      main       | 10091 |   TCP    |       Active        | -                                                |
| piaware                    |      main       |      main       | 10092 |   TCP    |       Active        | -                                                |
| podgrab                    |      main       |      main       | 10093 |   TCP    |       Active        | -                                                |
| pretend-youre-xyzzy        |      main       |      main       | 10094 |   TCP    |       Active        | -                                                |
| qbittorrent                |      main       |      main       | 10095 |   TCP    |       Active        | -                                                |
| reg                        |      main       |      main       | 10096 |   TCP    |       Active        | -                                                |
| sabnzbd                    |      main       |      main       | 10097 |   TCP    |       Active        | -                                                |
| shiori                     |      main       |      main       | 10098 |   TCP    |       Active        | -                                                |
| statping                   |      main       |      main       | 10099 |   TCP    |       Active        | -                                                |
| teedy                      |      main       |      main       | 10100 |   TCP    |       Active        | -                                                |
| promcord                   |      main       |     metrics     | 10101 |   TCP    |       Active        | -                                                |
| vaultwarden                |      main       |      main       | 10102 |   TCP    |       Active        | -                                                |
| zigbee2mqtt                |      main       |      main       | 10103 |   TCP    |       Active        | -                                                |
| tt-rss                     |      main       |      main       | 10104 |   TCP    |       Active        | -                                                |
| collabora-online           |      main       |      main       | 10105 |   TCP    |       Active        | -                                                |
| minio                      |       api       |       api       | 10106 |   TCP    |       Active        | -                                                |
| minio                      |      main       |      main       | 10107 |   TCP    |       Active        | -                                                |
| transmission               |      main       |      main       | 10109 |   TCP    |       Active        | -                                                |
| anonaddy                   |      main       |      main       | 10110 |   TCP    |       Active        | -                                                |
| blog                       |      main       |      main       | 10111 |   TCP    |       Active        | -                                                |
| bookstack                  |      main       |      main       | 10112 |   TCP    |       Active        | -                                                |
| quassel-core               |      ident      |      ident      | 10113 |   TCP    |       Active        | -                                                |
| icinga2                    |      main       |      main       | 10114 |   TCP    |       Active        | -                                                |
| icinga2                    |      https      |      https      | 10115 |   TCP    |       Active        | -                                                |
| icinga2                    |       api       |       api       | 10116 |   TCP    |       Active        | -                                                |
| leantime                   |      main       |      main       | 10117 |   TCP    |       Active        | -                                                |
| monica                     |      main       |      main       | 10119 |   TCP    |       Active        | -                                                |
| snipe-it                   |      main       |      main       | 10120 |   TCP    |       Active        | -                                                |
| xbackbone                  |      main       |      main       | 10121 |   TCP    |       Active        | -                                                |
| airsonic-advanced          |      main       |      main       | 10122 |   TCP    |       Active        | -                                                |
| dokuwiki                   |      main       |      main       | 10123 |   TCP    |       Active        | -                                                |
| emulatorjs                 |      front      |      front      | 10124 |   TCP    |       Active        | -                                                |
| ipfs                       |      main       |      main       | 10125 |   TCP    |       Active        | -                                                |
| nano-wallet                |      main       |      main       | 10126 |   TCP    |       Active        | -                                                |
| projectsend                |      main       |      main       | 10127 |   TCP    |       Active        | -                                                |
| endlessh                   |      main       |      main       | 10128 |   TCP    |       Active        | -                                                |
| darktable                  |      main       |      main       | 10129 |   TCP    |       Active        | -                                                |
| emulatorjs                 |      main       |      main       | 10130 |   TCP    |       Active        | -                                                |
| firefox                    |      main       |      main       | 10131 |   TCP    |       Active        | -                                                |
| hedgedoc                   |      main       |      main       | 10132 |   TCP    |       Active        | -                                                |
| libreoffice                |      main       |      main       | 10133 |   TCP    |       Active        | -                                                |
| mysql-workbench            |      main       |      main       | 10134 |   TCP    |       Active        | -                                                |
| openvscode-server          |      main       |      main       | 10135 |   TCP    |       Active        | -                                                |
| pidgin                     |      main       |      main       | 10136 |   TCP    |       Active        | -                                                |
| sqlitebrowser              |      main       |      main       | 10137 |   TCP    |       Active        | -                                                |
| emulatorjs                 |      ipfs       |      ipfs       | 10138 |   TCP    |       Active        | -                                                |
| couchpotato                |      main       |      main       | 10139 |   TCP    |       Active        | -                                                |
| paperless-ng               |      main       |      main       | 10140 |   TCP    |       Active        | -                                                |
| papermerge                 |      main       |      main       | 10141 |   TCP    |       Active        | -                                                |
| boinc                      |      main       |      main       | 10142 |   TCP    |       Active        | -                                                |
| dillinger                  |      main       |      main       | 10143 |   TCP    |       Active        | -                                                |
| domoticz                   |      main       |      main       | 10144 |   TCP    |       Active        | -                                                |
| fleet                      |      main       |      main       | 10145 |   TCP    |       Active        | -                                                |
| habridge                   |      main       |      main       | 10146 |   TCP    |       Active        | -                                                |
| ipfs                       |     gateway     |     gateway     | 10147 |   TCP    |       Active        | -                                                |
| kodi-headless              |      main       |      main       | 10148 |   TCP    |       Active        | -                                                |
| pwndrop                    |      main       |      main       | 10149 |   TCP    |       Active        | -                                                |
| pydio-cells                |      main       |      main       | 10150 |  HTTPS   |       Active        | -                                                |
| scrutiny                   |      main       |      main       | 10151 |   TCP    |       Active        | -                                                |
| kodi-headless              |    websocket    |    websocket    | 10152 |   TCP    |       Active        | -                                                |
| shlink                     |      main       |      main       | 10153 |   TCP    |       Active        | -                                                |
| shlink-web-client          |      main       |      main       | 10154 |   HTTP   |       Active        | -                                                |
| airdcpp-webclient          |      main       |      main       | 10155 |   TCP    |       Active        | -                                                |
| trilium-notes              |      main       |      main       | 10156 |   HTTP   |       Active        | -                                                |
| unmanic                    |      main       |      main       | 10157 |   TCP    |       Active        | -                                                |
| weblate                    |      main       |      main       | 10158 |   TCP    |       Active        | -                                                |
| photoview                  |      main       |      main       | 10159 |   TCP    |       Active        | -                                                |
| linkace                    |      main       |      main       | 10160 |   TCP    |       Active        | -                                                |
| librephotos                |      main       |      main       | 10161 |   TCP    |       Active        | -                                                |
| pydio-cells                |   healthcheck   |   healthcheck   | 10162 |   TCP    |       Active        | -                                                |
| grist                      |      main       |      main       | 10163 |   TCP    |       Active        | -                                                |
| grist                      |       api       |       api       | 10164 |   TCP    |       Active        | -                                                |
| budge                      |      main       |      main       | 10165 |   TCP    |       Active        | -                                                |
| alist                      |      main       |      main       | 10167 |   TCP    |       Active        | -                                                |
| ddns-go                    |      main       |      main       | 10168 |   TCP    |       Active        | -                                                |
| openhab                    |      main       |      main       | 10169 |   TCP    |       Active        | -                                                |
| openhab                    |      https      |      https      | 10170 |   TCP    |       Active        | -                                                |
| redmine                    |      main       |      main       | 10171 |   TCP    |       Active        | -                                                |
| matomo                     |      main       |      main       | 10172 |   HTTP   |       Active        | -                                                |
| matomo                     |      https      |      https      | 10173 |  HTTPS   |       Active        | -                                                |
| flexget                    |      main       |      main       | 10174 |   TCP    |       Active        | -                                                |
| qinglong                   |      main       |      main       | 10176 |   TCP    |       Active        | -                                                |
| lanraragi                  |      main       |      main       | 10177 |   TCP    |       Active        | -                                                |
| homer                      |      main       |      main       | 10178 |   TCP    |       Active        | -                                                |
| tinymediamanager           |      main       |      main       | 10179 |   TCP    |       Active        | -                                                |
| makemkv                    |      main       |      main       | 10180 |   TCP    |       Active        | -                                                |
| makemkv                    |       vnc       |       vnc       | 10181 |   TCP    |       Active        | -                                                |
| nextpvr                    |      main       |      main       | 10183 |   TCP    |       Active        | -                                                |
| ispy-agent-dvr             |      main       |      main       | 10184 |   TCP    |       Active        | -                                                |
| koel                       |      main       |      main       | 10185 |   TCP    |       Active        | -                                                |
| hammond                    |      main       |      main       | 10186 |   TCP    |       Active        | -                                                |
| filebrowser                |      main       |      main       | 10187 |   TCP    |       Active        | -                                                |
| iyuuplus                   |      main       |      main       | 10188 |   TCP    |       Active        | -                                                |
| kavita                     |      main       |      main       | 10189 |   TCP    |       Active        | -                                                |
| zerotier                   |      main       |      main       | 10190 |   UDP    |       Active        | -                                                |
| rsshub                     |      main       |      main       | 10191 |   TCP    |       Active        | -                                                |
| wekan                      |      main       |      main       | 10192 |   TCP    |       Active        | -                                                |
| verysync                   |      main       |      main       | 10193 |   TCP    |       Active        | -                                                |
| browserless-chrome         |      main       |      main       | 10194 |   TCP    |       Active        | -                                                |
| kutt                       |      main       |      main       | 10195 |   TCP    |       Active        | -                                                |
| outline                    |      main       |      main       | 10196 |   TCP    |       Active        | -                                                |
| chevereto                  |      main       |      main       | 10197 |   TCP    |       Active        | -                                                |
| kimai                      |      main       |      main       | 10198 |   TCP    |       Active        | -                                                |
| double-take                |      main       |      main       | 10200 |   TCP    |       Active        | -                                                |
| ml-workspace               |      main       |      main       | 10201 |   TCP    |       Active        | -                                                |
| ferdi-server               |      main       |      main       | 10206 |   TCP    |       Active        | -                                                |
| typecho                    |      main       |      main       | 10207 |   TCP    |       Active        | -                                                |
| xwiki                      |      main       |      main       | 10208 |   TCP    |       Active        | -                                                |
| picoshare                  |      main       |      main       | 10209 |   TCP    |       Active        | -                                                |
| linkding                   |      main       |      main       | 10210 |   TCP    |       Active        | -                                                |
| pinry                      |      main       |      main       | 10213 |   TCP    |       Active        | -                                                |
| drawio                     |      main       |      main       | 10214 |   TCP    |       Active        | -                                                |
| snapdrop                   |      main       |      main       | 10215 |   TCP    |       Active        | -                                                |
| metube                     |      main       |      main       | 10216 |   TCP    |       Active        | -                                                |
| cyberchef                  |      main       |      main       | 10219 |   TCP    |       Active        | -                                                |
| vikunja                    |      main       |      main       | 10220 |   TCP    |       Active        | -                                                |
| website-shot               |      main       |      main       | 10221 |   TCP    |       Active        | -                                                |
| ntfy                       |      main       |      main       | 10222 |   TCP    |       Active        | -                                                |
| audiobookshelf             |      main       |      main       | 10223 |   TCP    |       Active        | -                                                |
| fluidd                     |      main       |      main       | 10224 |   TCP    |       Active        | -                                                |
| rss-bridge                 |      main       |      main       | 10225 |   TCP    |       Active        | -                                                |
| nocodb                     |      main       |      main       | 10226 |   TCP    |       Active        | -                                                |
| ddns-updater               |      main       |      main       | 10227 |   TCP    |       Active        | -                                                |
| baserow                    |      main       |      main       | 10228 |   TCP    |       Active        | -                                                |
| inventree                  |      main       |      main       | 10231 |   TCP    |       Active        | -                                                |
| mkvtoolnix                 |      main       |      main       | 10236 |   TCP    |       Active        | -                                                |
| mkvtoolnix                 |       vnc       |       vnc       | 10237 |   TCP    |       Active        | -                                                |
| kopia                      |      main       |      main       | 10238 |   TCP    |       Active        | -                                                |
| mattermost                 |      main       |      main       | 10239 |   TCP    |       Active        | -                                                |
| commento-plusplus          |      main       |      main       | 10240 |   TCP    |       Active        | -                                                |
| jellyseerr                 |      main       |      main       | 10241 |   TCP    |       Active        | -                                                |
| fileflows                  |      main       |      main       | 10242 |   TCP    |       Active        | -                                                |
| meshroom                   |      main       |      main       | 10243 |   TCP    |       Active        | -                                                |
| clarkson                   |      main       |      main       | 10244 |   TCP    |       Active        | Potential conflict with: theme-park              |
| homarr                     |      main       |      main       | 10245 |   TCP    |       Active        | -                                                |
| prometheus                 |     thanos      |     thanos      | 10901 |   HTTP   |       Active        | -                                                |
| storj-node                 |      main       |      main       | 14002 |   TCP    |       Active        | -                                                |
| satisfactory               |     beacon      |     beacon      | 15000 |   UDP    |       Active        | -                                                |
| satisfactory               |      query      |      query      | 15777 |   UDP    |       Active        | -                                                |
| minecraft-bedrock          |      main       |      main       | 19132 |   UDP    |       Active        | -                                                |
| hyperion-ng                | boblightservice | boblightservice | 19333 |   TCP    |       Active        | -                                                |
| hyperion-ng                |   jsonservice   |   jsonservice   | 19444 |   TCP    |       Active        | -                                                |
| hyperion-ng                | protobufservice | protobufservice | 19445 |   TCP    |       Active        | -                                                |
| netdata                    |      main       |      main       | 19999 |   TCP    |       Active        | -                                                |
| syncthing                  |    discovery    |    discovery    | 21027 |   UDP    |       Active        | -                                                |
| airdcpp-webclient          | unencrypted-tcp | unencrypted-tcp | 21248 |   TCP    |       Active        | -                                                |
| airdcpp-webclient          |   search-udp    |   search-udp    | 21248 |   UDP    |       Active        | -                                                |
| airdcpp-webclient          |  encrypted-tcp  |  encrypted-tcp  | 21249 |   TCP    |       Active        | -                                                |
| syncthing                  |    listeners    |       tcp       | 22000 |   TCP    |       Active        | -                                                |
| syncthing                  |  listeners-udp  |       udp       | 22000 |   UDP    |       Active        | -                                                |
| impostor-server            |      main       |      main       | 22023 |   UDP    |       Active        | -                                                |
| verysync                   |     bt-udp2     |     bt-udp2     | 22027 |   UDP    |       Active        | -                                                |
| verysync                   |     bt-udp1     |     bt-udp1     | 22037 |   UDP    |       Active        | -                                                |
| joplin-server              |      main       |      main       | 22300 |   TCP    |       Active        | -                                                |
| verysync                   |      data       |      data       | 22330 |   TCP    |       Active        | -                                                |
| minecraft-java             |      main       |      main       | 25565 |   TCP    |       Active        | -                                                |
| minecraft-java             |      rcon       |      rcon       | 25575 |   TCP    |       Active        | -                                                |
| storj-node                 |     coretcp     |     coretcp     | 28967 |   TCP    |       Active        | -                                                |
| storj-node                 |     coreudp     |     coreudp     | 28967 |   UDP    |       Active        | -                                                |
| omada-controller           |    omada-udp    |   omada-udp1    | 29810 |   UDP    |       Active        | -                                                |
| omada-controller           |    omada-tcp    |   omada-tcp1    | 29811 |   TCP    |       Active        | -                                                |
| omada-controller           |    omada-tcp    |   omada-tcp2    | 29812 |   TCP    |       Active        | -                                                |
| omada-controller           |    omada-tcp    |   omada-tcp3    | 29813 |   TCP    |       Active        | -                                                |
| omada-controller           |    omada-tcp    |   omada-tcp4    | 29814 |   TCP    |       Active        | -                                                |
| minetest                   |      main       |      main       | 30000 |   UDP    |       Active        | -                                                |
| teamspeak3                 |      files      |      files      | 30033 |   TCP    |       Active        | -                                                |
| plex                       |      main       |      main       | 32400 |   TCP    |       Active        | -                                                |
| pydio-cells                |      gprc       |      gprc       | 33060 |   TCP    |       Active        | -                                                |
| xteve                      |      main       |      main       | 34400 |   TCP    |       Active        | -                                                |
| foldingathome              |     control     |     control     | 36330 |   TCP    |       Active        | -                                                |
| habridge                   |      comm       |      comm       | 50000 |   TCP    |       Active        | -                                                |
| ispy-agent-dvr             |     webrtc      |     webrtc0     | 50000 |   UDP    |       Active        | -                                                |
| ispy-agent-dvr             |     webrtc      |     webrtc1     | 50001 |   UDP    |       Active        | -                                                |
| ispy-agent-dvr             |     webrtc      |     webrtc2     | 50002 |   UDP    |       Active        | -                                                |
| ispy-agent-dvr             |     webrtc      |     webrtc3     | 50003 |   UDP    |       Active        | -                                                |
| ispy-agent-dvr             |     webrtc      |     webrtc4     | 50004 |   UDP    |       Active        | -                                                |
| ispy-agent-dvr             |     webrtc      |     webrtc5     | 50005 |   UDP    |       Active        | -                                                |
| ispy-agent-dvr             |     webrtc      |     webrtc6     | 50006 |   UDP    |       Active        | -                                                |
| ispy-agent-dvr             |     webrtc      |     webrtc7     | 50007 |   UDP    |       Active        | -                                                |
| ispy-agent-dvr             |     webrtc      |     webrtc8     | 50008 |   UDP    |       Active        | -                                                |
| ispy-agent-dvr             |     webrtc      |     webrtc9     | 50009 |   UDP    |       Active        | -                                                |
| ispy-agent-dvr             |     webrtc      |    webrtc10     | 50010 |   UDP    |       Active        | -                                                |
| appdaemon                  |       tcp       |       tcp       | 51050 |   TCP    |       Active        | -                                                |
| podgrab                    |       tcp       |       tcp       | 51080 |   TCP    |       Active        | -                                                |
| deluge                     |     torrent     |       tcp       | 51413 |   TCP    |       Active        | -                                                |
| deluge                     |   torrent-udp   |       udp       | 51413 |   UDP    |       Active        | -                                                |
| transmission               |     torrent     |     torrent     | 51414 |   TCP    |       Active        | -                                                |
| transmission               |   torrentudp    |   torrentudp    | 51414 |   UDP    |       Active        | -                                                |
| resilio-sync               |     bt-tcp      |     bt-tcp      | 55555 |   TCP    |       Active        | -                                                |
| resilio-sync               |     bt-udp      |     bt-udp      | 55555 |   UDP    |       Active        | -                                                |
| quassel-web                |      main       |      main       | 64080 |   TCP    |       Active        | -                                                |

## Dependency

| App        | Service | Port Name | Port  | Protocol | Status | Note |
| :--------- | :-----: | :-------: | :---: | :------: | :----: | :--- |
| promtail   |  main   |   main    | 3101  |   TCP    | Active | -    |
| mariadb    |  main   |   main    | 3306  |   TCP    | Active | -    |
| postgresql |  main   |   main    | 5432  |   TCP    | Active | -    |
| redis      |  main   |   main    | 6379  |   TCP    | Active | -    |
| memcached  |  main   |   main    | 11211 |   TCP    | Active | -    |
| mongodb    |  main   |   main    | 27017 |   TCP    | Active | -    |

## Incubator

| App                   |     Service     |    Port Name    | Port  | Protocol | Status | Note                                         |
| :-------------------- | :-------------: | :-------------: | :---: | :------: | :----: | :------------------------------------------- |
| adguard-home          |     dns-tcp     |     dns-tcp     |  53   |   TCP    | Active | Potential conflict with: pihole technitium   |
| adguard-home          |     dns-udp     |     dns-udp     |  53   |   UDP    | Active | -                                            |
| technitium            |     dns-tcp     |     dns-tcp     |  53   |   TCP    | Active | Potential conflict with: pihole adguard-home |
| technitium            |     dns-udp     |     dns-udp     |  53   |   UDP    | Active | -                                            |
| zabbix-server         |    snmptraps    |    snmptraps    |  162  |   UDP    | Active | -                                            |
| cups-server           |      main       |      main       |  631  |   TCP    | Active | -                                            |
| adguard-home          | dns-quic-udp-1  | dns-quic-udp-1  |  784  |   UDP    | Active | -                                            |
| adguard-home          | dns-quic-udp-2  | dns-quic-udp-2  |  853  |   UDP    | Active | -                                            |
| technitium            |     dns-tls     |     dns-tls     |  853  |   TCP    | Active | -                                            |
| frigate               |      rtmp       |      rtmp       | 1935  |   TCP    | Active | Potential conflict with: owncast             |
| frigate               |      main       |      main       | 5000  |   TCP    | Active | -                                            |
| technitium            |      main       |      main       | 5380  |   TCP    | Active | -                                            |
| adguard-home          |    dns-crypt    |    dns-crypt    | 5443  |   TCP    | Active | -                                            |
| adguard-home          |  dns-crypt-udp  |  dns-crypt-udp  | 5443  |   UDP    | Active | -                                            |
| homebridge            |      main       |      main       | 8581  |   TCP    | Active | -                                            |
| adguard-home          | dns-quic-udp-3  | dns-quic-udp-3  | 8853  |   UDP    | Active | -                                            |
| piwigo                |      main       |      main       | 10027 |   TCP    | Active | -                                            |
| jump                  |      main       |      main       | 10108 |   TCP    | Active | -                                            |
| senseai-server        |      main       |      main       | 10118 |   TCP    | Active | -                                            |
| ghost                 |      main       |      main       | 10166 |   TCP    | Active | -                                            |
| self-service-password |      main       |      main       | 10182 |   TCP    | Active | -                                            |
| filerun               |      main       |      main       | 10199 |   TCP    | Active | -                                            |
| technitium            |    dns-cert     |    dns-cert     | 10202 |   TCP    | Active | -                                            |
| technitium            |    dns-https    |    dns-https    | 10203 |   TCP    | Active | -                                            |
| technitium            | dns-https-proxy | dns-https-proxy | 10204 |   TCP    | Active | -                                            |
| meshcentral           |      main       |      main       | 10205 |  HTTPS   | Active | -                                            |
| zabbix-server         |      main       |      main       | 10211 |   TCP    | Active | -                                            |
| zabbix-server         |     server      |     server      | 10212 |   TCP    | Active | -                                            |
| appsmith              |      main       |      main       | 10217 |   TCP    | Active | -                                            |
| appsmith              |   supervisor    |   supervisor    | 10218 |   TCP    | Active | -                                            |
| authentik             |      https      |      https      | 10229 |  HTTPS   | Active | -                                            |
| authentik             |      main       |      main       | 10230 |   TCP    | Active | -                                            |
| adguard-home          |      main       |      main       | 10232 |   TCP    | Active | -                                            |
| adguard-home          |    dns-http     |    dns-http     | 10233 |   TCP    | Active | -                                            |
| adguard-home          |    dns-https    |    dns-https    | 10234 |   TCP    | Active | -                                            |
| adguard-home          |  dns-https-udp  |  dns-https-udp  | 10234 |   UDP    | Active | -                                            |
| fancyindex            |      main       |      main       | 10235 |   TCP    | Active | -                                            |
| theme-park            |      main       |      main       | 10244 |   TCP    | Active | Potential conflict with: clarkson            |
| awesome-ttrss         |      main       |      main       | 10246 |   TCP    | Active | -                                            |
| jitsi                 |      main       |      main       | 10247 |   TCP    | Active | -                                            |
| wger                  |      main       |      main       | 10249 |   TCP    | Active | -                                            |
| openspeedtest         |      main       |      main       | 10251 |   TCP    | Active | -                                            |

## Official Apps

> Please keep mind that this list is not updated automatically like the rest of this doc

| App            |   Service   | Port  |                     Note                     |
| :------------- | :---------: | :---: | :------------------------------------------: |
| chia           |    main     | 8444  |                                              |
| chia           | farmerport  | 8447  |                                              |
| collabora      |    main     | 9980  |                                              |
| emby           |    main     | 9096  |                                              |
| home-assistant |    main     | 20810 |                                              |
| ipfs           |  swarmport  | 9401  |                                              |
| ipfs           |   apiport   | 9501  |                                              |
| ipfs           | gatewayport | 9880  |                                              |
| machinaris     |    main     | 9003  |                                              |
| machinaris     |   apiport   | 8927  |                                              |
| minio          |    main     | 9000  | Potential conflict with traefik (TrueCharts) |
| minio          | consoleport | 9002  |                                              |
| netdata        |    main     | 20489 |                                              |
| nextcloud      |    main     | 9001  |                                              |
| photoprism     |    main     | 20800 |                                              |
| pihole         |    main     | 20720 |                                              |
| pihole         |   dns-tcp   | 20721 |                                              |
| pihole         |   dns-upd   | 20721 |                                              |
| pihole         |    dhcp     | 20722 |                                              |
| plex           |    main     | 32400 |  Potential conflict with plex (TrueCharts)   |
| qbittorent     |    main     | 20909 |                                              |
| qbittorent     |  tcp_port   | 20988 |                                              |
| qbittorent     |  udp_port   | 20989 |                                              |
| syncthing      |    main     | 20910 |                                              |
| syncthing      |  tcp_port   | 20978 |                                              |
| syncthing      |  udp_port   | 20979 |                                              |

## TrueNAS Scale Services

> Please mind that this list is not updated automatically like the rest of this doc

| Service | Port  | Protocol | Note |
| :------ | :---: | :------: | :--: |
| ssh     |  22   |   TCP    |      |
| webui   |  80   |   HTTP   |      |
| webui   |  443  |  HTTPS   |      |
| kubelet | 10250 |   HTTP   |      |

## Ports that are blocked in major web browsers

> Please mind that this list is not updated automatically like the rest of this doc

| Port  |            Used by (example)             |
| :---: | :--------------------------------------: |
|   1   |                  tcpmux                  |
|   7   |                   echo                   |
|   9   |                 discard                  |
|  11   |                  systat                  |
|  13   |                 daytime                  |
|  15   |                 netstat                  |
|  17   |                   qotd                   |
|  19   |                 chargen                  |
|  20   |                 ftp data                 |
|  21   |                ftp access                |
|  22   |                   ssh                    |
|  23   |                  telnet                  |
|  25   |                   smtp                   |
|  37   |                   time                   |
|  42   |                   name                   |
|  43   |                 nicname                  |
|  53   |                  domain                  |
|  69   |                   tftp                   |
|  77   |                 priv-rjs                 |
|  79   |                  finger                  |
|  87   |                 ttylink                  |
|  95   |                  supdup                  |
|  101  |                hostriame                 |
|  102  |                 iso-tsap                 |
|  103  |                 gppitnp                  |
|  104  |                 acr-nema                 |
|  109  |                   pop2                   |
|  110  |                   pop3                   |
|  111  |                  sunrpc                  |
|  113  |                   auth                   |
|  115  |                   sftp                   |
|  117  |                uucp-path                 |
|  119  |                   nntp                   |
|  123  |                   NTP                    |
|  135  |              loc-srv /epmap              |
|  137  |                 netbios                  |
|  139  |                 netbios                  |
|  143  |                  imap2                   |
|  161  |                   snmp                   |
|  179  |                   BGP                    |
|  389  |                   ldap                   |
|  427  | SLP (Also used by Apple Filing Protocol) |
|  465  |                 smtp+ssl                 |
|  512  |               print / exec               |
|  513  |                  login                   |
|  514  |                  shell                   |
|  515  |                 printer                  |
|  526  |                  tempo                   |
|  530  |                 courier                  |
|  531  |                   chat                   |
|  532  |                 netnews                  |
|  540  |                   uucp                   |
|  548  |       AFP (Apple Filing Protocol)        |
|  554  |                   rtsp                   |
|  556  |                 remotefs                 |
|  563  |                 nntp+ssl                 |
|  587  |              smtp (rfc6409)              |
|  601  |          syslog-conn (rfc3195)           |
|  636  |                 ldap+ssl                 |
|  989  |                ftps-data                 |
|  990  |                   ftps                   |
|  993  |                 ldap+ssl                 |
|  995  |                 pop3+ssl                 |
| 1719  |               h323gatestat               |
| 1720  |               h323hostcall               |
| 1723  |                   pptp                   |
| 2049  |                   nfs                    |
| 3659  |       apple-sasl / PasswordServer        |
| 4045  |                  lockd                   |
| 5060  |                   sip                    |
| 5061  |                   sips                   |
| 6000  |                   X11                    |
| 6566  |                sane-port                 |
| 6665  |      Alternate IRC [Apple addition]      |
| 6666  |      Alternate IRC [Apple addition]      |
| 6667  |      Standard IRC [Apple addition]       |
| 6668  |      Alternate IRC [Apple addition]      |
| 6669  |      Alternate IRC [Apple addition]      |
| 6697  |                IRC + TLS                 |
| 10080 |                  Amanda                  |

> Note: TCP and UDP ports that are the same in some Apps, are not by mistake

> If you notice something wrong in the above info, please notify us so we can update the generator script

> Next available port should be 10252
