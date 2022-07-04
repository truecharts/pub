# PCI(-E) Devices Passthrough

To Passthrough your PCI(-E) cards you need to:

- Go to Installed Applications
- Click the menu button on the right side of the App card
- Select Edit
- Scroll down to "Resources and Devices" Section
- Under Configure Mount USB devices Click the Add button on the right (This will work for PCI devices too*)
- In "Host Device Path" & "Container Device Path" enter the /dev/path for your card (ex: for dvb devices it will be: /dev/dvb)
- Submit your changes

> *This method is not guaranteed to work, and we officially offer no support for PCI(-E) devices Passthrough at the moment.