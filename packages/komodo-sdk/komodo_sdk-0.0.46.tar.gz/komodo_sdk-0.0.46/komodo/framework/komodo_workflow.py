from paradag import DAG

from komodo.framework.komodo_context import KomodoContext


class KomodoWorkflow:
    def __init__(self, context=None):
        self.dag = DAG()
        self.prompts = {}
        self.context = context or KomodoContext()

    def add_node(self, agent, prompt):
        if agent in self.prompts:
            raise ValueError(f"Agent {agent} already exists in workflow. Cannot add it again.")
        self.dag.add_vertex(agent)
        self.prompts[agent] = prompt

    def add_edge(self, agent_from, agent_to):
        self.dag.add_edge(agent_from, agent_to)

    def generate_context(self, prompt=None):
        return self.context
