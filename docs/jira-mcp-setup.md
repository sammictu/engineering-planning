# Jira MCP Setup Guide

This guide helps you connect to Jira via Model Context Protocol (MCP) to integrate Jira data with your sprint planning documentation.

## Prerequisites

1. **Jira Account Access**
   - Jira instance URL (e.g., `https://yourcompany.atlassian.net`)
   - Jira API token or OAuth credentials
   - Appropriate permissions to read/write issues

2. **MCP Server**
   - Jira MCP server installed and configured
   - Node.js (if using a Node-based MCP server)

## Getting Your Jira API Token

1. Go to [Atlassian Account Settings](https://id.atlassian.com/manage-profile/security/api-tokens)
2. Click "Create API token"
3. Give it a label (e.g., "Cursor MCP")
4. Copy the generated token (you'll only see it once)

## MCP Configuration

### Option 1: Using Cursor Settings

1. Open Cursor Settings (Cmd+, on Mac, Ctrl+, on Windows/Linux)
2. Search for "MCP" or "Model Context Protocol"
3. Add MCP server configuration:

```json
{
  "mcpServers": {
    "jira": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-jira"
      ],
      "env": {
        "JIRA_URL": "https://yourcompany.atlassian.net",
        "JIRA_EMAIL": "your-email@company.com",
        "JIRA_API_TOKEN": "your-api-token-here"
      }
    }
  }
}
```

### Option 2: Manual Configuration File

If you need to configure manually, the MCP configuration is typically in:
- **macOS**: `~/Library/Application Support/Cursor/User/globalStorage/anysphere.cursor-mcp/settings.json`
- **Windows**: `%APPDATA%\Cursor\User\globalStorage\anysphere.cursor-mcp\settings.json`
- **Linux**: `~/.config/Cursor/User/globalStorage/anysphere.cursor-mcp/settings.json`

## Configuration Parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| `JIRA_URL` | Your Jira instance URL | `https://yourcompany.atlassian.net` |
| `JIRA_EMAIL` | Your Jira account email | `user@company.com` |
| `JIRA_API_TOKEN` | Your Jira API token | `ATATT3xFfGF0...` |
| `JIRA_PROJECT_KEY` | (Optional) Default project key | `PROJ` |

## Testing the Connection

After configuration:

1. Restart Cursor
2. Open the MCP panel or check the status
3. Try querying Jira data:
   - List projects
   - Get issues
   - Search for issues

## Available MCP Tools

Once connected, you can use these MCP tools:

- **List Projects**: Get all Jira projects
- **Get Issue**: Retrieve issue details by key
- **Search Issues**: Search issues using JQL (Jira Query Language)
- **Create Issue**: Create new issues
- **Update Issue**: Update existing issues
- **Get Sprint**: Retrieve sprint information
- **List Boards**: Get all boards

## Integration with Documentation

Once connected, you can:

1. **Sync Features from Jira**
   - Pull issues/epics from Jira projects
   - Update `product-features.md` with Jira issue data
   - Link features to Jira tickets

2. **Update Sprint Planning**
   - Pull current sprint issues
   - Update `sprint-planning-context.md` with real-time data
   - Track sprint progress

3. **Sync Team Information**
   - Pull assignee information
   - Update `engineering-org.md` with team workload
   - Track team capacity

## Example Queries

### Get Current Sprint Issues
```
Search for issues in current sprint: project = PROJ AND sprint in openSprints()
```

### Get High Priority Features
```
Search for high priority issues: project = PROJ AND priority = High AND type = Epic
```

### Get Team Workload
```
Search for issues assigned to team: project = PROJ AND assignee in (user1, user2, user3)
```

## Troubleshooting

### Connection Issues

**Problem**: Cannot connect to Jira
- **Solution**: Verify API token is correct and not expired
- **Solution**: Check Jira URL is correct (include `https://`)
- **Solution**: Ensure your account has API access enabled

**Problem**: Authentication failed
- **Solution**: Regenerate API token
- **Solution**: Verify email matches your Jira account
- **Solution**: Check account permissions

**Problem**: MCP server not found
- **Solution**: Install the Jira MCP server: `npm install -g @modelcontextprotocol/server-jira`
- **Solution**: Verify Node.js is installed: `node --version`

### Permission Issues

**Problem**: Cannot read issues
- **Solution**: Verify project permissions in Jira
- **Solution**: Check API token has appropriate scopes
- **Solution**: Contact Jira admin for access

## Security Best Practices

1. **Never commit API tokens to version control**
   - Use environment variables
   - Use secure configuration files
   - Add `.env` files to `.gitignore`

2. **Rotate tokens regularly**
   - Set reminders to regenerate tokens
   - Revoke old tokens when creating new ones

3. **Use least privilege**
   - Only grant necessary permissions
   - Use read-only tokens when possible

## Next Steps

After connecting:

1. Test basic queries to verify connection
2. Set up automated sync (if desired)
3. Update documentation templates to include Jira links
4. Configure filters for relevant projects/boards

## Additional Resources

- [Jira REST API Documentation](https://developer.atlassian.com/cloud/jira/platform/rest/v3/)
- [Jira Query Language (JQL) Guide](https://support.atlassian.com/jira-service-management-cloud/docs/use-advanced-search-with-jira-query-language-jql/)
- [MCP Documentation](https://modelcontextprotocol.io/)

---

**Last Updated:** [Date]  
**Maintained By:** [Name/Team]
