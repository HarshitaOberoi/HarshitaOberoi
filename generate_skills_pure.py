import html

categories = [
    {
        "title": "Generative AI / LLM",
        "skills": ["Agentic AI", "Multi-agent pipelines", "LangChain", "LangGraph", "Prompt Engineering", "RAG", "CoT/ReAct"]
    },
    {
        "title": "Languages",
        "skills": ["Python (Expert)", "JavaScript (ES6)", "C", "SQL"]
    },
    {
        "title": "Frameworks & Libraries",
        "skills": ["FastAPI", "Flask", "Streamlit", "React", "Next.js", "Node.js", "TensorFlow", "PyTorch", "Scikit-learn"]
    },
    {
        "title": "Integrations & Automation",
        "skills": ["REST APIs", "Webhooks", "Zapier", "Pabbly", "WhatsApp API", "Payment Gateways"]
    },
    {
        "title": "DevOps & Cloud",
        "skills": ["Docker", "GitHub Actions", "AWS (EC2, S3)", "Microservices", "CI/CD", "Vercel"]
    },
    {
        "title": "Data, Databases & CRM",
        "skills": ["MongoDB", "MySQL", "Redis", "Zoho CRM", "Salesforce/HubSpot", "Adv Excel/Sheets", "Data Visualization"]
    }
]

char_width = 7
padding_x = 16
tag_height = 22
gap_x = 6
gap_y = 6
container_width = 340
start_x = 20
current_y = 60

svg_content = [
    '<svg xmlns="http://www.w3.org/2000/svg" width="380" height="700">',
    '<!-- Background -->',
    '<rect width="100%" height="100%" fill="#161b22" rx="12" stroke="#30363d" stroke-width="1" />',
    '<!-- Main Title -->',
    '<rect x="20" y="24" width="4" height="16" rx="2" fill="#00f2ff" />',
    '<text x="32" y="38" font-family="\'Inter\', sans-serif" font-size="16" font-weight="600" fill="#fff">Technical Skills</text>'
]

for cat in categories:
    # Category Title
    title = html.escape(cat["title"])
    svg_content.append(f'<text x="{start_x}" y="{current_y}" font-family="\'Inter\', sans-serif" font-size="12" fill="#8b949e" style="text-transform: uppercase; letter-spacing: 1px;">{title}</text>')
    svg_content.append(f'<line x1="{start_x}" y1="{current_y + 6}" x2="360" y2="{current_y + 6}" stroke="#30363d" stroke-width="1" />')
    current_y += 25

    current_x = start_x
    
    for skill in cat["skills"]:
        escaped_skill = html.escape(skill)
        text_width = len(skill) * char_width
        tag_width = text_width + padding_x
        
        if current_x + tag_width > start_x + container_width:
            current_x = start_x
            current_y += tag_height + gap_y

        svg_content.append(f'<rect x="{current_x}" y="{current_y}" width="{tag_width}" height="{tag_height}" rx="4" fill="rgba(0, 242, 255, 0.05)" stroke="rgba(0, 242, 255, 0.15)" stroke-width="1" />')
        svg_content.append(f'<text x="{current_x + (padding_x/2) + 1}" y="{current_y + 15}" font-family="\'Inter\', sans-serif" font-size="11" font-weight="500" fill="#00f2ff">{escaped_skill}</text>')
        
        current_x += tag_width + gap_x

    current_y += 40

svg_content.append('</svg>')

with open('h:/profile/skills.svg', 'w', encoding='utf-8') as f:
    f.write('\n'.join(svg_content))
