# This package is obsolete and will not reliably work. Install [zha-ng/zigpy-znp's custom component](https://github.com/zha-ng/zigpy-znp/blob/dev/custom_components/zha_custom_radios.py) instead.

----

# zha-custom-radios

Adds support for custom radio modules to Home Assistant's [ZHA (Zigbee Home Automation) integration component](https://www.home-assistant.io/integrations/zha/). This custom component allows users to test out new modules before they're integrated into ZHA and develop new zigpy radio modules without having to modify the Home Assistant source code.

## Installation

If you're using HACS, add `https://github.com/zha-ng/zha-custom-radios` as [a custom repository](https://hacs.xyz/docs/faq/custom_repositories). Otherwise, copy `custom_components/custom_zha_radios` into your Home Assistant installation's `custom_components` folder.

The latest release of [`zigpy-znp`](https://github.com/zha-ng/zigpy-znp) is already a dependency in the `manifest.json` so all you need to do is add the following section to your `configuration.yaml`:

```yaml
custom_zha_radios:
  znp:
    module: zigpy_znp.zigbee.application
    description: TI CC13x2, CC26x2, and ZZH
```

The latest release of `zigpy-znp` will be installed every time you restart Home Assistant.
