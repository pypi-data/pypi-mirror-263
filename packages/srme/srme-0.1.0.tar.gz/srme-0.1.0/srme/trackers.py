import typing as t

import srme.metrics as m
from srme.core import MetricCollector, Tracker
from srme.savers.csv_tracker import CSVSaver


def _get_basic_collector() -> MetricCollector:
    collector = MetricCollector()
    collector.register("cpu_usage_percent", m.get_cpu_percent)
    collector.register("vm_percent", m.get_vm_percent)
    collector.register("disk_left_percent", m.get_disk_usage_percent)
    return collector


class CSVLogger(Tracker):
    def __init__(
        self,
        save_path: str = "srme_metrics.csv",
        collector: t.Optional[MetricCollector] = None,
        save_freq: int = 1,
    ) -> None:
        if not collector:
            collector = _get_basic_collector()

        saver = CSVSaver(save_path)
        super().__init__(collector, saver, save_freq)


class MlFlowLogger(Tracker):
    def __init__(self, collector: t.Optional[MetricCollector], save_freq: int = 1) -> None:
        from srme.savers.mlflow_saver import MlFlowSaver

        mlflow_saver = MlFlowSaver()

        if not collector:
            collector = _get_basic_collector()

        super().__init__(collector, mlflow_saver, save_freq)
