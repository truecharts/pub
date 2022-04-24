# Introduction

Minisatip is a multi-threaded satip server version 1.2 that runs under Linux.

TrueCharts are designed to be installed as TrueNAS SCALE app only. We can not guarantee this charts works as a stand-alone helm installation.
**This chart is not maintained by the upstream project and any issues with the chart should be raised [here](https://github.com/truecharts/apps/issues/new/choose)**

## Source Code

* <https://hub.docker.com/r/linuxserver/minisatip>

## Requirements

Kubernetes: `>=1.16.0-0`

## Dependencies

| Repository | Name | Version |
|------------|------|---------|
| https://library-charts.truecharts.org | common | 9.2.9 |

## Installing the Chart

To install this App on TrueNAS SCALE check our [Quick-Start Guide](https://truecharts.org/manual/Quick-Start%20Guides/02-Installing-an-App/).

## TV-Cards Passthrough 

To Passthrough your cards you need to :
- Go to Installed Applications
- Click the menu button on the right side of the minisatip App card
- Select Edit 
- Scroll down to "Resources and Devices" Section
- Under Configure Mount USB devices Click the Add button on the right (This will work for PCI devices too)
- In "Host Device Path" & "Container Device Path" enter your enter the /dev/path for you card (For dvb devices it will be: /dev/dvb)
- Submit your changes


## Upgrading, Rolling Back and Uninstalling the Chart

To upgrade, rollback or delete this App from TrueNAS SCALE check our [Quick-Start Guide](https://truecharts.org/manual/Quick-Start%20Guides/04-Upgrade-rollback-delete-an-App/).

## Support

- Please check our [quick-start guides](https://truecharts.org/manual/Quick-Start%20Guides/01-Adding-TrueCharts/) first.
- See the [Wiki](https://truecharts.org)
- Check our [Discord](https://discord.gg/tVsPTHWTtr)
- Open a [issue](https://github.com/truecharts/apps/issues/new/choose)
---
All Rights Reserved - The TrueCharts Project
