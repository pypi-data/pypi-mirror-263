# aind-hpc-client

[![License](https://img.shields.io/badge/license-MIT-brightgreen)](LICENSE)
[![semantic-release: angular](https://img.shields.io/badge/semantic--release-angular-e10079?logo=semantic-release)](https://github.com/semantic-release/semantic-release)
![Python](https://img.shields.io/badge/python->=3.7-blue?logo=python)

### Usage

```python
from aind_hpc_client import ApiClient as Client
from aind_hpc_client import Configuration as Config
from aind_hpc_client.api.slurm_api import SlurmApi
from aind_hpc_client.models.v0036_job_submission import V0036JobSubmission
from aind_hpc_client.models.v0036_job_properties import V0036JobProperties

host = "http://slurm/api"
username = "*****"  # Change this
# Ideally, the password and access_token are set as secrets and read in using a secrets manager
password = "*****"  # Change this
access_token = "*****"  # Change this
config = Config(host=host, password=password, username=username, access_token=access_token)
slurm = SlurmApi(Client(config))
slurm.api_client.set_default_header(header_name='X-SLURM-USER-NAME', header_value=username)
slurm.api_client.set_default_header(header_name='X-SLURM-USER-PASSWORD', header_value=password)
slurm.api_client.set_default_header(header_name='X-SLURM-USER-TOKEN', header_value=access_token)

command_str = [
            "#!/bin/bash",
            "\necho",
            "'Hello World?'",
            "&&",
            "sleep",
            "120",
            "&&",
            "echo",
            "'Example json string'",
            "&&",
            "echo",
            "'",
            '{"input_source":"/path/to/directory","output_directory":"/path/to/another_directory"}',
            "'",
            "&&",
            "echo",
            "'Goodbye!'"
        ]
script = " ".join(command_str)

hpc_env = {"PATH": "/bin:/usr/bin/:/usr/local/bin/", "LD_LIBRARY_PATH": "/lib/:/lib64/:/usr/local/lib",}

job_props = V0036JobProperties(
  partition = "aind",  # Change this if needed
  name = "test_job1",
  environment = hpc_env,
  standard_out = "/path/for/logs/test_job1.out",  # Change this
  standard_error = "/path/for/logs/test_job1_error.out",  # Change this
  memory_per_cpu = 500,
  tasks = 1,
  minimum_cpus_per_node = 1,
  nodes = [1, 1],
  time_limit = 5  # In minutes
)

job_submission = V0036JobSubmission(script=script, job=job_props)
submit_response = slurm.slurmctld_submit_job_0(v0036_job_submission=job_submission)
job_id = submit_response.job_id
job_response = slurm.slurmctld_get_job_0(job_id=submit_response.job_id)
print(job_response.jobs[0].job_state)
```

## Installation
The code is automatically generated using openapi tools and the specification from slurm.

### To get the specification from slurm
```bash
curl -s -H X-SLURM-USER-NAME:$SLURM_USER_NAME \
 -H X-SLURM-USER-PASSWORD:$SLURM_USER_PASSWORD \
 -H X-SLURM-USER-TOKEN:$SLURM_USER_TOKEN \
 -X GET 'http://slurm/api/openapi/v3' > openapi.json
```

### Update schema
The original specification has some validation issues, so the output is modified. The changes are tracked in `schema_changes.json`.

### To create the python code, openapi tools is used. `generateSourceCodeOnly` in `configs.json` can be set to `False` to generate tests and additional files.
```bash
docker run --rm \
  -u "$(id -u):$(id -g)" \
  -v ${PWD}:/local openapitools/openapi-generator-cli generate \
  --skip-validate-spec \
  --config /local/configs.json \
  -i /local/openapi.json \
  -g python \
  -o /local/src
```

## Contributing
We can update the openapi.json specification if validation errors are raised.

### Pull requests

For internal members, please create a branch. For external members, please fork the repository and open a pull request from the fork. We'll primarily use [Angular](https://github.com/angular/angular/blob/main/CONTRIBUTING.md#commit) style for commit messages. Roughly, they should follow the pattern:
```text
<type>(<scope>): <short summary>
```

where scope (optional) describes the packages affected by the code changes and type (mandatory) is one of:

- **build**: Changes that affect build tools or external dependencies (example scopes: pyproject.toml, setup.py)
- **ci**: Changes to our CI configuration files and scripts (examples: .github/workflows/ci.yml)
- **docs**: Documentation only changes
- **feat**: A new feature
- **fix**: A bugfix
- **perf**: A code change that improves performance
- **refactor**: A code change that neither fixes a bug nor adds a feature
- **test**: Adding missing tests or correcting existing tests

### Semantic Release

The table below, from [semantic release](https://github.com/semantic-release/semantic-release), shows which commit message gets you which release type when `semantic-release` runs (using the default configuration):

| Commit message                                                                                                                                                                                   | Release type                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------- |
| `fix(pencil): stop graphite breaking when too much pressure applied`                                                                                                                             | ~~Patch~~ Fix Release, Default release                                                                          |
| `feat(pencil): add 'graphiteWidth' option`                                                                                                                                                       | ~~Minor~~ Feature Release                                                                                       |
| `perf(pencil): remove graphiteWidth option`<br><br>`BREAKING CHANGE: The graphiteWidth option has been removed.`<br>`The default graphite width of 10mm is always used for performance reasons.` | ~~Major~~ Breaking Release <br /> (Note that the `BREAKING CHANGE: ` token must be in the footer of the commit) |
