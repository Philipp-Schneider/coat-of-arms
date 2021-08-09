from unittest import TestCase
from src.label_checker_automata import LabelCheckerAutomata

automata = LabelCheckerAutomata()
accepted_labels = {
    'O G lion rampant': 'ccom',
    'A G lion rampant': 'ccom',
    'G A fess dancetty': 'ccom',
    'O X GB fess checky': 'ccccom',
    'G AGG chief': 'cccco'
}

rejected_labels = {
    '3 pales; 2 cows; =; = :: label   {OG, OG, B}': '',
    'A G': 'cc',
    'fess G': 'oc'
}

class LabelCheckerAutomataTest(TestCase):
    def test_is_valid_passes(self):
        for label, parsed_label in accepted_labels.items():
            self.assertTrue(automata.is_valid(label))

    def test_is_valid_fails(self):
        for label, parsed_label in rejected_labels.items():
            self.assertFalse(automata.is_valid(label))

    def test_parse_label(self):
        for label, parsed_label in accepted_labels.items():
            assert automata._parse_label(label) == parsed_label

        for label, parsed_label in rejected_labels.items():
            assert automata._parse_label(label) == parsed_label

    def test_is_combination_color(self):
        assert automata._is_combination_color('AA') == True
        assert automata._is_combination_color('AGO') == True
        assert automata._is_combination_color('&s') == False

    def test_get_combination_color(self):
        assert automata._get_combination_color('AA') == 'cc'
        assert automata._get_combination_color('AGO') == 'ccc'