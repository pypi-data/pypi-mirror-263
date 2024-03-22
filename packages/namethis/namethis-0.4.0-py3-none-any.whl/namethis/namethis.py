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
    location_short = os.getenv('LOCATIONSHORT', 'aue').lower()[:3]
    return lzid, environment, location_short

def load_resource_definition():
    try:
        data_files = files('namethis').joinpath('data/resourceDefinition.json')
        return json.loads(data_files.read_text())
    except IOError as e:
        sys.exit(f"Error reading file {data_files}: {e}")

def generate_resource_name(slug, max_length, supports_dashes, scope, lzid, environment, location_short, instance_number):
    assert slug and lzid, "Slug and LZID are mandatory"
    assert len(lzid) == 4, "LZID must be exactly 4 digits"

    separator = '-' if supports_dashes and max_length >= 16 else ''

    # Adjusting for two-digit instance number in naming, directly integrated.
    instance_suffix = None
    if instance_number is not None:
        assert 1 <= instance_number <= 99, "Instance number must be between 1 and 99"
        instance_suffix = f"{separator}{instance_number:02d}" if instance_number >= 1 else ""
    
    # Start building the name with mandatory parts
    parts = [slug, lzid]
    parts.append(environment)

    # Initially, attempt to include all parts
    if scope != 'global':
        parts.append(location_short)
    elif scope == 'global' and slug in ['st', 'kv']:
        parts.append(location_short)

    # Construct the initial name with separator handling
    initial_name = separator.join(filter(None, parts))
    if instance_suffix is not None:
        initial_name += instance_suffix

    # Function to iteratively remove optional parts and adjust for max_length
    def adjust_name(name, max_len, sep, includes_suffix):
        if len(name) <= max_len:
            return name
        adjusted_parts = parts.copy()  # Work on a copy to avoid modifying the original parts list
        while adjusted_parts and len(name) > max_len:
            # Remove parts from the end (environment or location_short)
            removed_part = adjusted_parts.pop()
            # Special handling when instance_number is considered
            if includes_suffix and removed_part == environment and not supports_dashes:
                name = sep.join(filter(None, adjusted_parts))
                if instance_suffix is not None:
                    name += instance_suffix.replace("-", "")
            else:
                name = sep.join(filter(None, adjusted_parts))
                if instance_suffix is not None:
                    name += instance_suffix
            if len(name) <= max_len:
                return name
        return name[:max_len]  # Final catch-all, in case all optional parts are removed but still exceeding max_length

    # Adjust the name to fit within max_length, taking into account the instance_suffix
    final_name = adjust_name(initial_name, max_length, separator, True)

    return final_name.lower()

def parse_args():
    parser = argparse.ArgumentParser(description="Generate Azure resource names based on specifications.")
    parser.add_argument("--pretty-print", action="store_true", help="Pretty print the resource names to stdout.")
    return parser.parse_args()

def namethis(instance_count=1):
    if instance_count > 1: 
        instance_count += 1 # Adjusting for zero-based index
    args = parse_args()
    lzid, environment, location_short = fetch_environment_variables()
    resources_definition = load_resource_definition()
    
    resource_names = {}
    for resource in resources_definition:
        base_resource_name = resource['name'].replace('azurerm_', '').lower()
        for idx in range(instance_count):
            # Determine whether to append an index suffix and adjust 'location_short' accordingly
            index_suffix = f"{idx}" if idx > 0 else ""
            adjusted_location_short = location_short if idx == 0 else ""

            # Generate the resource name, potentially without 'location_short' for additional instances
            generated_name = generate_resource_name(
                resource['slug'],
                resource['max_length'],
                resource['dashes'],
                resource['scope'],
                lzid,
                environment,
                adjusted_location_short,
                int(index_suffix) if index_suffix else None
            )

            # Append index suffix to the resource name key for additional instances only
            resource_name_key = base_resource_name + index_suffix

            # Ensure the generated name does not exceed 'max_length'
            if len(generated_name) > resource['max_length']:
                print(f"Warning: Generated name '{generated_name}' exceeds max length of {resource['max_length']}. Truncating.")
                generated_name = generated_name[:resource['max_length']]

            resource_names[resource_name_key] = generated_name.lower()
    
    if args.pretty_print:
        print(json.dumps(resource_names, indent=4, sort_keys=True))
    else:
        return resource_names

if __name__ == "__main__":
    namethis()
