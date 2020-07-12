import logging
import importlib

LOGGER = logging.getLogger(__name__)
DOMAIN = "custom_zha_radios"


def inject_enum_member(target_enum, name, value):
    """
    Hack to inject a new member into an enum.
    """

    member = target_enum._member_type_.__new__(target_enum)
    member._name_ = name
    member._value_ = value

    if not isinstance(value, tuple):
        args = (value,)
    else:
        args = value

    target_enum.__init__(member, *args)

    target_enum._member_names_.append(name)
    target_enum._member_map_[name] = member
    target_enum._value2member_map_[value] = member
    type.__setattr__(target_enum, name, member)


def setup(hass, config):
    """
    Injects modules specified in `custom_zha_radios`'s configration into `zha`.
    """

    try:
        from homeassistant.components.zha.core.const import RadioType
    except ImportError:
        LOGGER.error("It looks like HA has not finished setting up its dependencies yet"
                     " on first launch. Restart Home Assistant once it finishes.")
        return False

    custom_names = list(config[DOMAIN].keys())
    original_names = list(RadioType._member_names_)

    for name, obj in config[DOMAIN].items():
        module = importlib.import_module(obj["module"])
        app = module.ControllerApplication
        description = obj["description"]

        LOGGER.info("Injecting %s (%s) as a new radio type", name, obj)
        inject_enum_member(RadioType, name, (description, app))

    # New keys are moved up top
    RadioType._member_names_ = custom_names + original_names

    return True
