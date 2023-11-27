# Mostly Default Config for Home Assistant

Implements a mostly default config for those who wish for their configuration to follow the default configuration, but without specific components.

## Installation

1. Remove `default_config` from `configuration.yaml` and replace it with something like:

```
mostly_default_config:
  excepting:
    - map
    - logbook
    - ...
```

2. Restart Home Assistant
3. Enjoy a default config without the specific component you wanted to disable

See [here](https://github.com/home-assistant/core/blob/master/homeassistant/components/default_config/manifest.json) for a list of components that are loaded by `default_config` and can be excepted by this component.

## Limitations

Current implementation will always load `recorder` since that particular component requires special setup.