"""
Local, editable learning data for Drug Information Explorer.

Keep each summary short, educational, and linked to its references. Medicines,
indications, warnings, and approved uses can vary by country and formulation.
Check current local guidance and product information when studying a real case.
"""

DRUGS = [
    {
        "generic_name": "Paracetamol",
        "aliases": ["acetaminophen"],
        "class_name": "Non-opioid analgesic; antipyretic",
        "mechanism": (
            "Acts centrally to reduce pain and fever. Its precise mechanism is "
            "not fully established."
        ),
        "therapeutic_uses": [
            "Relief of mild to moderate pain",
            "Reduction of fever",
        ],
        "adverse_effects": [
            "Usually few effects at recommended use",
            "Skin or hypersensitivity reactions can occur",
            "Overdose can cause severe liver injury",
        ],
        "precautions": [
            "Check combination products to avoid accidentally taking more than one "
            "product containing paracetamol/acetaminophen.",
            "Liver disease and regular heavy alcohol use are important safety "
            "considerations.",
        ],
        "clinical_pearls": [
            "Paracetamol is the name commonly used in many countries; acetaminophen "
            "is the name used in the United States.",
            "The key serious toxicity to recognize is dose-related liver injury.",
        ],
        "references": [
            {
                "title": "MedlinePlus: Acetaminophen Drug Information",
                "url": "https://medlineplus.gov/druginfo/meds/a681004.html",
            },
            {
                "title": "DailyMed: Acetaminophen product labels",
                "url": "https://dailymed.nlm.nih.gov/dailymed/search.cfm?query=acetaminophen",
            },
        ],
    },
    {
        "generic_name": "Metformin",
        "aliases": [],
        "class_name": "Biguanide antihyperglycemic",
        "mechanism": (
            "Lowers blood glucose mainly by reducing glucose production by the "
            "liver and improving the body's response to insulin."
        ),
        "therapeutic_uses": [
            "Management of type 2 diabetes mellitus",
        ],
        "adverse_effects": [
            "Diarrhea",
            "Nausea and abdominal discomfort",
            "Gas or indigestion",
            "A metallic or altered taste",
        ],
        "precautions": [
            "Kidney function is important because impaired renal clearance can "
            "increase the risk of metformin-associated lactic acidosis.",
            "Acute severe illness, dehydration, or low-oxygen states require "
            "clinical review.",
        ],
        "clinical_pearls": [
            "Gastrointestinal effects are among the most frequently reported "
            "problems.",
            "Lactic acidosis is rare but serious; assess risk factors and renal "
            "function using current guidance.",
        ],
        "references": [
            {
                "title": "MedlinePlus: Metformin Drug Information",
                "url": "https://medlineplus.gov/druginfo/meds/a696005.html",
            },
            {
                "title": "DailyMed: Metformin product labels",
                "url": "https://dailymed.nlm.nih.gov/dailymed/search.cfm?query=metformin",
            },
        ],
    },
    {
        "generic_name": "Amlodipine",
        "aliases": [],
        "class_name": "Dihydropyridine calcium-channel blocker",
        "mechanism": (
            "Blocks L-type calcium channels, predominantly in vascular smooth "
            "muscle, causing arterial vasodilation."
        ),
        "therapeutic_uses": [
            "Hypertension",
            "Certain types of angina",
            "Coronary artery disease",
        ],
        "adverse_effects": [
            "Peripheral edema, especially ankle swelling",
            "Dizziness or light-headedness",
            "Flushing",
            "Fatigue or nausea",
        ],
        "precautions": [
            "Monitor for symptomatic hypotension or worsening chest pain.",
            "Use clinical judgment in severe hepatic impairment and with other "
            "blood-pressure-lowering medicines.",
        ],
        "clinical_pearls": [
            "Peripheral edema is a characteristic adverse effect of "
            "dihydropyridine calcium-channel blockers.",
            "Regular use can help prevent angina, but amlodipine does not stop an "
            "episode of chest pain once it has started.",
        ],
        "references": [
            {
                "title": "MedlinePlus: Amlodipine Drug Information",
                "url": "https://medlineplus.gov/druginfo/meds/a692044.html",
            },
            {
                "title": "DailyMed: Amlodipine product labels",
                "url": "https://dailymed.nlm.nih.gov/dailymed/search.cfm?query=amlodipine",
            },
        ],
    },
    {
        "generic_name": "Atenolol",
        "aliases": [],
        "class_name": "Beta-1-selective adrenergic blocker",
        "mechanism": (
            "Blocks beta-1 adrenergic receptors in the heart, reducing heart "
            "rate and cardiac workload."
        ),
        "therapeutic_uses": [
            "Hypertension",
            "Angina",
            "Selected care after myocardial infarction",
        ],
        "adverse_effects": [
            "Dizziness or light-headedness",
            "Tiredness",
            "Slow heart rate",
            "Nausea or diarrhea",
        ],
        "precautions": [
            "Use caution with bradycardia, heart block, or decompensated heart "
            "failure.",
            "Beta blockers may mask some warning signs of hypoglycemia and can "
            "worsen bronchospasm in susceptible patients.",
            "Abrupt withdrawal can worsen angina or precipitate cardiac events; "
            "changes should be clinician-directed.",
        ],
        "clinical_pearls": [
            "Atenolol is relatively beta-1 selective, but selectivity is not "
            "absolute.",
            "Check heart rate, blood pressure, comorbidities, and concomitant "
            "medicines when reviewing beta-blocker therapy.",
        ],
        "references": [
            {
                "title": "MedlinePlus: Atenolol Drug Information",
                "url": "https://medlineplus.gov/druginfo/meds/a684031.html",
            },
            {
                "title": "DailyMed: Atenolol product labels",
                "url": "https://dailymed.nlm.nih.gov/dailymed/search.cfm?query=atenolol",
            },
        ],
    },
    {
        "generic_name": "Omeprazole",
        "aliases": [],
        "class_name": "Proton-pump inhibitor (PPI)",
        "mechanism": (
            "Suppresses gastric acid secretion by inhibiting the H+/K+-ATPase "
            "proton pump in gastric parietal cells."
        ),
        "therapeutic_uses": [
            "Gastroesophageal reflux disease (GERD)",
            "Acid-related esophageal injury and peptic-ulcer conditions",
            "Helicobacter pylori eradication as part of combination therapy",
        ],
        "adverse_effects": [
            "Headache",
            "Abdominal discomfort",
            "Nausea",
            "Diarrhea or constipation",
        ],
        "precautions": [
            "Review for clinically important drug interactions, including "
            "interactions that may affect other medicines.",
            "Long-term use has additional potential risks; ongoing need should be "
            "reviewed in the context of current guidance.",
        ],
        "clinical_pearls": [
            "PPIs reduce acid production; they are not the same as immediate "
            "acid-neutralizing antacids.",
            "Omeprazole is also used in combination regimens for H. pylori; it "
            "is not used alone to eradicate the organism.",
        ],
        "references": [
            {
                "title": "MedlinePlus: Omeprazole Drug Information",
                "url": "https://medlineplus.gov/druginfo/meds/a693050.html",
            },
            {
                "title": "DailyMed: Omeprazole product labels",
                "url": "https://dailymed.nlm.nih.gov/dailymed/search.cfm?query=omeprazole",
            },
        ],
    },
    {
        "generic_name": "Amoxicillin",
        "aliases": [],
        "class_name": "Aminopenicillin beta-lactam antibiotic",
        "mechanism": (
            "Binds penicillin-binding proteins and interferes with bacterial "
            "cell-wall synthesis, inhibiting susceptible bacteria."
        ),
        "therapeutic_uses": [
            "Treatment of selected infections caused by susceptible bacteria",
            "H. pylori eradication as part of combination therapy",
        ],
        "adverse_effects": [
            "Nausea or vomiting",
            "Diarrhea",
            "Skin rash",
        ],
        "precautions": [
            "A history of serious penicillin or beta-lactam allergy is important.",
            "Severe or persistent diarrhea during or after antibiotic therapy "
            "needs clinical assessment.",
            "Use depends on the suspected organism, local resistance, infection "
            "site, and current guidance.",
        ],
        "clinical_pearls": [
            "Antibiotics such as amoxicillin do not treat viral infections such "
            "as the common cold or flu.",
            "Amoxicillin is a penicillin-family antibiotic; allergy history "
            "should be checked.",
        ],
        "references": [
            {
                "title": "MedlinePlus: Amoxicillin Drug Information",
                "url": "https://medlineplus.gov/druginfo/meds/a685001.html",
            },
            {
                "title": "DailyMed: Amoxicillin product labels",
                "url": "https://dailymed.nlm.nih.gov/dailymed/search.cfm?query=amoxicillin",
            },
        ],
    },
    {
        "generic_name": "Salbutamol",
        "aliases": ["albuterol"],
        "class_name": "Short-acting beta-2 agonist (SABA)",
        "mechanism": (
            "Stimulates beta-2 adrenergic receptors in bronchial smooth muscle, "
            "increasing intracellular cAMP and promoting bronchodilation."
        ),
        "therapeutic_uses": [
            "Relief or prevention of bronchospasm in asthma",
            "Bronchospasm associated with other obstructive airway diseases",
            "Prevention of exercise-related bronchospasm with some inhaled products",
        ],
        "adverse_effects": [
            "Tremor",
            "Nervousness",
            "Headache",
            "Palpitations or a faster heart rate",
        ],
        "precautions": [
            "Use caution in people with cardiovascular disease, arrhythmias, or "
            "conditions that may be affected by beta-agonists.",
            "Increasing symptoms or unusually frequent need for a reliever "
            "inhaler can indicate inadequate control and warrants clinical review.",
        ],
        "clinical_pearls": [
            "Salbutamol is called albuterol in the United States.",
            "It is a bronchodilator, not an inhaled anti-inflammatory controller "
            "medicine.",
        ],
        "references": [
            {
                "title": "MedlinePlus: Albuterol Oral Inhalation",
                "url": "https://medlineplus.gov/druginfo/meds/a682145.html",
            },
            {
                "title": "DailyMed: Albuterol product labels",
                "url": "https://dailymed.nlm.nih.gov/dailymed/search.cfm?query=albuterol",
            },
        ],
    },
    {
        "generic_name": "Atorvastatin",
        "aliases": [],
        "class_name": "HMG-CoA reductase inhibitor (statin)",
        "mechanism": (
            "Inhibits HMG-CoA reductase, reducing hepatic cholesterol synthesis "
            "and increasing clearance of LDL cholesterol from the blood."
        ),
        "therapeutic_uses": [
            "Treatment of dyslipidemia",
            "Reduction of cardiovascular risk in selected patients",
        ],
        "adverse_effects": [
            "Diarrhea or indigestion",
            "Joint or muscle pain",
            "Headache",
        ],
        "precautions": [
            "Assess for muscle symptoms and clinically important interactions "
            "that can increase myopathy risk.",
            "Liver disease, pregnancy, and breastfeeding are important "
            "considerations; consult current product labeling and guidance.",
        ],
        "clinical_pearls": [
            "New unexplained muscle pain, tenderness, or weakness is important "
            "to recognize because rare serious muscle injury can occur.",
            "Atorvastatin is a statin; its principal lipid effect is lowering "
            "LDL cholesterol.",
        ],
        "references": [
            {
                "title": "MedlinePlus: Atorvastatin Drug Information",
                "url": "https://medlineplus.gov/druginfo/meds/a600045.html",
            },
            {
                "title": "DailyMed: Atorvastatin product labels",
                "url": "https://dailymed.nlm.nih.gov/dailymed/search.cfm?query=atorvastatin",
            },
        ],
    },
    {
        "generic_name": "Aspirin",
        "aliases": ["acetylsalicylic acid"],
        "class_name": "Salicylate NSAID; antiplatelet agent",
        "mechanism": (
            "Irreversibly inhibits cyclooxygenase enzymes. This reduces "
            "prostaglandin synthesis and, in platelets, thromboxane A2 formation."
        ),
        "therapeutic_uses": [
            "Pain and fever relief",
            "Anti-inflammatory use in selected conditions",
            "Antiplatelet therapy for selected cardiovascular indications",
        ],
        "adverse_effects": [
            "Stomach irritation or heartburn",
            "Nausea",
            "Bleeding, including gastrointestinal bleeding",
            "Ringing in the ears at toxic exposure",
        ],
        "precautions": [
            "Use caution with a history of ulcer or bleeding, anticoagulants, "
            "other medicines that increase bleeding risk, or aspirin allergy.",
            "Avoid use in children and teenagers with viral illness unless "
            "specifically directed by a clinician because of Reye syndrome risk.",
        ],
        "clinical_pearls": [
            "Aspirin's platelet effect is irreversible and lasts for the life "
            "of the affected platelet.",
            "The intended use matters: analgesic/anti-inflammatory use and "
            "antiplatelet use have different risk-benefit considerations.",
        ],
        "references": [
            {
                "title": "MedlinePlus: Aspirin Drug Information",
                "url": "https://medlineplus.gov/druginfo/meds/a682878.html",
            },
            {
                "title": "DailyMed: Aspirin product labels",
                "url": "https://dailymed.nlm.nih.gov/dailymed/search.cfm?query=aspirin",
            },
        ],
    },
    {
        "generic_name": "Cetirizine",
        "aliases": [],
        "class_name": "Second-generation H1 antihistamine",
        "mechanism": (
            "Blocks peripheral histamine H1 receptors, reducing symptoms caused "
            "by histamine release."
        ),
        "therapeutic_uses": [
            "Allergic rhinitis symptoms",
            "Urticaria (hives)",
        ],
        "adverse_effects": [
            "Drowsiness",
            "Fatigue",
            "Dry mouth",
        ],
        "precautions": [
            "Drowsiness can still occur; take care with driving, alcohol, or "
            "other sedating medicines.",
            "Kidney impairment may affect medicine handling; consult current "
            "product information and clinical guidance.",
        ],
        "clinical_pearls": [
            "Cetirizine is generally less sedating than first-generation "
            "antihistamines, but it can still cause drowsiness.",
            "It blocks histamine H1 receptors; it does not treat the underlying "
            "cause of an allergy.",
        ],
        "references": [
            {
                "title": "MedlinePlus: Cetirizine Drug Information",
                "url": "https://medlineplus.gov/druginfo/meds/a623043.html",
            },
            {
                "title": "DailyMed: Cetirizine product labels",
                "url": "https://dailymed.nlm.nih.gov/dailymed/search.cfm?query=cetirizine",
            },
        ],
    },
]
