# ReleaseHound

Welcome to ReleaseHound

## Getting Started

First, you need to ensure you have `docker`, `git`, `pipenv`, and `python3` installed locally, and the `docker` daemon is running.

Then, you can setup your local environment via:

```bash
# Install the dependencies
pipenv install --deploy --ignore-pipfile --dev

# Build the image
pipenv run invoke build

# Run the image
docker run seiso/release_hound:2023.01.00 --help
```

## Troubleshooting

If you're troubleshooting the results of any of the invoke tasks, you can add `--debug` to enable debug logging, for instance:

```bash
pipenv run invoke build --debug
```
