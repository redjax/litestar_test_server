from subprocess import PIPE, STDOUT
import subprocess
import shlex

from typing import Any, Union


## env names correlate to Poetry groups, i.e. --group=dev
#  "prod" will use the default Poetry environment
#  If you create a new Poetry group (i.e. --group=ci),
#  update accepted_envs and envs below.
accepted_envs = ["prod", "dev"]
## Requirements file for each env name
envs = {
    "prod": {"requirements_file": "requirements.txt"},
    "dev": {"requirements_file": "requirements.dev.txt"},
}


def export_requirements(env: str = "prod") -> dict[str, Any]:
    """
    Accept an env name, export requirements to file defined in envs dict above.

    Env passed must be in "accepted_envs."

    Env names correlate to Poetry groups, i.e. poetry --group=dev.
    """

    ## Check for valid env
    if env.lower() not in accepted_envs:
        raise ValueError(
            f"Unrecognized environment name: {env}. Must be one of: {accepted_envs}"
        )

    ## Initialize env dict with env_name. Leave requirements_file None for now.
    env_obj = {"env_name": env, "requirements_file": None}

    ## Loop over environments in envs
    for _env_dict in envs:
        ## Match envs dict to env name passed to this function
        if _env_dict == env:
            ## Get env dict
            dict_match = envs[_env_dict]
            # print(f"[DEBUG] Matched dict to env '{env}': {dict_match}")

            ## Update env_obj dict with requirements file
            env_obj.update(dict_match)

    # print(f"Using environment: {env_obj}")

    ## Build command
    export_cmd = f"poetry export -f requirements.txt --output {env_obj['requirements_file']} --without-hashes"
    print(f"[DEBUG] Export requirements command: {export_cmd}")

    ## Run command to export Poetry requirements
    try:
        ## Command must be run with shell=True to access Poetry
        _process = subprocess.run(
            export_cmd,
            shell=True,
            check=True,
            capture_output=True,
            encoding="utf-8",
            timeout=5,
        )

    except subprocess.CalledProcessError as exc:
        print(f"[Error] Process failed due to non-successful return code")
        raise Exception(f"[Exception] [{exc.returncode}]:\n{exc}")
    except subprocess.TimeoutExpired as exc:
        print(f"[ERROR] Process timed out")
        raise Exception(f"[EXCEPTION]\n{exc}")
    except Exception as exc:
        raise Exception(f"[EXCEPTION] Unhandled exception:\n{exc}")

    finally:
        ## Get output from command
        _output = _process.stdout.strip()

        ## Check for errors
        if not _process.stderr:
            _errors = None
        else:
            _errors = _process.stderr.strip()

        ## Build return object
        return_object = {
            "cmd": export_cmd,
            "stdout": _output,
            "stderr": _errors,
            "details": {
                "result_code": _process.returncode,
                "env_name": env_obj["env_name"],
                "output_file": env_obj["requirements_file"],
            },
        }

    # print(f"[DEBUG] Return object: {return_object}")
    return return_object


if __name__ == "__main__":
    ## Export prod requirements
    export_prod_env = export_requirements()
    print(f"Export Prod env results: {export_prod_env['details']}")

    ## Export dev requirements
    export_dev_env = export_requirements(env="dev")
    print(f"Export Dev env results: {export_dev_env['details']}")
