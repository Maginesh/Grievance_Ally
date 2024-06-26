# grievance_classifier.py

import openai

openai.api_key = "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"

indian_ministries = [
    "Agriculture and Farmers Welfare",
    "Agriculture Research and Education",
    "Animal Husbandry, Dairying",
    "Atomic Energy",
    "Ayush",
    "Bio Technology",
    "Central Board of Direct Taxes(Income Tax)",
    "Central Board of Excise and Customs",
    "Chemicals and Petrochemicals",
    "Civil Aviation",
    "Coal",
    "Commerce",
    "Consumer Affairs",
    "Cooperation",
    "Corporate Affairs",
    "Culture",
    "Defence",
    "Defence Finance",
    "Defence Production",
    "Defence Research and Development",
    "Development of North Eastern Region",
    "Drinking Water and Sanitation",
    "Earth Sciences",
    "Economic Affairs",
    "Electronics & Information Technology",
    "Empowerment of Persons with Disabilities",
    "Environment, Forest and Climate Change",
    "Ex Servicemen Welfare",
    "Expenditure",
    "External Affairs",
    "Fertilizers",
    "Financial Services",
    "Financial Services(Banking Division)",
    "Financial Services(Insurance Division)",
    "Fisheries",
    "Food and Public Distribution",
    "Food Processing Industries",
    "Health & Family Welfare",
    "Health Research",
    "Heavy Industry",
    "Higher Education",
    "Home Affairs",
    "House and Urban Affairs",
    "Information and Broadcasting",
    "Investment & Public Asset Management",
    "Justice",
    "Labour and Employment",
    "Land Resources",
    "Legal Affairs",
    "Legislative Department",
    "Micro Small and Medium Enterprises",
    "Military Affairs",
    "Mines",
    "Minority Affairs",
    "New and Renewable Energy",
    "NITI Aayog",
    "O/o the Comptroller & Auditor General of India",
    "Official Language",
    "Panchayati Raj",
    "Parliamentary Affairs",
    "Personnel and Training",
    "Petroleum and Natural Gas",
    "Pharmaceutical",
    "Posts",
    "Power",
    "Promotion of Industry and Internal Trade",
    "Public Enterprises",
    "Railways, Railway Board",
    "Revenue",
    "Road Transport and Highways",
    "Rural Development",
    "School Education and Literacy",
    "Science and Technology",
    "Scientific & Industrial Research",
    "Shipping",
    "Skill Development and Entrepreneurship",
    "Social Justice and Empowerment",
    "Space",
    "Sports",
    "Staff Selection Commission",
    "Statistics and Programme Implementation",
    "Steel",
    "Telecommunication",
    "Textiles",
    "Tourism",
    "Tribal Affairs",
    "Unique Identification Authority of India",
    "Water Resources, River Development & Ganga Rejuvenation",
    "Women and Child Development",
    "Youth Affairs",
    "Administrative Reforms and Public Grievances",
    "State Governments/Others"
]

def classify_grievance(grievance):
    selected_ministry = indian_ministries[0]
    system_message = (
        f"You are an assistant used for grievance readdressal. Output a list of data that contains the departments to which the given grievance can be submitted under Indian ministry from the list {indian_ministries}. The department must be given only from the {indian_ministries}. Example Output: 'Department1', 'Department2', 'Department3', ..."
    )
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": "There has been a marked decrease in the quality of water in the locality. This is posing a sanitation risk in our area. Please look into the issue."},
            {"role": "assistant", "content": f"Drinking Water and Sanitation,Health & Family Welfare, Environment, Forest and Climate Change"},
            {"role": "user", "content": grievance},
        ]
    )
    return response['choices'][0]['message']['content'].split(',')
