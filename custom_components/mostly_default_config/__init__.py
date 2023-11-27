"""Component providing mostly default configuration for somewhat new users."""
from .const import DOMAIN

import asyncio

from homeassistant import core
from homeassistant.loader import async_get_integration
from homeassistant.setup import async_setup_component


async def async_setup(hass: core.HomeAssistant, config: dict) -> bool:
    conf = config.get(DOMAIN)
    excepting = set(conf['excepting'] if 'excepting' in conf else [])

    default_component = await async_get_integration(hass, 'default_config')
    default_dependencies = set(default_component.manifest['dependencies'])
    to_load = default_dependencies - excepting

    await asyncio.gather(
        *(
            async_setup_component(hass, domain, config)
            for domain in to_load
        )
    )

    return True
