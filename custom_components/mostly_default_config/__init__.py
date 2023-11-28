"""Component providing mostly default configuration for somewhat new users."""
from .const import *

import asyncio

from homeassistant import core
from homeassistant.loader import async_get_integration
from homeassistant.setup import async_setup_component


async def async_setup(hass: core.HomeAssistant, config: dict) -> bool:
    conf = config.get(DOMAIN)
    exclude = set(conf.get(EXCLUDE, []))

    default_component = await async_get_integration(hass, DEFAULT_CONFIG)
    default_dependencies = set(default_component.manifest[DEPENDENCIES])

    await asyncio.gather(
        *(
            async_setup_component(hass, domain, config)
            for domain in default_dependencies - exclude
        )
    )

    return True
