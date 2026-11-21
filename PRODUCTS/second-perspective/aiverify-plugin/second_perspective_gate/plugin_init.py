# -*- coding: utf-8 -*-
"""plugin_init.py — official v2 contract wiring (draft).

Per the aiverify-algorithm-template: this module registers the CLI arguments
and builds the ``plugin_argument_values`` dictionary handed to ``algo_init.py``.
Final wiring happens when the scaffold is generated through cookiecutter
against the official template.
"""

CLI_ARGUMENTS = [
    {
        "name": "--require-anchor",
        "help": "Force BLOCK unless the responsibility anchor is ANCHORED",
        "type": bool,
        "default": False,
    },
]
