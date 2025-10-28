# simple billing engine: computes cost from OpenAI usage dict
from typing import Dict


class BillingEngine:
def __init__(self, rate_per_token_input: float=0.000002, rate_per_token_output: float=0.00001):
self.rate_in = rate_per_token_input
self.rate_out = rate_per_token_output


def compute_cost(self, usage: Dict) -> float:
# usage is expected in OpenAI format: {'prompt_tokens': N, 'completion_tokens': M, 'total_tokens': P}
p = usage.get('prompt_tokens', 0)
c = usage.get('completion_tokens', 0)
return round(p * self.rate_in + c * self.rate_out, 8)
