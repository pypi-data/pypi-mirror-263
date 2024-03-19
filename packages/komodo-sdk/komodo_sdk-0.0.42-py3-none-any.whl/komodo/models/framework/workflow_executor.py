from komodo.models.framework.agent_runner import AgentRunner

from komodo.models.framework.chat_message import ChatMessage


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
            for tag, content in self.context.data:
                message = ChatMessage.build(tag, content, role='system')
                message.add_tag('Workflow Context')
                data.append(message)

        for vertex in self.workflow.dag.predecessors(agent):
            key = vertex.shortcode
            content = self.outputs[key] if key in self.outputs else None
            if content:
                message = ChatMessage.build(key, content, role='assistant')
                message.add_tag('Workflow Agent Output')
                data.append(message)
        return data
