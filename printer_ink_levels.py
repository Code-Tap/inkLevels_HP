import requests
import xmltodict
from nested_lookup import nested_lookup
from pprint import pprint


def grabXML(URL):
    resp = requests.get(URL)
    return resp.text


def main(URL):
    results = {}
    try:
        for k, v in URL.items():
            try:
                doc = xmltodict.parse(grabXML(v))
                results[k] = dict(
                    zip(
                        nested_lookup("dd:ConsumableLabelCode", doc)[:4],
                        nested_lookup("dd:ConsumablePercentageLevelRemaining", doc),
                    )
                )
            except Exception:
                results[k] = {"M": "Err", "C": "Err", "Y": "Err", "K": "Err"}
                pass

        return results
    except Exception as e:
        print(e)
        return -1


if __name__ == "__main__":
    URL = {
        "Alpha": "http://10.10.0.10/DevMgmt/ConsumableConfigDyn.xml",
        "Bravo": "http://10.10.0.11/DevMgmt/ConsumableConfigDyn.xml",
        "Charlie": "http://10.10.0.12/DevMgmt/ConsumableConfigDyn.xml",
    }

    colours = {
        "C": "Cyan",
        "M": "Magenta",
        "Y": "Yellow",
        "K": "Black",
    }

    collated = {}

    results = main(URL)

    for k, v in results.items():
        printerName = {}
        for key, value in v.items():
            printerName[colours[key]] = value
        collated[k] = printerName


pprint(collated)
