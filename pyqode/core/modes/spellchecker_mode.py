# -*- coding: utf-8 -*-
"""
This module contains the spell checker mode
"""
from pyqode.qt import QtWidgets
from pyqode.core.modes import CheckerMode


WARNING = 1
WORD_PATTERN = r'(?P<word>\w\w\w+)'


def run_spellcheck(request_data):

    import re
    import spellchecker
    import string

    sc = spellchecker.SpellChecker(request_data.get('language', 'en'))
    ignore = request_data.get('ignore', [])
    messages = []
    code = request_data['code']    
    for group in re.finditer(WORD_PATTERN, code):
        # Strip off starting and trailing underscores. This could probably
        # be included in the regular expression, but this is easier.
        word = group.group('word')
        end = group.end()
        if word.startswith('__'):
            word = word[2:]
        if word.endswith('__'):
            word = word[:-2]
            end -= 2
        # Ignore words that start with a digit, that are in the ignore list, or
        # that are part of the dictionary
        if (
            word[0] in string.digits or
            word in ignore or
            not sc.unknown([word])
        ):
            continue
        messages.append((
            '[spellcheck] {}'.format(word),
            WARNING,
            0,
            (end - len(word), end)
        ))
    return messages


class SpellCheckerMode(CheckerMode):

    def __init__(self):
        
        super(SpellCheckerMode, self).__init__(
            run_spellcheck,
            delay=1000,
            show_tooltip=False
        )
