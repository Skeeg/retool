---
hide:
  - footer
---

# Description

The `description` object holds information related to the clone list itself, and is
always at the top of the file. It is mandatory to include.

A `description` object looks similar to the following example:

```json
"description": {
  "name": "Sony - PlayStation (Redump)",
  "lastUpdated": "24 July 2022",
  "minimumVersion": "2.00"
}
```

A `description` object contains the following keys:

* `name (str)`: The system name and release group of the DAT the clone list is related to.

* `lastUpdated (str)`: The last time the clone list was updated, in DD-MMMM-YYYY format.

* `minimumVersion (str)`: The minimum version of Retool required to understand all the
  features of the clone list.

The `minimumVersion` key is the only data in the description used by Retool, the rest is
to make parsing and updating the clone list easier for humans.
