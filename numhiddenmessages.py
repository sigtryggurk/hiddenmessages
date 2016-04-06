import unittest
DELIMITER = '_'
CHAR_TO_MORSE = {' ': DELIMITER,
                 'A': '*-',
                 'B': '-***',
                 'C': '-*-*',
                 'D': '-**',
                 'E': '*',
                 'F': '**-*',
                 'G': '--*',
                 'H': '****',
                 'I': '**',
                 'J': '*---',
                 'K': '-*-',
                 'L': '*-**',
                 'M': '--',
                 'N': '-*',
                 'O': '---',
                 'P': '*--*',
                 'Q': '--*-',
                 'R': '*-*',
                 'S': '***',
                 'T': '-',
                 'U': '**-',
                 'V': '***-',
                 'W': '*--',
                 'X': '-**-',
                 'Y': '-*--',
                 'Z': '--**',
                 '0': '-----',
                 '1': '*----',
                 '2': '**---',
                 '3': '***--',
                 '4': '****-',
                 '5': '*****',
                 '6': '-****',
                 '7': '--***',
                 '8': '---**',
                 '9': '----*'
}

MORSE_TO_CHAR = {v: k for k, v in CHAR_TO_MORSE.items()}
MORSE_TO_CHAR[' '] = ' '


def convertASCII_to_Morse(uncoded):
  return DELIMITER.join(map(lambda char: CHAR_TO_MORSE[char.upper()], list(uncoded)))

def convertMorse_to_ASCII(morse_code):
  morse_code = morse_code.replace("___","_ _")
  return "".join(map(lambda morse: MORSE_TO_CHAR[morse], morse_code.split(DELIMITER)))

def get_seq_minus_subseq(seq, subseq, seen, minusseq = ''):
  if not subseq:
    minusseq += seq
    seen.add(minusseq)
    return
  if not seq:
    return

  if seq[0] == subseq[0]:
    get_seq_minus_subseq(seq[1:], subseq[1:], seen, minusseq)

  minusseq += seq[0]
  get_seq_minus_subseq(seq[1:], subseq, seen, minusseq)

class Sequence:
  def __init__(self, sequence=''):
    self.sequence = convertASCII_to_Morse(sequence)
  def subtract(self, other):
    if len(self.sequence) < len(other.sequence) or set(other.sequence).intersection(set(self.sequence)) != set(other.sequence):
      raise ValueError(str(other) + " is not a subsequence of " + str(self))
    unique_minus_seq = set([])
    get_seq_minus_subseq(self.sequence, other.sequence, unique_minus_seq)
    return unique_minus_seq
  def __sub__(self, other):
    return self.subtract(other)
  def __repr__(self):
    return str(self.sequence)

class TestStringMethods(unittest.TestCase):
  def test_convert_char_to_morse(self):
    char = 'A'
    morse_char = convertASCII_to_Morse(char.upper())
    self.assertEqual(morse_char, '*-')
    self.assertEqual(convertMorse_to_ASCII(morse_char), char)

  def test_convert_word_to_morse(self):
    char = "AMMA"
    morse_char = convertASCII_to_Morse(char)
    self.assertEqual(morse_char, '*-_--_--_*-')
    self.assertEqual(convertMorse_to_ASCII(morse_char), char)

  def test_convert_sentence_to_morse(self):
    char = "AMMA ILLA ER HER"
    morse_char = convertASCII_to_Morse(char)
    self.assertEqual(morse_char, '*-_--_--_*-___**_*-**_*-**_*-___*_*-*___****_*_*-*')
    self.assertEqual(convertMorse_to_ASCII(morse_char), char)

  def test_a_minus_a(self):
    seq = Sequence("A")
    self.assertTrue(seq-seq == set(['']))

  def test_ab_minus_r(self):
    seq = Sequence("AB")
    subseq = Sequence("R")

    seqminus = seq - subseq
    self.assertTrue(len(seqminus) == 2)
    self.assertEqual(seqminus, set(['_-**', '-_**']))

  def test_hello_world_minus_help(self):
    seq = Sequence("HELLO WORLD")
    subseq = Sequence("HELP")

 #   self.assertTrue(len(seq-subseq) == 1311)


if __name__ == "__main__":
  unittest.main()
