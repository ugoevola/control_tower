import os
import subprocess


def run():
    result = subprocess.run(['behave'], cwd=os.path.join(os.path.dirname(__file__), '.', 'features'))
    if result.returncode != 0:
        raise SystemExit(result.returncode)


if __name__ == '__main__':
    run()
