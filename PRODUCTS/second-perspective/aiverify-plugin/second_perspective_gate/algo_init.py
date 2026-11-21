# -*- coding: utf-8 -*-
"""algo_init.py — official v2 contract wiring (draft).

Per the aiverify-algorithm-template: this module constructs the algorithm
instance and passes ``input_arguments`` (values of the custom arguments declared
in ``input.schema.json``) into it. Final wiring happens when the scaffold is
generated through cookiecutter against the official template.
"""

input_arguments = {
    "require_anchor": False,
}
