import indigo

from Shelly import Shelly
from ..components.functional.switch import Switch
from ..components.functional.input import Input
from ..components.system.system import System
from ..components.system.wifi import WiFi
from ..components.system.ethernet import Ethernet
from ..components.system.ble import BLE
from ..components.system.mqtt import MQTT


class ShellyPro2(Shelly):
    """
    Creates a Shelly Pro 2 device class.
    """

    display_name = "Shelly Pro 2"

    def __init__(self, device_id):
        super(ShellyPro2, self).__init__(device_id)

        self.system_components = {
            'system': System(self),
            'wifi': WiFi(self),
            'ethernet': Ethernet(self),
            'ble': BLE(self),
            'mqtt': MQTT(self)
        }

        self.switch_0 = self.register_component(Switch, "Switch 1", comp_id=0)
        self.switch_1 = self.register_component(Switch, "Switch 2", comp_id=1)
        self.input_0 = self.register_component(Input, "Input 1", comp_id=0)
        self.input_1 = self.register_component(Input, "Input 2", comp_id=1)

    def handle_notify_status(self, component_type, instance_id, status):
        """
        Handler for NotifyStatus RPC messages.

        :param component_type: The component type.
        :param instance_id: The identifier of the component.
        :param status: Data for the notification.
        :return: None
        """

        super(ShellyPro2, self).handle_notify_status(component_type, instance_id, status)

    def handle_notify_event(self, component_type, instance_id, event):
        """
        Handler for NotifyEvent RPC messages.

        :param component_type: The component type.
        :param instance_id: The identifier of the component.
        :param event: The event to handle.
        :return: None
        """

        super(ShellyPro2, self).handle_notify_event(component_type, instance_id, event)

    def handle_action(self, action):
        """
        The method that gets called when an Indigo action takes place.

        :param action: The Indigo action.
        :return: None
        """

        super(ShellyPro2, self).handle_action(action)
