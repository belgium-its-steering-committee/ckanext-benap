# TODO: translations
FREQUENCY = [
    (
        "http://publications.europa.eu/resource/authority/frequency/1MIN",
        {
            "en": "Every minute",
            "fr": "Toutes les minutes",
            "nl": "Elke minuut",
            "de": "Minütlich",
        },
        False,
    ),
    (
        "http://publications.europa.eu/resource/authority/frequency/5MIN",
        {
            "en": "Every five minutes",
            "fr": "Toutes les 5 minutes",
            "nl": "Om de vijf minuten",
            "de": "Alle fünf Minuten",
        },
        False,
    ),
    (
        "http://publications.europa.eu/resource/authority/frequency/10MIN",
        {
            "en": "Every ten minutes",
            "fr": "Toutes les 10 minutes",
            "nl": "Om de tien minuten",
            "de": "Alle zehn Minuten",
        },
        False,
    ),
    (
        "http://publications.europa.eu/resource/authority/frequency/15MIN",
        {
            "en": "Every fifteen minutes",
            "fr": "Toutes les 15 minutes",
            "nl": "Om de vijftien minuten",
            "de": "Viertelstündlich",
        },
        False,
    ),
    (
        "http://publications.europa.eu/resource/authority/frequency/30MIN",
        {
            "en": "Every thirty minutes",
            "fr": "Toutes les 30 minutes",
            "nl": "Om de dertig minuten",
            "de": "Halbstündlich",
        },
        False,
    ),
    (
        "http://publications.europa.eu/resource/authority/frequency/HOURLY",
        {
            "en": "Hourly",
            "fr": "Toutes les heures",
            "nl": "Om het uur",
            "de": "Stündlich",
        },
        False,
    ),
    (
        "http://publications.europa.eu/resource/authority/frequency/BIHOURLY",
        {
            "en": "Bihourly",
            "fr": "Toutes les deux heures",
            "nl": "Om de twee uur",
            "de": "Alle zwei Stunden",
        },
        False,
    ),
    (
        "http://publications.europa.eu/resource/authority/frequency/TRIHOURLY",
        {
            "en": "Trihourly",
            "fr": "Toutes les trois heures",
            "nl": "Om de drie uur",
            "de": "Alle drei Stunden",
        },
        False,
    ),
    (
        "http://publications.europa.eu/resource/authority/frequency/12HRS",
        {
            "en": "Every twelve hours",
            "fr": "Toutes les 12 heures",
            "nl": "Om de twaalf uur",
            "de": "Alle zwölf Stunden",
        },
        False,
    ),
    (
        "http://publications.europa.eu/resource/authority/frequency/DAILY",
        {"en": "Daily", "fr": "Quotidien", "nl": "Dagelijks", "de": "Täglich"},
        False,
    ),
    (
        "http://publications.europa.eu/resource/authority/frequency/WEEKLY",
        {"en": "Weekly", "fr": "Hebdomadaire", "nl": "Wekelijks", "de": "Wöchentlich"},
        False,
    ),
    (
        "http://publications.europa.eu/resource/authority/frequency/MONTHLY",
        {"en": "Monthly", "fr": "Mensuel", "nl": "Maandelijks", "de": "Monatlich"},
        False,
    ),
    (
        "http://publications.europa.eu/resource/authority/frequency/QUARTERLY",
        {
            "en": "Quarterly",
            "fr": "Trimestriel",
            "nl": "Driemaandelijks",
            "de": "Vierteljährlich",
        },
        False,
    ),
    (
        "http://publications.europa.eu/resource/authority/frequency/ANNUAL_2",
        {
            "en": "Semiannual",
            "fr": "Semestriel",
            "nl": "Halfjaarlijks",
            "de": "Halbjährlich",
        },
        False,
    ),
    (
        "http://publications.europa.eu/resource/authority/frequency/ANNUAL",
        {"en": "Annual", "fr": "Annuel", "nl": "Jaarlijks", "de": "Jährlich"},
        False,
    ),
    (
        "http://publications.europa.eu/resource/authority/frequency/IRREG",
        {
            "en": "Less frequent than yearly",
            "fr": "Moins qu'une fois par an",
            "nl": "Minder vaak dan één keer per jaar",
            "de": "Weniger häufig als einmal pro Jahr",
        },
        False,
    ),
    (
        "http://publications.europa.eu/resource/authority/frequency/IRREG",
        {
            "en": "On occurence",
            "fr": "Dès que disponible",
            "nl": "Zodra beschikbaar",
            "de": "Sofort",
        },
        False,
    ),
    (
        "http://publications.europa.eu/resource/authority/frequency/IRREG",
        {
            "en": "Irregular",
            "fr": "Irrégulier",
            "nl": "Onregelmatig",
            "de": "Unregelmäßig",
        },
        False,
    ),
    (
        "http://publications.europa.eu/resource/authority/frequency/UNKNOWN",
        {"de": "Unknown", "en": "Unknown", "fr": "Inconnu", "nl": "Unknown"},
        True,
    ),
    (
        "http://publications.europa.eu/resource/authority/frequency/TRIDECENNIAL",
        {
            "de": "Tridecennial",
            "en": "Tridecennial",
            "fr": "Tous les trente ans",
            "nl": "Tridecennial",
        },
        True,
    ),
    (
        "http://publications.europa.eu/resource/authority/frequency/DAILY_2",
        {
            "de": "Twice a day",
            "en": "Twice a day",
            "fr": "Deux fois par jour",
            "nl": "Twice a day",
        },
        True,
    ),
    (
        "http://publications.europa.eu/resource/authority/frequency/UPDATE_CONT",
        {
            "de": "Continuously updated",
            "en": "Continuously updated",
            "fr": "Continuously updated",
            "nl": "Continuously updated",
        },
        True,
    ),
    (
        "http://publications.europa.eu/resource/authority/frequency/OTHER",
        {"de": "Other", "en": "Other", "fr": "Other", "nl": "Other"},
        True,
    ),
    (
        "http://publications.europa.eu/resource/authority/frequency/MONTHLY_3",
        {
            "de": "Three times a month",
            "en": "Three times a month",
            "fr": "Three times a month",
            "nl": "Three times a month",
        },
        True,
    ),
    (
        "http://publications.europa.eu/resource/authority/frequency/SEXENNIAL",
        {"de": "Sexennial", "en": "Sexennial", "fr": "Sexennial", "nl": "Sexennial"},
        True,
    ),
    (
        "http://publications.europa.eu/resource/authority/frequency/MONTHLY_2",
        {
            "de": "Semimonthly",
            "en": "Semimonthly",
            "fr": "Bimensuel",
            "nl": "Semimonthly",
        },
        True,
    ),
    (
        "http://publications.europa.eu/resource/authority/frequency/WEEKLY_5",
        {
            "de": "Five times a week",
            "en": "Five times a week",
            "fr": "Five times a week",
            "nl": "Five times a week",
        },
        True,
    ),
    (
        "http://publications.europa.eu/resource/authority/frequency/BIDECENNIAL",
        {
            "de": "Bidecennial",
            "en": "Bidecennial",
            "fr": "Tous les vingt ans",
            "nl": "Bidecennial",
        },
        True,
    ),
    (
        "http://publications.europa.eu/resource/authority/frequency/WEEKLY_3",
        {
            "de": "Three times a week",
            "en": "Three times a week",
            "fr": "Trois fois par semaine",
            "nl": "Drie keer per week",
        },
        True,
    ),
    (
        "http://publications.europa.eu/resource/authority/frequency/DECENNIAL",
        {"de": "Decennial", "en": "Decennial", "fr": "Decennial", "nl": "Decennial"},
        True,
    ),
    (
        "http://publications.europa.eu/resource/authority/frequency/QUINQUENNIAL",
        {
            "de": "Quinquennial",
            "en": "Quinquennial",
            "fr": "Tous les cinq ans",
            "nl": "Om de vijf jaar",
        },
        True,
    ),
    (
        "http://publications.europa.eu/resource/authority/frequency/AS_NEEDED",
        {"de": "As needed", "en": "As needed", "fr": "As needed", "nl": "As needed"},
        True,
    ),
    (
        "http://publications.europa.eu/resource/authority/frequency/BIENNIAL",
        {"de": "Biennial", "en": "Biennial", "fr": "Biennal", "nl": "Biennial"},
        True,
    ),
    (
        "http://publications.europa.eu/resource/authority/frequency/ANNUAL_3",
        {
            "de": "Three times a year",
            "en": "Three times a year",
            "fr": "Trois fois par an",
            "nl": "Three times a year",
        },
        True,
    ),
    (
        "http://publications.europa.eu/resource/authority/frequency/QUADRENNIAL",
        {
            "de": "Quadrennial",
            "en": "Quadrennial",
            "fr": "Tous les quatre ans",
            "nl": "Quadrennial",
        },
        True,
    ),
    (
        "http://publications.europa.eu/resource/authority/frequency/BIMONTHLY",
        {"de": "Bimonthly", "en": "Bimonthly", "fr": "Bimestriel", "nl": "Bimonthly"},
        True,
    ),
    (
        "http://publications.europa.eu/resource/authority/frequency/OP_DATPRO",
        {
            "de": "Provisional data",
            "en": "Provisional data",
            "fr": "Provisional data",
            "nl": "Provisional data",
        },
        True,
    ),
    (
        "http://publications.europa.eu/resource/authority/frequency/TRIENNIAL",
        {"de": "Triennial", "en": "Triennial", "fr": "Triennial", "nl": "Triennial"},
        True,
    ),
    (
        "http://publications.europa.eu/resource/authority/frequency/BIWEEKLY",
        {"de": "Biweekly", "en": "Biweekly", "fr": "Biweekly", "nl": "Biweekly"},
        True,
    ),
    (
        "http://publications.europa.eu/resource/authority/frequency/WEEKLY_2",
        {
            "de": "Zweimal pro woche",
            "en": "Semiweekly",
            "fr": "Bihebdomadaire",
            "nl": "Twee keer per week",
        },
        True,
    ),
    (
        "http://publications.europa.eu/resource/authority/frequency/NOT_PLANNED",
        {
            "de": "Not planned",
            "en": "Not planned",
            "fr": "Non planifié",
            "nl": "Not planned",
        },
        True,
    ),
    (
        "http://publications.europa.eu/resource/authority/frequency/NEVER",
        {"de": "Never", "en": "Never", "fr": "Jamais", "nl": "Never"},
        True,
    ),
    (
        "http://publications.europa.eu/resource/authority/frequency/CONT",
        {"de": "Continuous", "en": "Continuous", "fr": "Continuel", "nl": "Continuous"},
        True,
    ),
]
