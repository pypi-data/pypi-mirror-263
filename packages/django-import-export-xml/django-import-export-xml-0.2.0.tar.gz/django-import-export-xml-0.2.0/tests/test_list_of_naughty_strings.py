import json
from io import BytesIO
from pathlib import Path
from xml.etree.cElementTree import parse

import pytest

from import_export_xml.formats import XML
from testapp.models import StringModel, StringResource


def known_fail(s: str):
    # dicttoxml has 0 tests...
    return any(
        unhandled in s
        for unhandled in [
            "\ufffe",
            "\x07",
            "\x0b",
            "\x1b",
        ]
    )


with (Path(__file__).parent / "blns.json").open("rb") as f:
    BLNS = json.load(f)


@pytest.mark.parametrize("naughty_string", BLNS)
def test_naughty_strings(db, naughty_string):
    if known_fail(naughty_string):
        pytest.xfail(f"dicttoxml issue with {naughty_string}")

    format = XML()
    StringModel.objects.create(chars=naughty_string, text=naughty_string)
    dataset = StringResource().export(queryset=StringModel.objects.all())

    xml_content = format.export_data(dataset)
    assert isinstance(xml_content, bytes)

    tree = parse(BytesIO(initial_bytes=xml_content))
    item_el, *unexpected_els = tree.findall("item")
    assert not unexpected_els
    chars_el, *unexpected_els = item_el.findall("chars")
    assert not unexpected_els
    text_el, *unexpected_els = item_el.findall("text")
    assert not unexpected_els

    # dict2xml turns "" into an empty element, but etree parser el.text of empty
    # element is None
    assert chars_el.text == (naughty_string if naughty_string else None)
    assert text_el.text == (naughty_string if naughty_string else None)
