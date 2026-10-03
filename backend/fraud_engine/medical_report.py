from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class TestResult:
    name: str
    value: float
    reference_min: Optional[float] = None
    reference_max: Optional[float] = None
    unit: Optional[str] = None


@dataclass
class MedicalReport:
    report_number: str
    patient_id: str
    patient_name: str
    report_date: str
    doctor: str
    hospital: str
    diagnosis: str
    tests: List[TestResult] = field(default_factory=list)