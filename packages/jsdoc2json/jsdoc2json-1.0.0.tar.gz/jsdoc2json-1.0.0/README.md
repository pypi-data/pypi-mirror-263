# jsdoc2json

`jsdoc2json` is a Python tool designed for Game Maker developers. It serves to convert JSDoc comments from Game Maker Language (GML) files into a structured JSON format. With jsdoc2json, you can easily extract and transform JSDoc comments, making it easier to analyze and integrate their code documentation into other systems or workflows.

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [Example](#example)
4. [Project Structure](#project-structure)
5. [Contributing](#contributing)
6. [License](#license)

## Installation

Install `jsdoc2json` using the following command:

```bash
pip install jsdoc2json
```

## Usage

Usage:

```bash
python -m jsdoc2json (-file FILE_PATH | -folder FOLDER_PATH) -output OUTPUT_PATH [-debug]
```

## Example

### Single File Conversion

To convert a single GML file "Player.gml" and save it as "Player.json":

```bash
python -m jsdoc2json -file Player.gml -output ./documentation_folder
```

**Input: `Player.gml`**

```gml
/**
 * @function                   player_move
 * @description                Move the player in the given direction
 * @param {Real}  a            The speed of the player
 * @param {Real}  b            The direction of the player
 * @return {Array<Real>}       The new coordinates
 */
function player_move(speed, direction) {
    player.x += speed * cos(player.direction);
    player.y += speed * sin(player.direction);
	return [player.x, player.y];
}
```

**Output: `Player.json`**

```json
{
    "jsdoc": [
        {
            "function_tag": {
                "description": "player_move"
            },
            "description_tag": {
                "description": "Move the player in the given direction"
            },
            "param_tags": [
                {
                    "name": "a",
                    "type": "Real",
                    "description": "The speed of the player"
                },
                {
                    "name": "b",
                    "type": "Real",
                    "description": "The direction of the player"
                }
            ],
            "return_tag": {
                "type": "Array Real",
                "description": "The new coordinates"
            }
        }
    ]
}
```

### Folder Conversion

To convert all GML files within a Game Maker project "My_project":

```bash
python -m jsdoc2json -folder ./My_project -output ./documentation_folder
```

## Project Structure

The `jsdoc2json` project directory structure:

```
jsdoc2json/
│
├── main.py
│
├── modules/
│   ├── jsdoc_data.py
│   ├── lexical_parser.py
│   ├── lexical_regex.py
│   ├── lexical_tokens.py
│   └── syntax_parser.py
│
└── data/
    ├── input/
    │   ├── test1.gml
    │   ├── test2.gml
    │   ├── Player.gml
    │   └── folder_containing_tests
    │       ├── test3.gml
    |       └── folder_containing_tests
    |           └── test4.gml
    └── output/
        ├── test1.json
        ├── test2.json
        └── Player.json
```

## Contributing

### Reporting Bugs

If you encounter a bug, please open an issue on our [issue tracker](https://github.com/Cooleure/jsdoc2json/issues) and provide detailed information about the bug, including how to reproduce it.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.