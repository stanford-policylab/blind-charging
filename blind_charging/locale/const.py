INDICATOR_POS_PREFIX = "prefix"
INDICATOR_POS_SUFFIX = "suffix"

# full list is from
# http://bcdcspatial.blogspot.com/2012/09/normalize-to-usps-street-abbreviations.html
# take partial list based on https://trafficsignstore.com/abbreviations.html
# removed some of them as they may cause confusion or ambiguity
# removed route, is, court, center
USPS_STREET_ABBR = {
    "alley",
    "avenue",
    "boulevard",
    "bridge",
    "canyon",
    "circle",
    "crescent",
    "drive",
    "expressway",
    "freeway",
    "highway",
    "hill",
    "island",
    "junction",
    "lane",
    "lake",
    "loop",
    "mount",
    "mountain",
    "parkway",
    "place",
    "plaza",
    "port",
    "river",
    "road",
    "square",
    "street",
    "terrace",
    "trail",
    "turnpike",
    "way",
    "aly",
    "ave",
    "blvd",
    "brg",
    "cyn",
    "ctr",
    "cir",
    "ct",
    "cres",
    "dr",
    "expy",
    "fwy",
    "hwy",
    "hl",
    "jct",
    "ln",
    "lk",
    "loop",
    "mt",
    "mtn",
    "park",
    "pkwy",
    "pl",
    "plz",
    "prt",
    "riv",
    "rd",
    "rte",
    "sq",
    "st",
    "ter",
    "trl",
    "tpke",
    "way",
}
