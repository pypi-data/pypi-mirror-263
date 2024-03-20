from collections import defaultdict
from typing import Type, cast, List

from log_with_context import add_logging_context, Logger
from pydantic import BaseModel, Field
from pymultirole_plugins.v1.processor import ProcessorParameters, ProcessorBase
from pymultirole_plugins.v1.schema import Document, Category

logger = Logger("pymultirole")


class CategoriesFromAnnotationsParameters(ProcessorParameters):
    multi_label_threshold: float = Field(0.5,
                                         description="only categories with a score greater than threshold are kept")


class CategoriesFromAnnotationsProcessor(ProcessorBase):
    """Create categories from annotations"""

    def process(
            self, documents: List[Document], parameters: ProcessorParameters
    ) -> List[Document]:  # noqa: C901
        params: CategoriesFromAnnotationsParameters = cast(CategoriesFromAnnotationsParameters, parameters)
        for document in documents:
            with add_logging_context(docid=document.identifier):
                categories = []
                if document.annotations:
                    anns = defaultdict(list)
                    for a in document.annotations:
                        anns[a.labelName].append(a)
                    for lbl, alist in anns.items():
                        a = alist[0]
                        score = float(len(alist) / len(document.annotations))
                        if score > params.multi_label_threshold:
                            categories.append(Category(labelName=a.labelName, label=a.label,
                                                       score=score))
                document.categories = categories
                document.annotations = None
        return documents

    @classmethod
    def get_model(cls) -> Type[BaseModel]:
        return CategoriesFromAnnotationsParameters
