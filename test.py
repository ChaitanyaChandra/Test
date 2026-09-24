from webhook.app.routers.requests_limits import cpu_to_milli_cpu
print(cpu_to_milli_cpu("1"))
print(cpu_to_milli_cpu("1m"))
print(cpu_to_milli_cpu(1))
