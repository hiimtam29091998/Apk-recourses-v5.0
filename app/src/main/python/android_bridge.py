"""Native Android bridge: same exact SciPy/HiGHS optimizer as desktop v5.

No HTTP server is started and no networking is required at runtime.
"""
from __future__ import annotations
import base64
import json
from optimizer import optimize, boss_reward


def optimize_json(config_json: str) -> str:
    config = json.loads(config_json)
    result = optimize(config)
    return json.dumps(result, ensure_ascii=False, separators=(',', ':'))


def excel_base64(config_json: str, profile: str) -> str:
    from excel_export import make_excel
    data = make_excel(optimize(json.loads(config_json)), profile)
    return base64.b64encode(data).decode('ascii')


def csv_base64(config_json: str, profile: str) -> str:
    from server import make_export
    data = make_export(optimize(json.loads(config_json)), profile)
    return base64.b64encode(data).decode('ascii')


def reward_for_damage(damage: float) -> int:
    return boss_reward(damage)
