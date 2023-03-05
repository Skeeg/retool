# user-config.yaml example

This file should be stored in the `config` folder.

```yaml
---
# ==============
# LANGUAGE ORDER
# ==============
# If the -l option is used, only include titles with the following languages.
# Comment out languages you don't want. Order is important.
language order:
# - English
# - Afrikaans
# - Albanian
# - Arabic
# - Bulgarian
# - Catalan
# - Chinese
# - Cornish
# - Croatian
# - Czech
# - Danish
# - Dutch
# - Estonian
# - Finnish
# - French
# - Gaelic
# - German
# - Greek
# - Hebrew
# - Hindi
# - Hungarian
# - Icelandic
# - Indonesian
# - Italian
# - Japanese
# - Korean
# - Latvian
# - Lithuanian
# - Macedonian
# - Norwegian
# - Polish
# - Portuguese
# - Punjabi
# - Romanian
# - Russian
# - Serbian
# - Slovak
# - Slovenian
# - Spanish
# - Swedish
# - Tamil
# - Thai
# - Turkish
# - Ukranian

# ============
# REGION ORDER
# ============
# Only include titles with the following regions. Comment out the regions you
# don't want. Order is important.
region order:
- USA
- World
- Canada
- UK
- Australia
- New Zealand
- Singapore
- Ireland
- Europe
- Japan
- Asia
- Thailand
- Spain
- Mexico
- Argentina
- Latin America
- Brazil
- Portugal
- France
- Belgium
- Netherlands
- Germany
- Austria
- Italy
- Switzerland
- Hong Kong
- China
- Taiwan
- Korea
- Russia
- Ukraine
- Estonia
- Poland
- Latvia
- Lithuania
- Denmark
- Norway
- Sweden
- Scandinavia
- Finland
- Iceland
- Hungary
- Czech
- Greece
- Macedonia
- India
- South Africa
- Israel
- Slovakia
- Turkey
- Croatia
- Slovenia
- United Arab Emirates
- Bulgaria
- Romania
- Albania
- Serbia
- Indonesia
- Unknown

# ===========
# VIDEO ORDER
# ===========
# Priority for titles with a video tag in their name. Do not comment out any
# lines.
video order:
- NTSC
- PAL
- PAL 60Hz
- MPAL
- SECAM

# ============================
# LIST NAMES PREFIX AND SUFFIX
# ============================
# If the --listnames option is used, you can optionally add a prefix and
# suffix to each title.
#
# If you start a prefix with http://, https://, or ftp://, each line in the
# list will be URL encoded.
#
# The text must be inside double quotes. You must escape other double quotes
# and backslashes inside the quotes like so: \", \\
list prefix:
# - "This text will be at the start of each line"

list suffix:
# - "This text will be at the end of each line"

# =======================================
# GLOBAL EXCLUDE AND INCLUDE USER FILTERS
# =======================================
# Exclude or include specific titles by adding your own text strings to match
# against. Items in the list are case sensitive. See the documentation for more
# information, and pay particular attention to how system user filters interact
# with global user filters.
#
# The formatting is as follows:
#
# * Plain text indicates a partial string match.
# * A prefix of / indicates a regular expression match.
# * A prefix of | indicates a full string match.
# * Additionally, wrap a string in <> to also remove any match's related clones.
#
# The text must be inside double quotes. You must escape double quotes and
# backslashes like so: \", \\
#
# Comment out lines you don't want.
exclude:
# - "[b]"
# - "/.*?\(Virtual*"

include:
# - "|My favorite title (Japan)"

# ============
# GUI SETTINGS
# ============
# GUI settings only, not used by the CLI.
gui settings:
- exclude:
- output:
```