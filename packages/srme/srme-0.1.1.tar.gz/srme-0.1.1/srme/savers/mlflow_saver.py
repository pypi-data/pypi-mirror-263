import mlflow

from srme.core import MetricsSaver


class MlFlowSaver(MetricsSaver):
    def __init__(self) -> None:
        super().__init__()

    def __call__(self, metrics: dict[str, float], step: int) -> None:
        mlflow.log_metrics(metrics, step=step)
