# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.5.2] - 2024-10-15

### Fixed

* Fixed whitespace not being replaced.
* Fixed backticks in template leading to error.

## [0.5.1] - 2024-09-17

### Fixed

* Fixed `command` ninja macro joining command and parameters if only one line break separates them.


## [0.5.0] - 2024-09-07

### Added

* Added command jinja macro.
* Added removal of whitespace and of empty lines.


### Changed

* Changed example images to ascii art without whitespace.


## [0.4.1] - 2024-07-31

### Fixed

* Fixed bug, with error message not being detected as such.


## [0.4.0] - 2024-06-29

### Added

* Added more os being detected by default detection of `__os__`.
* Added compact layout for radios with elements that have no description.


### Changed

* Switched to longer os names: `windows`, `linux`, `macos`.
* Made default value detection extensible for new default values.


## [0.3.1] - 2024-06-28

### Fixed

* Fixed default os not being rendered.


## [0.3.0] - 2024-06-28

### Added

* Added warning color to erroneous render output.
* Added automatic default for operating systems.


### Changed

* Delimiter in radios is now only shown, when a description exists.


### Fixed

* Fixed failed rendering on empty default.


## [0.2.1] - 2024-06-27

### Fixed

* Fixed setuptool build.


## [0.2.0] - 2024-06-27

### Added

* Added `raise` macro for template.
* Added release github workflow for pypi.


### Changed

* Updated `install.cfg` to adhere to `installation-instruction == 0.4.0`.
* Bumped dependency to at least `installation-instruction >= 0.4.0`


## [0.1.0] - 2024-06-14

Initial release.


[unreleased]: https://github.com/instructions-d-installation/web-installation-instruction/compare/v0.5.2...HEAD
[0.5.2]: https://github.com/instructions-d-installation/web-installation-instruction/compare/v0.5.1...v0.5.2
[0.5.1]: https://github.com/instructions-d-installation/web-installation-instruction/compare/v0.5.0...v0.5.1
[0.5.0]: https://github.com/instructions-d-installation/web-installation-instruction/compare/v0.4.1...v0.5.0
[0.4.1]: https://github.com/instructions-d-installation/web-installation-instruction/compare/v0.4.0...v0.4.1
[0.4.0]: https://github.com/instructions-d-installation/web-installation-instruction/compare/v0.3.1...v0.4.0
[0.3.1]: https://github.com/instructions-d-installation/web-installation-instruction/compare/v0.3.0...v0.3.1
[0.3.0]: https://github.com/instructions-d-installation/web-installation-instruction/compare/v0.2.1...v0.3.0
[0.2.1]: https://github.com/instructions-d-installation/web-installation-instruction/compare/v0.2.0...v0.2.1
[0.2.0]: https://github.com/instructions-d-installation/web-installation-instruction/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/instructions-d-installation/web-installation-instruction/releases/tag/v0.1.0