from io import BytesIO
import logging
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from core.logging_config import setup_logging

logger = setup_logging()

class PdfService:
    @staticmethod
    def generate_resume_pdf(resume_data: dict) -> BytesIO:
        buffer = BytesIO()
        try:
            logger.info("🚀 Starting PDF generation...")

            doc = SimpleDocTemplate(
                buffer,
                pagesize=A4,
                rightMargin=36,
                leftMargin=36,
                topMargin=36,
                bottomMargin=36,
            )
            styles = getSampleStyleSheet()
            story = []

            # ✅ Basic Info
            name = (resume_data.get("name") or "").strip()
            email = (resume_data.get("email") or "").strip()
            phone = (resume_data.get("phone") or "").strip()

            story.append(
                Paragraph(f"<b>{name}</b>", styles["Title"])
            )

            contact = f"""
            <a href="mailto:{email}">{email}</a><br/>
            {phone}<br/>
            <a href="{resume_data.get('linkedin', '')}">LinkedIn</a><br/>
            <a href="{resume_data.get('github', '')}">GitHub</a><br/>
            <a href="{resume_data.get('portfolio', '')}">Portfolio</a>
            """

            story.append(
                Paragraph(contact, styles["Normal"])
            )

            story.append(Spacer(1, 12))

            # ✅ Summary Section
            if resume_data.get("summary"):
                story.append(Paragraph("<b>Summary</b>", styles["Heading2"]))
                story.append(Paragraph(resume_data["summary"], styles["Normal"]))
                story.append(Spacer(1, 12))

            # ✅ Experience Section
            if resume_data.get("experience"):
                story.append(Paragraph("<b>Experience</b>", styles["Heading2"]))
                for exp in resume_data.get("experience", []):
                    title = exp.get("title", "No Title")
                    company = exp.get("company", "Unknown Company")
                    start = exp.get("start", "?")
                    end = exp.get("end", "Present")
                    story.append(
                        Paragraph(
                            f"<b>{title}</b> — {company} ({start} - {end})",
                            styles["Normal"]
                        )
                    )

                    if exp.get("description"):
                        story.append(Paragraph(exp["description"], styles["Normal"]))
                    story.append(Spacer(1, 6))

            # project section
            projects = resume_data.get("projects") or []

            if projects:

                story.append(
                    Paragraph("<b>Projects</b>", styles["Heading2"])
                )

                for project in projects:

                    title = project.get("title", "")
                    desc = project.get("description", "")
                    tech = ", ".join(project.get("technologies", []))

                    story.append(
                        Paragraph(f"<b>{title}</b>", styles["Normal"])
                    )

                    story.append(
                        Paragraph(desc, styles["Normal"])
                    )

                    if tech:

                        story.append(
                            Paragraph(
                                f"<i>Technologies:</i> {tech}",
                                styles["Normal"]
                            )
                        )

                    story.append(Spacer(1, 6))

            # Certification section
            certifications = resume_data.get("certifications") or []

            if certifications:

                story.append(
                    Paragraph("<b>Certifications</b>", styles["Heading2"])
                )

                for cert in certifications:

                    story.append(
                        Paragraph(
                            f"{cert.get('name')} - {cert.get('issuer')} ({cert.get('year')})",
                            styles["Normal"]
                        )
                    )

                story.append(Spacer(1, 6))
            
            # Language section
            languages = resume_data.get("languages") or []

            if languages:

                story.append(
                    Paragraph("<b>Languages</b>", styles["Heading2"])
                )

                for lang in languages:

                    story.append(
                        Paragraph(
                            f"{lang.get('name')} - {lang.get('proficiency')}",
                            styles["Normal"]
                        )
                    )

                story.append(Spacer(1, 6))


            # ✅ Education Section
            if resume_data.get("education"):
                story.append(Paragraph("<b>Education</b>", styles["Heading2"]))
                for edu in resume_data.get("education", []):
                    degree = edu.get("degree", "No Degree")
                    institution = edu.get("institution", "Unknown Institution")
                    year = edu.get("year", "N/A")
                    story.append(
                        Paragraph(
                            f"{degree} — {institution} ({year})",
                            styles["Normal"]
                        )
                    )

                story.append(Spacer(1, 12))

            # ✅ Skills Section
            if resume_data.get("skills"):
                skills = resume_data.get("skills") or []

                if skills:

                    story.append(
                        Paragraph("<b>Skills</b>", styles["Heading2"])
                    )

                    table_data = []

                    for i in range(0, len(skills), 2):

                        row = skills[i:i + 2]

                        if len(row) == 1:
                            row.append("")

                        table_data.append(row)

                    table = Table(table_data)

                    table.setStyle(
                        TableStyle([
                            ("LEFTPADDING", (0, 0), (-1, -1), 0),
                        ])
                    )

                    story.append(table)

                    story.append(Spacer(1, 8))

            # ✅ Build PDF
            doc.build(story)
            buffer.seek(0)

            logger.info("✅ PDF generated successfully for: %s", resume_data.get("name"))
            return buffer

        except Exception as e:
            logger.error("❌ Error generating PDF: %s", str(e))
            raise
