import json
from pathlib import Path

from pymultirole_plugins.v1.schema import Document
from pyprocessors_categories_from_annotations.categories_from_annotations import CategoriesFromAnnotationsProcessor, \
    CategoriesFromAnnotationsParameters


def test_model():
    model = CategoriesFromAnnotationsProcessor.get_model()
    model_class = model.construct().__class__
    assert model_class == CategoriesFromAnnotationsParameters


def test_categories_from_annotations():
    testdir = Path(__file__).parent
    source = Path(testdir, "data/response_1622736571452.json")

    with source.open("r") as fin:
        jdocs = json.load(fin)
    docs = [Document(**jdoc) for jdoc in jdocs]
    processor = CategoriesFromAnnotationsProcessor()
    parameters = CategoriesFromAnnotationsParameters()
    docs = processor.process(docs, parameters)
    doc0 = docs[0]
    assert len(doc0.categories) == 1
    assert doc0.categories[0].label == "person"

    docs = [Document(**jdoc) for jdoc in jdocs]
    parameters.multi_label_threshold = 0.0
    docs = processor.process(docs, parameters)
    doc0 = docs[0]
    assert len(doc0.categories) == 3
