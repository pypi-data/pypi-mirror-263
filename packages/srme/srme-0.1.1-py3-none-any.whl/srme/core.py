import threading
import time
import abc
from typing import Callable

METRIC_T = dict[str, float]


class MetricCollector:
    """
    Class responsible for registering and collecting metrics.
    """

    def __init__(self) -> None:
        self.collectors = {}

    def register(self, metric_name: str, metric_fn: Callable[..., float]) -> None:
        """
        Register a metric function with a given name.

        :param metric_name: The name of the metric.
        :type metric_name: str
        :param metric_fn: The function to compute the metric.
        :type metric_fn: Callable[..., float]
        :raises ValueError: If metric_name is already registered.
        """
        if metric_name in self.collectors:
            raise ValueError(f"metric name: <{metric_name}> already registered")
        self.collectors[metric_name] = metric_fn

    def __call__(self) -> METRIC_T:
        """Call method to collect metrics.

        :return: A dictionary containing metric names and their values.
        :rtype: METRIC_T
        """
        result = {}
        for metric_name, metric_fn in self.collectors.items():
            result[metric_name] = metric_fn()
        return result


class MetricsSaver(abc.ABC):
    @abc.abstractmethod
    def __call__(self, metrics: METRIC_T, step: int) -> None:
        """Abstract method for saving metrics.

        :param metrics: A dictionary containing metric names and their values.
        :type metrics: METRIC_T
        :param step: The step at which metrics are collected.
        :type step: int
        """
        ...


def run_track_task(
    event: threading.Event,
    collector: MetricCollector,
    saver: MetricsSaver,
    freq: int = 1,
) -> None:
    """Function to run a tracking task.

    :param event: Event for tracking task control.
    :type event: threading.Event
    :param collector: Metric collector instance.
    :type collector: MetricCollector
    :param saver: Metrics saver instance.
    :type saver: MetricsSaver
    :param freq: Frequency of metric collection in seconds, defaults to 1
    :type freq: int, optional
    """
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
        """Initialize Tracker instance.

        :param collector: Metric collector instance.
        :type collector: MetricCollector
        :param saver: Metrics saver instance.
        :type saver: MetricsSaver
        :param save_freq: Frequency of saving metrics., defaults to 1
        :type save_freq: int, optional
        """
        self.track_event = threading.Event()

        # it could be better to capture sigint
        # to properly join the thread.
        self.track_thread = threading.Thread(
            target=run_track_task, args=(self.track_event, collector, saver, save_freq), daemon=True
        )
        self.track_thread.start()
        self.start()

    def start(self) -> None:
        """Start tracking. You don't need to call is explicitly."""
        if not self.track_event.is_set():
            self.track_event.set()

    def end(self) -> None:
        """End tracking."""
        self.track_event.clear()
