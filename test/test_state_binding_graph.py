import pylage as ps
from pylage.ENGINE import Column, Heading, State
from pylage.ENGINE.core.binding import StateBinding
from pylage.ENGINE.core.graph import DependencyGraph


def test_state_binding_builds_dependency_graph():
    state = State(0)
    heading = Heading(text=state)
    app = Column(heading)

    graph = DependencyGraph()

    StateBinding(
        app,
        lambda component, props: None,
        graph=graph,
    )

    assert (heading, "text") in graph.get_dependents(state)
