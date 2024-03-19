from policyengine_us.model_api import *


class ctc_adult_individual_maximum(Variable):
    value_type = float
    entity = Person
    label = "CTC maximum amount (adult dependent)"
    unit = USD
    documentation = (
        "The CTC entitlement in respect of this person as an adult dependent."
    )
    definition_period = YEAR
    reference = (
        "https://www.law.cornell.edu/uscode/text/26/24#a",
        "https://www.law.cornell.edu/uscode/text/26/24#h",
        "https://www.law.cornell.edu/uscode/text/26/24#i",
    )

    def formula(person, period, parameters):
        ctc = parameters(period).gov.irs.credits.ctc
        is_dependent = person("is_tax_unit_dependent", period)
        is_child = person("ctc_child_individual_maximum", period) > 0
        is_adult_dependent = ~is_child & is_dependent
        return is_adult_dependent * ctc.amount.adult_dependent
