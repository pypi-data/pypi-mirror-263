import csv
import os

from srme.core import MetricsSaver


class CSVSaver(MetricsSaver):
    def __init__(self, save_path: str) -> None:
        super().__init__()
        self.save_path = save_path

    def __call__(self, metrics: dict[str, float], step: int) -> None:
        names = ["step"] + list(metrics.keys())

        # check if header already exists.
        # assume writing logs into same file
        has_header = False
        if os.path.exists(self.save_path):
            with open(self.save_path, "r") as csv_file:
                sniffer = csv.Sniffer()
                has_header = sniffer.has_header(csv_file.read(2048))

        with open(self.save_path, "a+") as csv_file:
            writer = csv.DictWriter(
                csv_file,
                fieldnames=names,
                delimiter=",",
                quotechar="|",
                quoting=csv.QUOTE_MINIMAL,
            )
            if not has_header:
                writer.writeheader()
            writer.writerow(metrics | {"step": step})
