def parse_number(val):
    return int(val) if val.is_integer() else val

def cpu_to_milli_cpu(cpu):
    if cpu is None:
        return None

    cpu = str(cpu).strip()

    try:
        if cpu.endswith("m"):
            return parse_number(float(cpu[:-1]))
        return parse_number(float(cpu) * 1000)
    except ValueError:
        return None


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

    if memory.endswith("K"):
        return parse_number(float(memory[:-1]) * 1000 / (1024 * 1024))

    if memory.endswith("M"):
        return parse_number(float(memory[:-1]) * 1000000 / (1024 * 1024))

    if memory.endswith("G"):
        return parse_number(float(memory[:-1]) * 1000000000 / (1024 * 1024))

    if memory.endswith("m"):
        return parse_number(float(memory[:-1]) * 0.001 / (1024 * 1024))

    try:
        return parse_number(float(memory) / (1024 * 1024))
    except ValueError:
        return None


print(f"1 cpu --> {cpu_to_milli_cpu('1')}")
print(f"10 cpu --> {cpu_to_milli_cpu('10')}")
print(f"0.5 cpu --> {cpu_to_milli_cpu('0.5')}")
print(f"0.5m cpu --> {cpu_to_milli_cpu('0.5m')}")
print(f"0.05m cpu --> {cpu_to_milli_cpu('0.05m')}")
print(f"0.005m cpu --> {cpu_to_milli_cpu('0.005m')}")
print(f"0.005 cpu --> {cpu_to_milli_cpu('0.005')}")
print(f"500m cpu --> {cpu_to_milli_cpu('500m')}")


print(f"1024Mi memory --> {memory_to_mb('1024Mi')}")
print(f"1024Ki memory --> {memory_to_mb('1024Ki')}")
print(f"1Gi memory --> {memory_to_mb('1Gi')}")
print(f"0.5Gi memory --> {memory_to_mb('0.5Gi')}")
print(f"5000Ki memory --> {memory_to_mb('5000Ki')}")
print(f"0.5Ti memory --> {memory_to_mb('0.5Ti')}")