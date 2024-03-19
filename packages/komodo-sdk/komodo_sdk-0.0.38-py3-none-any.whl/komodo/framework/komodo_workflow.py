from paradag import DAG


class KomodoWorkflow:
    def __init__(self):
        self.dag = DAG()
        self.prompts = {}

    def add_node(self, agent, prompt):
        if agent in self.prompts:
            raise ValueError(f"Agent {agent} already exists in workflow. Cannot add it again.")
        self.dag.add_vertex(agent)
        self.prompts[agent] = prompt

    def add_edge(self, agent_from, agent_to):
        self.dag.add_edge(agent_from, agent_to)

    def generate_context(self):
        return None
