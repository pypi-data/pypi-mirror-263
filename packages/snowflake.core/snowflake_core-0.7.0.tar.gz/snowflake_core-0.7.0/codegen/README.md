# OpenAPI code generation workflow

## Overview
This is a customized OpenAPI generator to generate Python REST client for SnowAPI.

## Usage

These instructions should be used when you want to update the PythonAPI REST
SDK bindings to the latest Snowflake REST API OpenAPI specs.

* Make sure you have access to this repo: `github.com/snowflakedb/dev-snowflake-rest-api-specs`
* Make sure you have `git`, `curl`, `mvn`, `java-11` installed

`./generate.py` is the script that generates the code from the OpenAPI specs
in that repository.  It handles both cloning that repository locally, and
running the OpenAPI spec generator with our custom templates.

Try `./generate.py --help` for options and details.

You can generate the code against a commit other than `HEAD` on the spec repo
`main` branch by using the `-b`/`--branch` option.

You can generate a subset of resources with the `-r`/`--resources` option, by
specifying a comma-separated list of resources, or by using `:all:` (the
default) to generate all supported resources.

## Generation history

As best we can, we try to capture details about the generation history so that
you can reproduce the generated code.  This history is kept in the
`spec_versions.json` file, which contains a mapping (stored in human readable
JSON format) from resource name to the commits and timestamp used to generate
that resource's code.

* Commit hash checked out from `dev-snowflake-rest-api-specs` used as the
  source YAML files.
* Closest commit from `main` of *this* repository that we could find.  This is
  tricky because you might be in a PR branch where the actually commit you're
  looking at will get squashed away.  The commit captured here may not be
  exactly right, but it's the best we can do and should help you reproduce the
  generation, if the mustache template files have changed since then.
* Timestamp the resource was generated, in ISO 8601 UTC format.
