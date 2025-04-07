from praisonaiagents import Agent, MCP

whatsapp_agent = Agent(
    instructions="Whatsapp Agent",
    llm="groq/llama-3.3-70b-versatile",
    tools=MCP("python D:\sandbox\whatsapp-mcp\whatsapp-mcp-server\main.py")
)

whatsapp_agent.start("Send Hello to +919267913652")
