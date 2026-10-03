from typing import List, Dict

from indicator_categories import get_indicator_category

from indicator_severity import get_indicator_severity

def format_indicators(
    indicators: List[Dict]
) -> List[Dict]:
    """
    Add a category to every validation/fraud indicator.
    """

    formatted_indicators = []

    for indicator in indicators:

        formatted_indicator = indicator.copy()

        indicator_type = formatted_indicator.get(
            "type",
            "UNKNOWN"
        )

        formatted_indicator["category"] = (
            get_indicator_category(indicator_type)
        )

        formatted_indicator["severity"] = (
            get_indicator_severity(indicator_type)
        )

        formatted_indicators.append(
            formatted_indicator
        )

    return formatted_indicators