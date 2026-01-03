# Smart Query Discovery - Working Notes

**Status:** Discovery phase - exploring the problem space
**Date:** 2026-01-03

## The Problem

MCP Assist already solves the "entity dump" problem by using dynamic discovery. However, LLMs still struggle with complex queries because they don't know WHAT to search for.

### Current State (Levels 0-2)

**Level 0:** No knowledge - asks wrong questions
- Query: "who is home" → discovers person domain
- Result: Gets states but not locations
- ❌ Doesn't know to look for BLE area sensors

**Level 1:** Basic knowledge - knows some patterns
- Queries multiple domains (person + motion)
- ❌ Can't map relationships (which person → which room)

**Level 2:** Good knowledge - knows specific entity patterns
- Knows to search for "ble_area" sensors
- ✅ Gets right answer
- ❌ Required specific domain knowledge (what is a BLE area sensor?)

**Level 3 (Target):** Smart query
- Single query that understands intent
- Discovers all relevant entity types
- Returns structured, interpreted results

---

## Example Use Cases

### Example 1: "Who is home and where are they?"

**Challenge:** LLM needs to know:
- person.* entities have home/away state
- Location requires checking related sensors BY NAME
- Pattern: person.mike → sensor.mike_*_ble_area, device_tracker.mike_*

**Level 2 Solution:** LLM knows to query `name_contains="ble_area"`
**Level 3 Goal:** Single query that automatically infers person→sensor relationships

---

### Example 2: "What's the temperature in each room?"

**Challenge:** LLM needs to know:
- Which sensors measure room temperature (not device/rack temps)
- Preference: air quality sensors > radiator thermostats
- Filtering: exclude outdoor, device, hardware sensors

**Level 2 Solution:** Query temperature sensors, manually filter by area
**Level 3 Goal:** Returns one representative temp per room with source preference

---

### Example 3: "Are any doors or windows open?"

**Challenge:** Categorization
- External doors (security relevant) vs internal doors (less relevant)
- Windows (usually important) vs appliance doors (exclude)

**Level 2 Solution:** Query by device_class, includes everything
**Level 3 Goal:** Pre-categorized by security relevance

---

### Example 4: "How's the air quality today?"

**Challenge:** Multi-metric interpretation
- Air quality = CO2 + VOC + PM2.5 + humidity + ...
- LLM needs to know these are the relevant metrics
- Each metric has different units and thresholds

**Level 2 Solution:** Query each metric separately, dump numbers
**Level 3 Goal:** Discovers all air quality sensors, groups by room

**Key Insight from This Example:**
- Domain knowledge (CO2 >1000ppm = poor) → LLM already knows this ✅
- Entity discovery (which sensors exist) → LLM doesn't know ❌
- The tool should help with discovery, not interpretation

---

## Key Insights

### What Should NOT Be Hardcoded
❌ Entity names (user-specific)
❌ Threshold values (LLM already knows CO2 >1000 is bad)
❌ Interpretations (LLM can reason about good/bad/moderate)
❌ Response formatting (LLM should compose the answer)

### What SHOULD Be Provided
✅ Entity relationships (person → BLE sensors, by name inference)
✅ Entity categorization (external vs internal, room vs device)
✅ Search guidance (what entity types/patterns are relevant)
✅ System structure (areas, devices, entity metadata)

### The Core Problem
**LLM doesn't know what to search for in HA's entity namespace.**

For "air quality":
- LLM knows air quality = CO2, VOC, PM2.5, etc. (domain knowledge)
- LLM doesn't know if this HA has Apollo AIR-1, generic sensors, or nothing (system knowledge)
- LLM doesn't know to search device_class="carbon_dioxide" or name_contains="co2" (discovery patterns)

---

## What We're NOT Doing

1. **Not replacing LLM reasoning**
   - LLM should interpret values (754ppm CO2 is good)
   - LLM should compose summaries
   - LLM should decide what's important

2. **Not hardcoding entity patterns**
   - Not: "Mike's sensor is sensor.apollo_air_1_bedroom_co2"
   - Instead: "Find CO2 sensors in all rooms"

3. **Not dumping entire entity list**
   - That's what we're trying to avoid
   - Need focused, relevant results only

---

## Open Questions

### 1. Intent Detection
- Who detects intent? The calling LLM or smart_query itself?
- Natural language input or structured parameters?
- Examples:
  - `smart_query("who is home")` ← natural language
  - `smart_query(intent="person_location")` ← structured

### 2. Discovery Patterns
How does smart_query know what entities are relevant for "air quality"?
- Option A: Predefined search patterns (device_class + name patterns)
- Option B: Analyze all sensors, return anything that looks relevant
- Option C: Ask LLM to provide search hints ("I need CO2, VOC sensors")

### 3. Entity Relationships
How to discover that person.mike → sensor.mike_ble_area?
- Name similarity matching (already exists in discovery.py)
- Device registry (entities from same device)
- Area registry (entities in same area)
- User-configured mappings?

### 4. Categorization
How to know external vs internal doors?
- Area assignments (external area = outside?)
- Naming patterns ("front_door" vs "bathroom_door")
- Device metadata
- User configuration

### 5. Result Structure
What does smart_query return?
- Option A: Filtered entity list with metadata
- Option B: Pre-structured results by room/category
- Option C: Both raw data + suggested structure

---

## Initial Spec from Other Claude Instance

The other Claude instance proposed:
- Intent categories: person_location, device_state, sensor_reading, security_status
- Query chaining for complex intents
- Structured output with summaries

**Issue identified:** Over-reliance on hardcoded patterns and domain vocabulary

**Revised approach needed:**
- Leverage LLM's existing domain knowledge
- Focus on system discovery and entity relationships
- Avoid rigid intent categorization

---

## Next Steps (Not Yet Decided)

1. Define what information smart_query needs to provide
2. Determine how to discover relevant entities dynamically
3. Decide on API design (natural language vs structured)
4. Choose implementation approach
5. Start with one use case (person_location?) to prove concept

---

## Notes
- This is a working document, not a final design
- We're still in problem exploration phase
- Don't implement until we've fully thought through the approach
