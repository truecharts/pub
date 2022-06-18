# Introduction

Store securely encrypted backups on cloud storage services!

TrueCharts are designed to be installed as TrueNAS SCALE app only. We can not guarantee this charts works as a stand-alone helm installation.
**This chart is not maintained by the upstream project and any issues with the chart should be raised [here](https://github.com/truecharts/apps/issues/new/choose)**

## Source Code

* <https://hub.docker.com/r/linuxserver/duplicati/>
* <https://github.com/duplicati/duplicati>

## Requirements

Kubernetes: `>=1.16.0-0`

## Dependencies

| Repository | Name | Version |
|------------|------|---------|
| https://library-charts.truecharts.org | common | 10.0.10 |

## Installing the Chart

To install this App on TrueNAS SCALE check our [Quick-Start Guide](https://truecharts.org/manual/Quick-Start%20Guides/02-Installing-an-App/).

## Ingress 

This chart requires Ingress to be enabled after initial install due to the configuration of the application upstream (the Duplicati team). Please install the application without Ingress, access settings of the application and add your hostname inside the settings of the app.

![image](https://user-images.githubusercontent.com/89483932/174445638-bac32cc8-375f-4fdb-a99f-f8b75a4613e1.png)

Once this is done you can successful add Ingress using the steps outlined inside our [Quick-Start Guide](https://truecharts.org/manual/Quick-Start%20Guides/09-add-ingress/)

## Upgrading, Rolling Back and Uninstalling the Chart

To upgrade, rollback or delete this App from TrueNAS SCALE check our [Quick-Start Guide](https://truecharts.org/manual/Quick-Start%20Guides/04-Upgrade-rollback-delete-an-App/).

## Support

- Please check our [quick-start guides](https://truecharts.org/manual/Quick-Start%20Guides/01-Adding-TrueCharts/) first.
- See the [Wiki](https://truecharts.org)
- Check our [Discord](https://discord.gg/tVsPTHWTtr)
- Open a [issue](https://github.com/truecharts/apps/issues/new/choose)
---
All Rights Reserved - The TrueCharts Project
