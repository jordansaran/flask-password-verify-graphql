""""
Dataclasses API
"""
from dataclasses import dataclass, field

from constants import ConstVerify


@dataclass
class DcRule:

    rule: str
    value: int


@dataclass
class DcVerification:

    password: str
    rules: list[DcRule] = field(default_factory=list)

    def __init__(self, password: str = None, rules: list = None):
        self.password = password
        self.__set_list_rules(rules)

    def __set_list_rules(self, rules: list = None):
        self.rules = []
        for rule in rules:
            self.rules.append(
                DcRule(rule.get(ConstVerify.RULE), rule.get(ConstVerify.VALUE))
            )
