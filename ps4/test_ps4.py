import ps4a


def test_get_permutations():
    assert ps4a.get_permutations("abc") == ["abc", "bac", "bca", "acb", "cab", "cba"]
    assert ps4a.get_permutations("bush") == ['bush', 'ubsh', 'usbh', 'ushb', 'bsuh', 'sbuh', 'subh', 'suhb', 'bshu', 'sbhu', 'shbu', 'shub', 'buhs', 'ubhs', 'uhbs', 'uhsb', 'bhus', 'hbus', 'hubs', 'husb', 'bhsu', 'hbsu', 'hsbu', 'hsub']
    assert ps4a.get_permutations("idiot") == ['idiot', 'diiot', 'diiot', 'dioit', 'dioti', 'iidot', 'iidot', 'idiot', 'idoit', 'idoti', 'iiodt', 'iiodt', 'ioidt', 'iodit', 'iodti', 'iiotd', 'iiotd', 'ioitd', 'iotid', 'iotdi', 'idoit', 'dioit', 'doiit', 'doiit', 'doiti', 'iodit', 'oidit', 'odiit', 'odiit', 'oditi', 'ioidt', 'oiidt', 'oiidt', 'oidit', 'oidti', 'ioitd', 'oiitd', 'oiitd', 'oitid', 'oitdi', 'idoti', 'dioti', 'doiti', 'dotii', 'dotii', 'iodti', 'oidti', 'oditi', 'odtii', 'odtii', 'iotdi', 'oitdi', 'otidi', 'otdii', 'otdii', 'iotid', 'oitid', 'otiid', 'otiid', 
'otidi', 'idito', 'diito', 'diito', 'ditio', 'ditoi', 'iidto', 'iidto', 'idito', 'idtio', 'idtoi', 'iitdo', 'iitdo', 'itido', 'itdio', 'itdoi', 'iitod', 'iitod', 'itiod', 'itoid', 'itodi', 'idtio', 'ditio', 'dtiio', 'dtiio', 'dtioi', 'itdio', 'tidio', 'tdiio', 'tdiio', 'tdioi', 'itido', 'tiido', 'tiido', 'tidio', 'tidoi', 'itiod', 'tiiod', 'tiiod', 'tioid', 'tiodi', 'idtoi', 'ditoi', 'dtioi', 'dtoii', 'dtoii', 'itdoi', 'tidoi', 'tdioi', 'tdoii', 'tdoii', 'itodi', 'tiodi', 'toidi', 'todii', 'todii', 'itoid', 'tioid', 'toiid', 'toiid', 'toidi']
    