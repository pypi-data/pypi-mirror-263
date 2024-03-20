"""An amazing sample package!"""
import os

__version__ = '0.1'

# 내장
import os
import sys
from pathlib import Path


# NOTE: `REPO_ROOT` 는 이 파일의 부모 경로
REPO_ROOT = os.path.abspath(Path(os.path.dirname(__file__), '..'))
SUBMODULES_ROOT = Path(REPO_ROOT, 'submodules')
PROJECT_A_ROOT = Path(SUBMODULES_ROOT, 'repo-korea')
PROJECT_B_ROOT = Path(SUBMODULES_ROOT, 'repo-china')

assert os.path.isdir(REPO_ROOT), f'`{REPO_ROOT}`는 디렉토리가 아닙니다.'
context = f'`{REPO_ROOT}`에는 {os.listdir(REPO_ROOT)} 파일, 경로들이 존재합니다.'
assert os.path.isdir(
    SUBMODULES_ROOT
), f'`{SUBMODULES_ROOT}`는 디렉토리가 아닙니다. {context}'
assert os.path.isdir(
    PROJECT_A_ROOT
), f'`{PROJECT_A_ROOT}`는 디렉토리가 아닙니다. {context}'
assert os.path.isdir(
    PROJECT_A_ROOT
), f'`{PROJECT_B_ROOT}`는 디렉토리가 아닙니다. {context}'


if (p := os.path.realpath(PROJECT_A_ROOT)) not in sys.path:
    sys.path.append(p)
    print(f'경로 `{p}`를 sys.path 에 추가했습니다.')

if (p := os.path.realpath(PROJECT_B_ROOT)) not in sys.path:
    sys.path.append(p)
    print(f'경로 `{p}`를 sys.path 에 추가했습니다.')
