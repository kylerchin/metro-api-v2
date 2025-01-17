# Versioning

## When to update
In general, we keep the version number in sync with the API version number and use [Semantic Versioning](https://semver.org/).
## How to update

Run the following command from the root directory of the project:

```shell
git tag -a v2.1.10 -m "MVP Release"
```

### Checking the version

```shell
git tag
```

### Pushing the version

```shell
git push -tags
```

## Other notes

### Versioning History

(2.0.4)
2.0.0

Branches --> Image:
- main (v2.0.4) --> metro-api-v2:2.0
- dev  (v2.0.5) --> metro-api-v2:2.0-dev
  dev  (v2.0.50)

"Early Access" Release: 2.1.0 (2.0.50)

- main (v2.1.0) --> metro-api-v2:2.1
- dev  (v2.1.1) --> metro-api-v2:2.1-dev

"Full" Release: 2.2.0 (2.1.50)


-----------------

MVP Release: 2.0.0
- main (v2.0.0) --> metro-api-v2:2.0

"Early Access" Release: 2.1.0
- dev  (v2.1.0) --> metro-api-v2:2.1-dev
  dev  (v2.1.0)
- main (v2.1.0) --> metro-api-v2:2.1
  hotfix (v2.1.1)

"Full" Release: 2.2.0
- dev  (v2.2.0) --> metro-api-v2:2.2-dev
- main (v2.2.0) --> metro-api-v2:2.2