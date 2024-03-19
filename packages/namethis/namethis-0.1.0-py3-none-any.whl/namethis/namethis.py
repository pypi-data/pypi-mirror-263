import json
import os
import sys
import argparse
from importlib.resources import files

def fetch_environment_variables():
    lzid = os.getenv('LZID', "0000").lower()
    if not lzid.isdigit() or len(lzid) != 4:
        sys.exit(f"Error: LZID must be a 4-digit number. Provided value was: {lzid}")
    environment = os.getenv('ENVIRONMENT', 'UAT').lower()
    location_short = os.getenv('LOCATION_SHORT', 'aue').lower()[:3]
    return lzid, environment, location_short

def load_resource_definition():
    try:
        data_files = files('namethis').joinpath('data/resourceDefinition.json')
        return json.loads(data_files.read_text())
    except IOError as e:
        sys.exit(f"Error reading file {data_files}: {e}")

def generate_resource_name(slug, max_length, supports_dashes, scope, lzid, environment, location_short):
    separator = '-' if supports_dashes else ''
    parts = [slug]

    if scope != 'global':
        parts.append(location_short)

    parts += [environment, lzid]  # Tentatively include environment and lzid
    resource_name = separator.join(parts)

    if len(resource_name) > max_length:
        if scope != 'global':
            # Calculate space for environment with consideration of reducing a separator if needed
            separator_count = 3 if supports_dashes else 0
            env_allowed_length = max_length - len(slug) - len(lzid) - len(location_short) - separator_count
            if env_allowed_length < 3:
                # Remove environment part and adjust for one less separator
                parts.pop(-2)  # Remove environment part
                separator_count -= 1  # Adjust separator count
            else:
                parts[-2] = environment[:env_allowed_length]  # Truncate environment part to fit
        else:
            parts.pop(-2)  # For global, remove environment (location_short not included)

        resource_name = separator.join(parts)[:max_length]

        # Further adjustments if still too long, focusing on truncating slug
        if len(resource_name) > max_length:
            slug_allowed_length = max_length - len(lzid) - (1 if supports_dashes and scope != 'global' else 0)
            if scope != 'global' and environment in parts:
                slug_allowed_length -= len(environment) + 1  # Adjust for environment and its separator
            parts[0] = slug[:slug_allowed_length]
            resource_name = separator.join(parts)[:max_length]

    return resource_name.lower()

def parse_args():
    parser = argparse.ArgumentParser(description="Generate Azure resource names based on specifications.")
    parser.add_argument("--pretty-print", action="store_true", help="Pretty print the resource names to stdout.")
    return parser.parse_args()

def namethis():
    args = parse_args()
    lzid, environment, location_short = fetch_environment_variables()
    resources_definition = load_resource_definition()
    
    resource_names = {
        resource['name'].replace('azurerm_', '').lower(): generate_resource_name(
            resource['slug'], 
            resource['max_length'], 
            resource['dashes'], 
            resource['scope'], 
            lzid, 
            environment, 
            location_short
        ) for resource in resources_definition
    }
    
    if args.pretty_print:
        print(json.dumps(resource_names, indent=4, sort_keys=True))
    else:
        return resource_names

if __name__ == "__main__":
    namethis()
