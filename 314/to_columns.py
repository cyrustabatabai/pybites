from typing import List  # not needed when we upgrade to 3.9


def print_names_to_columns(names: List[str], cols: int = 2) -> None:

    lines = []
    for i in range(0,len(names),cols):
        names_part = [f"{name:<10}" for name in names[i:i +cols]]
        lines.append(f"| {'| '.join(names_part)}")

    print('\n'.join(lines))


        


