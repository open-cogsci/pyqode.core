# -*- coding: utf-8 -*-
"""
This module contains the spell checker mode
"""
from pyqode.core.modes import CheckerMode


def run_spellcheck(request_data):

    import re
    import spellchecker

    sc = spellchecker.SpellChecker(request_data.get('ignore_rules', 'en'))
    WARNING = 1
    messages = []
    code = request_data['code']
    for group in re.finditer(r'\w\w(\w+)', code):
        word = code[group.start():group.end()]
        if sc.unknown([word]):
            messages.append((
                '[spellcheck] {}'.format(word),
                WARNING,
                0,
                (group.start(), group.end())
            ))
    return messages


class SpellCheckerMode(CheckerMode):

    def __init__(self):
        super(SpellCheckerMode, self).__init__(
            run_spellcheck,
            delay=1000,
            show_tooltip=False
        )
