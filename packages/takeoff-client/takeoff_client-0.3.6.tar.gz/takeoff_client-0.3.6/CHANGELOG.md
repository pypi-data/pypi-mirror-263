# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog],
and this project adheres to [Semantic Versioning].

For information about how to release Takeoff Client see [Release Process](https://www.notion.so/tytnai/Releasing-Takeoff-Client-52deed2f60ba4af9890f8cbbc8876d4d?pm=c)

## [Unreleased]

## [0.4.0] - 2024-03-07

### Added

- Support for management api endpoints, new release process that pushes takeoff-config to pypi alongside the client with the same version [PR 1079](https://github.com/TNBase/pantheon/pull/1079)


## [0.3.0] - 2024-02-27

### Fixed
- fix the client package unit tests support for python 3.8
- fix the compatibility issue in takeoff client 

## [0.2.0] - 2024-02-19

### Added

- add support for image to text models, by adding an `image_path` keyword argument to the `generate` method. 

### Changed
- Changed default value for embedding endpoint from `'embed'` to `'primary'` to match takeoff defaults.

## [0.1.0] - 2024-02-07

### Added

- add classify to the takeoff client to match the new endpoint

## [0.0.4] - 2024-01-06

### Added

- add sseclient-py dependency into pyproject.toml 


## [0.0.3] - 2024-01-05

- initial release
- add takeoff python client, publishing on [PyPI](https://pypi.org/project/takeoff-client/)

<!-- Links -->
[keep a changelog]: https://keepachangelog.com/en/1.0.0/
[semantic versioning]: https://semver.org/spec/v2.0.0.html
