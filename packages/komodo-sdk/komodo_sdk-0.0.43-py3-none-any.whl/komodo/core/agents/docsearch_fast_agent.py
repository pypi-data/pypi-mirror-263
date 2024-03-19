import json

from komodo.core.utils.indexer import Indexer
from komodo.core.utils.rag_context import RagContext
from komodo.framework.komodo_agent import KomodoAgent
from komodo.framework.komodo_context import KomodoContext
from komodo.models.framework.agent_runner import AgentRunner


class DocSearchFastAgent(KomodoAgent):
    shortcode = "docsearchfast"
    name = "Document Search Agent"
    purpose = "Answer questions based on documents provided."
    instructions = "You are a Document QnA Agent. You will be given vector search results and a question. " \
                   "You must answer the question based on the provided data. " \
                   "Do not use any external sources."

    def __init__(self, shortcode, rc: RagContext):
        super().__init__(shortcode=shortcode,
                         name=self.name + f" ({rc.basename()})",
                         purpose=self.purpose,
                         instructions=self.instructions)
        self.rag_context = rc

    def generate_context(self, prompt=None):
        result = self.rag_context.search(prompt)
        context = KomodoContext()
        context.extend(super().generate_context(prompt))
        context.add("Vector Search Results", json.dumps(result) if len(result) > 0 else "No results found.")
        return context

    @classmethod
    def create(cls, rc: RagContext):
        shortcode = cls.shortcode + "_" + rc.collection_name if rc.collection_name != 'default' else cls.shortcode
        return cls(shortcode, rc)

    def index(self, reindex=False):
        indexer = Indexer(self.rag_context)
        indexer.run(reindex=reindex)


def run_search():
    agent = DocSearchFastAgent.create(RagContext(path="./data/test1"))
    agent.index()
    runner = AgentRunner(agent)
    response = runner.run("What did the G20 leaders agreed in 2009?")
    print(response.text)

    response = runner.run("tell me more about unique swap identifiers (USI) of each clearing swap?")
    print(response.text)


if __name__ == "__main__":
    run_search()
