class CorpusData:
    def __init__(self, corpus_id, name, description, dtProvision, enabled, swapQenc, swapIenc, textless, encrypted, encoderId, metadataMaxBytes, customDimensions, filterAttributes):
        self.corpus_id = corpus_id
        self.name = name
        self.description = description
        self.dtProvision = dtProvision
        self.enabled = enabled
        self.swapQenc = swapQenc
        self.swapIenc = swapIenc
        self.textless = textless
        self.encrypted = encrypted
        self.encoderId = encoderId
        self.metadataMaxBytes = metadataMaxBytes
        self.customDimensions = customDimensions
        self.filterAttributes = filterAttributes

    def to_dict(self):
        return {
            "id": self.corpus_id,
            "name": self.name,
            "description": self.description,
            "dtProvision": self.dtProvision,
            "enabled": self.enabled,
            "swapQenc": self.swapQenc,
            "swapIenc": self.swapIenc,
            "textless": self.textless,
            "encrypted": self.encrypted,
            "encoderId": self.encoderId,
            "metadataMaxBytes": self.metadataMaxBytes,
            "customDimensions": self.customDimensions,
            "filterAttributes": self.filterAttributes,
        }
