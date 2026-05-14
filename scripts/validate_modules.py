#!/usr/bin/env python3
"""Validate the cognitive skill module layout."""

from __future__ import annotations

import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "skills" / "catalog.json"
COMMON_REQUIRED = {
    "SKILL.md",
    "description.md",
    "schema.json",
    "workflow.yaml",
    "trigger_rules.json",
    "examples.json",
    "eval_cases.json",
    "failure_cases.json",
    "version.json",
}


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def load_json(path: Path) -> object:
    try:
        with path.open(encoding="utf-8") as handle:
            return json.load(handle)
    except Exception as exc:  # pragma: no cover - diagnostic path
        fail(f"invalid JSON in {path.relative_to(ROOT)}: {exc}")


def validate_json_files() -> None:
    for path in sorted(ROOT.rglob("*.json")):
        load_json(path)
        print(f"json ok: {path.relative_to(ROOT)}")


def validate_yaml_files() -> None:
    try:
        import yaml  # type: ignore
    except Exception as exc:  # pragma: no cover - environment dependent
        fail(
            "PyYAML is required to validate YAML files. "
            "Install dependencies with `python3 -m pip install -r requirements.txt`. "
            f"Original error: {exc}"
        )

    for path in sorted(ROOT.rglob("*.yaml")) + sorted(ROOT.rglob("*.yml")):
        try:
            with path.open(encoding="utf-8") as handle:
                yaml.safe_load(handle)
        except Exception as exc:  # pragma: no cover - diagnostic path
            fail(f"invalid YAML in {path.relative_to(ROOT)}: {exc}")
        print(f"yaml ok: {path.relative_to(ROOT)}")


def validate_catalog() -> None:
    catalog = load_json(CATALOG)
    if not isinstance(catalog, dict):
        fail("skills/catalog.json must contain an object")

    modules = catalog.get("modules")
    if not isinstance(modules, list) or not modules:
        fail("skills/catalog.json must contain a non-empty modules list")

    for module in modules:
        if not isinstance(module, dict):
            fail("each catalog module must be an object")

        name = module.get("name")
        path_value = module.get("path")
        resources = module.get("resources")
        if not isinstance(name, str) or not name:
            fail("catalog module is missing name")
        if not isinstance(path_value, str) or not path_value:
            fail(f"catalog module {name} is missing path")
        if not isinstance(resources, list):
            fail(f"catalog module {name} is missing resources list")

        module_dir = ROOT / path_value
        if not module_dir.is_dir():
            fail(f"module path not found: {path_value}")

        required = set(COMMON_REQUIRED)
        required.update(str(item) for item in resources)
        for required_file in sorted(required):
            if not (module_dir / required_file).is_file():
                fail(f"{name} missing required file: {required_file}")

        skill_text = (module_dir / "SKILL.md").read_text(encoding="utf-8")
        for resource in resources:
            if resource not in skill_text:
                fail(f"{name} SKILL.md does not reference {resource}")

        version_data = load_json(module_dir / "version.json")
        if isinstance(version_data, dict) and version_data.get("module") != name:
            fail(f"{name} version.json module mismatch")

        validate_model_routing(name, module_dir)

        print(f"module ok: {name}")


def validate_model_routing(name: str, module_dir: Path) -> None:
    trigger_rules_path = module_dir / "trigger_rules.json"
    model_cards_path = module_dir / "model_cards.json"
    if not trigger_rules_path.is_file() or not model_cards_path.is_file():
        return

    trigger_rules = load_json(trigger_rules_path)
    model_cards = load_json(model_cards_path)
    if not isinstance(trigger_rules, dict) or not isinstance(model_cards, dict):
        return

    models = model_cards.get("models")
    if not isinstance(models, list):
        fail(f"{name} model_cards.json must contain a models list")

    model_names = {
        item.get("name")
        for item in models
        if isinstance(item, dict) and isinstance(item.get("name"), str)
    }

    referenced_models: set[str] = set()
    for route in trigger_rules.get("routing", []):
        if not isinstance(route, dict):
            continue
        for model in route.get("models", []):
            if isinstance(model, str):
                referenced_models.add(model)

    for category in trigger_rules.get("category_routing", []):
        if not isinstance(category, dict):
            continue
        for model in category.get("typical_models", []):
            if isinstance(model, str):
                referenced_models.add(model)

    missing = sorted(referenced_models - model_names)
    if missing:
        fail(
            f"{name} trigger_rules.json references models missing from "
            f"model_cards.json: {', '.join(missing)}"
        )


def main() -> int:
    validate_json_files()
    validate_yaml_files()
    validate_catalog()
    print("all module checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
