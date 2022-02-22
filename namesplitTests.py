
## Temp def for namesplit
def namesplit(string):
    return {'artist': '', 'songname': ''}

#####################################################################

## Testing function
def test(dic1, dic2):
    
    if not dic1 or not dic2:
        print("Test FAILED | ", dic1, " =/= ", dic2)
        return False

    elif dic1 != dic2:
        print("Test FAILED | ", dic1, " =/= ", dic2)
        return False
    
    elif dic1 == dic2:
        print("Test Passed")
        return True

    else:
        print("Unusual Case")
        return False


#####################################################################
    
