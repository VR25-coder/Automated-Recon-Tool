from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML

def generate_report(data):

    env = Environment(
        loader=FileSystemLoader("templates")
    )

    template = env.get_template(
        "report_template.html"
    )

    html_output = template.render(data=data)

    html_path = "reports/report.html"
    pdf_path = "reports/report.pdf"

    with open(html_path, "w") as file:
        file.write(html_output)

    print("[+] HTML report generated")

    try:

        HTML(string=html_output).write_pdf(pdf_path)

        print("[+] PDF report generated")

    except Exception as e:

        print("[!] PDF generation failed")
        print(e)
