import markdown2
from datetime import datetime

# Read the markdown file
with open('JobTasker_PRD.md', 'r', encoding='utf-8') as f:
    md_content = f.read()

# Convert markdown to HTML
html_content = markdown2.markdown(md_content, extras=['tables', 'fenced-code-blocks', 'header-ids'])

# Create a styled HTML document
html_template = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>JobTasker - Product Requirements Document</title>
    <style>
        @page {{
            size: A4;
            margin: 2cm;
        }}
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 210mm;
            margin: 0 auto;
            padding: 20px;
        }}
        h1 {{
            color: #1F21A8;
            border-bottom: 3px solid #4e5ae8;
            padding-bottom: 10px;
            margin-top: 30px;
        }}
        h2 {{
            color: #4e5ae8;
            border-bottom: 2px solid #8687E7;
            padding-bottom: 8px;
            margin-top: 25px;
        }}
        h3 {{
            color: #8687E7;
            margin-top: 20px;
        }}
        code {{
            background-color: #f4f4f4;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
        }}
        pre {{
            background-color: #f4f4f4;
            padding: 15px;
            border-radius: 5px;
            border-left: 4px solid #4e5ae8;
            overflow-x: auto;
        }}
        pre code {{
            background-color: transparent;
            padding: 0;
        }}
        ul, ol {{
            margin-left: 20px;
        }}
        li {{
            margin-bottom: 8px;
        }}
        table {{
            border-collapse: collapse;
            width: 100%;
            margin: 20px 0;
        }}
        th, td {{
            border: 1px solid #ddd;
            padding: 12px;
            text-align: left;
        }}
        th {{
            background-color: #4e5ae8;
            color: white;
        }}
        .header {{
            text-align: center;
            margin-bottom: 40px;
            padding: 20px;
            background: linear-gradient(135deg, #1F21A8, #4e5ae8);
            color: white;
            border-radius: 10px;
        }}
        .header h1 {{
            color: white;
            border: none;
            margin: 0;
        }}
        .footer {{
            margin-top: 40px;
            padding-top: 20px;
            border-top: 2px solid #4e5ae8;
            text-align: center;
            color: #666;
            font-size: 0.9em;
        }}
        blockquote {{
            border-left: 4px solid #8687E7;
            padding-left: 20px;
            margin-left: 0;
            color: #666;
            font-style: italic;
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>JobTasker</h1>
        <p style="font-size: 1.2em; margin: 10px 0;">Product Requirements Document</p>
        <p>Version 1.0 | {datetime.now().strftime('%B %d, %Y')}</p>
    </div>
    
    {html_content}
    
    <div class="footer">
        <p><strong>JobTasker</strong> - Master Your Tasks & Land Your Dream Job</p>
        <p>Contact: karimabokamel74@gmail.com | +20 1148779202</p>
        <p>© 2026 JobTasker. All rights reserved.</p>
    </div>
</body>
</html>
"""

# Save the HTML file
with open('JobTasker_PRD.html', 'w', encoding='utf-8') as f:
    f.write(html_template)

print("HTML file created successfully: JobTasker_PRD.html")
print("You can now open this file in a browser and print to PDF, or use a tool like wkhtmltopdf to convert it.")
