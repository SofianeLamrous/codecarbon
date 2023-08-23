from prometheus_client import CollectorRegistry, Gauge

registry = CollectorRegistry()

# TODO: add labelnames
# timestamp: str
# run_id: str
# python_version: str
# longitude: float
# latitude: float
# on_cloud: str = "N"

# TODO: Set up the possible labels
labelnames = [
    "project_name",
    "country_name",
    "country_iso_code",
    "region",
    "cloud_provider",
    "cloud_region",
    "os",
    "codecarbon_version",
    "cpu_model",
    "cpu_count",
    "gpu_model",
    "gpu_count",
    "tracking_mode",
    "ram_total_size",
]

labelnames2 = ["project_name"]

duration_gauge = Gauge(
    "codecarbon_duration",
    "Duration from last measure (s)",
    labelnames=labelnames2,
    registry=registry,
)
emissions_gauge = Gauge(
    "codecarbon_emissions",
    "Emissions as CO₂-equivalents [CO₂eq] (kg)",
    labelnames=labelnames2,
    registry=registry,
)
emissions_rate_gauge = Gauge(
    "codecarbon_emissions_rate",
    "Emissions divided per duration (Kg/s)",
    labelnames=labelnames2,
    registry=registry,

)
cpu_power_gauge = Gauge(
    "codecarbon_cpu_power",
    "CPU power (W)",
    labelnames=labelnames2,
    registry=registry,
)
gpu_power_gauge = Gauge(
    "codecarbon_gpu_power",
    "GPU power (W)",
    labelnames=labelnames2,
    registry=registry,
)
ram_power_gauge = Gauge(
    "codecarbon_ram_power",
    "RAM power (W)",
    labelnames=labelnames2,
    registry=registry,
)
cpu_energy_gauge = Gauge(
    "codecarbon_cpu_energy",
    "Energy used per CPU (kWh)",
    labelnames=labelnames2,
    registry=registry,
)
gpu_energy_gauge = Gauge(
    "codecarbon_gpu_energy",
    "Energy used per GPU (kWh)",
    labelnames=labelnames2,
    registry=registry,
)
ram_energy_gauge = Gauge(
    "codecarbon_ram_energy",
    "Energy used per RAM (kWh)",
    labelnames=labelnames2,
    registry=registry,
)
energy_consumed_gauge = Gauge(
    "codecarbon_energy_consumed",
    "Sum of cpu_energy, gpu_energy and ram_energy (kW)",
    labelnames=labelnames2,
    registry=registry,
)
