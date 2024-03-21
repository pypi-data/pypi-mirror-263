# 내장
import os
import sys
from pathlib import Path


SUBMODULES_ROOT = Path(os.path.dirname(__file__), 'submodules')
PROJECT_KOREA_ROOT = Path(SUBMODULES_ROOT, 'repo-greeting-korea')
PROJECT_CHINA_ROOT = Path(SUBMODULES_ROOT, 'repo-greeting-china')

context = f'`{SUBMODULES_ROOT}`에는 {os.listdir(SUBMODULES_ROOT)} 파일, 경로들이 존재합니다.'
assert os.path.isdir(
    SUBMODULES_ROOT
), f'`{SUBMODULES_ROOT}`는 디렉토리가 아닙니다. {context}'
assert os.path.isdir(
    PROJECT_KOREA_ROOT
), f'`{PROJECT_KOREA_ROOT}`는 디렉토리가 아닙니다. {context}'
assert os.path.isdir(
    PROJECT_KOREA_ROOT
), f'`{PROJECT_CHINA_ROOT}`는 디렉토리가 아닙니다. {context}'


if (p := os.path.realpath(PROJECT_KOREA_ROOT)) not in sys.path:
    sys.path.append(p)
    print(f'경로 `{p}`를 sys.path 에 추가했습니다.')

if (p := os.path.realpath(PROJECT_CHINA_ROOT)) not in sys.path:
    sys.path.append(p)
    print(f'경로 `{p}`를 sys.path 에 추가했습니다.')
