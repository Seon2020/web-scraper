import pytest
from web_scraper.scraper import get_citations_needed_count, get_citations_needed_report

def test_citations_count():
    actual = get_citations_needed_count('https://en.wikipedia.org/wiki/The_Grudge')
    expected = 3
    assert actual == expected 

def test_citations_text_report():
    actual = get_citations_needed_report('https://en.wikipedia.org/wiki/The_Grudge')
    expected = """In late 2002, the unexpected success of the English-language remake of The Ring finally gave Sony Pictures confidence to green-light an English-language remake of Ju-On: The Grudge. That same day, Takashi Shimizu, the director and creator of the original film, was hired to direct the film, with Stephen Susco writing the screenplay, and Sam Raimi through its Ghost House Pictures banner producing the project, alongside Robert Tapert and Takashige Ichise. Shimizu was eager to work on a remake of his own film, as he saw it as an opportunity to improve and fix some of the perceived problems and flaws that were present in the original film.[citation needed]

The Grudge was released on VHS, DVD, and UMD on February 1, 2005, as a standard version of the film with only a few special features.[12] On May 17, 2005, the unrated director's cut of The Grudge was released on DVD in North America. The release included several scenes that were cut to achieve a lower rating from the MPAA.[citation needed] This version of the film was used as the theatrical run in Japan. The release also contained new deleted scenes and commentaries, director Takashi Shimizu's original Ju-On short films, Katasumi and 4444444444, and more.[13] The film was released on Blu-ray Disc in the US on May 12, 2009, the same day that The Grudge 3 was released on DVD. It was made available to purchase on iTunes in 2008.[citation needed]

The Grudge was released on VHS, DVD, and UMD on February 1, 2005, as a standard version of the film with only a few special features.[12] On May 17, 2005, the unrated director's cut of The Grudge was released on DVD in North America. The release included several scenes that were cut to achieve a lower rating from the MPAA.[citation needed] This version of the film was used as the theatrical run in Japan. The release also contained new deleted scenes and commentaries, director Takashi Shimizu's original Ju-On short films, Katasumi and 4444444444, and more.[13] The film was released on Blu-ray Disc in the US on May 12, 2009, the same day that The Grudge 3 was released on DVD. It was made available to purchase on iTunes in 2008.[citation needed]"""
    assert actual == expected 

