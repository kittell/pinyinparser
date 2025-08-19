'''
Created on Oct 9, 2021

@author: Kirk Kittell
'''

class PinyinParser:
    def __init__(self):
        self.tone_map = dict()
        self.tone_map['a'] = 'aāáǎàa'
        self.tone_map['e'] = 'eēéěèe'
        self.tone_map['i'] = 'iīíǐìi'
        self.tone_map['o'] = 'oōóǒòo'
        self.tone_map['u'] = 'uūúǔùu'
        self.tone_map['v'] = 'üǖǘǚǜü'
        self.tone_map['ü'] = 'üǖǘǚǜü'


    def tone_number_to_diacritic(self, input_text, char_replace, tone):
        result = None
        
        if int(tone) not in (1, 2, 3, 4):
            tone = 0    # All invalid tone numbers set to zero
        else:
            tone = int(tone)
        
        if len(char_replace) == 1:
            key = char_replace.lower()
            value = self.tone_map[key]
            char_final = value[tone]
            
            if char_replace.isupper():
                # Return capital letter if input was a capital letter
                char_final = char_final.upper()
            
            result = input_text.replace(char_replace, char_final)
        else:
            result = input_text
        
        return result
    
    def parse_pinyin_entry(self, input_text):
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
                parsed_syllable = self.tone_number_to_diacritic(syllable, c_replace, tone)
    
                # Remove tone number
                parsed_syllable = ''.join([i for i in parsed_syllable if not i.isdigit()])
            
            result += parsed_syllable
        
        return result
