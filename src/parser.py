'''
Created on Oct 9, 2021

@author: Kirk Kittell
'''

def tone_number_to_diacritic(input_text, c_replace, tone):
    
    tone_map = dict()
    tone_map['a1'] = 'ā'
    tone_map['e1'] = 'ē'
    tone_map['i1'] = 'ī'
    tone_map['o1'] = 'ō'
    tone_map['u1'] = 'ū'
    tone_map['v1'] = 'ǖ'
    tone_map['ü1'] = 'ǖ'
    tone_map['a2'] = 'á'
    tone_map['e2'] = 'é'
    tone_map['i2'] = 'í'
    tone_map['o2'] = 'ó'
    tone_map['u2'] = 'ú'
    tone_map['v2'] = 'ǘ'
    tone_map['ü2'] = 'ǘ'
    tone_map['a3'] = 'ǎ'
    tone_map['e3'] = 'ě'
    tone_map['i3'] = 'ǐ'
    tone_map['o3'] = 'ǒ'
    tone_map['u3'] = 'ǔ'
    tone_map['v3'] = 'ǚ'
    tone_map['ü3'] = 'ǚ'
    tone_map['a4'] = 'à'
    tone_map['e4'] = 'è'
    tone_map['i4'] = 'ì'
    tone_map['o4'] = 'ò'
    tone_map['u4'] = 'ù'
    tone_map['v4'] = 'ǜ'
    tone_map['ü4'] = 'ǜ'

    key = c_replace.lower() + str(tone)

    
    if len(key) > 1 and int(tone) in [1, 2, 3, 4]:
        c_final = tone_map[key]
        if c_replace.isupper():
            # Return capital letter if input was a capital letter
            c_final = c_final.upper()
        result = input_text.replace(c_replace, c_final)
    else:
        result = input_text
    
    
    return result

def parse_pinyin_entry(input_text):
    result = ''
    syllable_list = list()
    
    # Separate syllables
    temp_result = ''
    for c in input_text:
        if c.isdigit():
            temp_result += c
            syllable_list.append(temp_result)
            temp_result = ''
        else:
            temp_result += c
    
    print(syllable_list)

    for syllable in syllable_list:
        # Get tone number
        tone = syllable[-1:]
        parsed_syllable = ''
        if int(tone) in [1, 2, 3, 4, 5]:
            # Count vowels
            n_vowels = 0
            vowels = ''
            for c in syllable:
                if c in 'aeiouüAEIOUÜ':
                    n_vowels += 1
                    vowels += c
            
            # Determine pinyin replacement rule
            lower_vowels= vowels.lower()
            c_replace = ''
            if n_vowels == 1:
                # (0) One vowel: put diacritic on it
                c_replace = vowels
            elif n_vowels > 1:
                # (1) Put diacritic on 'a' or 'e'
                for c in ['a', 'A', 'e', 'E']:
                    if c in vowels:
                        c_replace = c
                        break
                if len(c_replace) == 0:
                    if 'ou' in lower_vowels:
                        # (2) Put diacritic on 'o' of 'ou'
                        if 'o' in vowels:
                            c_replace = 'o'
                        else:
                            c_replace = 'O'
                    else:
                        # (3) Put diacritic on second vowel
                        c_replace = vowels[1]
                

            # Add diacritic mark to specific characters
            parsed_syllable = tone_number_to_diacritic(syllable, c_replace, tone)

            # Remove tone number
            parsed_syllable = ''.join([i for i in parsed_syllable if not i.isdigit()])
        
        result += parsed_syllable
    
    return result