# -*- coding: utf-8 -*-
"""
This module contains the spell checker mode
"""
from pyqode.core.modes import CheckerMode


WARNING = 1
# Matches all words of at least three characters that are preceded whitespace
# or opening brackets
WORD_PATTERN = r'[\s\[\(\{](?P<word>\w\w(\w+))'


def run_spellcheck(request_data):

    import re
    import spellchecker

    sc = spellchecker.SpellChecker(request_data.get('ignore_rules', 'en'))
    messages = []
    code = request_data['code']
    for group in re.finditer(WORD_PATTERN, code):
        word = group.group('word')
        if sc.unknown([word]):
            messages.append((
                '[spellcheck] {}'.format(word),
                WARNING,
                0,
                (group.end() - len(word), group.end())
            ))
    return messages


class SpellCheckerMode(CheckerMode):

    def __init__(self):
        super(SpellCheckerMode, self).__init__(
            run_spellcheck,
            delay=1000,
            show_tooltip=False
        )
