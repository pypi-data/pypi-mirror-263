# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## 0.8.1 - 2024-03-22

### Added

- Add documentation section to readme.

### Changed

- Improve package level help documentation.

## 0.8.0 - 2024-03-08

### Added

- Export `Child` type from package.
- Add `py.typed` file for external tooling (i.e. mypy).

## 0.7.0 - 2024-02-29

### Added

- Add documentation for `form` and `label` elements.

## 0.6.0 - 2024-02-22

### Added

- Add `html5` component for improved HTML document creation.

## Fixed

- Specify which files to include in the `sdist` target build.

## 0.5.0 - 2024-02-21

### Added

- Add type support and documentation for most common elements.

### Changed

- Rename `HtmlElement` protocol type to `SupportsHtml`.
- Make doctype prefix lowercase for `<html>` element.

## Fixed

- Copypasta in `<link>` element attribute docstring.
- Adapt bad attribute type error message.

## 0.4.0 - 2024-02-14

### Added

- Separate void elements into their own `VoidElement` class.
- Add typing for HTML global attributes.
- Add type support and documentation for known void elements.
- Expose `Html` and `HtmlElement` types.

### Fixed

- Support integer attribute value when serializing.

## 0.3.0 - 2024-01-16

### Added

- Do not render children if value is `False` or `None`.
- Render `Html` new type based on the `str` type.
- Support iterable as element child.

## 0.2.0 - 2024-01-09

### Added

- Add special `fragment` tag element.
- Prepend html DOCTYPE to `html` tag element.

## 0.1.0 - 2024-01-06

### Added

- Add `Element` class for lazily building HTML elements.
- Handle reserved words in attributes.
- Support self closing void elements.
- Escape inner HTML and attribute values.
