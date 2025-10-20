<div align="center">

# Trin Decor Pack — Props, Furniture, Signs

Immersive Vehicles (MTS/IV) content pack adding decor items, furniture, signage, and world props to build detailed environments.

</div>

[![Discord](https://img.shields.io/badge/Discord-join-7289DA?logo=discord&logoColor=white)](https://discord.gg/ujQR3wf)
[![Build Status](https://github.com/TheOddlySeagull/Trin-Decor-Pack/actions/workflows/build.yml/badge.svg)](https://github.com/TheOddlySeagull/Trin-Decor-Pack/actions/workflows/build.yml)

## Overview

The Decor Pack delivers hundreds of decorative items and modular elements for supermarkets, bars, workshops, and more. Some items include light effects, storage, seats, and simple animations.

## Download

- GitHub Actions artifacts: each CI run uploads JARs for 1.12.2 and 1.16.5.
- Releases: push a tag (e.g., `v2.2.0`) to trigger a release with attached JARs.

## Requirements

- Minecraft with Immersive Vehicles (MTS/IV)
- Trin Part Pack recommended for complementary parts

## Installation (Players)

1. Install Immersive Vehicles (MTS/IV).
2. Download this pack’s JAR for your MC version.
3. Place it into your `mods` folder.
4. Launch the game.

## Building (Developers)

Prereqs:
- JDK 8
- Git and Gradle wrapper (included)

Quick build:
- Windows: `gradlew.bat buildForge1122 && gradlew.bat buildForge1165`
- Linux/macOS: `./gradlew buildForge1122 && ./gradlew buildForge1165`

Artifacts appear under `out/`.

CI:
- GitHub Actions builds on push/PR, uploads artifacts, and publishes releases on tags.

## Changelog

See [CHANGELOG.md](./CHANGELOG.md) for version history and warnings.

## License & Credits

- Content and branding © TheOddlySeagull and contributors. All rights reserved unless otherwise stated.
- Immersive Vehicles by its respective authors.

## Community

- Discord: https://discord.gg/ujQR3wf
- Issues: Use this repo’s Issues for bugs and feature requests.

---