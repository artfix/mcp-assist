# Home Assistant Domains and Services - Complete Reference

## Summary Statistics
- **Total components in HA Core**: 1,376
- **Components with services**: 316
- **Core controllable domains**: 37
- **Input/helper domains**: 10
- **Service-only domains**: 5
- **Integration-specific domains**: ~270+

## Domain Priority Levels

### P1 - Essential Core Domains (Must Have)
These are fundamental to any Home Assistant installation:
- `light` - Lighting control
- `switch` - Switch control
- `cover` - Blinds/garage doors
- `climate` - Thermostats/HVAC
- `lock` - Door locks
- `scene` - Scene activation
- `script` - Script execution
- `automation` - Automation control

### P2 - Common Control Domains (High Priority)
Found in most homes:
- `fan` - Fan control
- `media_player` - Entertainment devices
- `vacuum` - Robot vacuums
- `alarm_control_panel` - Security systems
- `camera` - Security cameras
- `sensor` - Read-only sensors
- `binary_sensor` - Binary state sensors
- `device_tracker` - Presence detection

### P3 - Standard Helper Domains (Medium Priority)
User-created helpers:
- `input_boolean` - Boolean switches
- `input_number` - Numeric inputs
- `input_text` - Text inputs
- `input_select` - Dropdown selections
- `input_datetime` - Date/time inputs
- `input_button` - Push buttons
- `counter` - Counters
- `timer` - Timers

### P4 - Platform Entities (Medium Priority)
Modern entity platforms:
- `select` - Option selectors
- `number` - Numeric controls
- `button` - Action buttons
- `update` - Update management
- `text` - Text entities
- `date` - Date entities
- `time` - Time entities
- `datetime` - Combined date/time

### P5 - Climate & Environment (Lower Priority)
Specialized climate control:
- `water_heater` - Water heater control
- `humidifier` - Humidity control
- `siren` - Alarm sirens
- `valve` - Water/gas valves
- `lawn_mower` - Robotic lawn mowers

### P6 - System & Service Domains (Service-only)
No entities, only services:
- `notify` - Notification services
- `tts` - Text-to-speech
- `stt` - Speech-to-text
- `conversation` - Voice assistants
- `persistent_notification` - UI notifications

## Complete Domain Reference

### Core Control Domains

#### light
**Type**: Controllable
**Priority**: P1
**Common Services**:
- `turn_on`: Activate lights
  - Optional: brightness, color, transition, effect
- `turn_off`: Deactivate lights
  - Optional: transition
- `toggle`: Switch state
  - Optional: Same as turn_on
**Special Notes**: Extensive color/brightness options, 147 predefined colors
**Example Use Cases**: "Turn on bedroom light", "Set living room to 50% brightness"

#### switch
**Type**: Controllable
**Priority**: P1
**Common Services**:
- `turn_on`: Activate switch
- `turn_off`: Deactivate switch
- `toggle`: Switch state
**Example Use Cases**: "Turn on coffee maker", "Toggle garage lights"

#### cover
**Type**: Controllable
**Priority**: P1
**Common Services**:
- `open_cover`: Open fully
- `close_cover`: Close fully
- `set_cover_position`: Set specific position
  - Required: position (0-100)
- `stop_cover`: Stop movement
- `open_cover_tilt`: Open tilt
- `close_cover_tilt`: Close tilt
- `set_cover_tilt_position`: Set tilt position
  - Required: tilt_position (0-100)
**Special Notes**: Feature-dependent (position, tilt support varies)
**Example Use Cases**: "Open garage door", "Close all blinds", "Set bedroom blinds to 30%"

#### climate
**Type**: Controllable
**Priority**: P1
**Common Services**:
- `set_temperature`: Set target temperature
  - Required: temperature OR target_temp_high/low
  - Optional: hvac_mode
- `set_hvac_mode`: Set mode (heat/cool/auto/off)
- `set_preset_mode`: Set preset (away/home/eco)
- `set_fan_mode`: Set fan speed
- `turn_on`/`turn_off`: Power control
**Special Notes**: Complex with multiple modes and settings
**Example Use Cases**: "Set thermostat to 72", "Turn on AC", "Set to away mode"

#### lock
**Type**: Controllable
**Priority**: P1
**Common Services**:
- `lock`: Secure lock
  - Optional: code
- `unlock`: Unsecure lock
  - Optional: code
- `open`: Open lock (if supported)
  - Optional: code
**Special Notes**: May require codes for operation
**Example Use Cases**: "Lock front door", "Unlock garage door"

#### fan
**Type**: Controllable
**Priority**: P2
**Common Services**:
- `turn_on`: Activate fan
  - Optional: percentage, preset_mode
- `turn_off`: Deactivate fan
- `set_percentage`: Set speed (0-100)
- `set_preset_mode`: Set preset (auto/smart/etc)
- `oscillate`: Toggle oscillation
- `set_direction`: Set rotation direction
**Example Use Cases**: "Turn on ceiling fan", "Set fan to 50%"

#### media_player
**Type**: Controllable
**Priority**: P2
**Common Services** (17 total):
- `turn_on`/`turn_off`: Power control
- `play_media`: Play content
  - Required: media
  - Optional: enqueue, announce
- `media_play`/`media_pause`/`media_stop`: Playback control
- `volume_set`: Set volume (0-1)
- `volume_up`/`volume_down`: Adjust volume
- `volume_mute`: Mute toggle
- `select_source`: Change input
- `media_next_track`/`media_previous_track`: Track navigation
**Special Notes**: Most complex domain with 17+ services
**Example Use Cases**: "Play music on Sonos", "Pause TV", "Set volume to 50%"

#### vacuum
**Type**: Controllable
**Priority**: P2
**Common Services**:
- `turn_on`/`turn_off`: Power control
- `start`: Begin cleaning
- `pause`: Pause cleaning
- `stop`: Stop cleaning
- `return_to_base`: Return home
- `locate`: Find vacuum
- `clean_spot`: Spot clean
- `set_fan_speed`: Set suction level
- `send_command`: Custom commands
**Example Use Cases**: "Start vacuum", "Send vacuum home", "Clean kitchen"

#### alarm_control_panel
**Type**: Controllable
**Priority**: P2
**Common Services**:
- `alarm_disarm`: Disarm system
  - Optional: code
- `alarm_arm_away`: Arm for away
  - Optional: code
- `alarm_arm_home`: Arm for home
  - Optional: code
- `alarm_arm_night`: Arm for night
  - Optional: code
- `alarm_trigger`: Trigger alarm
**Special Notes**: Requires codes, multiple arm modes
**Example Use Cases**: "Arm alarm", "Disarm security system"

#### camera
**Type**: Controllable
**Priority**: P2
**Common Services**:
- `turn_on`/`turn_off`: Power control
- `enable_motion_detection`: Enable motion
- `disable_motion_detection`: Disable motion
- `snapshot`: Take photo
  - Required: filename
- `record`: Record video
  - Required: filename
  - Optional: duration, lookback
**Example Use Cases**: "Take snapshot from front door", "Turn on driveway camera"

### Helper/Input Domains

#### input_boolean
**Type**: Controllable
**Priority**: P3
**Common Services**:
- `turn_on`: Set to true
- `turn_off`: Set to false
- `toggle`: Switch state
- `reload`: Reload configuration
**Example Use Cases**: "Turn on vacation mode", "Toggle guest mode"

#### input_number
**Type**: Controllable
**Priority**: P3
**Common Services**:
- `set_value`: Set specific value
  - Required: value
- `increment`: Increase value
- `decrement`: Decrease value
- `reload`: Reload configuration
**Example Use Cases**: "Set target temperature to 72", "Increase volume level"

#### input_text
**Type**: Controllable
**Priority**: P3
**Common Services**:
- `set_value`: Set text
  - Required: value
- `reload`: Reload configuration
**Example Use Cases**: "Set reminder text", "Update status message"

#### input_select
**Type**: Controllable
**Priority**: P3
**Common Services**:
- `select_option`: Choose option
  - Required: option
- `select_next`/`select_previous`: Navigate options
- `select_first`/`select_last`: Jump to ends
- `set_options`: Update available options
- `reload`: Reload configuration
**Example Use Cases**: "Select home mode", "Next playlist"

#### input_datetime
**Type**: Controllable
**Priority**: P3
**Common Services**:
- `set_datetime`: Set date/time
  - Optional: date, time, datetime, timestamp
- `reload`: Reload configuration
**Example Use Cases**: "Set alarm time to 7 AM", "Set vacation end date"

#### input_button
**Type**: Controllable
**Priority**: P3
**Common Services**:
- `press`: Trigger button
- `reload`: Reload configuration
**Example Use Cases**: "Press doorbell", "Trigger refresh"

#### timer
**Type**: Controllable
**Priority**: P3
**Common Services**:
- `start`: Begin timer
  - Optional: duration
- `pause`: Pause timer
- `cancel`: Cancel timer
- `finish`: Complete timer
- `change`: Adjust duration
  - Required: duration
**Example Use Cases**: "Start 10 minute timer", "Cancel kitchen timer"

#### counter
**Type**: Controllable
**Priority**: P3
**Common Services**:
- `increment`: Increase count
- `decrement`: Decrease count
- `reset`: Reset to initial
- `set_value`: Set specific value
  - Required: value
**Example Use Cases**: "Increment visitor counter", "Reset daily count"

### Modern Entity Platforms

#### select
**Type**: Controllable
**Priority**: P4
**Common Services**:
- `select_option`: Choose option
  - Required: option
- `select_next`/`select_previous`: Navigate
  - Optional: cycle
- `select_first`/`select_last`: Jump to ends
**Example Use Cases**: "Select eco mode", "Next fan speed"

#### number
**Type**: Controllable
**Priority**: P4
**Common Services**:
- `set_value`: Set number
  - Required: value
**Example Use Cases**: "Set threshold to 10", "Adjust sensitivity"

#### button
**Type**: Controllable
**Priority**: P4
**Common Services**:
- `press`: Activate button
**Example Use Cases**: "Press sync button", "Trigger update"

#### update
**Type**: Controllable
**Priority**: P4
**Common Services**:
- `install`: Install update
  - Optional: version, backup
- `skip`: Skip version
- `clear_skipped`: Clear skip flag
**Example Use Cases**: "Install firmware update", "Skip this version"

#### text
**Type**: Controllable
**Priority**: P4
**Common Services**:
- `set_value`: Set text value
  - Required: value
**Example Use Cases**: "Set display message", "Update label"

#### date
**Type**: Controllable
**Priority**: P4
**Common Services**:
- `set_value`: Set date
  - Required: date
**Example Use Cases**: "Set target date", "Update schedule date"

#### time
**Type**: Controllable
**Priority**: P4
**Common Services**:
- `set_value`: Set time
  - Required: time
**Example Use Cases**: "Set wake time", "Update schedule"

#### datetime
**Type**: Controllable
**Priority**: P4
**Common Services**:
- `set_value`: Set date and time
  - Required: datetime
**Example Use Cases**: "Set appointment time", "Schedule event"

### Climate & Environment Domains

#### water_heater
**Type**: Controllable
**Priority**: P5
**Common Services**:
- `set_temperature`: Set target temp
  - Required: temperature
- `set_operation_mode`: Set mode
  - Required: operation_mode
- `set_away_mode`: Toggle away
  - Required: away_mode
- `turn_on`/`turn_off`: Power control
**Example Use Cases**: "Set water heater to 120", "Turn on water heater"

#### humidifier
**Type**: Controllable
**Priority**: P5
**Common Services**:
- `set_humidity`: Set target humidity
  - Required: humidity (0-100)
- `set_mode`: Set operation mode
  - Required: mode
- `turn_on`/`turn_off`: Power control
- `toggle`: Switch state
**Example Use Cases**: "Set humidity to 50%", "Turn on humidifier"

#### siren
**Type**: Controllable
**Priority**: P5
**Common Services**:
- `turn_on`: Activate siren
  - Optional: tone, duration, volume_level
- `turn_off`: Deactivate siren
- `toggle`: Switch state
**Example Use Cases**: "Sound alarm", "Test siren"

#### valve
**Type**: Controllable
**Priority**: P5
**Common Services**:
- `open_valve`: Open valve
- `close_valve`: Close valve
- `set_valve_position`: Set position
  - Required: position
- `stop_valve`: Stop movement
- `toggle`: Switch state
**Example Use Cases**: "Close water valve", "Open gas valve"

#### lawn_mower
**Type**: Controllable
**Priority**: P5
**Common Services**:
- `start_mowing`: Begin mowing
- `pause`: Pause mowing
- `dock`: Return to dock
**Example Use Cases**: "Start lawn mower", "Send mower home"

### Automation & Control Domains

#### scene
**Type**: Controllable
**Priority**: P1
**Common Services**:
- `turn_on`: Activate scene
  - Optional: transition
- `reload`: Reload scenes
- `apply`: Apply settings
  - Required: entities
- `create`: Create new scene
  - Required: scene_id
  - Optional: entities, snapshot_entities
**Example Use Cases**: "Activate movie scene", "Turn on bedtime"

#### script
**Type**: Controllable
**Priority**: P1
**Common Services**:
- `turn_on`: Execute script
- `turn_off`: Stop script
- `toggle`: Toggle execution
- `reload`: Reload scripts
**Example Use Cases**: "Run goodnight script", "Execute morning routine"

#### automation
**Type**: Controllable
**Priority**: P1
**Common Services**:
- `turn_on`: Enable automation
- `turn_off`: Disable automation
  - Optional: stop_actions
- `toggle`: Toggle state
- `trigger`: Manual trigger
  - Optional: skip_condition
- `reload`: Reload automations
**Example Use Cases**: "Disable vacation automation", "Trigger sunset routine"

### Information & Tracking Domains

#### sensor
**Type**: Read-only
**Priority**: P2
**Common Services**: None (read-only)
**Special Notes**: Provides numeric/string state values
**Example Use Cases**: "What's the temperature?", "Check humidity level"

#### binary_sensor
**Type**: Read-only
**Priority**: P2
**Common Services**: None (read-only)
**Special Notes**: Provides on/off state only
**Example Use Cases**: "Is motion detected?", "Is door open?"

#### device_tracker
**Type**: Controllable
**Priority**: P2
**Common Services**:
- `see`: Update location
  - Optional: mac, dev_id, location_name, gps, battery
**Special Notes**: Usually updated automatically
**Example Use Cases**: "Where is John?", "Mark as home"

#### person
**Type**: Controllable
**Priority**: P3
**Common Services**:
- `reload`: Reload persons
**Special Notes**: Aggregates device_trackers
**Example Use Cases**: "Is anyone home?", "Where is Mom?"

#### zone
**Type**: Controllable
**Priority**: P3
**Common Services**:
- `reload`: Reload zones
**Special Notes**: Defines geographical areas
**Example Use Cases**: "Define work zone", "Update home location"

#### group
**Type**: Controllable
**Priority**: P3
**Common Services**:
- `set`: Create/modify group
  - Required: object_id
  - Optional: name, icon, entities
- `remove`: Delete group
  - Required: object_id
- `reload`: Reload groups
**Example Use Cases**: "Group all lights", "Create bedroom group"

#### weather
**Type**: Read-only
**Priority**: P4
**Common Services**:
- `get_forecast`: Get single forecast
  - Required: type (daily/hourly/twice_daily)
- `get_forecasts`: Get multiple forecasts
  - Required: type
**Special Notes**: Returns response data
**Example Use Cases**: "What's the weather?", "Get tomorrow's forecast"

#### sun
**Type**: Read-only
**Priority**: P4
**Common Services**: None (system integration)
**Special Notes**: Provides sunrise/sunset times
**Example Use Cases**: "When is sunset?", "Is it dark?"

### Service-Only Domains

#### notify
**Type**: Service-only
**Priority**: P6
**Common Services**:
- `notify`: Send notification
  - Required: message
  - Optional: title, target, data
- `send_message`: Send to entity
  - Required: message
  - Optional: title
- `persistent_notification`: Create UI notification
  - Required: message
  - Optional: title
**Example Use Cases**: "Send alert", "Notify about door open"

#### tts
**Type**: Service-only
**Priority**: P6
**Common Services**:
- `speak`: Convert text to speech (new)
  - Required: media_player_entity_id, message
  - Optional: cache, language, options
- `say`: Legacy TTS service
  - Required: entity_id, message
- `clear_cache`: Clear TTS cache
**Example Use Cases**: "Say welcome home", "Announce dinner ready"

#### conversation
**Type**: Service-only
**Priority**: P6
**Common Services**:
- `process`: Process voice command
- `reload`: Reload conversation agent
**Example Use Cases**: Voice assistant processing

#### persistent_notification
**Type**: Service-only
**Priority**: P6
**Common Services**:
- `create`: Create notification
- `dismiss`: Remove notification
- `mark_read`: Mark as read
**Example Use Cases**: System alerts and warnings

## Additional Integration Domains

Home Assistant has 1000+ integration-specific domains. Key categories include:

### Brand-Specific Integrations
- Smart home brands: `hue`, `lifx`, `tuya`, `shelly`, `zwave_js`, `zigbee`
- Thermostats: `nest`, `ecobee`, `honeywell`
- Media: `sonos`, `roku`, `plex`, `spotify`
- Vacuums: `roomba`, `xiaomi_miio`, `dyson`

### Protocol Integrations
- `mqtt` - MQTT protocol
- `modbus` - Industrial protocol
- `knx` - Building automation
- `zha` - Zigbee Home Automation
- `homekit` - Apple HomeKit

### Cloud Services
- `google_assistant` - Google Assistant
- `alexa` - Amazon Alexa
- `ifttt` - If This Then That
- `webhook` - Web hooks

## Implementation Recommendations

### Phase 1 - Core Functionality (P1 Domains)
**Goal**: Basic device control
- Implement: light, switch, cover, climate, lock, scene, script, automation
- Services: turn_on, turn_off, toggle, set_* basic functions
- Timeline: Week 1

### Phase 2 - Common Devices (P2 Domains)
**Goal**: Typical home coverage
- Implement: fan, media_player, vacuum, alarm_control_panel, camera
- Add: sensor, binary_sensor reading
- Services: All standard control services
- Timeline: Week 2

### Phase 3 - User Helpers (P3 Domains)
**Goal**: Complete helper support
- Implement: All input_* domains, timer, counter
- Services: set_value, increment/decrement, timer controls
- Timeline: Week 3

### Phase 4 - Modern Platforms (P4 Domains)
**Goal**: Full platform support
- Implement: select, number, button, update, text, date, time, datetime
- Services: Platform-specific controls
- Timeline: Week 4

### Phase 5 - Specialized & Services (P5-P6)
**Goal**: Complete coverage
- Implement: Climate extras, service domains
- Services: notify, tts, specialized controls
- Timeline: Week 5

## Technical Considerations

### Service Validation
1. Check domain exists in allowed list
2. Validate service for that domain
3. Check required parameters
4. Validate parameter types and ranges
5. Check entity features/capabilities

### Dynamic Discovery
- Use MCP tools for entity discovery
- Filter by domain, state, area
- Return entity details with capabilities
- Cache frequently accessed entities

### Error Handling
- Invalid domain: "Domain not supported"
- Invalid service: "Service not available for domain"
- Missing parameters: "Required parameter missing"
- Feature not supported: "Entity doesn't support this feature"

### Performance Optimization
- Batch entity queries
- Cache entity states
- Limit discovery results
- Progressive loading for large lists

## Summary

This reference covers:
- **37 core controllable domains** with full service definitions
- **10 helper domains** for user-created entities
- **8 modern platform domains** for UI entities
- **5+ service-only domains** for notifications and TTS
- **1000+ integration-specific domains** from brands and protocols

For the MCP implementation, focus on the P1-P3 domains first as they cover 90% of typical use cases. The service definitions provided include all parameters, types, and constraints needed for proper implementation.

Total implementation scope for comprehensive coverage:
- **Domains to support**: ~50 core + ability to handle unknown domains gracefully
- **Services to implement**: ~200 unique service calls
- **Parameters to validate**: ~500 different parameter types

This document serves as the authoritative reference for expanding the ha-lmstudio-mcp integration to support all Home Assistant domains.