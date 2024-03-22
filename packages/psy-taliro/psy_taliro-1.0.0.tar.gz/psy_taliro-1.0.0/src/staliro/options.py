"""
Definitions for the options that can be used to customize the testing behavior.

Behavior customization is accomplished through the `TestObject` class, which must
be provided as an argument to either the `staliro` or `setup` functions.

Examples
--------

.. code-block:: python

    import staliro

    options = staliro.TestOptions(
        runs = 10,
        iterations = 450,
        static_inputs={
            "speed": (0, 100),
            "fuel": [0, 255],
        },
    )
"""

from __future__ import annotations

import random
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal

from attrs import Attribute, converters, define, field, validators
from typing_extensions import TypeAlias

from .signals import Interval, IntervalLike, SignalInput, _to_interval

if TYPE_CHECKING:
    AnyAttr: TypeAlias = Attribute[Any]


def _seed_factory() -> int:
    return random.randint(0, 2**32 - 1)


def _to_static_inputs(inputs: Mapping[str, IntervalLike]) -> dict[str, Interval]:
    return {name: _to_interval(interval) for name, interval in inputs.items()}


def _to_signals(signals: Mapping[str, SignalInput]) -> dict[str, SignalInput]:
    return dict(signals)


def _parallelization(_: Any, a: AnyAttr, value: Literal["cores"] | int | None) -> None:
    if value is None:
        return

    if isinstance(value, int) and value < 1:
        raise ValueError(f"{a.name} must be greater than 0")

    if isinstance(value, str) and value != "cores":
        raise ValueError(f"{a.name} only supports literal option 'cores'")


@define(kw_only=True)
class TestOptions:
    """General options for controlling falsification behavior.

    :param tspan: The time interval for testing
    :param static_inputs: Parameters that will be provided to the system at the beginning and are time invariant (initial conditions).
    :param signals: System inputs that will vary over time
    :param seed: The initial seed of the random number generator
    :param iterations: The number of search iterations to perform in a run
    :param runs: The number times to run the optimizer
    :param processes: Number of processes to use to parallelize sample evaluation
    :param threads: Number of threads to use to parallelize sample evaluation
    """

    tspan: Interval | None = field(
        default=None,
        converter=converters.optional(_to_interval),
    )

    static_inputs: dict[str, Interval] = field(
        factory=dict,
        converter=_to_static_inputs,
    )

    signals: dict[str, SignalInput] = field(
        factory=dict,
        converter=_to_signals,
    )

    runs: int = field(
        default=1,
        validator=[validators.instance_of(int), validators.gt(0)],
    )

    iterations: int = field(
        default=400,
        validator=[validators.instance_of(int), validators.gt(0)],
    )

    seed: int = field(
        factory=_seed_factory,
        validator=[validators.instance_of(int), validators.gt(0)],
    )

    processes: Literal["cores"] | int | None = field(
        default=None,
        validator=_parallelization,
    )

    threads: Literal["cores"] | int | None = field(
        default=None,
        validator=_parallelization,
    )

    @tspan.validator
    def _tspan(self, _: AnyAttr, tspan: Interval) -> None:
        if tspan and tspan[0] >= tspan[1]:
            raise ValueError("Interval lower bound must be less than upper bound")

    @static_inputs.validator
    def _static_inputs(self, _: AnyAttr, inputs: dict[str, Interval]) -> None:
        for interval in inputs.values():
            if interval[0] >= interval[1]:
                raise ValueError("Interval lower bound must be less than upper bound")

    @signals.validator
    def _signals(self, _: AnyAttr, signals: dict[str, SignalInput]) -> None:
        for signal in signals.values():
            if not isinstance(signal, SignalInput):
                raise TypeError("Signal inputs must be values of type SignalInput")
