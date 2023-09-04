import itertools
import logging
import os
import subprocess
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

logger = logging.getLogger()


def main() -> None:
    python_exe = os.environ.get("PYTHON_EXE", os.path.join(__file__, "../.venv/Scripts/python.exe"))
    code_dir = Path(os.environ.get("DEFAULT_CODE_DIR", os.path.join(__file__, "../src/code"))).resolve()
    append_python_path = os.pathsep.join(
        os.path.abspath(p)
        for p in os.environ.get("DEFAULT_APPEND_PYTHON_PATH", os.path.join(__file__, "../src")).split(",")
    )
    logger.info(f"{python_exe=}")
    logger.info(f"code_dir={str(code_dir)}")
    logger.info(f"{append_python_path=}")

    python_path = "PYTHONPATH"
    if python_path in os.environ:
        os.environ[python_path] = os.environ[python_path].rstrip(os.pathsep) + os.pathsep + append_python_path
    else:
        os.environ[python_path] = append_python_path
    logger.info(f"PYTHONPATH={os.environ[python_path]}")

    with ThreadPoolExecutor() as executor:
        result = list(
            executor.map(
                run_solution,
                itertools.repeat(python_exe),
                [solution for solution in code_dir.glob("*.py") if solution.is_file()],
            )
        )
    success_count = sum(result)
    failed_count = len(result) - success_count
    logger.info(f"{success_count} success, {failed_count} failed in {len(result)} solutions")

    if failed_count > 0:
        exit(1)


def run_solution(python_exe: str, solution: Path) -> bool:
    process = subprocess.run([str(python_exe), str(solution)], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    if process.returncode == 0:
        logger.info(f"SUCCESS {solution.stem}")
    else:
        logger.error(f"FAIL {solution.stem}")
        logger.error(process.stdout)
    return process.returncode == 0


if __name__ == "__main__":
    logging.basicConfig(format="%(asctime)s|%(levelname)s|%(message)s", level="INFO")
    main()
