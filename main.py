import subprocess

result = subprocess.check_output(
    [
        "nvidia-smi",
        "--query-gpu=name,temperature.gpu,utilization.gpu,memory.used,memory.total",
        "--format=csv,noheader,nounits"
    ]
)

print("GPU STATUS")
print(result.decode())
