const fs = require('fs');

const categories = [
    {
        title: "Generative AI / LLM",
        skills: ["Agentic AI", "Multi-agent pipelines", "LangChain", "LangGraph", "Prompt Engineering", "RAG", "CoT/ReAct"]
    },
    {
        title: "Languages",
        skills: ["Python (Expert)", "JavaScript (ES6)", "C", "SQL"]
    },
    {
        title: "Frameworks & Libraries",
        skills: ["FastAPI", "Flask", "Streamlit", "React", "Next.js", "Node.js", "TensorFlow", "PyTorch", "Scikit-learn"]
    },
    {
        title: "Integrations & Automation",
        skills: ["REST APIs", "Webhooks", "Zapier", "Pabbly", "WhatsApp API", "Payment Gateways"]
    },
    {
        title: "DevOps & Cloud",
        skills: ["Docker", "GitHub Actions", "AWS (EC2, S3)", "Microservices", "CI/CD", "Vercel"]
    },
    {
        title: "Data, Databases & CRM",
        skills: ["MongoDB", "MySQL", "Redis", "Zoho CRM", "Salesforce/HubSpot", "Adv Excel/Sheets", "Data Visualization"]
    }
];

const charWidth = 7;
const paddingX = 16; 
const tagHeight = 22;
const gapX = 6;
const gapY = 6;
const containerWidth = 340;
const startX = 20;
let currentY = 60;

let svgContent = `<svg xmlns="http://www.w3.org/2000/svg" width="380" height="700">
    <style>
        .title { font-family: 'Inter', sans-serif; font-size: 16px; font-weight: 600; fill: #fff; }
        .cat-title { font-family: 'Inter', sans-serif; font-size: 12px; fill: #8b949e; text-transform: uppercase; letter-spacing: 1px; }
        .tag-text { font-family: 'Inter', sans-serif; font-size: 11px; font-weight: 500; fill: #00f2ff; }
        .tag-rect { fill: rgba(0, 242, 255, 0.05); stroke: rgba(0, 242, 255, 0.15); stroke-width: 1; }
    </style>
    
    <!-- Background -->
    <rect width="100%" height="100%" fill="#161b22" rx="12" stroke="#30363d" stroke-width="1" />
    
    <!-- Main Title -->
    <rect x="20" y="24" width="4" height="16" rx="2" fill="#00f2ff" />
    <text x="32" y="38" class="title">Technical Skills</text>
`;

categories.forEach(cat => {
    // Category Title
    svgContent += `<text x="${startX}" y="${currentY}" class="cat-title">${cat.title}</text>`;
    svgContent += `<line x1="${startX}" y1="${currentY + 6}" x2="${360}" y2="${currentY + 6}" stroke="#30363d" stroke-width="1" />`;
    currentY += 25;

    let currentX = startX;
    
    cat.skills.forEach(skill => {
        const textWidth = skill.length * charWidth;
        const tagWidth = textWidth + paddingX;
        
        if (currentX + tagWidth > startX + containerWidth) {
            currentX = startX;
            currentY += tagHeight + gapY;
        }

        svgContent += `<rect x="${currentX}" y="${currentY}" width="${tagWidth}" height="${tagHeight}" rx="4" class="tag-rect" />`;
        svgContent += `<text x="${currentX + (paddingX/2) + 1}" y="${currentY + 15}" class="tag-text">${skill}</text>`;
        
        currentX += tagWidth + gapX;
    });

    currentY += 40; // Spacing between categories
});

svgContent += `</svg>`;

fs.writeFileSync('h:/profile/skills.svg', svgContent);
