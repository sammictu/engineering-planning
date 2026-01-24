#!/bin/bash
# List Jira projects - run locally: ./scripts/list-jira-projects.sh
# Uses credentials from Cursor MCP config

JIRA_URL="https://pointdf.atlassian.net"
JIRA_EMAIL="whuang@point.com"
# Read token from MCP config (or set JIRA_API_TOKEN env var)
CONFIG="$HOME/Library/Application Support/Cursor/User/globalStorage/anysphere.cursor-mcp/settings.json"
if [ -n "$JIRA_API_TOKEN" ]; then
  TOKEN="$JIRA_API_TOKEN"
else
  TOKEN=$(grep -o '"JIRA_API_TOKEN": "[^"]*"' "$CONFIG" 2>/dev/null | cut -d'"' -f4)
fi
if [ -z "$TOKEN" ]; then
  echo "Error: Could not find JIRA_API_TOKEN. Set JIRA_API_TOKEN or ensure MCP config exists."
  exit 1
fi

echo "Fetching Jira projects from $JIRA_URL ..."
echo ""

RESP=$(curl -s -u "$JIRA_EMAIL:$TOKEN" -H "Accept: application/json" "$JIRA_URL/rest/api/3/project")
echo "$RESP" | python3 -c "
import sys, json
try:
    data = json.load(sys.stdin)
    if isinstance(data, list):
        for p in data:
            print(f\"  {p.get('key', '')}  {p.get('name', '')}\")
    elif isinstance(data, dict) and 'errorMessages' in data:
        print('Error:', data.get('errorMessages', ['Unknown']))
    else:
        print(json.dumps(data, indent=2))
except Exception as e:
    print('Parse error:', e)
" 2>/dev/null || echo "$RESP"
