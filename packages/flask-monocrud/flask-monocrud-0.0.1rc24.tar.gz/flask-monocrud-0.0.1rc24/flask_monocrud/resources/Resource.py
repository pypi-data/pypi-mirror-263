from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any

from masoniteorm import Model

from packages.experimental.flask_cruddy import ResourceNameMutations, TableModel


@dataclass
class Resource:
    resource: str = field(default_factory=str)  # This is a variable name
    model: Model = field(default_factory=Model)
    name: ResourceNameMutations = field(default_factory=ResourceNameMutations)
    label: str = field(default_factory=str)
    icon: str | bool = field(default_factory=bool)
    table: TableModel = field(default_factory=TableModel)

    display_in_nav: bool = field(default_factory=bool)

    header_metrics: list[dict[str, Any]] = field(default_factory=list)
    fillable: list[dict[str, Any]] = field(default_factory=list)

    models: list[dict[str, Any]] = field(default_factory=list)
    permissions: dict[str, bool] = field(default_factory=dict)

    result_set: Any = field(default_factory=dict)

    def get_header_metrics(self) -> list[dict[str, Any]]:
        pass

    def get_fillable(self) -> list[dict[str, Any]]:
        pass

    def get_table(self) -> list[dict[str, Any]]:
        pass

    def get_relations(self) -> list[dict[str, Any]]:
        pass

    def get_table_actions(self) -> list[dict[str, Any]]:
        pass

    def get_table_filters(self) -> list[dict[str, Any]]:
        pass

    def get_table_tabs(self) -> list[dict[str, Any]]:
        pass
