import logging
import os
import subprocess
from pathlib import Path

logger = logging.getLogger()


def main() -> None:
    python_exe = Path(os.environ.get("PYTHON_EXE", os.path.join(__file__, "../.venv/Scripts/python.exe"))).resolve()
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

    for solution in code_dir.glob("*.py"):
        if solution.is_file():
            try:
                subprocess.run([str(python_exe), str(solution)], capture_output=True, text=True, check=True)
                logger.info(f"SUCCESS {solution.stem}")
            except subprocess.CalledProcessError as e:
                logger.error(f"FAILED {solution.stem}")
                logger.error(f"stderr: {e.stderr}")
                logger.error(f"stdout: {e.stdout}")
                exit(e.returncode)
    logger.info("ALL DONE")


if __name__ == "__main__":
    logging.basicConfig(format="%(asctime)s|%(levelname)s|%(message)s", level="INFO")
    main()
