import ps4a
from ps4b import *
from ps4c import *

def test_get_permutations():
    assert ps4a.get_permutations("abc") == ["abc", "bac", "bca", "acb", "cab", "cba"]
    assert ps4a.get_permutations("bush") == ['bush', 'ubsh', 'usbh', 'ushb', 'bsuh', 'sbuh', 'subh', 'suhb', 'bshu', 'sbhu', 'shbu', 'shub', 'buhs', 'ubhs', 'uhbs', 'uhsb', 'bhus', 'hbus', 'hubs', 'husb', 'bhsu', 'hbsu', 'hsbu', 'hsub']


def test_caesar_encrypt():
    plaintext = PlaintextMessage('The killer is root', 3)
    ciphertext = CiphertextMessage('Wkh nloohu lv urrw')
    assert plaintext.get_message_text_encrypted() == 'Wkh nloohu lv urrw'
    assert ciphertext.decrypt_message() == (24, 'The killer is root')


def test_substitution_encrypt():
    message = SubMessage("A plan")
    permutation = "ouiea"
    enc_dict = message.build_transpose_dict(permutation)
    assert message.apply_transpose(enc_dict) == "O plon"
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    assert enc_message.decrypt_message() == "A plan"