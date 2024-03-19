import typing as t

import srme.metrics as m
from srme.core import MetricCollector, Tracker


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
        """
        Log resource usage into csv file.

        :param save_path: open in wa model, so keep the file clean, defaults to "srme_metrics.csv"
        :type save_path: str, optional
        :param collector: metrics collector class, defaults to None
        :type collector: t.Optional[MetricCollector], optional
        :param save_freq: frequency in second (sleep between writings), defaults to 1
        :type save_freq: int, optional
        """
        from srme.savers.csv_saver import CSVSaver

        if not collector:
            collector = _get_basic_collector()

        saver = CSVSaver(save_path)
        super().__init__(collector, saver, save_freq)


class MlFlowLogger(Tracker):
    def __init__(self, collector: t.Optional[MetricCollector] = None, save_freq: int = 1) -> None:
        """
        Track system resource usage to MLFlow.

        :param collector: metrics collector class, defaults to None
        :type collector: t.Optional[MetricCollector], optional
        :param save_freq: frequency in second (sleep between writings), defaults to 1
        :type save_freq: int, optional
        """
        from srme.savers.mlflow_saver import MlFlowSaver

        mlflow_saver = MlFlowSaver()

        if not collector:
            collector = _get_basic_collector()

        super().__init__(collector, mlflow_saver, save_freq)
