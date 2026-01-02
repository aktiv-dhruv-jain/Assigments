companyHierarchy = {
    "Robert": {
        "TL": [
            {
                "Mark": {
                    "experience": 8,
                    "developers": [
                        {"Leonardo": {"experience": 1}},
                        {"Alexandra": {"experience": 1}}
                    ]
                }
            },
            {
                "Smith": {
                    "experience": 5,
                    "developers": [
                        {"Walker": {"experience": 2.7}},
                        {"Diana": {"experience": 2.7}},
                        {"Sophie": {"experience": 3.8}}
                    ]
                }
            },
            {"Samuel": {"experience": 8}},
            {
                "Paul": {
                    "experience": 8,
                    "developers": [
                        {"Fergal": {"experience": 4.5}}
                    ]
                }
            },
            {
                "Tom": {
                    "experience": 8,
                    "developers": [
                        {"Jerry": {"experience": 1.5}},
                        {"John": {"experience": 1.6}}
                    ]
                }
            }
        ]
    },
    "Anne": {
        "TL": [
            {
                "Chris": {
                    "experience": 5,
                    "TL": [
                        {
                            "James": {
                                "developers": [
                                    {"Jennifer": {"experience": 3.8}},
                                    {"Scott": {"experience": 3.8}},
                                    {"Sophie": {"experience": 3.8}}
                                ]
                            }
                        }
                    ]
                }
            },
            {"Pratt": {"experience": 5}},
            {"Emma": {"experience": 5}},
            {
                "Will": {
                    "experience": 5,
                    "developers": [
                        {"Edge": {"experience": 3}},
                        {"Ryan": {"experience": 3.5}}
                    ]
                }
            },
            {"Smith": {"experience": 5}}
        ]
    }
}

#a. Display all employees' names for the given project manager name.
def employeeByPm(pmname):
    tlunderpmname = []
    for teamleaders in companyHierarchy[pmname]['TL']:
        teamleader = list(teamleaders.keys())
        #companyHierarchy[pmname]['TL'][]
        tlunderpmname.append(teamleader)
        
    print(tlunderpmname)
        #print(f"employees directly under ${pmname} are ${teamleaders}")
        
#employeeByPm('Anne')
print(companyHierarchy['Robert']['TL'])
