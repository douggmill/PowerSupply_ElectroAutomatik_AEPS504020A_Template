# Doug Gammill
# 4/28/2026
# Rev 1.0
# Python 3.13
# main

from PowerSupply_ElectroAutomatik_EAPS504020A import set_PSU_VOLTAGE, connect_PSU, disconnect_PSU, read_PSU_Volt_Amp



connect_PSU() # connect to PSU, look in this function to set max amps

volt = 32.0
set_PSU_VOLTAGE(volt)

read_PSU_Volt_Amp()

disconnect_PSU() # disconnect to PSU


