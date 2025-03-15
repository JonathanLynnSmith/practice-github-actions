# Get the directory of the current PowerShell script
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path

# Define the path to main.py (navigate to src from the scripts folder)
$pythonScriptPath = Join-Path $scriptDir "..\src\main.py"

# Prepare the command to run main.py with --lint-all flag
$command = "python $pythonScriptPath --validate-log"

# Run the Python script in the same window and output the result
Invoke-Expression $command
