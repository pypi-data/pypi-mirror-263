import threading
import time
import abc
from typing import Callable

METRIC_T = dict[str, float]


class MetricCollector:
    def __init__(self) -> None:
        self.collectors = {}

    def register(self, metric_name: str, metric_fn: Callable[..., float]) -> None:
        if metric_name in self.collectors:
            raise ValueError(f"metric name: <{metric_name}> already registered")
        self.collectors[metric_name] = metric_fn

    def __call__(self) -> METRIC_T:
        result = {}
        for metric_name, metric_fn in self.collectors.items():
            result[metric_name] = metric_fn()
        return result


class MetricsSaver(abc.ABC):
    @abc.abstractmethod
    def __call__(self, metrics: METRIC_T, step: int) -> None: ...


def run_track_task(
    event: threading.Event,
    collector: MetricCollector,
    saver: MetricsSaver,
    freq: int = 30,
) -> None:
    step = 0
    event.wait()
    while event.is_set():
        metrics = collector()
        saver(metrics, step)

        # step in time
        time.sleep(freq)
        step += 1


class Tracker(abc.ABC):
    def __init__(
        self,
        collector: MetricCollector,
        saver: MetricsSaver,
        save_freq: int = 1,
    ) -> None:
        self.track_event = threading.Event()

        # it could be better to capture sigint
        # to properly join the thread.
        self.track_thread = threading.Thread(
            target=run_track_task, args=(self.track_event, collector, saver, save_freq), daemon=True
        )
        self.track_thread.start()
        self.start()

    def start(self) -> None:
        if not self.track_event.is_set():
            self.track_event.set()

    def end(self) -> None:
        self.track_event.clear()
