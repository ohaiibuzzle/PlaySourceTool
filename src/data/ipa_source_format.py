import json
import exceptions.ipa_source_exceptions as ipa_source_exceptions


class IPASourceFormat:

    # [
    #     {
    #         "bundleID": "xyz.skitty.Aidoku",
    #         "name": "Aidoku",
    #         "version": "0.5",
    #         "itunesLookup": "", // optional
    #         "link": "https://github.com/Aidoku/Aidoku/releases/download/v0.5/Aidoku.ipa" // must end in .ipa
    #     }
    # ]
    def __init__(self, bundleID, name, version, itunesLookup, link):
        self.bundleID = bundleID
        self.name = name
        self.version = version
        self.itunesLookup = itunesLookup
        self.link = link

    def to_json(self):
        return {
            "bundleID": self.bundleID,
            "name": self.name,
            "version": self.version,
            "itunesLookup": self.itunesLookup,
            "link": self.link,
        }

    def from_json(json):
        return IPASourceFormat(
            json["bundleID"],
            json["name"],
            json["version"],
            json["itunesLookup"],
            json["link"],
        )

    def validate(self):
        # iTunes Lookup is optional, but must start with https://
        if self.itunesLookup != "":
            if not self.itunesLookup.startswith("https://"):
                raise ipa_source_exceptions.LinkIsNotHTTPS

        if self.link != "":
            # Link must end with .ipa and start with https://
            if not self.link.endswith(".ipa"):
                raise ipa_source_exceptions.LinkIsNotIPA

            if not (self.link.startswith("https://") or self.link.startswith("file://")):
                raise ipa_source_exceptions.LinkIsNotFileNorHTTPS

        return True

    class JSONEncoder(json.JSONEncoder):
        def default(self, o):
            if isinstance(o, IPASourceFormat):
                return o.to_json()
            return json.JSONEncoder.default(self, o)
