from paradag import dag_run, SequentialProcessor, MultiThreadProcessor

from komodo.core.agents.groot_agent import GrootAgent
from komodo.core.agents.summarizer_agent import SummarizerAgent
from komodo.core.agents.translator_agent import TranslatorAgent
from komodo.framework.komodo_workflow import KomodoWorkflow
from komodo.models.framework.workflow_executor import WorkflowExecutor
from komodo.models.framework.workflow_selector import WorkflowSelector


class WorkflowRunner:
    def __init__(self, workflow, parallel=False, max_workers=4):
        self.workflow = workflow
        self.parallel = parallel
        self.max_workers = max_workers

    def run(self):
        processor = SequentialProcessor() if not self.parallel else MultiThreadProcessor()
        selector = WorkflowSelector(max_workers=self.max_workers)
        executor = WorkflowExecutor(self.workflow)

        processed = dag_run(self.workflow.dag, processor=processor, executor=executor, selector=selector)
        return {agent: executor.outputs[agent.shortcode] for agent in processed}


if __name__ == "__main__":
    workflow = KomodoWorkflow()
    groot = GrootAgent()
    summarizer = SummarizerAgent()
    translator_french = TranslatorAgent("French")
    translator_spanish = TranslatorAgent("Spanish")

    workflow.add_node(groot, "Who are you?")
    workflow.add_node(summarizer, "Summarize the Iliad")
    workflow.add_node(translator_french, "Translate to French")
    workflow.add_node(translator_spanish, "Translate to Spanish")

    workflow.add_edge(summarizer, translator_french)
    workflow.add_edge(summarizer, translator_spanish)

    runner = WorkflowRunner(workflow, parallel=True, max_workers=4)
    results = runner.run()
    for k, v in results.items():
        print(f'{k.name} ({k.shortcode}): {v}')
