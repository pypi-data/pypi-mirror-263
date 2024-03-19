# Using the Python SDK

You can interact with Guardian Scanner's API by importing the python classes in your code. The initial set-up is similar to the CLI. You need to install the guardian-scanner package and set-up the environment variables.

``` python
# Import the Guardian API client
from guardian_scanner.api import GuardianAPIClient

# Define the location of the Guardian Scanner's API and your model
base_url = ""
model_uri = ""

# Initiate the client
guardian = GuardianAPIClient(base_url=base_url)

# Scan the model
response = guardian.scan(model_uri=model_uri)


# Evaluate the scan response against a threshold
assert response.get("http_status_code") == 200
assert response.get("scan_status_json") != None
assert response.get("scan_status_json").get("status") == "FINISHED"

reason, should_block = guardian.evaluate(respon.get("scan_status_json"))
  
if should_block:
  print(f"Model {model_uri} was blocked with reason: {reason}")
```

## Class GuardianAPIClient

``` python
  def __init__(
      self,
      base_url: str,
      scan_endpoint: str = "scans",
      api_version: str = "v1",
      log_level: str = "INFO",
  ) -> None:
      """
      Initializes the Guardian API client.

      Args:
          base_url (str): The base URL of the Guardian API.
          scan_endpoint (str, optional): The endpoint for scanning. Defaults to "scans".
          api_version (str, optional): The API version. Defaults to "v1".
          log_level (str, optional): The log level. Defaults to "INFO".

      Raises:
          ValueError: If the log level is not one of "DEBUG", "INFO", "ERROR", or "CRITICAL".

      """
```

### Methods
#### GuardianAPIClient.scan
``` python
  def scan(self, model_uri: str) -> Dict[str, Any]:
      """
      Submits a scan request for the given URI and polls for the scan status until it is completed.

      Args:
          uri (str): The URI to be scanned.

      Returns:
          dict: A dictionary containing the HTTP status code and the scan status JSON.
                If an error occurs during the scan submission or polling, the dictionary
                will also contain the error details.

      """
```

#### GuardianAPIClient.evaluate
``` python
  def evaluate(
      self,
      status_json: Dict[str, Any],
      threshold: str = "CRITICAL",
      block_on_scan_errors: bool = False,
  ) -> Tuple[str, bool]:
      """
      Evaluates the status of a scan based on the provided status JSON.

      Args:
          status_json (object): The status JSON object containing scan information obtained from scan method.
          threshold (str, optional): The threshold level to consider for blocking. Defaults to "CRITICAL".
          block_on_scan_errors (bool, optional): Whether to block if there are errors in scanning. Defaults to False.

      Returns:
          Tuple[str, bool]: A tuple containing the evaluation result message and a boolean indicating if blocking is required.

          Raises:
              ValueError: If the threshold is not one of "LOW", "MEDIUM", "HIGH", or "CRITICAL".
      """
```


# Using CLI

The Guardian Scanner's CLI offer a convenient way of submitting a scan and receive either the full scan report or get a block decision depending upon whether a model contains potential security vulernabilities.

## Installation

``` shell
pip install guardian-scanner
```

## Setup Environment Variables
The environment variables are for setting up the authorization with the API. The admin of your account should be able to provide you with these. See: Setup Identity Provider

``` shell

# Client ID
export GUARDIAN_SCANNER_CLIENT_ID=
  
# Client Secret
export GUARDIAN_SCANNER_CLIENT_SECRET=
  
# OIDP (Keycloak) Endpoint
export GUARDIAN_SCANNER_OIDP_TOKEN_ENDPOINT=
```

## Running Your Scans
That's it, now you should be all set to start scanning your models.

``` shell

guardian-scanner <base_url> <model_uri> \
       [--threshold <threshold>] \
       [--block-on-errors] \
       [--log-level <log-level>] \
       [--silent] || echo $?
```

### Arguments

`base_url` The API URL (required)

`model_uri` The Path where the model is stored e.g. S3 bucket (required)

`--threshold` The minimum threshold at which a model should be blocked. Take following values: low, medium, high, critical. Default is critical

`--block-on-errors` A boolean flag indicating the error in scanning should also lead to a block. These errors are only specific to model scanning.

`--log-level` Can be set to any of the following: error, info, or debug

`--silent` Disable all logging

`--report-only` Prints out the scan report and does not evaluate it for blocking.

### Exit Codes
The CLI returns following exit codes that downstream application (e.g. your CI/CD pipeline) can test to block a deployment

0 Successful scan without issues at or above the threshold (default CRITICAL)

1 Successful scan with issues at or above the threshold (default CRITICAL)

2 Scan failed for any reason

## Examples
``` shell

# To see the report from scanning the mode.
guardian-scanner https://protectai.dev/guardian/v1 s3://a-bucket/path/ --report-only

# To get a block decision for model security vulnerability at or higher than "MEDIUM"
guardian-scanner https://protectai.dev/guardian/v1 s3://a-bucket/path/ --threshold MEDIUM || echo $?
```