## Usage

#### In your shell:
```sh
export LAUNCHDARKLY_SERVER_KEY="some-random-key"
export LAUNCHDARKLY_FLAGS="foo"
```

This script provides several command-line options:

- `-f` or `--flag`: This option is used to specify the flag key to evaluate. This option is required and can be used multiple times. The value for this option can also be provided through the `LAUNCHDARKLY_FLAGS` environment variable.

- `--sdk-key`: This option is used to specify the LaunchDarkly SDK server key. The value for this option can also be provided through the `LAUNCHDARKLY_SERVER_KEY` environment variable.

- `-v` or `--verbose`: This option is used to increase logging verbosity. The more times this option is used, the more verbose the logging.

> :warning: You can specify either environment variables or command-line options.

For example, to run the script with a flag key of "foo" and an SDK key of "sdk-34324dfd-fake-ke5", you would use the following command:
```py
ld-flag-lookup -f "foo" --sdk-key "sdk-34324dfd-fake-key" -vv
```
