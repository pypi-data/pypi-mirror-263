# NameThis

NameThis is a Python utility for generating standardized names for Azure resources based on environmental variables and predefined naming conventions. It uses a JSON file with resource definitions to create names that adhere to constraints such as length, inclusion of specific substrings, and whether dashes are supported. This tool is ideal for developers and cloud architects looking to automate the creation of Azure resources with consistent and meaningful names.

> The naming spec comes from Azure CAF [provider](https://github.com/aztfmod/terraform-provider-azurecaf) for platform engineering.

Source file: https://raw.githubusercontent.com/aztfmod/terraform-provider-azurecaf/main/resourceDefinition.json

Using commit hash `7a79e20720eb5de4a8498f72fe66c854d4cbc391`.

## Features

- **Environment Variable Integration**: Leverages environment variables for dynamic naming based on the deployment context (e.g., development, staging, production).
- **Custom Naming Rules**: Applies custom naming rules defined in a JSON file, allowing for flexibility in how resources are named.
- **Adherence to Constraints**: Ensures generated names meet Azure's naming requirements, such as maximum length and character restrictions.

## Prerequisites

Before you begin, ensure you have the following:

- Python 3.6 or later
- Access to the terminal or command prompt

## Installation

This package is designed to be used directly from the source code. Clone or download the repository to your local machine to get started.

## Configuration

1. **Environment Variables**: Set the following environment variables to influence the naming conventions:
   - `LZID`: A 4-digit identifier for your landing zone.
        - Author uses [`lzid`](https://pypi.org/project/lzid) for this.
   - `ENVIRONMENT`: Your deployment environment (e.g., dev, prod, lab).
   - `LOCATION_SHORT`: A 3-letter code representing the deployment location (e.g., uae, nzn).

2. **Resource Definitions JSON**: The `resourceDefinition.json` file sourced as described above. Defines properties such as `slug`, `max_length`, and whether dashes are supported.

## Usage

To run NameThis, navigate to the script's directory and execute:

## From the CLI
```bash
python namethis.py --pretty-print
```

The script will read the resourceDefinition.json file and environment variables, then print the generated resource names set to the console.

## From your Python code
Try it:
```python
from namethis import namethis

print(json.dumps(namethis(), indent=4, sort_keys=True))
```

You can then use it for real:
```python
from namethis import namethis

nameset=namethis()

container = sdk.createContainer(name=nameset['storage_container'])
```

## Customization

Modify/Replace the `resourceDefinition.json` file to include your specific resource naming requirements. Use the URL above or follow the sample below.

```json
[
  {
    "name": "exampleResource",
    "slug": "exrsrc",
    "max_length": 20,
    "dashes": false,
    "scope": "global"
  }
]
```

## Contributing

Contributions are welcome! Feel free to fork the repository and submit pull requests. For major changes or questions, please open an issue first to discuss what you would like to change.
License

This project is licensed under the MIT License - see the LICENSE file for details.