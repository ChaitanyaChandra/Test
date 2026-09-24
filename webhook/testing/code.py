def parse_number(val):
    return int(val) if val.is_integer() else val

def cpu_to_milli_cpu(cpu):
    if cpu is None:
        return None

    cpu = str(cpu).strip()

    if cpu.endswith("m"):
        return parse_number(float(cpu[:-1]))

    return parse_number(float(cpu) * 1000)


def memory_to_mb(memory):
    if memory is None:
        return None

    memory = str(memory).strip()

    if memory.endswith("Ki"):
        return parse_number(float(memory[:-2]) / 1024)

    if memory.endswith("Mi"):
        return parse_number(float(memory[:-2]))

    if memory.endswith("Gi"):
        return parse_number(float(memory[:-2]) * 1024)

    if memory.endswith("Ti"):
        return parse_number(float(memory[:-2]) * 1024 * 1024)

    try:
        return parse_number(float(memory) / (1024 * 1024))
    except ValueError:
        return None


print(cpu_to_milli_cpu("1"))
print(cpu_to_milli_cpu("10"))
print(cpu_to_milli_cpu("0.5"))
print(cpu_to_milli_cpu("0.5m"))
print(cpu_to_milli_cpu("0.005m"))
print(cpu_to_milli_cpu("0.005"))
print(cpu_to_milli_cpu("500m"))

print(memory_to_mb("1024Mi"))
print(memory_to_mb("1024Ki"))
print(memory_to_mb("1Gi"))
print(memory_to_mb("0.5Gi"))
print(memory_to_mb("5000Ki"))
print(memory_to_mb("0.5Ti"))