def is_criticality_balanced(temperature, neutrons_emitted):
    if temperature < 800 and neutrons_emitted > 500 and temperature*neutrons_emitted<500000:
        return True
    else: 
        return False

def reactor_efficiency(voltage, current, theoretical_max_power):
    generated_power = voltage * current
    efficiency = (generated_power/theoretical_max_power) * 100
    if efficiency >= 80:
        return "green"
    if efficiency >= 60:
        return "orange"
    if efficiency >=30:
        return "red"
    else: 
        return "black"


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    temperature_neutrons = temperature * neutrons_produced_per_second
    if temperature_neutrons < (threshold * 0.9):
        return "LOW"
    if (threshold*0.9) <= temperature_neutrons <= (threshold*1.1):
        return "NORMAL"
    else:
        return "DANGER"