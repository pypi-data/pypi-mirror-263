from komodo.framework.komodo_agent import KomodoAgent
from komodo.framework.komodo_config import KomodoConfig
from komodo.framework.komodo_context import KomodoContext
from komodo.framework.komodo_features import KomodoFeatures, KomodoApplianceType, Komodo
from komodo.framework.komodo_tool import KomodoTool
from komodo.framework.komodo_tool_registry import KomodoToolRegistry
from komodo.framework.komodo_workflow import KomodoWorkflow


class KomodoApp:

    def __init__(self, shortcode, name, purpose, config=None, context=None, company=None, type=None, features=None):
        self.shortcode = shortcode
        self.name = name
        self.purpose = purpose
        self.agents: [KomodoAgent] = []
        self.tools: [KomodoTool] = []
        self.workflows: [KomodoWorkflow] = []
        self.config = config or KomodoConfig()
        self.context = context or KomodoContext()
        self.company = Komodo.company if company is None else company
        self.type = KomodoApplianceType.enterprise if type is None else type
        self.features = [e for e in KomodoFeatures] if features is None else features

    def add_agent(self, agent):
        self.agents += [agent]
        return self

    def add_tool(self, tool):
        self.tools.extend(KomodoToolRegistry.get_tools([tool]))
        return self

    def add_workflow(self, workflow):
        self.workflows += [workflow]
        return self

    def generate_context(self, prompt=None):
        return self.context

    def index(self, reindex=False):
        for agent in self.agents:
            agent.index(reindex=reindex)

    @staticmethod
    def default():
        return KomodoApp(name="Placeholder", shortcode="placeholder", purpose="Placeholder", config=KomodoConfig())
