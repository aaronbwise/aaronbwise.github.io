"""Generate a styled PDF CV from CV_AaronWise_2026.md using fpdf2."""

from fpdf import FPDF

OUTPUT = "assets/docs/Aaron_Wise_CV_2026.pdf"

# Brand colors
NAVY = (27, 58, 92)
TEAL = (42, 157, 143)
DARK = (45, 52, 54)
MUTED = (99, 110, 114)
LIGHT_BG = (240, 247, 250)

FONT = "Calibri"


class CVPDF(FPDF):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Register Calibri (Unicode-capable TTF from Windows)
        self.add_font("Calibri", "", "C:/Windows/Fonts/calibri.ttf", uni=True)
        self.add_font("Calibri", "B", "C:/Windows/Fonts/calibrib.ttf", uni=True)
        self.add_font("Calibri", "I", "C:/Windows/Fonts/calibrii.ttf", uni=True)
        self.add_font("Calibri", "BI", "C:/Windows/Fonts/calibriz.ttf", uni=True)

    def header(self):
        pass  # No running header

    def footer(self):
        self.set_y(-12)
        self.set_font(FONT, "", 7)
        self.set_text_color(*MUTED)
        self.cell(0, 10, "Aaron Wise  |  aaron@a3di.dev  |  www.aaronbwise.com", align="C")

    def section_heading(self, text):
        self.ln(4)
        self.set_font(FONT, "B", 13)
        self.set_text_color(*NAVY)
        self.cell(0, 8, text)
        self.ln(8)
        # Teal underline
        x = self.get_x()
        y = self.get_y()
        self.set_draw_color(*TEAL)
        self.set_line_width(0.6)
        self.line(x, y, x + self.epw, y)
        self.ln(4)

    def org_heading(self, org, dates_location):
        self.set_font(FONT, "B", 10)
        self.set_text_color(*NAVY)
        self.cell(0, 6, org)
        self.ln(5.5)
        self.set_font(FONT, "", 8.5)
        self.set_text_color(*MUTED)
        self.cell(0, 5, dates_location)
        self.ln(5.5)

    def bullet(self, text):
        self.set_font(FONT, "", 9)
        self.set_text_color(*DARK)
        x = self.get_x()
        # Bullet marker
        self.set_x(x + 3)
        bullet_x = self.get_x()
        self.cell(4, 5, chr(8226))
        # Text with wrapping
        self.multi_cell(self.epw - 7, 5, text)
        self.ln(0.5)

    def edu_entry(self, degree, school, dates, detail=None):
        # Degree
        self.set_font(FONT, "B", 10)
        self.set_text_color(*NAVY)
        w_degree = self.get_string_width(degree) + 4
        self.cell(w_degree, 6, degree)
        # Dates on the right
        self.set_font(FONT, "", 9)
        self.set_text_color(*MUTED)
        self.cell(0, 6, dates, align="R")
        self.ln(6)
        # School
        self.set_font(FONT, "", 9)
        self.set_text_color(*DARK)
        self.cell(0, 5, school)
        self.ln(5)
        if detail:
            self.set_font(FONT, "I", 8.5)
            self.set_text_color(*MUTED)
            self.cell(0, 5, detail)
            self.ln(5)
        self.ln(3)


def build_pdf():
    pdf = CVPDF("P", "mm", "A4")
    pdf.set_auto_page_break(auto=True, margin=18)
    pdf.set_margins(18, 15, 18)
    pdf.add_page()

    # --- Name ---
    pdf.set_font(FONT, "B", 24)
    pdf.set_text_color(*NAVY)
    pdf.cell(0, 12, "Aaron Bradley Wise", align="C")
    pdf.ln(11)

    # --- Contact line ---
    pdf.set_font(FONT, "", 9)
    pdf.set_text_color(*MUTED)
    pdf.cell(0, 5, "Gainesville, FL, USA  |  aaron@a3di.dev  |  linkedin.com/in/aaronbwise  |  github.com/aaronbwise  |  a3di.dev", align="C")
    pdf.ln(5)

    # Thin teal line under contact
    pdf.set_draw_color(*TEAL)
    pdf.set_line_width(0.4)
    x = pdf.get_x()
    pdf.line(x, pdf.get_y() + 2, x + pdf.epw, pdf.get_y() + 2)
    pdf.ln(6)

    # --- Profile ---
    pdf.section_heading("Profile")
    pdf.set_font(FONT, "", 9.5)
    pdf.set_text_color(*DARK)
    pdf.multi_cell(0, 5,
        "Food security expert with over 15 years of experience leading data-driven "
        "projects in development and humanitarian contexts. Specialized in acute food "
        "security analysis, early warning systems, and decision support tools across "
        "diverse geographies. Proficient in integrating complex datasets to produce "
        "actionable insights for humanitarian interventions. Experienced in leveraging "
        "technology to enhance the design and implementation of food security monitoring "
        "systems and communication strategies."
    )
    pdf.ln(1)

    # --- Professional Experience ---
    pdf.section_heading("Professional Experience")

    # WFP 2022-2025
    pdf.org_heading("World Food Programme (WFP)", "May 2022 \u2013 Dec 2025  |  Remote  |  Multiple Offices")
    for b in [
        "Led data quality assurance, cleaning, and analysis for Rounds 12 and 13 of the joint FAO-WFP Food Security and Livelihoods Assessment in Myanmar, including trend analysis across historical rounds and preparation of findings for IPC classification and inter-agency reporting.",
        "Led the analysis of WFP Myanmar\u2019s Remote Food Security Monitoring (RFSM) survey, developing reproducible analytical pipelines and generating key food security indicators for programme decision-making.",
        "Led analyses of WFP Afghanistan beneficiary data to develop data-driven recommendations for optimizing food assistance targeting strategies.",
        "Supported food security analyses for multiple rounds of a joint WFP-FAO remote food security survey in Myanmar, the results of which inform both organisations\u2019 ongoing operations and feed into the IPC.",
        "Led the analysis of a joint WFP-Ministry of Agriculture national food security survey in Timor-Leste and provided strategic recommendations to key stakeholders for mitigating food insecurity impacts of price inflation and drought.",
        "Updated and optimized the Python backend for WFP Pacific\u2019s food security data pipeline, ensuring seamless operations and continued data availability for regional government partners.",
        "Supported WFP offices (Pakistan, Sri Lanka, Lao PDR, Philippines) in the design and operationalization of remote phone-based food security monitoring systems (mVAM).",
    ]:
        pdf.bullet(b)
    pdf.ln(2)

    # FHI 360
    pdf.org_heading("FHI 360 (Alive & Thrive Initiative)", "Apr 2022 \u2013 Dec 2022; Jul\u2013Aug 2023  |  Remote  |  Viet Nam")
    pdf.bullet(
        "Analysed disparities in Maternal, Infant, and Young Child Nutrition (MIYCN) outcomes across Cambodia, "
        "Viet Nam, and Lao PDR using MICS and DHS datasets (2000\u20132021), generating equity-focused recommendations "
        "to improve access and utilization of services for vulnerable populations."
    )
    pdf.ln(2)

    # WFP 2021
    pdf.org_heading("World Food Programme (WFP)", "Sep 2021 \u2013 Dec 2021  |  Remote  |  Thailand")
    pdf.bullet(
        "Provided strategic and technical guidance to WFP offices in the Asia Pacific region, including estimating "
        "populations in need (PIN) and evaluating targeting criteria, ensuring alignment with WFP\u2019s acute food security frameworks."
    )
    pdf.ln(2)

    # WFP Cambodia 2021
    pdf.org_heading("World Food Programme (WFP)", "Jan 2021 \u2013 Jul 2021  |  Cambodia")
    pdf.bullet(
        "Led WFP Cambodia\u2019s food security analysis activities, including in-house GIS experts and developers, "
        "providing critical information to UN agencies and partners during restrictive COVID-19 lockdowns."
    )
    pdf.ln(2)

    # WFP 2019-2020
    pdf.org_heading("World Food Programme (WFP)", "Nov 2019 \u2013 Dec 2020  |  Thailand")
    for b in [
        "Provided technical support for COVID-19 remote food security assessments in the Philippines, Pacific Islands, and Myanmar, and delivered strategic guidance in the Philippines to align assessment outputs with the government\u2019s social protection system (4Ps) while enhancing WFP\u2019s role as a technical partner.",
        "Led a series of resource mobilisation efforts targeting emergent food security issues with ECHO (urban EPR), IKI (climate change), and IPP (remote sensing/climate).",
    ]:
        pdf.bullet(b)
    pdf.ln(2)

    # IGN
    pdf.org_heading("Iodine Global Network (IGN)", "Jul 2020 \u2013 Aug 2020  |  Remote  |  Namibia")
    pdf.bullet(
        "Analysed the 2015-16 Namibia Household Income and Expenditure Survey (NHIES) using tailored Python scripts, "
        "calculating micronutrient consumption by demographic characteristics to inform national discussions on micronutrient fortification strategies."
    )
    pdf.ln(2)

    # WFP Mozambique
    pdf.org_heading("World Food Programme (WFP)", "Aug 2018 \u2013 Aug 2019  |  Mozambique")
    for b in [
        "Established a remote food security and nutrition monitoring system (mVAM) for areas of the country affected by chronic food insecurity, climate variability, and recent natural disasters.",
        "Analysed food security monitoring data for WFP South Sudan to enhance the effectiveness and efficiency of program targeting.",
    ]:
        pdf.bullet(b)
    pdf.ln(2)

    # WFP Italy
    pdf.org_heading("World Food Programme (WFP)", "Feb 2018 \u2013 Jun 2018  |  Italy")
    pdf.bullet(
        "Conceptualised and developed an automated solution to generate monthly mVAM bulletins for Yemen and Syria "
        "(including data extraction, storage, analysis, and visualisation)."
    )
    pdf.ln(2)

    # WFP Thailand 2014-2017
    pdf.org_heading("World Food Programme (WFP)", "Aug 2014 \u2013 Dec 2017  |  Thailand")
    for b in [
        "Led the design and implementation of a $1.2M DFID-funded project in Bangladesh to enhance government capacity for generating and utilizing data on social safety net programs and developed an equity-based targeting mechanism for the joint WFP/Ministry of Education school feeding program in Bhutan.",
        "Managed data analytics and reporting for remote food security monitoring surveys in Papua New Guinea and coordinated food security analysis for the Rohingya refugee emergency in Cox\u2019s Bazar, Bangladesh, ensuring effective targeting during the initial influx in 2017.",
        "Conducted critical assessments in Afghanistan and Fiji, including reviewing WFP Afghanistan\u2019s food security analysis to inform the Country Strategic Plan and leading the Fiji Food Security and Livelihoods Recovery Needs Assessment to guide post-cyclone recovery programming.",
    ]:
        pdf.bullet(b)
    pdf.ln(2)

    # WFP Guinea-Bissau
    pdf.org_heading("World Food Programme (WFP)", "Feb 2016 \u2013 Jul 2016  |  Guinea-Bissau")
    pdf.bullet("Designed and implemented a school feeding baseline survey for WFP\u2019s USDA-funded school meals programme in Guinea-Bissau.")
    pdf.ln(2)

    # WFP Myanmar 2016
    pdf.org_heading("World Food Programme (WFP)", "Jan 2016 \u2013 Feb 2016  |  Remote  |  Myanmar")
    pdf.bullet("Analysed data from the 2015 Southeast and Rakhine State Food Security and Poverty Survey for incorporation into WFP Myanmar\u2019s 2016 Food Security Atlas.")
    pdf.ln(2)

    # WFP Bangladesh 2015
    pdf.org_heading("World Food Programme (WFP)", "Aug 2015 \u2013 Sep 2015  |  Bangladesh")
    pdf.bullet("Finalised the 2013 Bangladesh Urban Slum Survey data analysis and report; presented key findings to high-level Government stakeholders.")
    pdf.ln(2)

    # UNICEF Thailand
    pdf.org_heading("United Nations Children\u2019s Fund (UNICEF)", "Oct 2013 \u2013 Jul 2014  |  Thailand")
    pdf.bullet(
        "Provided technical and strategic guidance to UNICEF\u2019s emergency-prone offices on developing nutrition information "
        "systems and led emergency nutrition surge support in Tacloban City during the immediate aftermath of Typhoon Haiyan, "
        "delivering actionable data to inform critical decision-making."
    )
    pdf.ln(2)

    # WFP Cambodia 2012-2013
    pdf.org_heading("World Food Programme (WFP)", "Jun 2012 \u2013 Jun 2013  |  Cambodia")
    pdf.bullet(
        "Developed tools and coordinated stakeholder reviews to enhance the usability and design of the Ministry of Planning\u2019s "
        "IDPoor household poverty database for UN and development partners."
    )
    pdf.ln(2)

    # UNICEF Cambodia 2011-2012
    pdf.org_heading("United Nations Children\u2019s Fund (UNICEF)", "Oct 2011 \u2013 May 2012  |  Cambodia")
    pdf.bullet(
        "Conducted trend analyses to identify the main determinants of inequitable MIYCN outcomes and utilisation of services "
        "from the 2000, 2005, and 2010 Cambodia Demographic and Health Surveys (DHS)."
    )
    pdf.ln(2)

    # WFP Cambodia 2011-2012
    pdf.org_heading("World Food Programme (WFP)", "Dec 2011 \u2013 Mar 2012  |  Cambodia")
    pdf.bullet("Coordinated a multi-stakeholder household survey to assess the relief and recovery needs of rural populations affected by the 2011 floods in rural Cambodia.")
    pdf.ln(2)

    # UNICEF Liberia
    pdf.org_heading("United Nations Children\u2019s Fund (UNICEF)", "Jul 2011 \u2013 Sep 2011  |  Liberia")
    pdf.bullet(
        "Coordinated the finalization of the Liberia National Micronutrient Survey with UNICEF and the Ministry of Health "
        "and Social Welfare and analysed blood serum data to produce accurate prevalence estimates of iron and vitamin A "
        "deficiencies in children, supporting evidence-based nutrition interventions."
    )
    pdf.ln(2)

    # WFP Cambodia 2010-2011
    pdf.org_heading("World Food Programme (WFP)", "Nov 2010 \u2013 Feb 2011  |  Cambodia")
    pdf.bullet("Coordinated a household nutrition survey to assess the effectiveness of WFP\u2019s \u201cSupport to Mother and Child\u201d project.")
    pdf.ln(2)

    # UNICEF Cambodia 2010
    pdf.org_heading("United Nations Children\u2019s Fund (UNICEF)", "Aug 2010 \u2013 Nov 2010  |  Cambodia")
    pdf.bullet("Supported development of a food security and nutrition early warning system to increase the Government\u2019s capacity for predicting and responding to natural disasters.")
    pdf.ln(2)

    # Concern Worldwide
    pdf.org_heading("Concern Worldwide", "May 2010 \u2013 Jul 2010  |  South Sudan")
    pdf.bullet("Coordinated two nutrition surveys in South Sudan, the results of which Concern Worldwide used to authorise emergency programme activities.")
    pdf.ln(2)

    # UNICEF Ethiopia
    pdf.org_heading("United Nations Children\u2019s Fund (UNICEF)", "Jun 2009 \u2013 Dec 2009  |  Ethiopia")
    pdf.bullet(
        "Developed and implemented a therapeutic feeding program (TFP) monitoring system in collaboration with Ethiopian "
        "Regional Health Bureaus, NGOs, and UNICEF, assessed compliance and performance at TFP sites across Oromia and "
        "Amhara regions, and coordinated efforts to address logistical and supply gaps to enhance service delivery."
    )
    pdf.ln(2)

    # UNICEF Zimbabwe
    pdf.org_heading("United Nations Children\u2019s Fund (UNICEF)", "Jun 2007 \u2013 Jun 2009  |  Zimbabwe")
    pdf.bullet(
        "Supported UNICEF\u2019s Multiple Indicator Monitoring Survey with the Central Statistical Office and analysed 2008 "
        "micronutrient survey data to guide policy with Zimbabwe\u2019s Food and Nutrition Council."
    )
    pdf.ln(2)

    # --- Education ---
    pdf.section_heading("Education")

    pdf.edu_entry(
        "BS Computer Science (In Progress)",
        "Oregon State University, USA",
        "2023 \u2013 Present",
    )
    pdf.edu_entry(
        "MPH \u2013 International Health and Development",
        "Tulane University School of Public Health and Tropical Medicine, USA",
        "Jul 2006 \u2013 Dec 2007",
        "Concentration: Nutrition in Developing Countries",
    )
    pdf.edu_entry(
        "BA \u2013 Chemistry",
        "Washington University in St. Louis, USA",
        "Aug 2001 \u2013 May 2005",
        "Concentration: Biochemistry",
    )

    # --- Skills ---
    pdf.section_heading("Skills & Technologies")
    pdf.set_font(FONT, "", 9.5)
    pdf.set_text_color(*DARK)
    pdf.multi_cell(0, 5,
        "Highly proficient in Python, R, Stata, SPSS, and SQL for data management and analysis. "
        "Experienced with Tableau for data visualisation. Skilled in Git, HTML/CSS, Flask, Bash, "
        "PostgreSQL, ODK/KoboToolbox, and automated data pipeline development."
    )
    pdf.ln(2)

    # --- Publications ---
    pdf.section_heading("Publications & Presentations")
    pdf.set_font(FONT, "", 9)
    pdf.set_text_color(*DARK)
    pdf.multi_cell(0, 5,
        "Prak, S., Dahl, M.I., Oeurn, S., Conkle, J., Wise, A., & Laillou, A. \u201cBreastfeeding Trends "
        "in Cambodia, and the Increased Use of Breast-Milk Substitute\u2014Why Is It a Danger?\u201d "
        "Nutrients 6 (2014): 2920-2930. doi:10.3390/nu6072920"
    )
    pdf.ln(3)
    pdf.multi_cell(0, 5,
        "Sandalinas, F., Wise, A., Baawo, K., Faigao, K., Johnston, R., Thurnham, D., & Kupka, R. "
        "\u201cAdjustment of indicators of iron and vitamin A status in a nationally representative sample "
        "of Liberian children.\u201d Hidden Hunger Conference 2013, University of Hohenheim, Stuttgart, Germany."
    )

    pdf.output(OUTPUT)
    print(f"PDF generated: {OUTPUT}")


if __name__ == "__main__":
    build_pdf()
