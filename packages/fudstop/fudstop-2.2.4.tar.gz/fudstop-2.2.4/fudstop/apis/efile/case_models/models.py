import pandas as pd


class Events:
    def __init__(self, data):
        """Case Events"""

        self.filingID = [i.get('filingID') for i in data]
        self.filingCode = [i.get('filingCode') for i in data]
        self.description = [i.get('description') for i in data]
        self.submitted = [i.get('submitted') for i in data]
        self.submitterFullName = [i.get('submitterFullName') for i in data]
        self.docketed = [i.get('docketed') for i in data]
        self.isHiddenFromPublic = [i.get('isHiddenFromPublic') for i in data]
        self.hasManualSecurityOverride = [i.get('hasManualSecurityOverride') for i in data]
        self.jurisdiction = [i.get('jurisdiction') for i in data]
        self.jurisdictionKey = [i.get('jurisdictionKey') for i in data]
        self.externalKey = [i.get('externalKey') for i in data]
        self.ofsFilingID = [i.get('ofsFilingID') for i in data]
        self.documents = [i.get('documents') for i in data]
        self.hasNoReportedDocuments = [i.get('hasNoReportedDocuments') for i in data]
        self.case = [i.get('case') for i in data]
        self.hasHiddenDocument = [i.get('hasHiddenDocument') for i in data]
        self.hasNoDocument = [i.get('hasNoDocument') for i in data]
        self.eventType = [i.get('eventType') for i in data]
        self.type = [i.get('type') for i in data]
        self.highlights = [i.get('highlights') for i in data]

        self.data_dict = {
            "filingID": self.filingID,
            "filingCode": self.filingCode,
            "description": self.description,
            "submitted": self.submitted,
            "submitterFullName": self.submitterFullName,
            "docketed": self.docketed,
            "isHiddenFromPublic": self.isHiddenFromPublic,
            "hasManualSecurityOverride": self.hasManualSecurityOverride,
            "jurisdiction": self.jurisdiction,
            "jurisdictionKey": self.jurisdictionKey,
            "externalKey": self.externalKey,
            "ofsFilingID": self.ofsFilingID,
            "documents": self.documents,
            "hasNoReportedDocuments": self.hasNoReportedDocuments,
            "case": self.case,
            "hasHiddenDocument": self.hasHiddenDocument,
            "hasNoDocument": self.hasNoDocument,
            "eventType": self.eventType,
            "type": self.type,
            "highlights": self.highlights
        }


        self.as_dataframe = pd.DataFrame(self.data_dict)
