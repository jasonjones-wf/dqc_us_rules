from .util import facts, messages
from collections import defaultdict
from datetime import timedelta

_CODE_NAME_33 = 'DQC.US.0033'
_CODE_NAME_36 = 'DQC.US.0036'
_RULE_VERSION = '1.0'


def doc_period_end_date_check(val):
    results = _doc_period_end_date_check(val.modelXbrl)
    for warn_list in results.get('warning', []):
        code, context_date, mod_obj, default_dped_fact = warn_list
        val.modelXbrl.error(code, messages.get_message("36"),
                            dped_context_date=context_date,
                            modelObject=(mod_obj, default_dped_fact),
                            ruleVersion=_RULE_VERSION)
    for err_list in results.get('error', []):
        code, fact_label, mod_obj, default_dped_fact = err_list
        val.modelXbrl.error(code, messages.get_message("33"),
                            dei_fact_label=fact_label,
                            modelObject=(mod_obj, default_dped_fact),
                            ruleVersion=_RULE_VERSION)


def _doc_period_end_date_check(modelXbrl):
    """
    Compares the value of DocumentPeriodEndDate against the end date of its context. If the
    difference is more than 3 days, fires a validation error.
    For each DocumentPeriodEndDate, if the above check doesn't fire, check all DEI fact context end dates against it.
    """
    dped_facts, dei_facts = _setup_dei_facts(modelXbrl)
    default_dped_fact = _get_default_dped(dped_facts)
    result_group = defaultdict(list)
    if default_dped_fact is None:
        return result_group

    # loop through the DocumentPeriodEndDate's to check for consistant dates
    for eop_facts in dped_facts.values():
        eop_fact = eop_facts[0]
        eop_context = eop_fact.context
        if eop_context is None or eop_context.endDatetime is None:
            continue
        fact_eop_date = eop_fact.xValue.date()
        # Arelle adjusts context end date to end-of-day midnight
        # Reverse the adjustment to get the expected date value by subtracting one day
        context_eop_date = eop_context.endDatetime.date() - timedelta(days=1)
        delta = context_eop_date - fact_eop_date
        if abs(delta.days) > 3:
            result_group['warning'].append((_CODE_NAME_36, context_eop_date, eop_fact, default_dped_fact))

    # loop through the dei facts and compare against their LEA's DocumentPeriodEndDate
    for lea_key, fact_group in dei_facts.items():
        eop_fact = dped_facts.get(lea_key, default_dped_fact)[0]
        if eop_fact is None or eop_fact.context is None or eop_fact.context.endDatetime is None:
            continue
        fact_eop_date = eop_fact.xValue.date()
        # Arelle adjusts context end date to end-of-day midnight
        # Reverse the adjustment to get the expected date value by subtracting one day
        context_eop_date = eop_fact.context.endDatetime.date() - timedelta(days=1)
        if len(fact_group) > 0:
            #check all DEI facts against this DocumentPeriodEndDate.  If the DocumentPeriodEndDate context check doesn't fire, we will check all dei fact context end dates against it.
            for fact in fact_group:
                if fact.context is None or fact.context.endDatetime is None or fact.concept.periodType != 'duration':
                    continue

                if context_eop_date != fact.context.endDatetime.date() - timedelta(days=1):
                    result_group['error'].append((_CODE_NAME_33, fact.concept.label(), fact, default_dped_fact))
    return result_group


def _setup_dei_facts(modelXbrl):
    """
    return a tuple of the dictionary of a list of 1 DocumentPeriodEndDate per LegalEntityAxis and
    the dictionary of the list of dei facts per LegalEntityAxis
    """
    ignored_fact_list = ['EntityCommonStockSharesOutstanding', 'EntityPublicFloat', 'DocumentPeriodEndDate']
    dei_facts = facts.LegalEntityAxis_facts_by_member(_get_dei_facts(modelXbrl, ignored_fact_list))
    dped_facts = facts.LegalEntityAxis_facts_by_member(facts.get_facts_dei(['DocumentPeriodEndDate'], modelXbrl))
    return dped_facts, dei_facts


def _get_dei_facts(modelXbrl, exclude_list=[None]):
    """
    Returns a list of all the modelXbrl's DEI facts that aren't in the exclude_list; this can be fed into prepare_facts_for_calculation.
    """
    return [f for f in modelXbrl.facts if f.namespaceURI in facts.DEI_NAMESPACE_LIST and f.qname.localName not in exclude_list]


def _get_default_dped(dped_facts):
    """
    returns the default DocumentPeriodEndDate fact or None if there are no DocumentPeriodEndDate facts
    and a list of None if it doesn't exist or can't be figured out.
    """
    keys = dped_facts.keys()
    if len(keys) == 0:
        return None
    elif len(keys) == 1:
        return [f for f in dped_facts.values()]
    else:
        return dped_facts.get('', [None])

__pluginInfo__ = {
    'name': '{}, {}'.format(_CODE_NAME_33, _CODE_NAME_36),
    'version': _RULE_VERSION,
    'description': '''Checks the doc period end date relative to fact contexts.''',
    'license': 'Apache-2',
    'author': 'Brian Myers',
    'copyright': '(c) Workiva, 2015',
    #Mount points
    'Validate.XBRL.Finally': doc_period_end_date_check,
}
