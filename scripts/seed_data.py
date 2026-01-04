import os
import django
import datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from core.models import Part, Article, Amendment, Judgment

def seed():
    print("Seeding enhanced data...")
    
    # Clear existing to avoid duplicates during re-seed
    # Warning: This wipes data, as per user plan instruction
    Part.objects.all().delete()
    Article.objects.all().delete()
    Amendment.objects.all().delete()
    Judgment.objects.all().delete()

    # 1. Parts and Key Articles
    parts_data = [
        ("Part I", "The Union and its Territory", [
            ("1", "Name and territory of the Union"),
            ("3", "Formation of new States and alteration of areas/boundaries/names of existing States")
        ]),
        ("Part III", "Fundamental Rights", [
            ("12", "Definition of State"),
            ("14", "Equality before law"),
            ("19", "Protection of certain rights regarding freedom of speech, etc."),
            ("21", "Protection of life and personal liberty"),
            ("32", "Remedies for enforcement of rights conferred by this Part")
        ]),
        # ... (Abbreviated for brevity, but model supports all)
    ]

    for p_num, p_title, articles in parts_data:
        part, _ = Part.objects.get_or_create(number=p_num, title=p_title)
        for a_num, a_title in articles:
            Article.objects.create(
                number=a_num,
                title=a_title,
                content="Content placeholder for educational purpose...",
                part=part,
                is_key_article=True
            )

    # 2. Amendments (Detailed)
    amendments = [
        {
            "number": 1,
            "year": 1951,
            "desc": "Added Ninth Schedule to protect land reforms from judicial review.",
            "reason": "To overcome judicial hurdles in implementing land reforms and abolishing the Zamindari system.",
            "impact": "Created a constitutional vault (9th Schedule) where laws were initially immune from judicial scrutiny.",
            "link": "https://legislative.gov.in/constitution-of-india"
        },
        {
            "number": 42,
            "year": 1976,
            "desc": "The 'Mini-Constitution'. Added 'Socialist', 'Secular', 'Integrity' to Preamble.",
            "reason": "Enacted during the Emergency to centralize power and assert parliamentary sovereignty.",
            "impact": "Altered the Preamble, reduced power of Judiciary, added Fundamental Duties (Part IVA). Much of it was later reversed by the 44th Amendment.",
            "link": "https://legislative.gov.in/constitution-of-india"
        },
        {
            "number": 73,
            "year": 1992,
            "desc": "Panchayati Raj institutions given constitutional status.",
            "reason": "To strengthen grassroots democracy and provide a uniform structure for local self-government.",
            "impact": "Mandated regular elections, reservation for women/SCs/STs in local bodies. Part IX added.",
            "link": "https://www.india.gov.in/my-government/constitution-india/amendments/constitution-india-seventy-third-amendment-act-1992"
        },
        {
            "number": 106,
            "year": 2023,
            "desc": "Women's Reservation Bill (Nari Shakti Vandan Adhiniyam).",
            "reason": "To ensure greater representation of women in policy making.",
            "impact": "Reserves one-third of seats in Lok Sabha and State Legislative Assemblies for women.",
            "link": "https://prsindia.org/billtrack/the-constitution-one-hundred-and-twenty-eighth-amendment-bill-2023"
        }
    ]

    for data in amendments:
        Amendment.objects.create(
            number=data["number"],
            date_enacted=datetime.date(data["year"], 1, 1), # Approx date
            description=data["desc"],
            reason=data["reason"],
            impact=data["impact"],
            long_description=f"This amendment, enacted in {data['year']}, had identifying features: {data['desc']}...",
            official_link=data["link"]
        )

    # 3. Judgments (With Links)
    judgments = [
        {
            "title": "Golaknath v. State of Punjab",
            "year": 1967,
            "outcome": "Parliament cannot curtail Fundamental Rights.",
            "significance": "Historical struggle between Judiciary and Parliament.",
            "link": "https://frontline.thehindu.com/the-nation/the-check-on-power/article9995648.ece",
            "source": "The Hindu (Frontline Archives)"
        },
        {
            "title": "Kesavananda Bharati v. State of Kerala",
            "year": 1973,
            "outcome": "Basic Structure Doctrine established.",
            "significance": "Saved the Constitution from authoritarian alterations.",
            "link": "https://www.thehindu.com/opinion/op-ed/the-case-that-saved-indian-democracy/article4647800.ece",
            "source": "The Hindu (Archives)"
        },
        {
            "title": "Maneka Gandhi v. Union of India",
            "year": 1978,
            "outcome": "Expanded Article 21 to include 'Due Process'.",
            "significance": "Golden Triangle of Articles 14, 19, 21 established.",
            "link": "https://indianexpress.com/article/explained/explained-law/maneka-gandhi-case-passport-act-personal-liberty-9419194/",
            "source": "Indian Express (Explained)"
        },
        {
            "title": "K.S. Puttaswamy v. Union of India",
            "year": 2017,
            "outcome": "Right to Privacy is a Fundamental Right.",
            "significance": "Crucial for digital rights in 2025.",
            "link": "https://www.thehindu.com/news/national/supreme-court-judgment-on-right-to-privacy/article19551468.ece",
            "source": "The Hindu (2017)"
        }
    ]

    for data in judgments:
        Judgment.objects.create(
            title=data["title"],
            year=data["year"],
            outcome=data["outcome"],
            significance=data["significance"],
            source_link=data["link"],
            source_name=data["source"]
        )

    print("Seeding with enhanced content complete.")

if __name__ == "__main__":
    seed()
