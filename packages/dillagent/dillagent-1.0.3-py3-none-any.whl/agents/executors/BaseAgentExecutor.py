from abc import ABC, abstractmethod
from src.tools.Tool import Tool
from typing import List
from src.agents.agents.BaseAgent import BaseAgent
from src.dependencies.parsers.intermediate.IntermediateParser import IntermediateParser


class BaseAgentExecutor(ABC):
    def __init__(self, agent: BaseAgent, intermediate_parser: IntermediateParser):
        self.agent = agent
        self.im_parser = intermediate_parser

    @abstractmethod
    def run(self, prompt):
        pass
