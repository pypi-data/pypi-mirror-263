from komodo.models.framework.agent_runner import AgentRunner
from komodo.models.framework.assistant import ModelRequest


class WorkflowExecutor:
    def __init__(self, workflow):
        self.workflow = workflow
        self.context = workflow.generate_context()
        self.outputs = {}

    def param(self, agent):
        return agent

    def execute(self, agent):
        runner = AgentRunner(agent)
        prompt = self.workflow.prompts[agent] if agent in self.workflow.prompts else ""
        data = self.inputs(agent)
        response = runner.run(prompt, history=data)
        self.outputs[agent.shortcode] = response.text
        return response

    def inputs(self, agent):
        data = []
        if self.context:
            data.append(ModelRequest.build_message('WORKFLOW', self.context))

        for vertex in self.workflow.dag.predecessors(agent):
            key = vertex.shortcode
            output = self.outputs[key] if key in self.outputs else None
            if output:
                data.append(ModelRequest.build_message(key, output, 'assistant'))

        return data

    def report_start(self, vertices):
        pass  # print('Start:', vertices)

    def report_running(self, vertices):
        pass  # print('Current running:', vertices)

    def report_finish(self, agents_result):
        pass
        # print('Finished:', agents_result)
        # for agent, result in agents_result:
        # prompt = self.workflow.prompts[agent] if agent in self.workflow.prompts else ""
        # print('{}\nPrompt: {}\nResponse: {}\n-------------'.format(agent, prompt, result.text))

    def deliver(self, vertex, result):
        pass  # print('Deliver:', vertex, result)
