from datetime import datetime, timedelta

from hgraph import generator, TS, MIN_TD, graph, EvaluationClock, evaluate_graph, GraphConfiguration, EvaluationMode, \
    GraphRecorder
from hgraph.nodes import debug_print


@generator
def simple_replay(count: int, _clock: EvaluationClock = None) -> TS[datetime]:
    now_ = _clock.now
    for i in range(count):
        yield now_ + timedelta(milliseconds=10) * i, _clock.now


@graph
def simple_graph(count: int) -> TS[int]:
    ts = simple_replay(count)
    debug_print("time", ts)
    return ts


# def test_simple_graph():
#     config = GraphConfiguration(
#         run_mode=EvaluationMode.RECORDING,
#         start_time=(start_tm := datetime.utcnow()),
#         end_time=start_tm + timedelta(seconds=1),
#         recorder=...
#     )
#     v = evaluate_graph(simple_graph, config, count=5)
