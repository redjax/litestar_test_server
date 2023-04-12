from typing import Any
from pathlib import Path
import yaml


def check_yml(yml_file: str = None) -> dict[str, Any]:
    """
    Ensure .yaml file can be loaded.

    Returns dict object with results of file load attempt.

    If a try/if statement creates a details dict object, append to return object
    before returning. The "details" dict is optional.
    """

    if not yml_file:
        raise ValueError(f"Missing value: yml_file (str)")

    ## Empty variable. If populated within this function, the
    #  details will be appended to the return object.
    details = None

    ## Ensure file exists
    if not Path(yml_file).exists():
        details = {"details": FileNotFoundError(f"Cannot find .yml file: {yml_file}")}
        res = False

    try:
        with open(yml_file, "r") as stream:
            ## Attempt to load file into yaml string
            try:
                _lint = yaml.safe_load(stream)
                stream.close()

                res = True

            except yaml.YAMLError as exc:
                ## Error parsing yaml. Create details object
                print(
                    f"[LINTERROR] Error in file [{yml_file}]. Exception details:\n{exc}"
                )
                details = {"details": exc}

                res = False

            except Exception as exc:
                ## Uncaught exception. Create details object
                print(f"[EXCEPTION] Uncaught exception. Exception details:\n{exc}")
                details = {"details": exc}
                res = False

    except Exception as exc:
        ## Uncaught exception opening file. Create details object
        print(f"[ERROR] Uncaught exception. Exception details: {exc}")
        details = {"details": exc}

    ## Create results object
    results = {"success": res, "file": {yml_file}}

    ## If there are exception details, append them to the results
    if details:
        results.update(details)

    return results


def load_from_yml(yml_file: str = None) -> dict[str, Any]:
    """
    Attempt to load a .yml file. Parse into a dict object.
    """

    if not yml_file:
        raise ValueError(f"Missing value: yml_file (str)")

    if not Path(yml_file).exists():
        raise FileNotFoundError(f"Cannot open .yml file: {yml_file}")

    try:
        print(f"[DEBUG] Loading config from: {yml_file}")
        with open(yml_file, "r") as stream:
            _conf = yaml.safe_load(stream)

    except Exception as exc:
        raise Exception(
            f"[EXCEPTION] Failed to open .yml config. Exception details: {exc}"
        )

    return _conf
