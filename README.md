# rackspacetest

Exec Process:
- Run ```python <code>``` for normal execution
- Run ```python <code> -o <offset value>``` to get matching tz
- Run ```python <code> -m <tz_name>``` to get specific tz
  
Note: 
  - for matching timezone with value, the user should provide string of length greater than 4. 
  - String lower than 4 will be matched against the abbr.
  - For a space separted input please send -m="<input>" eg: -m="India Standard Time"
  
Assumptions:
  - By default the program should parse information from the above JSON and return all time zones in a user-friendly format - This is assumed a formatted string output 
  - Complete Timezone is skipped if --match and --offset is passed
  - The program does not accept --match and --offset at the same time. This is by intent, however can be easily enhanced. 
