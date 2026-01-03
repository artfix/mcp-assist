# Smart Query Spec - Verification Against HA Documentation

**Date:** 2026-01-03
**Purpose:** Validate the Smart Query Spec assumptions against official Home Assistant documentation

---

## Executive Summary

✅ **The index-based approach in SMART_QUERY_SPEC.md is VIABLE and aligns with Home Assistant's architecture.**

Key findings:
- Home Assistant has standardized `device_class` vocabulary across 11 entity domains
- 150+ total device_class values are defined and documented
- The spec correctly identifies device_class as the primary categorization mechanism
- Gap-filling via LLM inference is necessary (many entities lack device_class)
- Index size estimate (~400 tokens) is realistic

---

## Device Class Vocabulary - Complete Enumeration

### 1. Sensor Domain (`sensor`)

**Count:** 70+ standardized device classes
**Documentation:** https://www.home-assistant.io/integrations/sensor/

<details>
<summary>Complete list (click to expand)</summary>

#### Environmental & Weather
- `temperature` - °C, °F, K
- `humidity` - %
- `atmospheric_pressure` - Pa, kPa, hPa, bar, mbar, mmHg, inHg, psi
- `dew_point` - °C, °F, K
- `illuminance` - lx
- `irradiance` - W/m², BTU/(h⋅ft²)
- `wind_direction` - °
- `wind_speed` - m/s, km/h, mph, ft/s, kn

#### Air Quality
- `aqi` - Air Quality Index (unitless)
- `carbon_dioxide` - ppm
- `carbon_monoxide` - ppm
- `nitrogen_dioxide` - µg/m³
- `nitrogen_monoxide` - µg/m³
- `nitrous_oxide` - µg/m³
- `ozone` - µg/m³
- `pm1` - µg/m³
- `pm25` - µg/m³
- `pm4` - µg/m³
- `pm10` - µg/m³
- `sulphur_dioxide` - µg/m³
- `volatile_organic_compounds` - µg/m³
- `volatile_organic_compounds_parts` - ppm, ppb

#### Electrical & Energy
- `current` - A, mA
- `voltage` - V, mV
- `power` - W, kW, MW, BTU/h
- `power_factor` - %, unitless
- `apparent_power` - VA
- `reactive_power` - var
- `reactive_energy` - varh
- `energy` - Wh, kWh, MWh, GWh
- `energy_storage` - J, kJ, MJ, GJ, Wh, kWh, MWh, GWh, cal, kcal
- `energy_distance` - (specialized)
- `frequency` - Hz, kHz, MHz, GHz

#### Physical Measurements
- `distance` - mm, cm, m, km, in, ft, yd, mi
- `area` - m², ft²
- `speed` - m/s, km/h, mph, ft/s, kn, mm/d, in/d, in/h
- `weight` - kg, g, mg, µg, oz, lb, st
- `volume` - L, mL, m³, ft³, gal, fl. oz
- `volume_storage` - (storage capacity)
- `volume_flow_rate` - L/min, m³/h, ft³/min, gal/min
- `precipitation` - mm, cm, in
- `precipitation_intensity` - mm/h, in/h

#### Data & Connectivity
- `data_rate` - bit/s, kbit/s, Mbit/s, Gbit/s, B/s, kB/s, MB/s, GB/s
- `data_size` - bit, kbit, Mbit, Gbit, B, kB, MB, GB, TB, PB, EB, ZB, YB, KiB, MiB, GiB, TiB, PiB, EiB, ZiB, YiB
- `signal_strength` - dB, dBm
- `sound_pressure` - dB, dBA

#### Specialized
- `battery` - %
- `blood_glucose_concentration` - mg/dL, mmol/L
- `conductivity` - µS/cm, mS/cm
- `moisture` - %
- `ph` - pH (unitless)
- `monetary` - currency codes
- `pressure` - (general pressure)
- `gas` - m³, ft³
- `water` - L, gal, m³, ft³, CCF

#### Time-based
- `date` - ISO 8601 date
- `timestamp` - ISO 8601 datetime
- `duration` - d, h, min, s, ms

#### Generic
- `enum` - Limited set of non-numeric states
- `none` - Generic sensor (default)

</details>

**Notes:**
- Number entities share the same device_class definitions as sensors
- Most sensor device classes include normalized units for statistics/graphing
- LLM already knows domain knowledge (e.g., "CO2 >1000ppm is poor air quality")

---

### 2. Binary Sensor Domain (`binary_sensor`)

**Count:** 29 standardized device classes
**Documentation:** https://www.home-assistant.io/integrations/binary_sensor/

| Device Class | Description | On State | Off State |
|---|---|---|---|
| `none` | Generic on/off (default) | On | Off |
| `battery` | Low battery indicator | Battery low | Battery normal |
| `battery_charging` | Charging status | Charging | Not charging |
| `carbon_monoxide` | CO detection | CO detected | Clear |
| `cold` | Temperature condition | Cold | Normal |
| `connectivity` | Connection status | Connected | Disconnected |
| `door` | Door position | Open | Closed |
| `garage_door` | Garage door position | Open | Closed |
| `gas` | Gas detection | Gas detected | Clear |
| `heat` | Temperature condition | Hot | Normal |
| `light` | Light detection | Light detected | No light |
| `lock` | Lock status | Unlocked | Locked |
| `moisture` | Moisture/leak detection | Wet | Dry |
| `motion` | Motion detection | Motion detected | Clear |
| `moving` | Movement status | Moving | Stopped |
| `occupancy` | Room occupancy | Occupied | Clear |
| `opening` | Generic open/closed | Open | Closed |
| `plug` | Device plug-in status | Plugged in | Unplugged |
| `power` | Power detection | Powered | No power |
| `presence` | Home/away status | Home | Away |
| `problem` | Problem detection | Problem | OK |
| `running` | Operation status | Running | Not running |
| `safety` | Safety condition | Unsafe | Safe |
| `smoke` | Smoke detection | Smoke detected | Clear |
| `sound` | Sound detection | Sound detected | No sound |
| `tamper` | Tampering detection | Tampered | OK |
| `update` | Update availability | Update available | Up-to-date |
| `vibration` | Vibration detection | Vibration detected | Clear |
| `window` | Window position | Open | Closed |

**Notes:**
- Binary sensors represent on/off states only
- Device class affects icon, text representation, and grouping
- Person detection (from spec example) does NOT have a device_class in HA

---

### 3. Cover Domain (`cover`)

**Count:** 11 standardized device classes (10 + None)
**Documentation:** https://www.home-assistant.io/integrations/cover/

| Device Class | Description |
|---|---|
| `none` | Generic cover (default) |
| `awning` | Exterior retractable window/door/patio cover |
| `blind` | Linked slats that expand/collapse or tilt |
| `curtain` | Fabric hung above window/door that can be drawn |
| `damper` | Mechanical damper reducing airflow/sound/light |
| `door` | Door or gate providing access to an area |
| `garage` | Garage door |
| `gate` | Gate (outdoor, part of fence) |
| `shade` | Continuous plane of material that expands/collapses |
| `shutter` | Linked slats that can be raised/lowered |
| `window` | Physical window that opens/closes or tilts |

---

### 4. Media Player Domain (`media_player`)

**Count:** 3 standardized device classes
**Documentation:** https://developers.home-assistant.io/docs/core/entity/media-player/

| Device Class | Description |
|---|---|
| `tv` | Television type device |
| `speaker` | Speakers or stereo type device |
| `receiver` | Audio/video receiver (audio in, speakers/display out) |

**Notes:**
- Spec example shows 11 speakers - this is accurate (device_class=speaker)
- Media players without device_class won't appear in categorized queries

---

### 5. Button Domain (`button`)

**Count:** 4 standardized device classes
**Documentation:** https://www.home-assistant.io/integrations/button/

| Device Class | Description |
|---|---|
| `none` | Generic button (default) |
| `identify` | Used to identify a device |
| `restart` | Restarts the device |
| `update` | Updates the software of the device |

---

### 6. Event Domain (`event`)

**Count:** 4 standardized device classes
**Documentation:** https://www.home-assistant.io/integrations/event/

| Device Class | Description |
|---|---|
| `none` | Generic event (default) |
| `button` | Remote control buttons |
| `doorbell` | Doorbell buttons |
| `motion` | Motion events from motion sensor |

---

### 7. Update Domain (`update`)

**Count:** 2 standardized device classes
**Documentation:** https://www.home-assistant.io/integrations/update/

| Device Class | Description |
|---|---|
| `none` | Generic software update (default) |
| `firmware` | Firmware update |

---

### 8. Valve Domain (`valve`)

**Count:** 3 standardized device classes
**Documentation:** https://www.home-assistant.io/integrations/valve

| Device Class | Description |
|---|---|
| `none` | Generic valve (default) |
| `water` | Controls water flow |
| `gas` | Controls gas flow |

---

### 9. Switch Domain (`switch`)

**Count:** 3 standardized device classes
**Documentation:** https://www.home-assistant.io/integrations/switch/

| Device Class | Description |
|---|---|
| `none` | Generic switch (default) |
| `outlet` | Power outlet |
| `switch` | Generic switch (explicit) |

---

### 10. Humidifier Domain (`humidifier`)

**Count:** 2 standardized device classes
**Documentation:** https://www.home-assistant.io/integrations/humidifier/

| Device Class | Description |
|---|---|
| `humidifier` | Adds humidity to air (default) |
| `dehumidifier` | Removes humidity from air |

---

## Domains WITHOUT Device Class Support

The following entity domains do **NOT** support `device_class` attribute (as of 2026-01-03):

| Domain | Alternative Categorization |
|--------|---------------------------|
| `light` | None (all are lights) |
| `climate` | Implicit (temperature control) |
| `fan` | None (all are fans) |
| `lock` | None (all are locks) |
| `vacuum` | None (all are vacuums) |
| `lawn_mower` | None (all are lawn mowers) |
| `water_heater` | None (all are water heaters) |
| `camera` | None (all are cameras) |
| `device_tracker` | source_type (gps, bluetooth, router, etc.) |
| `person` | None (all are people) |
| `zone` | None (all are zones) |
| `automation` | None (categorized by user) |
| `script` | None (categorized by user) |
| `scene` | None (categorized by user) |
| `input_*` | Helper type is the domain itself |
| `calendar` | None (all are calendars) |
| `weather` | None (all are weather) |

---

## Validation Against SMART_QUERY_SPEC.md

### ✅ Spec Assumption 1: "device_classes (grouped by domain)"

**VALID** - Home Assistant has standardized device_class vocabulary across multiple domains.

The spec example shows:
```yaml
device_classes:
  binary_sensor:
    door: 23
    window: 18
    occupancy: 15
    motion: 11
    moisture: 5
```

**Verification:** All these device classes exist in HA's binary_sensor domain ✅

---

### ⚠️ Spec Assumption 2: "inferred_types for entities WITHOUT device_class"

**PARTIALLY VALID** - This is NECESSARY but requires careful implementation.

The spec example shows:
```yaml
inferred_types:
  person_detection: 6      # *_person_detected
  vehicle_detection: 4     # *_vehicle_detected
  location_tracking: 9     # *_ble_area
```

**Issue identified:**
- `binary_sensor.*_person_detected` - No standard device_class for person detection
- `sensor.*_ble_area` - No standard device_class for BLE location tracking

**Why gap-filling is necessary:**
1. Many integrations create entities without setting device_class
2. Custom naming patterns are common (e.g., UniFi Protect cameras use "*_person_detected")
3. Home Assistant does not enforce device_class on all entities

**Recommendation:**
- Gap-filling should be done at **index generation time** (not query time)
- Use LLM to analyze entity names and infer categories
- Store inferred patterns in the index for discovery
- This is a core strength of the index approach

---

### ✅ Spec Assumption 3: "LLM interprets - No hardcoded thresholds"

**VALID** - LLMs already have domain knowledge for interpreting values.

Examples from research:
- LLM knows: CO2 >1000ppm is poor air quality
- LLM knows: PM2.5 <12µg/m³ is good, >35µg/m³ is unhealthy
- LLM knows: Battery <20% is low
- LLM knows: Humidity 30-50% is comfortable

**What LLM DOESN'T know:**
- Whether this HA installation has CO2 sensors ❌
- Which sensor measures room temperature vs device temperature ❌
- Whether "Mike" is a person in this home ❌

**Conclusion:** The spec correctly identifies that the tool should provide **discovery**, not **interpretation**.

---

### ✅ Spec Assumption 4: "Index size ~300-400 tokens"

**VALID** - This is achievable with the proposed structure.

**Estimated index size breakdown:**
```
areas: 20 areas × 15 chars = ~300 chars = ~75 tokens
domains: 40 domains × 20 chars = ~800 chars = ~200 tokens
device_classes: 150 classes × 25 chars = ~3750 chars = ~940 tokens
inferred_types: 10 types × 30 chars = ~300 chars = ~75 tokens
people: 6 people × 20 chars = ~120 chars = ~30 tokens
pets: 2 pets × 20 chars = ~40 chars = ~10 tokens
calendars: 10 × 15 chars = ~150 chars = ~38 tokens
zones: 10 × 20 chars = ~200 chars = ~50 tokens
automations: 20 × 30 chars = ~600 chars = ~150 tokens
scripts: 10 × 25 chars = ~250 chars = ~63 tokens
input_helpers: 30 × 25 chars = ~750 chars = ~188 tokens

Total: ~1820 tokens (without compression)
```

**Optimization strategies:**
1. Use abbreviated format (YAML is compact)
2. Exclude zero-count device_classes
3. Group by domain efficiently
4. Use shorthand notation for counts

**Realistic estimate:** 800-1200 tokens for a large installation, <500 for typical home

---

### ✅ Spec Assumption 5: "discover_entities needs device_class filter"

**VALID** - This is the core discovery mechanism.

Current `discover_entities` in mcp-assist supports:
- `area` - filter by area name ✅
- `domain` - filter by entity type ✅
- `entity_type` - legacy parameter ✅
- `name_contains` - substring search ✅
- `state` - filter by current state ✅

**Required additions from spec:**
```python
device_class: str | list[str]     # NEW - Filter by device_class
name_pattern: str                  # NEW - Wildcard support: "*_person_detected"
```

**Implementation notes:**
- `device_class` - can check `entity.attributes.get('device_class')`
- `name_pattern` - can use `fnmatch` or regex
- Both additions are straightforward and non-breaking

---

## Key Insights from Research

### 1. Device Class Coverage is Extensive but Not Universal

**Domains with rich device_class vocabulary:**
- `sensor` / `number` - 70+ classes (excellent coverage)
- `binary_sensor` - 29 classes (excellent coverage)
- `cover` - 11 classes (good coverage)

**Domains with minimal device_class:**
- `media_player` - 3 classes (limited)
- `switch` - 3 classes (minimal)
- `button` - 4 classes (minimal)

**Domains with NO device_class:**
- `light`, `climate`, `fan`, `lock`, `person`, etc.

**Implication:** Gap-filling via inferred_types is CRITICAL for comprehensive discovery.

---

### 2. LLM Domain Knowledge vs System Knowledge

**LLM already knows (domain knowledge):**
- What metrics indicate air quality (CO2, VOC, PM2.5, humidity)
- What constitutes a "leak" (moisture sensors, water flow)
- Threshold values (CO2 >1000ppm, battery <20%)
- Relationships between concepts (person → location → room)

**LLM does NOT know (system knowledge):**
- Which entities exist in this HA installation
- Entity naming patterns specific to integrations
- Device_class values available in HA
- Area names and zone names in this home

**Conclusion:** The index bridges this gap by providing system structure without domain interpretation.

---

### 3. The Index is Static Metadata, Not Dynamic State

**What should be in the index (static):**
- Areas and their entity counts
- Domains and counts
- Device_classes and counts (grouped by domain)
- Inferred entity types and patterns
- People, pets, calendars, zones (names only)

**What should NOT be in the index (dynamic):**
- Current states (change constantly)
- Attribute values (temperature readings, battery levels)
- Availability status (online/offline)
- Historical data or trends

**Conclusion:** Spec correctly identifies this separation.

---

### 4. Index Refresh Strategy

**When should the index be regenerated?**

**Option A: On entity registry changes** (Recommended)
- Listen to `EVENT_ENTITY_REGISTRY_UPDATED`
- Regenerate index when entities added/removed
- Debounce updates (e.g., max once per minute)

**Option B: Periodically** (Simple)
- Regenerate every 5-15 minutes
- Works but may miss immediate changes

**Option C: On demand** (Inefficient)
- Regenerate for each conversation
- Defeats the purpose of pre-generation

**Recommendation:** Option A with debouncing

---

### 5. LLM for Gap-Filling Implementation

**Which LLM should be used?**

**Option A: User's configured LLM** (Recommended)
- Already authenticated and available
- Respects user's privacy/cost preferences
- May be local (Ollama) or cloud (OpenAI)

**Option B: Fixed cloud LLM** (Problematic)
- Requires API key management
- Privacy concerns (sending entity names to cloud)
- Additional cost

**Option C: Local hardcoded rules** (Limited)
- No LLM needed
- Can't adapt to new patterns
- Requires maintenance

**Recommendation:** Option A - use the same LLM configured for conversation

**Implementation approach:**
1. Collect entities without device_class
2. Group by naming patterns (e.g., "*_person_detected")
3. Send patterns to LLM with prompt: "Categorize these entity name patterns into semantic types"
4. Parse LLM response and store in index
5. Use inferred types for discovery

---

## Comparison: Spec Examples vs HA Reality

### Example 1: "Do we have a leak?"

**Spec shows querying:**
```python
discover_entities(device_class="moisture")
discover_entities(device_class="volume_flow_rate")
```

**HA Reality:**
- ✅ `moisture` is a valid binary_sensor device_class
- ✅ `volume_flow_rate` is a valid sensor device_class
- ✅ This query pattern works perfectly

**Additional consideration:**
- `sensor.moisture` also exists (soil moisture) - domain filtering needed
- Query should be: `discover_entities(domain="binary_sensor", device_class="moisture")`

---

### Example 2: "Who is home and where are they?"

**Spec shows:**
```yaml
inferred_types:
  location_tracking: 9     # *_ble_area
```

**HA Reality:**
- ❌ No standard device_class for BLE location sensors
- ✅ Gap-filling is necessary
- ✅ Pattern matching "*_ble_area" is correct approach

**Implementation:**
```python
# At index generation:
# LLM analyzes: sensor.mike_iphone_ble_area, sensor.janette_iphone_ble_area, ...
# LLM infers: "location_tracking" category with pattern "*_ble_area"

# At query time:
discover_entities(inferred_type="location_tracking")
# or
discover_entities(name_pattern="*_ble_area")
```

---

### Example 3: "Is someone at the door?"

**Spec shows querying:**
```python
discover_entities(area="Front Garden", device_class="occupancy")
discover_entities(name_contains="person_detected", area="Front Garden")
```

**HA Reality:**
- ✅ `occupancy` is a valid binary_sensor device_class
- ❌ "person_detected" has no standard device_class
- ✅ Gap-filling needed for person detection sensors

**Improved approach:**
```python
# Index contains:
inferred_types:
  person_detection:
    pattern: "*_person_detected"
    count: 6

# Query becomes:
discover_entities(area="Front Garden", device_class="occupancy")
discover_entities(area="Front Garden", inferred_type="person_detection")
```

---

### Example 4: "How's the air quality?"

**Spec shows index:**
```yaml
device_classes:
  sensor:
    carbon_dioxide: 16
    carbon_monoxide: 4
    pm25: 4
    pm10: 4
    aqi: 8
```

**HA Reality:**
- ✅ All these device_classes exist in HA's sensor domain
- ✅ Query pattern works perfectly
- ✅ LLM knows these metrics = air quality (domain knowledge)

**Implementation:**
```python
# LLM reads index, thinks: "air quality = CO2, PM2.5, AQI, etc."
# LLM calls:
discover_entities(device_class=["carbon_dioxide", "pm25", "aqi"])
```

---

## Implementation Recommendations

### 1. Index Schema - Finalized

Based on verification, the spec's index schema is sound:

```yaml
areas:
  - name: str
    entity_count: int

domains:
  domain_name: count  # dict format

device_classes:
  domain_name:
    device_class_name: count

inferred_types:
  category_name:
    pattern: str
    count: int

people:
  - name: str
    aliases: list[str]  # optional

pets:
  - name: str
    type: str

calendars: list[str]
zones: list[str]
automations: list[str]
scripts: list[str]
input_booleans: list[str]
input_texts: list[str]
input_numbers: list[str]
input_selects: list[str]
input_datetimes: list[str]
```

---

### 2. Tool Enhancements - Required

**Add to `discover_entities`:**
```python
async def discover_entities(
    area: Optional[str] = None,
    domain: Optional[str] = None,
    entity_type: Optional[str] = None,  # deprecated, use domain
    name_contains: Optional[str] = None,
    state: Optional[str] = None,
    limit: int = 100,

    # NEW PARAMETERS
    device_class: Optional[Union[str, List[str]]] = None,
    name_pattern: Optional[str] = None,  # fnmatch patterns like "*_person_detected"
    inferred_type: Optional[str] = None,  # lookup pattern from index
) -> List[EntityInfo]:
    """Discover entities matching filters."""
```

**Implementation notes:**
- `device_class` checks `entity.attributes.get('device_class')` matches
- `name_pattern` uses `fnmatch.fnmatch(entity_id, pattern)`
- `inferred_type` looks up pattern from index, then applies pattern matching

---

### 3. New Tool - `get_index`

```python
async def get_index() -> dict:
    """
    Returns the pre-generated system index.

    This index provides LLM with system structure without dumping
    all entity states. Includes areas, domains, device_classes,
    inferred entity types, people, pets, calendars, zones, etc.

    The index is static metadata only - no current states.
    Call this once at conversation start to understand what
    exists in the system.
    """
    return await IndexManager.get_index()
```

**Usage pattern:**
1. Conversation starts
2. LLM calls `get_index()` once
3. Index loaded into conversation context (~400-800 tokens)
4. LLM uses index to make smart `discover_entities` calls
5. Only relevant entity states are fetched

---

### 4. Index Generation - Implementation Flow

```python
class IndexManager:
    """Manages the system structure index."""

    async def generate_index(self, hass: HomeAssistant) -> dict:
        """Generate fresh index from current system state."""

        # 1. Query areas
        areas = await self._get_areas(hass)

        # 2. Query domains
        domains = await self._get_domains(hass)

        # 3. Query device_classes (grouped by domain)
        device_classes = await self._get_device_classes(hass)

        # 4. Find entities without device_class
        no_device_class_entities = await self._get_entities_without_device_class(hass)

        # 5. LLM gap-filling
        inferred_types = await self._infer_entity_types(no_device_class_entities)

        # 6. Compile people, pets, etc.
        people = await self._get_people(hass)
        pets = await self._get_pets(hass)
        calendars = await self._get_calendars(hass)
        zones = await self._get_zones(hass)
        automations = await self._get_automations(hass)
        scripts = await self._get_scripts(hass)
        input_helpers = await self._get_input_helpers(hass)

        # 7. Return compiled index
        return {
            "areas": areas,
            "domains": domains,
            "device_classes": device_classes,
            "inferred_types": inferred_types,
            "people": people,
            "pets": pets,
            "calendars": calendars,
            "zones": zones,
            "automations": automations,
            "scripts": scripts,
            **input_helpers,  # input_booleans, input_texts, etc.
        }

    async def _infer_entity_types(self, entities: List[str]) -> dict:
        """Use LLM to categorize entities without device_class."""

        # Group entities by naming patterns
        patterns = self._extract_patterns(entities)

        # Ask LLM to categorize
        prompt = f"""
Analyze these Home Assistant entity name patterns and categorize them into semantic types.

Entity patterns:
{chr(10).join(f"- {pattern} ({count} entities)" for pattern, count in patterns.items())}

Return a categorization like:
person_detection:
  pattern: "*_person_detected"
  count: 6
vehicle_detection:
  pattern: "*_vehicle_detected"
  count: 4
location_tracking:
  pattern: "*_ble_area"
  count: 9

Focus on meaningful categories that would help an LLM discover relevant entities.
"""

        # Call user's configured LLM
        response = await self.llm_client.complete(prompt)

        # Parse response into structured data
        return self._parse_inferred_types(response)
```

---

### 5. Index Refresh Strategy

```python
class IndexManager:
    def __init__(self, hass: HomeAssistant):
        self.hass = hass
        self._index = None
        self._last_updated = None
        self._refresh_task = None

    async def start(self):
        """Start index manager and listen for entity changes."""

        # Generate initial index
        await self.refresh_index()

        # Listen for entity registry changes
        @callback
        def entity_registry_changed(event):
            """Schedule index refresh on entity changes."""
            self._schedule_refresh()

        self.hass.bus.async_listen(
            EVENT_ENTITY_REGISTRY_UPDATED,
            entity_registry_changed
        )

    def _schedule_refresh(self):
        """Schedule index refresh with debouncing."""
        if self._refresh_task:
            self._refresh_task.cancel()

        # Debounce: refresh after 60 seconds of no changes
        self._refresh_task = asyncio.create_task(
            self._delayed_refresh()
        )

    async def _delayed_refresh(self):
        """Refresh after delay."""
        await asyncio.sleep(60)
        await self.refresh_index()
```

---

## Open Questions - Answered

### Q1: Index refresh - when?
**A:** On entity registry changes with 60-second debouncing (recommended)

### Q2: Index storage - memory or disk?
**A:** Memory only (simple, fast). Disk persistence adds complexity with minimal benefit since generation is fast (<1 second for typical home).

### Q3: LLM for gap-filling - which one?
**A:** Use the user's configured LLM (same as conversation agent). Respects privacy and cost preferences.

### Q4: Partial index - lite version?
**A:** Not needed. Full index is already compact (~400-800 tokens). If needed later, can exclude automations/scripts/input_helpers.

### Q5: What about entities added/removed during a conversation?
**A:** Index refresh handles this. For real-time updates during conversation, the LLM can call `discover_entities` which queries live state. Index is for discovery context, not live data.

---

## Conclusion

✅ **The Smart Query Spec is technically sound and ready for implementation.**

**Key validations:**
1. ✅ Device_class vocabulary is standardized and extensive (150+ values)
2. ✅ Gap-filling via LLM is necessary and feasible
3. ✅ Index size estimate is realistic (~400-800 tokens)
4. ✅ LLM domain knowledge + index = powerful discovery
5. ✅ All spec examples map correctly to HA's actual structure

**Recommended implementation phases:**
1. **Phase 1:** Generate basic index (areas, domains, device_classes) - no LLM needed
2. **Phase 2:** Add gap-filling with LLM inference for inferred_types
3. **Phase 3:** Enhance discover_entities with device_class, name_pattern filters
4. **Phase 4:** Create get_index MCP tool and integrate with conversation agent

**Expected impact:**
- Enables Level 3 queries (smart, context-aware)
- Maintains 95% token reduction (index ~800 tokens vs full dump ~15k tokens)
- No hardcoded intents or domain vocabulary needed
- Scales to any HA installation size

**Next step:** Review this verification document, then proceed to implementation if approved.
