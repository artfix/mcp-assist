# Domain Registry Implementation Guide

## Overview

The Domain Registry is a centralized system for managing Home Assistant domain and service definitions in the ha-lmstudio-mcp integration. It replaces hardcoded domain lists with a maintainable, extensible registry pattern.

## Architecture

### Files

- **`domain_registry.py`**: Core registry containing all domain definitions, services, and validation logic
- **`mcp_server.py`**: Updated to use domain registry for validation instead of hardcoded lists

### Key Components

1. **DOMAIN_REGISTRY**: Dictionary containing all domain configurations
2. **Validation Functions**: Check if domain/action combinations are valid
3. **Action Mapping**: Maps common aliases to correct service names
4. **Type Classification**: Categorizes domains as controllable, read-only, or service-only

## Supported Domains (45 Total)

### By Priority

- **P1 Essential (8)**: light, switch, cover, climate, lock, scene, script, automation
- **P2 Common (9)**: fan, media_player, vacuum, alarm_control_panel, camera, sensor, binary_sensor, device_tracker
- **P3 Standard (11)**: input_*, timer, counter, person, zone, group
- **P4 Extended (8)**: select, number, button, update, text, date, time, datetime
- **P5 Specialized (9)**: water_heater, humidifier, siren, valve, lawn_mower, weather, sun, notify, tts

### By Type

- **Controllable (38)**: Domains that can change state
- **Read-only (4)**: sensor, binary_sensor, weather, sun
- **Service-only (3)**: notify, tts, persistent_notification

## Usage Examples

### Basic Light Control
```python
# User says: "Turn on the lights"
domain = "light"
action = "turn_on"  # or "activate" - will be mapped to "turn_on"
```

### Vacuum Control with Aliases
```python
# User says: "Clean the house"
domain = "vacuum"
action = "clean"  # Will be mapped to "start"

# User says: "Send vacuum home"
domain = "vacuum"
action = "home"  # Will be mapped to "return_to_base"
```

### Read-only Domain Handling
```python
# User says: "Turn on the temperature sensor"
domain = "sensor"
action = "turn_on"
# Returns error: "Sensors are read-only. Use 'get_entity_details' to read values."
```

## Action Aliases

The registry supports common action aliases that map to proper service names:

| Alias | Maps To | Examples |
|-------|---------|----------|
| activate | turn_on | "Activate lights" |
| deactivate | turn_off | "Deactivate switch" |
| secure | lock | "Secure front door" |
| open | open_cover | "Open garage" |
| play | media_play | "Play music" |
| clean | start | "Clean house" (vacuum) |
| home | return_to_base | "Send vacuum home" |

## Adding New Domains

To add a new domain, edit `domain_registry.py`:

```python
DOMAIN_REGISTRY = {
    # ... existing domains ...
    "new_domain": {
        "type": TYPE_CONTROLLABLE,  # or TYPE_READ_ONLY, TYPE_SERVICE_ONLY
        "priority": PRIORITY_COMMON,  # 1-5
        "services": ["service1", "service2"],
        "parameters": {
            "service1": {
                "required": ["param1"],
                "optional": ["param2"]
            }
        },
        "description": "Description of what this domain controls"
    }
}
```

## API Functions

### Core Functions

- `get_domain_info(domain)`: Get configuration for a domain
- `validate_domain_action(domain, action)`: Check if action is valid
- `map_action_to_service(domain, action)`: Map aliases to service names
- `get_supported_domains(priority=None)`: List domains by priority
- `get_domains_by_type(type)`: Get domains of specific type

### Validation Example

```python
from domain_registry import validate_domain_action

# Check if an action is valid
valid, result = validate_domain_action("light", "turn_on")
if valid:
    service_name = result  # "turn_on"
else:
    error_message = result  # Error description
```

## Benefits

1. **Maintainability**: Single source of truth for domains
2. **Extensibility**: Easy to add new domains/services
3. **Better UX**: Helpful error messages with suggestions
4. **Flexibility**: Support for action aliases
5. **Type Safety**: Clear parameter requirements
6. **Documentation**: Self-documenting code structure

## Future Enhancements

1. **Auto-discovery**: Detect available services from HA dynamically
2. **Custom domains**: Allow users to add their own domain mappings
3. **Feature detection**: Check entity capabilities before allowing services
4. **Version compatibility**: Track minimum HA version for services
5. **Service schemas**: Import actual service schemas from HA

## Testing

Run the test suite:
```bash
python3 test_domain_registry.py
```

This validates:
- Domain/action validation
- Action alias mapping
- Error messages
- Statistics generation

## Migration from Old System

The refactoring involved:
1. Extracting hardcoded domain lists from `mcp_server.py`
2. Creating centralized `domain_registry.py`
3. Updating validation to use registry functions
4. Removing enum restriction to allow all domains
5. Enhancing error messages with suggestions

## Summary

The Domain Registry provides a scalable, maintainable solution for managing Home Assistant domains in the MCP integration. It supports 45 domains out of the box with intelligent action mapping and helpful error messages, making it ready for public release while remaining easy to extend.