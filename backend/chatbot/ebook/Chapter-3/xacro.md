### `docs/chapter3/xacro.md`
```markdown
---
id: chapter3/xacro
title: Using Xacro for Robot Models
sidebar_label: Xacro
---

# Chapter 3: Xacro - Modular URDF

Xacro (XML Macros) makes URDF files cleaner, reusable, and modular by adding macros, properties, and includes.

<grok-card data-id="6e50ee" data-type="image_card"></grok-card>



<grok-card data-id="49f53e" data-type="image_card"></grok-card>


## Benefits
- Reusable components (e.g., wheel macro)
- Constants and math expressions
- Conditional includes

## Example Macro
```xml
<xacro:macro name="wheel" params="side">
  <link name="${side}_wheel"/>
  <joint name="${side}_wheel_joint" type="continuous">
    <!-- joint details -->
  </joint>
</xacro:macro>
