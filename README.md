# Customized EFF Diceware Wordlist

The EFF has published a [great set of diceware wordlists](https://www.eff.org/deeplinks/2016/07/new-wordlists-random-passphrases) and an [informative diceware page](https://www.eff.org/dice).  The wordlist can also be found in the EFF's [eff_diceware repo on GitHub](https://github.com/EFForg/eff_diceware) from which this repository is forked.

This repository contains a modified wordlist based on the EFF's 5-die "large" list.

The customized list replaces 3,609 words, including:
  - words of 8 or more characters,
  - hard-to-spell words,
  - words with homophones,
  - words that could make for unpleasant, unsavory, or politically insensitive passphrases,
  - some compound words that might be difficult to remember as a single "word,"
  - words with common alternative spellings,
  - words containing non-alphabetic characters, and
  - other words that seem out of place in a wordlist.

I've replaced most of the removed words with 3-6 character words from [hermitdave's FrequencyWords repo](https://github.com/hermitdave/FrequencyWords/).

### Files:

`eff_large_wordlist.txt` is in the original format of the repository, and is well-suited for use with dice to create passphrases.

`eff_large_wordlist-2025.txt` has an additional numbered column, and this particular file will *not* be updated in the future -- making it useful for encrypting a passphrase with one time pad as outlined in [my blog post](https://philthompson.me/2019/Diceware-Passphrases.html).  (If this particular URL/filename is noted with the encrypted passphrase, you can be sure you're decrypting the passphrase correctly.)

`lower_upper_digit_special-2025.txt` uses only 3- and 4-character words, but includes upper-case characters, digits, and special characters.

`eff_large_wordlist-2019.txt` was the previous version of the customized list, which replaced 433 words from the original EFF list.

## License

The wordlist file is distributed by the EFF under the [Creative Commons Attribution License](https://creativecommons.org/licenses/by/3.0/us/).

All other content in this repository is open source under the terms of the [MIT License](http://opensource.org/licenses/MIT).
