from collections import defaultdict
from collections.abc import Iterable
from dataclasses import dataclass
from uuid import uuid4

from dishka.dependency_source.factory import Factory
from dishka.entities.key import DependencyKey
from dishka.entities.scope import BaseScope
from dishka.registry import Registry


@dataclass
class Class:
    id: str
    name: str
    component: str
    scope: BaseScope
    dependencies: list[str]
    final: bool = False


def factory_to_class(factory: Factory, keys: dict[DependencyKey, str],
                     container: type):
    hint = factory.provides.type_hint
    scope = factory.scope
    if name := getattr(hint, "__name__", None):
        name = getattr(hint, "__module__", None) + "\n" + name
    else:
        name = str(hint)
    return Class(
        id=keys[factory.provides],
        name=name,
        scope=scope,
        component=factory.provides.component,
        dependencies=[
            keys[dep] for dep in factory.dependencies
        ],
    )


def render_class(cls: Class):
    if cls.final:
        return f"""    {cls.id}(["&#9971;  {cls.name}"])\n"""
    else:
        return f"""    {cls.id}["&#129513;  {cls.name}"]\n"""


def render_relations(cls: Class):
    return "".join(
        f"    {dep} --> {cls.id}\n" for dep in cls.dependencies
    )


def render_component(component: str, scope: BaseScope, classes: list[Class]):
    res = "\n"
    comp_id = component_id(scope, component)
    res += f"style {comp_id} {COMPONENT_COLOR}\n"
    res += f"""subgraph {comp_id}["Component {component!r}"]\n"""
    for cls in classes:
        res +=render_class(cls)
    res += "end\n"
    return res


def component_id(scope: BaseScope, component: str):
    return f"{component}_{scope.value}"


def render_scope(prev_scope: BaseScope | None, scope: BaseScope,
                 components: Iterable[str], color: str):
    res = f"style {scope.value} {color}\n"
    res += f"""subgraph {scope.value}["{scope}"]\n"""
    for component in components:
        comp_id = component_id(scope, component)
        res += f"    subgraph {comp_id}\n"
        res += "    end\n"
    res += "end\n"
    if prev_scope is not None:
        res += f"{prev_scope.value} -.-> {scope.value}\n\n"
    return res


SCOPE_COLORS = [
    "fill:#FFCDD2,stroke:#EF9A9A",
    "fill:#E1BEE7,stroke:#CE93D8",
    "fill:#C5CAE9,stroke:#9FA8DA",
    "fill:#B3E5FC,stroke:#81D4FA",
]
COMPONENT_COLOR = "fill:#ECEFF1,stroke:#B0BEC5"


def render(registries: list[Registry], container):
    keys: dict[DependencyKey, str] = {}
    all_classes: dict[Factory, Class] = {}
    requested = set()
    components: dict[tuple[str, BaseScope], list[Class]] = defaultdict(list)
    for registry in registries:
        for factory in registry.factories.values():
            keys[factory.provides] = str(uuid4()).replace("-", "_")

    res = "flowchart LR\n"
    for registry in registries:
        for factory in registry.factories.values():
            cls = factory_to_class(factory, keys, container)
            all_classes[factory] = cls
            for dep in factory.dependencies:
                requested.add(dep)
            res += render_relations(cls)
            component_key = factory.provides.component, factory.scope
            components[component_key].append(cls)

    for registry in registries:
        for factory in registry.factories.values():
            if factory.provides not in requested:
                all_classes[factory].final = True

    for (component, scope), classes in components.items():
        res += render_component(component, scope, classes)

    scopes: dict[BaseScope, list[str]] = defaultdict(list)
    for component, scope in components:
        scopes[scope].append(component)

    prev_scope = None
    for color, (scope, scomponents) in zip(SCOPE_COLORS, scopes.items(), strict=False):
        res += render_scope(prev_scope, scope, scomponents, color)
        prev_scope = scope
    return res
