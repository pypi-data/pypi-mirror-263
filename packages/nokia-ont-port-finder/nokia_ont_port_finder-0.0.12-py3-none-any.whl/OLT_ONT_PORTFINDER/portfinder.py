from OLT_ONT_PORTFINDER import ont_4ports, \
    ont_8ports, ont_20ports_R,ont_16ports, \
    ont_24ports, ont_12ports,ont_20ports_l


class PortFinder:
    """Collect data from external source and process it
        the slot must be a dict
        the slot must be a string like this '1/3' for slot with more than 4 ports
        and '1' for a 4 ports slot
    """

    def __init__(self, slots, slot_port=None):
        self.slots = slots
        self.slot_port = slot_port

    def get_target_port(self):
        """
            received data should be something like this:
            24_ports = {'1/1/3/10/1/1': '8', '1/1/3/10/1/3': '8', '1/1/1/1/1/4', '1/1/1/1/1/5'}
            16_ports = {'1/1/3/10/1/1': '8', '1/1/3/10/1/3': '8'}
            16_ports_plus4 = {'1/1/1/3/10/1': '4', '1/1/3/10/1/1': '8', '1/1/3/10/1/3': '8'}
            8_ports = {'1/1/3/10/1/1': '8'}
            4_ports = {'1/1/1/3/10/1': '4'}
        """

        if self.slots and self.slot_port:
            # check if 12 ports ont
            if len(self.slots) == 2 and list(self.slots.values()) == ['8', '4']:
                port = ont_12ports.SlotsPortsManager(self.slots, self.slot_port)
                port = port.get_target_port()
                return port

            # check if 16 ports ont
            elif len(self.slots) == 2 and list(self.slots.values()) == ['8', '8']:
                    port = ont_16ports.SlotsPortsManager(self.slots, self.slot_port)
                    port = port.get_target_port()
                    return port
            # check if 20 ports left to write
            # 20 ports ONT 4 + 8 + 8
            elif len(self.slots) == 3 and list(self.slots.values()) == ['4', '8', '8']:
                    port = ont_20ports_l.SlotsPortsManagerL(self.slots, self.slot_port)
                    port = port.get_target_port()
                    return port
            # check if 20 ports write to left
            # 20 ports ONT 8 + 8 + 4
            elif len(self.slots) == 3 and list(self.slots.values()) == ['8', '8', '4']:
                    port = ont_20ports_R.SlotsPortsManagerR(self.slots, self.slot_port)
                    port = port.get_target_port()
                    return port
            # 24 ports ONT 8 + 8 + 4 + 4
            elif len(self.slots) == 4 and list(self.slots.values()) == ['8', '8', '4', '4']:
                port = ont_24ports.SlotsPortsManager(self.slots, self.slot_port)
                port = port.get_target_port()
                return port
            # check if 8 ports
            elif len(self.slots) == 1 and list(self.slots.values()) == ['8']:
                    port = ont_8ports.SlotsPortsManager(self.slots, self.slot_port)
                    port = port.get_target_port()
                    return port
            # check if 4 ports
            elif len(self.slots) == 1 and list(self.slots.values()) == ['4']:
                    port = ont_4ports.SlotsPortsManager(self.slots, self.slot_port)
                    port = port.get_target_port()
                    return port
            else:
                return f"Hardware not supported in the OLT " \
                       f"SLOT: {self.slots} -- PORT: {self.slot_port}\n"
        else:
            return f"No data provided for the ONT Hardware " \
                   f"SLOT: {self.slots} -- PORT: {self.slot_port}\n"
