from typing import Any, Dict

def flatten(d: Dict[str, Any], parent_key: str = '', sep: str = '.') -> Dict[str, Any]:
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

if __name__ == '__main__':
    sample = {"user": {"profile": {"name": "vaio", "role": "admin"}}, "active": True}
    res = flatten(sample)
    print("Flattened:", res)
    assert res["user.profile.name"] == "vaio"
