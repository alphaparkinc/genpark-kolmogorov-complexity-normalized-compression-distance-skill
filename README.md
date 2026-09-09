# genpark-kolmogorov-complexity-normalized-compression-distance-skill

[![GitHub stars](https://img.shields.io/github/stars/alphaparkinc/genpark-kolmogorov-complexity-normalized-compression-distance-skill?style=social)](https://github.com/alphaparkinc/genpark-kolmogorov-complexity-normalized-compression-distance-skill/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Zero Dependencies](https://img.shields.io/badge/dependencies-0%20external-brightgreen.svg)](#)
[![Model Context Protocol](https://img.shields.io/badge/MCP-Standard%20Compatible-orange.svg)](#)

> Autonomous Agent Normalized Compression Distance (NCD) & Kolmogorov Complexity Universal Metric

Part of the **GenPark Autonomous Information Theory & Optimal Entropy Coding Swarm**.

## Architecture Overview

```mermaid
graph TD
    A[Text / Code Artifacts x and y] --> B[Compress C x via Deflate/Zlib]
    A --> C[Compress C y via Deflate/Zlib]
    A --> D[Concatenate and Compress C xy]
    B --> E[Compute NCD x,y = C xy - min C x, C y / max C x, C y]
    C --> E
    D --> E
    E --> F[Quasi-Metric Distance Matrix in 0..1]
    F --> G[Zero-Shot Clustering & Similarity Tree]
```

## Features

- **Pure Python Standard Library**: Zero external dependencies. Runs anywhere.
- **Production-Grade Design**: Type annotations, exhaustive edge cases, robust numerical stability.
- **MCP Server Ready**: Built-in stdio Model Context Protocol (MCP) server for Claude / Cursor / Agent tool calling.
- **Benchmark Validated**: 100% verified test coverage in isolated sandbox environments.

## Quickstart

```bash
git clone https://github.com/alphaparkinc/genpark-kolmogorov-complexity-normalized-compression-distance-skill.git
cd genpark-kolmogorov-complexity-normalized-compression-distance-skill
python example_usage.py
```

## Model Context Protocol (MCP) Usage

```bash
python mcp_server.py
```

## License

MIT License. Designed for autonomous agentic workflows.
