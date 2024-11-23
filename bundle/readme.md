# Steps:
---
1. Take user input for session cookie value
2. Generate year subdir at root
3. Generate subdirs within year for days 1-25
4. Read in template.yxmd as template
5. Generate start file in each subdir
    - Replace session cookie - taken from user input
    - Replace year in URL - parsed from today()
    - Replace day in URL - from range 1-25