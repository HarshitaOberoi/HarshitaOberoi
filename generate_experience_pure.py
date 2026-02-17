import html

experiences = [
    {
        "role": "Software Engineer Intern",
        "company": "Krins Digital",
        "desc": [
            "Engineered crypto futures trading bot (RSI, EMA, MACD) boosting win rate by 15% and reducing latency by 30%.",
            "Built secure REST APIs (Node.js, FastAPI) and React/Next.js dashboards.",
            "Automated CI/CD with Docker + GitHub Actions."
        ]
    },
    {
        "role": "Software Engineer Intern (Summer Analyst)",
        "company": "G S",
        "desc": [
            "Built Agentic AI workflows with LangGraph/LangChain using Router and Supervisor architectures.",
            "Scaled multi-agent pipelines for 10K–15K row datasets.",
            "Applied CoT, ReAct, Reflexion reasoning to reduce hallucinations."
        ]
    },
    {
        "role": "Backend Developer (Freelance)",
        "company": "LunaLady AI",
        "desc": [
            "Architected backend NLP APIs powering a women’s health assistant; scaled to 5K+ DAUs.",
            "Optimized query performance reducing response time by 40%."
        ]
    },
    {
        "role": "Software Engineer Intern",
        "company": "Kodefort",
        "desc": [
            "Engineered responsive web apps using React.js, Next.js, and Tailwind CSS.",
            "Built secure full-stack solutions with Laravel, MongoDB, and MySQL."
        ]
    }
]

svg_content = [
    '<svg xmlns="http://www.w3.org/2000/svg" width="480" height="680">',
    '<!-- Background -->',
    '<rect width="100%" height="100%" fill="#161b22" rx="12" stroke="#30363d" stroke-width="1" />',
    '<!-- Header -->',
    '<rect x="20" y="24" width="4" height="16" rx="2" fill="#00f2ff" />',
    '<text x="32" y="38" font-family="\'Inter\', sans-serif" font-size="16" font-weight="600" fill="#fff">Experience</text>',
    '<!-- Timeline Line -->',
    '<line x1="40" y1="60" x2="40" y2="640" stroke="#30363d" stroke-width="2" />'
]

current_y = 70
for exp in experiences:
    # Dot
    svg_content.append(f'<circle cx="40" cy="{current_y + 6}" r="6" fill="#090c10" stroke="#00f2ff" stroke-width="2" />')
    
    # Text Group
    # Role
    svg_content.append(f'<text x="60" y="{current_y + 10}" font-family="\'Inter\', sans-serif" font-size="15" font-weight="600" fill="#fff">{html.escape(exp["role"])}</text>')
    current_y += 20
    
    # Company
    svg_content.append(f'<text x="60" y="{current_y + 10}" font-family="\'Inter\', sans-serif" font-size="14" font-weight="500" fill="#00f2ff">{html.escape(exp["company"])}</text>')
    current_y += 25
    
    # Descriptions (Bullet points)
    for line in exp["desc"]:
        # Simple word wrap logic for SVG check
        words = line.split(' ')
        line_buffer = ""
        first_line = True
        
        for word in words:
            test_line = line_buffer + word + " "
            # lazy approximation of width: avg char ~ 7px. max width ~ 380px -> ~54 chars
            if len(test_line) > 55:
                # Flush line
                prefix = "• " if first_line else "  "
                svg_content.append(f'<text x="60" y="{current_y + 10}" font-family="\'Inter\', sans-serif" font-size="13" fill="#8b949e">{prefix}{html.escape(line_buffer)}</text>')
                current_y += 18
                line_buffer = word + " "
                first_line = False
            else:
                line_buffer = test_line
        
        # Flush remainder
        if line_buffer:
            prefix = "• " if first_line else "  "
            svg_content.append(f'<text x="60" y="{current_y + 10}" font-family="\'Inter\', sans-serif" font-size="13" fill="#8b949e">{prefix}{html.escape(line_buffer)}</text>')
            current_y += 18
            
    current_y += 20 # Spacing between items

svg_content.append('</svg>')

with open('h:/profile/experience.svg', 'w', encoding='utf-8') as f:
    f.write('\n'.join(svg_content))
