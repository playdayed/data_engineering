from pathlib import Path

current_dir = Path.cwd()

for path in current_dir.rglob("*"):
    print(path)

    if path.is_file():
        print("  File content:")
        print(path.read_text(encoding="utf-8"))