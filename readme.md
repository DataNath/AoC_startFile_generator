# AoC_startFile_gen

## What this file does:

1. Takes a user input for your [Advent of Code](https://adventofcode.com/) session cookie value
2. Generates a year directory next to the .exe save location
3. Generates subdirectories within year for days 1-25
4. Creates a start file within each relevant subdirectory

There is a template.yxmd file within the bundle which is treated as such:
- Dummy `session_cookie` is replaced - taken from user input
- URL value `year` is replaced - parsed from today()
- URL value `day` is replaced - from range 1-25

Note: Given `year` is generated from today(), this app ought to be dynamic for future events.

Download the latest version [here](https://github.com/DataNath/AoC_startFile_generator/releases/download/v1.0.0/AoC_startFile_gen.exe)!