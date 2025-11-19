#!/usr/bin/env python3
"""Fix OpenAPI specification issues:
1. Generate unique operationIds from paths
2. Fix schema issues (inline enums should be in components/schemas)
3. Fix missing schema references
"""

import json
import re
from pathlib import Path


def path_to_operation_id(path: str, method: str) -> str:
    """Generate a unique operationId from path and method."""
    # Remove /api prefix and /v1, /v2 suffixes
    path_clean = path.replace('/api/', '').replace('/v1', '').replace('/v2', '').replace('/v1_temp', '')
    # Replace slashes and special chars with underscores
    path_clean = re.sub(r'[^a-zA-Z0-9]', '_', path_clean)
    # Remove leading/trailing underscores and collapse multiple underscores
    path_clean = re.sub(r'_+', '_', path_clean).strip('_')
    # Convert to camelCase
    parts = path_clean.split('_')
    operation_id = method.lower() + '_' + '_'.join(parts)
    return operation_id


def fix_operation_ids(spec: dict) -> None:
    """Fix duplicate operationIds by generating unique ones."""
    paths = spec.get('paths', {})
    operation_ids_used = set()
    
    for path, methods in paths.items():
        for method, operation in methods.items():
            if isinstance(operation, dict) and 'operationId' in operation:
                # Generate unique operationId
                base_id = path_to_operation_id(path, method)
                operation_id = base_id
                counter = 1
                while operation_id in operation_ids_used:
                    operation_id = f"{base_id}_{counter}"
                    counter += 1
                
                operation['operationId'] = operation_id
                operation_ids_used.add(operation_id)


def fix_schema_issues(spec: dict) -> None:
    """Fix schema issues by creating missing schemas."""
    components = spec.setdefault('components', {})
    schemas = components.setdefault('schemas', {})
    
    # Create NetworkWithTestnet - includes testnet networks
    # Use NetworkWithAll as base and add testnet if it makes sense
    if 'NetworkWithTestnet' not in schemas:
        network_with_all = schemas.get('NetworkWithAll', {})
        if network_with_all and 'enum' in network_with_all:
            # NetworkWithTestnet likely includes testnet variants
            base_enum = network_with_all['enum']
            # Common pattern: add testnet to each network
            testnet_enum = base_enum + ['testnet']
            schemas['NetworkWithTestnet'] = {
                'type': 'string',
                'enum': testnet_enum
            }
        else:
            # Fallback to Network enum
            network_enum = schemas.get('Network', {}).get('enum', ['finney', 'nakamoto', 'kusanagi'])
            schemas['NetworkWithTestnet'] = {
                'type': 'string',
                'enum': network_enum + ['testnet']
            }
    
    # Create BigDecimal - typically a string representation of large decimal numbers
    if 'BigDecimal' not in schemas:
        schemas['BigDecimal'] = {
            'type': 'string',
            'description': 'Big decimal number represented as string'
        }
    
    # Create LiquidityPositionType - use LiquidityPositionStatus if it exists
    if 'LiquidityPositionType' not in schemas:
        liquidity_status = schemas.get('LiquidityPositionStatus', {})
        if liquidity_status and 'enum' in liquidity_status:
            schemas['LiquidityPositionType'] = {
                'type': 'string',
                'enum': liquidity_status['enum']
            }
        else:
            # Fallback to common values
            schemas['LiquidityPositionType'] = {
                'type': 'string',
                'enum': ['open', 'closed', 'all']
            }
    
    # Create Frequency - use FrequencyBlockHourDay if it exists (most common)
    if 'Frequency' not in schemas:
        freq_block_hour_day = schemas.get('FrequencyBlockHourDay', {})
        if freq_block_hour_day and 'enum' in freq_block_hour_day:
            schemas['Frequency'] = {
                'type': 'string',
                'enum': freq_block_hour_day['enum']
            }
        else:
            # Fallback to common frequency pattern
            schemas['Frequency'] = {
                'type': 'string',
                'enum': ['by_block', 'by_hour', 'by_day']
            }


def fix_parameter_schema_references(spec: dict) -> None:
    """Fix missing schema references in parameters."""
    paths = spec.get('paths', {})
    components = spec.setdefault('components', {})
    schemas = components.setdefault('schemas', {})
    
    for path, methods in paths.items():
        for method, operation in methods.items():
            if not isinstance(operation, dict) or 'parameters' not in operation:
                continue
            
            for param in operation['parameters']:
                if not isinstance(param, dict) or 'schema' not in param:
                    continue
                
                schema = param['schema']
                param_name = param.get('name', '')
                
                # Fix NetworkWithTestnet reference
                if param_name == 'network' and isinstance(schema, dict):
                    if 'enum' in schema:
                        if 'NetworkWithTestnet' not in schemas:
                            schemas['NetworkWithTestnet'] = {
                                'type': 'string',
                                'enum': schema['enum']
                            }
                        param['schema'] = {'$ref': '#/components/schemas/NetworkWithTestnet'}
                
                # Fix LiquidityPositionType reference
                if param_name == 'position_type' and isinstance(schema, dict):
                    if 'enum' in schema:
                        if 'LiquidityPositionType' not in schemas:
                            schemas['LiquidityPositionType'] = {
                                'type': 'string',
                                'enum': schema['enum']
                            }
                        param['schema'] = {'$ref': '#/components/schemas/LiquidityPositionType'}
                
                # Fix Frequency reference
                if param_name == 'frequency' and isinstance(schema, dict):
                    if 'enum' in schema:
                        if 'Frequency' not in schemas:
                            schemas['Frequency'] = {
                                'type': 'string',
                                'enum': schema['enum']
                            }
                        param['schema'] = {'$ref': '#/components/schemas/Frequency'}


def main():
    """Main function to fix OpenAPI spec."""
    spec_path = Path('openapi.json')
    
    print(f"Loading {spec_path}...")
    with open(spec_path, 'r', encoding='utf-8') as f:
        spec = json.load(f)
    
    print("Fixing operationIds...")
    fix_operation_ids(spec)
    
    print("Fixing schema issues...")
    fix_schema_issues(spec)
    
    print("Fixing parameter schema references...")
    fix_parameter_schema_references(spec)
    
    print(f"Saving fixed spec to {spec_path}...")
    with open(spec_path, 'w', encoding='utf-8') as f:
        json.dump(spec, f, indent=2, ensure_ascii=False)
    
    print("Done! Verifying...")
    # Verify no duplicate operationIds
    paths = spec.get('paths', {})
    operation_ids = []
    for path, methods in paths.items():
        for method, operation in methods.items():
            if isinstance(operation, dict) and 'operationId' in operation:
                operation_ids.append(operation['operationId'])
    
    duplicates = [op_id for op_id in operation_ids if operation_ids.count(op_id) > 1]
    if duplicates:
        print(f"WARNING: Still found duplicate operationIds: {set(duplicates)}")
    else:
        print(f"✓ All {len(operation_ids)} operationIds are unique")


if __name__ == '__main__':
    main()

