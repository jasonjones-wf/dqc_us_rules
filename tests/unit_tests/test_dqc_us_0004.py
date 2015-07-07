import unittest
from datetime import datetime, timedelta
from src.dqc_us_0004 import _assets_eq_liability_equity, _ASSETS_CONCEPT, _LIABILITIES_CONCEPT
from mock import Mock


class TestAssetsEqLiabilityEquity(unittest.TestCase):

    def test_bv_errors(self):
        asset_concept = Mock()
        asset_concept.qname = _ASSETS_CONCEPT
        liabilities_concept = Mock()
        liabilities_concept.qname = _LIABILITIES_CONCEPT

        mock_context = Mock(instantDatetime=datetime(2013, 12, 22, 11, 30, 59))

        asset_fact = Mock(contextID='valid', context=mock_context, unitID='unit1', isNil=False, xValid=True, xValue=1)
        liabilities_fact = Mock(contextID='valid', context=mock_context, unitID='unit1', isNil=False, xValid=True, xValue=2)

        mock_name_concepts_dict = {
            _ASSETS_CONCEPT: [asset_concept],
            _LIABILITIES_CONCEPT: [liabilities_concept]
        }

        mock_facts_by_qname = {
            asset_concept.qname: [asset_fact],
            liabilities_concept.qname: [liabilities_fact]
        }

        modelXbrl = Mock()
        modelXbrl.nameConcepts = mock_name_concepts_dict
        modelXbrl.factsByQname = mock_facts_by_qname

        error_count = 0
        for asset, liability, date in _assets_eq_liability_equity(modelXbrl):
            error_count += 1
            self.assertEqual(asset, asset_fact)
            self.assertEqual(liability, liabilities_fact)
            self.assertEqual(date, datetime(2013, 12, 22, 11, 30, 59) - timedelta(days=1))

        self.assertEqual(error_count, 1)

        mock_name_concepts_dict_no_liability = {
            _ASSETS_CONCEPT: [asset_concept],
            _LIABILITIES_CONCEPT: []
        }
        modelXbrl.nameConcepts = mock_name_concepts_dict_no_liability

        error_count = 0
        for asset, liability, date in _assets_eq_liability_equity(modelXbrl):
            error_count += 1
        self.assertEqual(error_count, 0)

    def test_bv_no_errors_duration(self):
        asset_concept = Mock()
        asset_concept.qname = _ASSETS_CONCEPT
        liabilities_concept = Mock()
        liabilities_concept.qname = _LIABILITIES_CONCEPT

        mock_context = Mock(instantDatetime=None)

        asset_fact = Mock(contextID='valid', context=mock_context, unitID='unit1', isNil=False, xValid=True, xValue=1)
        liabilities_fact = Mock(contextID='valid', context=mock_context, unitID='unit1', isNil=False, xValid=True, xValue=2)

        mock_name_concepts_dict = {
            _ASSETS_CONCEPT: [asset_concept],
            _LIABILITIES_CONCEPT: [liabilities_concept]
        }

        mock_facts_by_qname = {
            asset_concept.qname: [asset_fact],
            liabilities_concept.qname: [liabilities_fact]
        }

        modelXbrl = Mock()
        modelXbrl.nameConcepts = mock_name_concepts_dict
        modelXbrl.factsByQname = mock_facts_by_qname

        error_count = 0
        for asset, liability, date in _assets_eq_liability_equity(modelXbrl):
            error_count += 1
        self.assertEqual(error_count, 0)

    def test_bv_None_context(self):
        asset_concept = Mock()
        asset_concept.qname = _ASSETS_CONCEPT
        liabilities_concept = Mock()
        liabilities_concept.qname = _LIABILITIES_CONCEPT

        asset_fact = Mock(contextID='valid', context=None, unitID='unit1', isNil=False, xValid=True, xValue=1)
        liabilities_fact = Mock(contextID='valid', context=None, unitID='unit1', isNil=False, xValid=True, xValue=2)

        mock_name_concepts_dict = {
            _ASSETS_CONCEPT: [asset_concept],
            _LIABILITIES_CONCEPT: [liabilities_concept]
        }

        mock_facts_by_qname = {
            asset_concept.qname: [asset_fact],
            liabilities_concept.qname: [liabilities_fact]
        }

        modelXbrl = Mock()
        modelXbrl.nameConcepts = mock_name_concepts_dict
        modelXbrl.factsByQname = mock_facts_by_qname

        error_count = 0
        for asset, liability, date in _assets_eq_liability_equity(modelXbrl):
            error_count += 1
        self.assertEqual(error_count, 0)
