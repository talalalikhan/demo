import json
import pandas as pd
import lxml.etree as et
import pdfkit
with open("C:\\Users\\Middl\\OneDrive\\Documents\\mod3\\example_docs\\example1.json", "r") as f:
    data = json.loads(f.read())

# your_json = """{"url": "https://www.abc123.com", "extensionVersion": "4.51.0", "axeVersion": "4.6.3", "standard": "WCAG 2.1 AA", "testingStartDate": "2023-04-03T09:35:06.177Z", "testingEndDate": "2023-04-03T09:35:06.177Z", "bestPracticesEnabled": false, "issueSummary": {"critical": 2, "moderate": 0, "minor": 0, "serious": 0, "bestPractices": 0, "needsReview": 0}, "remainingTestingSummary": {"run": false}, "igtSummary": [], "failedRules": [{"name": "button-name", "count": 1, "mode": "automated"}, {"name": "select-name", "count": 1, "mode": "automated"}], "needsReview": [], "allIssues": [{"ruleId": "button-name", "description": "Ensures buttons have discernible text", "help": "Buttons must have discernible text", "helpUrl": "https://www.abc123.com", "impact": "critical", "needsReview": false, "isManual": false, "selector": [".livechat-button"], "summary": "Fix any of the following:\\n  Element does not have inner text that is visible to screen readers\\n  aria-label attribute does not exist or is empty\\n  aria-labelledby attribute does not exist, references elements that do not exist or references elements that are empty\\n  Element has no title attribute\\n  Element's default semantics were not overridden with role=\\"none\\" or role=\\"presentation\\"", "source": "<button class=\\"livechat-button items-center bg-black shadow-liveChat rounded-full text-white p-2 h-12 transition-all opacity-0 pointer-events-none w-sp-48 opacity-0 pointer-events-none\\">", "tags": ["cat.name-role-value", "wcag2a", "wcag412", "section508", "section508.22.a", "ACT"], "igt": "", "shareURL": "", "createdAt": "2023-04-03T09:35:06.177Z", "testUrl": "", "testPageTitle": "ABC123", "foundBy": "ab@bc.com", "axeVersion": "4.6.3"}, {"ruleId": "select-name", "description": "Ensures select element has an accessible name", "help": "Select element must have an accessible name", "helpUrl": "https://www.abc123.com", "impact": "critical", "needsReview": false, "isManual": false, "selector": ["#plp__sortSelected"], "summary": "Fix any of the following:\\n  Form element does not have an implicit (wrapped) <label>\\n  Form element does not have an explicit <label>\\n  aria-label attribute does not exist or is empty\\n  aria-labelledby attribute does not exist, references elements that do not exist or references elements that are empty\\n  Element has no title attribute\\n  Element's default semantics were not overridden with role=\\"none\\" or role=\\"presentation\\"", "source": "<select class=\\"w-full absolute opacity-0 appearance-none text-value-small font-bold text-black uppercase cursor-pointer bg-transparent outline-0\\" id=\\"plp__sortSelected\\">", "tags": ["cat.forms", "wcag2a", "wcag412", "section508", "section508.22.n", "ACT"], "igt": "", "shareURL": "", "createdAt": "2023-04-03T09:35:06.177Z", "testUrl": "https://www.abc123.com", "testPageTitle": "ABC123", "foundBy": "ab@bc.com", "axeVersion": "4.6.3"}]}"""
# data = json.loads(your_json)

## replace the above lines with the following in your case
# with open('your_file.json', 'r') as f:   
#     data = json.load(f)

html = et.Element("html")

# general info
html.append(et.fromstring(f"""<h4>Submission Time: {data['submission_time']}</h4>"""))
html.append(et.fromstring(f"""<h4>Summary:</h4>"""))
# html.append(et.fromstring(f"""<p><\p><\br>"""))

# summary table
summary = pd.Series(data['document_details'])
summary_table = et.fromstring(summary.to_frame().to_html(header=False))
summary_table.set('Field', 'Value')
html.append(summary_table)

# issue tables
# cols_of_interest = ['ruleId', 'description', 'help', 'impact', 'selector', 'summary', 'source']
# df = pd.DataFrame(data['allIssues'])[cols_of_interest].T
# for col in df.columns:
#     table = et.fromstring(df[[col]].to_html(header=False))
#     table.set('class', 'issue')
#     html.append(table)
#     html.append(et.fromstring('<br/>'))

pdfkit.from_string(et.tostring(html, encoding="unicode"), "./example1.pdf", css='style.css')