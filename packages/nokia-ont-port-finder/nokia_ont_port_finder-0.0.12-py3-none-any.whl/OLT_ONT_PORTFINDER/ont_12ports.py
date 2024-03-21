""""""


class SlotsPortsManager:
    """Process slots and  ports
    12_ports = {'1/1/3/10/1/1': '8', '1/1/1/3/10/1': '4'}
    """
    def __init__(self, slots, slot_port):
        self.slots_dict = slots
        self.slot_port = slot_port
        self.slot_port_erros = f"""
        [ {self.slot_port} ] is not a valid slot/port value
        These are the valid slots [1, 4]
        These are the valid ports [1-8]
        This is a slot/port example: 1/3
        """

    def get_target_port(self):
        """
            12_ports = {'1/1/3/10/1/1': '8', '1/1/1/3/10/1': '4'}
        """
        data = self.slots_dict
        if not self.slot_port:
            print(f"No slot/port value provided\n")
            print(f"These are the valid slots [1 and 3]")
            print(f"These are the valid ports [1-8]\n\n")
            exit()

        slot1 = {}
        slot4 = {}
        for k, v in data.items():
            if k.endswith('1') and '8' in v:
                slot1[k] = v
            if k.endswith('1') and '4' in v:
                slot4[k] = v

        if self.slot_port:
            if len(str(self.slot_port)) == 3:
                sl, _, port = list(self.slot_port)
                if str(sl).isnumeric() and str(port).isnumeric():
                    if int(sl) == 1:
                        # check if provided port is numeric
                        if str(port).isnumeric():
                            # check if provided port is in within the correct range
                            if int(port) in range(1, int(list(slot1.values())[0]) + 1):
                                target_port = f"{list(slot1.keys())[0]}/{port}"
                                return target_port
                            else:
                                print(f"\n[ {port} ] is no a valid port value for slot1 and slot3")
                                print(f"These are the valid port for slot1 and slot3 [1-8]\n")
                                exit()
                        else:
                            print(f"\n[ {sl} ] must be a numeric value")
                            print(f"These are the valid ports for slot1 and slot3 [1-8]\n")
                            exit()
                    elif int(sl) == 4:
                        # check if provided port is numeric
                        if str(port).isnumeric():
                            # check if provided port is in within the correct range
                            if int(port) in range(1, int(list(slot4.values())[0]) + 1):
                                target_port = f"{list(slot4.keys())[0]}/{port}"
                                return target_port
                            else:
                                print(f"\n[ {port} ] is no a valid port value for slot4")
                                print(f"These are the valid port for slot4 [1-4]\n")
                                exit()
                        else:
                            print(f"\n[ {sl} ] must be a numeric value")
                            print(f"These are the valid port for slot4 [1-4]\n")
                            exit()
                    else:
                        print(f"\n [ {self.slot_port} ] is not a valid slot value")
                        print(f"These are the valid slots in this hardware [1, 4]\n")
                        exit()
                else:
                    print(self.slot_port_erros)
                    exit()
            else:
                print(self.slot_port_erros)
                exit()
        else:
            print(self.slot_port_erros)
            exit()















#