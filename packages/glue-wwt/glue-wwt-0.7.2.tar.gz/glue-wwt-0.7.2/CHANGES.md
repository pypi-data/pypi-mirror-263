# Full changelog

## v0.7.1 - 2024-02-27

<!-- Release notes generated using configuration in .github/release.yml at main -->
### What's Changed

#### Bug Fixes

* Avoid using deprecated import from glue-core by @astrofrog in https://github.com/glue-viz/glue-wwt/pull/105

**Full Changelog**: https://github.com/glue-viz/glue-wwt/compare/v0.7.0...v0.7.1

## v0.7.0 - 2024-02-24

<!-- Release notes generated using configuration in .github/release.yml at main -->
### What's Changed

#### Other Changes

* Expose grid and constellation settings by @Carifio24 in https://github.com/glue-viz/glue-wwt/pull/97
* Updates for glue-qt by @Carifio24 in https://github.com/glue-viz/glue-wwt/pull/98
* Bump minimum glue-core by @Carifio24 in https://github.com/glue-viz/glue-wwt/pull/100
* Truncate SkyCoord exception if too long by @Carifio24 in https://github.com/glue-viz/glue-wwt/pull/92
* Update import location for astropy v6 by @Carifio24 in https://github.com/glue-viz/glue-wwt/pull/102

**Full Changelog**: https://github.com/glue-viz/glue-wwt/compare/v0.6.1...v0.7.0

## v0.6.1 - 2023-01-12

<!-- Release notes generated using configuration in .github/release.yml at main -->
### What's Changed

#### Bug Fixes

- Fix compatibility of .ui files with Qt6 by @astrofrog in https://github.com/glue-viz/glue-wwt/pull/93

**Full Changelog**: https://github.com/glue-viz/glue-wwt/compare/v0.6.0...v0.6.1

## v0.6.0 - 2022-11-08

<!-- Release notes generated using configuration in .github/release.yml at main -->
### What's Changed

#### New Features

- Added setting controls for image layers. by @Carifio24 in https://github.com/glue-viz/glue-wwt/pull/88

#### Bug Fixes

- Fix incorrect attribute reference by @Carifio24 in https://github.com/glue-viz/glue-wwt/pull/87

#### Other Changes

- Only apply longitude shifting conditionally by @Carifio24 in https://github.com/glue-viz/glue-wwt/pull/81
- Switch CI from Azure to GitHub actions by @dhomeier in https://github.com/glue-viz/glue-wwt/pull/82
- Add publishing workflow to GH Actions by @dhomeier in https://github.com/glue-viz/glue-wwt/pull/86
- Create table layers as non-selectable in pywwt by @Carifio24 in https://github.com/glue-viz/glue-wwt/pull/89

### New Contributors

- @Carifio24 made their first contribution in https://github.com/glue-viz/glue-wwt/pull/81
- @dhomeier made their first contribution in https://github.com/glue-viz/glue-wwt/pull/82

**Full Changelog**: https://github.com/glue-viz/glue-wwt/compare/v0.5...v0.6.0

## [0.5](https://github.com/glue-viz/glue-wwt/compare/v0.4...v0.5) - 2020-11-30

### What's Changed

#### New Features

- Included a save button to save the current view to the first slide of a tour. [https://github.com/glue-viz/glue-wwt/pull/70, https://github.com/glue-viz/glue-wwt/pull/72, https://github.com/glue-viz/glue-wwt/pull/73]
- 
- Added initial support for using glue-wwt in Jupyter. [https://github.com/glue-viz/glue-wwt/pull/64]
- 

#### Bug Fixes

- Fixed compatibility with glue-core 1.0. [https://github.com/glue-viz/glue-wwt/pull/77]
- 
- Fixed a bug that caused altitude unit to not work correctly on Windows. [https://github.com/glue-viz/glue-wwt/pull/74]
- 
- Fixed a bug related to reloading sessions with WWT viewers. [https://github.com/glue-viz/glue-wwt/pull/76]
- 

## [0.4](https://github.com/glue-viz/glue-wwt/compare/v0.3...v0.4) - 2019-06-23

### What's Changed

#### Bug Fixes

- Fixed bug with layer centering when NaN values are present. [https://github.com/glue-viz/glue-wwt/pull/55]
- 
- Fixed issues with layer visibility. [https://github.com/glue-viz/glue-wwt/pull/52]
- 
- Fixed bug that caused remonving layers to not work. [https://github.com/glue-viz/glue-wwt/pull/56]
- 
- Fixed issue with viewer options not being set correctly when loading from a session. [https://github.com/glue-viz/glue-wwt/pull/52]
- 
- Fixed compatibility with the latest developer version of glue. [https://github.com/glue-viz/glue-wwt/pull/52]
- 
- Fixed issue with automatic installation of dependencies. [https://github.com/glue-viz/glue-wwt/pull/52]
- 

## [0.3](https://github.com/glue-viz/glue-wwt/compare/v0.2...v0.3) - 2019-02-27

### What's Changed

#### New Features

- Added support for showing data on the surface of celestial bodies as well as
- in the 3D Solar System/Milky Way/Universe view. [https://github.com/glue-viz/glue-wwt/pull/40, https://github.com/glue-viz/glue-wwt/pull/42]
- 
- Added support for color-coding and changing point size based on attributes
- (requires PyWWT 0.6 or later). [https://github.com/glue-viz/glue-wwt/pull/44]
- 

## [0.2](https://github.com/glue-viz/glue-wwt/compare/v0.1...v0.2) - 2018-12-29

### What's Changed

#### New Features

- Add a Save button to save the current view to a file. [https://github.com/glue-viz/glue-wwt/pull/38]

#### Bug Fixes

- Fix compatibility with latest version of glue. [https://github.com/glue-viz/glue-wwt/pull/25]
- 
- Allow world coordinates to be used for the RA/Dec. [https://github.com/glue-viz/glue-wwt/pull/21]
- 

#### Other Changes

- Make use of PyWWT. [https://github.com/glue-viz/glue-wwt/pull/32, https://github.com/glue-viz/glue-wwt/pull/35]
- 
- Change default foreground and background imagery. [https://github.com/glue-viz/glue-wwt/pull/29]
- 

## [0.1](https://github.com/glue-viz/glue-wwt/releases/tag/v0.1) - 2017-08-23

- Initial release
