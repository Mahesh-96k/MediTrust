from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class AnalysisResult:
    """
    Structured result produced by the validation
    and fraud-detection engine.
    """

    indicators: List[Dict] = field(default_factory=list)

    @property
    def total_indicators(self) -> int:
        return len(self.indicators)

    @property
    def has_issues(self) -> bool:
        return self.total_indicators > 0

    def summary(self) -> str:
        if not self.indicators:
            return "No validation or fraud indicators found."

        return (
            f"{self.total_indicators} "
            "validation/fraud indicator(s) found."
        )